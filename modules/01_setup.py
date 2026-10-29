import os
import sys
import subprocess
import time
import warnings
import contextlib
import io
import copy
import re
import hashlib
import inspect
import uuid
import unicodedata
from copy import deepcopy
from collections import deque
import json
import requests
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo
from typing import Any, Callable, Dict, List, Optional, Sequence, Set, Tuple, TypedDict
import math
import multiprocessing as mp
import numpy as np
import pandas as pd
import yfinance as yf
from openai import OpenAI
from langgraph.graph import StateGraph, START, END
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import textwrap

try:
    import pandas_market_calendars as mcal
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', 'pandas_market_calendars'])
    import pandas_market_calendars as mcal

warnings.filterwarnings('ignore')

PROJECT_NAME = 'Dow Jones Market Data Preparation and Validation System'
DEFAULT_START_DATE = '2010-01-01'

def get_last_completed_new_york_session() -> str:
    """
    Returns the latest fully completed regular trading session
    of the New York stock exchanges.

    The XNYS calendar is used as a common reference
    because NYSE and Nasdaq share the primary calendar
    and regular trading hours.
    """
    new_york_timezone = ZoneInfo('America/New_York')
    now_new_york = datetime.now(new_york_timezone)
    calendar = mcal.get_calendar('XNYS')
    schedule_start = now_new_york.date() - timedelta(days=15)
    schedule_end = now_new_york.date()
    market_schedule = calendar.schedule(start_date=schedule_start, end_date=schedule_end)

    if market_schedule.empty:
        raise RuntimeError('Unable to determine the calendar of the New York stock exchanges.')

    current_timestamp_utc = pd.Timestamp(now_new_york).tz_convert('UTC')
    completed_sessions = market_schedule[market_schedule['market_close'] <= current_timestamp_utc]

    if completed_sessions.empty:
        raise RuntimeError('No completed trading session identified within the period checked.')

    last_completed_session = completed_sessions.index[-1]
    return pd.Timestamp(last_completed_session).strftime('%Y-%m-%d')

DEFAULT_END_DATE = get_last_completed_new_york_session()
DEFAULT_INTERVAL = '1d'

MAIN_MODEL = 'nvidia/Nemotron-3-Ultra-550b-a55b'
CRITIC_MODEL = MAIN_MODEL

ENABLE_CROSS_SOURCE_CHECK = True
TWELVE_DATA_API_KEY = os.environ.get('TWELVE_DATA_API_KEY') or os.environ.get('TWELVE_DATA')

MAX_CROSS_SOURCE_TICKERS = 5
CROSS_SOURCE_TOLERANCE_PERCENT = 0.1
RANDOM_SAMPLE_ROWS = 5
MAX_MISSING_RATIO = 0.01
MINIMUM_OBSERVATIONS = 252

NEBIUS_API_KEY = os.environ.get('NEBIUS_API_KEY')

if not NEBIUS_API_KEY:
    raise RuntimeError('Missing NEBIUS_API_KEY environment variable.')

LANGSMITH_API_KEY = os.environ.get('LANGSMITH_API_KEY')

os.environ['LANGSMITH_TRACING_V2'] = 'true' if LANGSMITH_API_KEY else 'false'
os.environ['LANGSMITH_ENDPOINT'] = 'https://api.smith.langchain.com'
os.environ['LANGSMITH_PROJECT'] = 'Agentic_AI'

MODEL_NAME = MAIN_MODEL

client = OpenAI(
    api_key=NEBIUS_API_KEY,
    base_url='https://api.tokenfactory.us-central1.nebius.com/v1/'
)

MODEL_NAME = MAIN_MODEL
FALLBACK_MODEL_NAME = 'nvidia/nemotron-3-super-120b-a12b'
MODELS = [MODEL_NAME, FALLBACK_MODEL_NAME]

if MODEL_NAME == FALLBACK_MODEL_NAME:
    raise ValueError('The primary model and the fallback model must be different.')

from typing import List
from collections import defaultdict
import requests
import re

DOW_JONES_TICKERS = [
    'AAPL', 'AMGN', 'AMZN', 'AXP', 'BA', 'CAT', 'CRM',
    'CSCO', 'CVX', 'DIS', 'GS', 'HD', 'HON', 'IBM',
    'JNJ', 'JPM', 'KO', 'MCD', 'MMM', 'MRK', 'MSFT',
    'NKE', 'NVDA', 'PG', 'SHW', 'TRV', 'UNH', 'V',
    'VZ', 'WMT'
]

EXPECTED_NUMBER_OF_TICKERS = 30

def normalize_ticker(ticker: str) -> str:
    return str(ticker).strip().upper().replace('.', '-')

def clean_ticker_list(raw_tickers) -> List[str]:
    cleaned_tickers = []
    for ticker in raw_tickers:
        normalized_ticker = normalize_ticker(ticker)
        if normalized_ticker in {'', 'NAN', 'NONE'}:
            continue
        cleaned_tickers.append(normalized_ticker)
    return list(dict.fromkeys(cleaned_tickers))

def validate_dow_jones_tickers(ticker_list: List[str]) -> List[str]:
    validated_tickers = clean_ticker_list(ticker_list)

    if len(validated_tickers) != EXPECTED_NUMBER_OF_TICKERS:
        raise ValueError(
            f'Invalid Dow Jones universe: {len(validated_tickers)} tickers found '
            f'instead of {EXPECTED_NUMBER_OF_TICKERS} expected.'
        )

    return validated_tickers

tickers = validate_dow_jones_tickers(DOW_JONES_TICKERS)

class MarketDataState(TypedDict, total=False):
    model_name: str
    data_source: str
    execution_status: str
    current_node: str
    user_request: str
    parsed_request: Dict[str, Any]
    tickers: List[str]
    raw_data: Any
    clean_data: Dict[str, pd.DataFrame]
    aligned_prices: pd.DataFrame
    aligned_volumes: pd.DataFrame
    simple_returns: pd.DataFrame
    log_returns: pd.DataFrame
    cleaning_report: pd.DataFrame
    alignment_report: Dict[str, Any]
    validation_report: pd.DataFrame
    cross_source_report: pd.DataFrame
    cross_source_comparison: pd.DataFrame
    cross_source_monthly_test: pd.DataFrame
    cross_source_summary: Dict[str, Any]
    cross_source_reference_date: Any
    cross_source_blocking_failure: bool
    critic_report: Dict[str, Any]
    certification: Dict[str, Any]
    failed_tickers: List[str]
    errors: List[str]

LLM_TIMEOUT_SECONDS = 60.0
LLM_MAX_RETRIES = 0
LLM_EMPTY_RESPONSE_RETRY = 1
LLM_RETRY_WAIT_SECONDS = 1.0

LLM_FALLBACK_MODEL = globals().get(
    'FALLBACK_MODEL_NAME',
    'nvidia/nemotron-3-super-120b-a12b'
)

if MAIN_MODEL == LLM_FALLBACK_MODEL:
    raise ValueError(
        'MAIN_MODEL and LLM_FALLBACK_MODEL must be two different models.'
    )

def extract_json_from_text(text: str) -> Dict[str, Any]:
    if not isinstance(text, str) or not text.strip():
        raise ValueError('The model response is empty or is not a string.')

    cleaned_text = (
        text.strip()
        .replace('```json', '')
        .replace('```JSON', '')
        .replace('```', '')
        .strip()
    )

    try:
        parsed_json = json.loads(cleaned_text)
    except json.JSONDecodeError:
        start_position = cleaned_text.find('{')
        end_position = cleaned_text.rfind('}')

        if start_position == -1 or end_position == -1:
            raise ValueError(
                'The model response does not contain a recognizable JSON object.'
            )

        json_text = cleaned_text[start_position:end_position + 1]

        try:
            parsed_json = json.loads(json_text)
        except json.JSONDecodeError as error:
            raise ValueError(
                f'The model returned JSON-like text, but with invalid syntax.\n\n'
                f'Response received:\n{cleaned_text}'
            ) from error

    if not isinstance(parsed_json, dict):
        raise ValueError('The JSON response must be a Python dictionary.')

    return parsed_json

def _call_openrouter_once(
    system_instruction: str,
    user_content: str,
    model: str,
    temperature: float
):
    return client.with_options(
        timeout=LLM_TIMEOUT_SECONDS,
        max_retries=LLM_MAX_RETRIES
    ).chat.completions.create(
        model=model,
        temperature=temperature,
        messages=[
            {'role': 'system', 'content': system_instruction},
            {'role': 'user', 'content': user_content}
        ]
    )

def call_llm_json(
    system_instruction: str,
    user_content: str,
    model: str = MAIN_MODEL,
    temperature: float = 0.0
) -> Dict[str, Any]:
    """
    Sends a request to Nebius and returns
    a Python dictionary.

    Process:

    1. tries the requested model, normally MAIN_MODEL;
    2. if the model returns an error, an empty response, or an
       unusable response, tries LLM_FALLBACK_MODEL;
    3. for each model, only one manual retry is allowed
       in case of an empty response;
    4. automatic client retries are disabled.

    The technical fallback is independent of the agents'
    validation/challenge logic.
    """
    complete_system_instruction = (
        system_instruction.strip()
        + '\n\n'
        + 'Return exclusively a single valid JSON object. '
        + 'Do not use Markdown blocks, comments, or additional text.'
    )

    requested_model = (
        model if isinstance(model, str) and model.strip()
        else MAIN_MODEL
    )

    models_to_try = [requested_model]

    if LLM_FALLBACK_MODEL not in models_to_try:
        models_to_try.append(LLM_FALLBACK_MODEL)

    total_attempts_per_model = 1 + LLM_EMPTY_RESPONSE_RETRY
    model_errors = {}

    for current_model in models_to_try:
        last_model_error = None

        for attempt in range(1, total_attempts_per_model + 1):
            try:
                response = _call_openrouter_once(
                    system_instruction=complete_system_instruction,
                    user_content=user_content,
                    model=current_model,
                    temperature=temperature
                )

                if response is None:
                    raise RuntimeError('Nebius did not return any response.')

                if response.choices:
                    response_text = response.choices[0].message.content

                    if response_text is not None and str(response_text).strip():
                        try:
                            parsed_response = extract_json_from_text(
                                response_text
                            )
                        except Exception as error:
                            raise ValueError(
                                f'The model responded, but did not produce valid JSON. '
                                f'Model: {current_model}. Error: {error}'
                            ) from error

                        parsed_response.setdefault(
                            '_llm_model_used',
                            current_model
                        )
                        parsed_response.setdefault(
                            '_llm_fallback_used',
                            current_model != requested_model
                        )

                        return parsed_response

                last_model_error = RuntimeError(
                    'Nebius returned an empty response.'
                )

            except Exception as error:
                last_model_error = error

            if attempt < total_attempts_per_model:
                time.sleep(LLM_RETRY_WAIT_SECONDS)
                continue

        model_errors[current_model] = str(last_model_error)

    error_details = '\n'.join([
        f'- {model_name}: {error_message}'
        for model_name, error_message in model_errors.items()
    ])

    raise RuntimeError(
        f'None of the configured models completed the call successfully.\n\n'
        f'Primary model: {requested_model}\n'
        f'Fallback model: {LLM_FALLBACK_MODEL}\n\n'
        f'Errors detected:\n{error_details}'
    )

def inspect_agent_output(agent_name, result, rows=5):
    if result is None:
        return

    if not isinstance(result, dict):
        return

    for key, value in result.items():
        if isinstance(value, pd.DataFrame):
            if value.empty:
                pass

        elif isinstance(value, pd.Series):
            if value.empty:
                pass

        elif isinstance(value, dict):
            if len(value) == 0:
                pass
            else:
                for sub_key, sub_value in list(value.items())[:rows]:
                    if isinstance(sub_value, pd.DataFrame):
                        if sub_value.empty:
                            pass
                    elif isinstance(sub_value, pd.Series):
                        if sub_value.empty:
                            pass
                    elif isinstance(sub_value, dict):
                        pass

        elif isinstance(value, list):
            if len(value) == 0:
                pass
            else:
                for item in value[:rows]:
                    if isinstance(item, dict):
                        pass

        elif isinstance(value, tuple):
            for item in value[:rows]:
                pass

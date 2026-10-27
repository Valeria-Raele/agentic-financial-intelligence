# ========= ORIGINAL NOTEBOOK CELL 8 =========
# ============================================================
# LIBRARIES
# ============================================================

# System, configuration, and utilities
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

# Serialization and HTTP communication
import json
import requests

# Dates, time, and time zones
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

# Type annotations
from typing import Any, Callable, Dict, List, Optional, Sequence, Set, Tuple, TypedDict

# Numerical computing and data analysis
import math
import multiprocessing as mp
import numpy as np
import pandas as pd

# Financial data
import yfinance as yf

# LLM and Google Colab configuration
from openai import OpenAI
from google.colab import userdata

# Agentic orchestration
from langgraph.graph import StateGraph, START, END

# Semantic analysis and text similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Text formatting
import textwrap

# ========= ORIGINAL NOTEBOOK CELL 10 =========
# ============================================================
# BOX 1 — LIBRARY IMPORTS AND GENERAL CONFIGURATION
# ============================================================
# In this box, we import the libraries required to:
# - configure the system's general parameters;
# - download financial data through yfinance;
# - process and validate historical time series;
# - orchestrate the agentic workflow with LangGraph;
# - configure Twelve Data as a secondary verification source;
# - define through Nebius the LLM model used
#   both as the primary model and as the critic model.
# ============================================================


# ------------------------------------------------------------
# NEW YORK STOCK EXCHANGE CALENDAR
# ------------------------------------------------------------
# Securities belonging to the Dow Jones Industrial Average are
# traded partly on the New York Stock Exchange and partly
# on Nasdaq.
#
# Both exchanges follow the same primary calendar
# and the same regular trading hours:
# from 09:30 to 16:00 in the New York time zone.
#
# The time reference used for the entire dataset is
# therefore the latest fully completed New York exchange
# trading session, regardless of the security's listing exchange.
# ------------------------------------------------------------

try:

    import pandas_market_calendars as mcal

except ImportError:

    subprocess.check_call(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "-q",
            "pandas_market_calendars"
        ]
    )

    import pandas_market_calendars as mcal


warnings.filterwarnings("ignore")


# ------------------------------------------------------------
# GENERAL PROJECT PARAMETERS
# ------------------------------------------------------------

PROJECT_NAME = (
    "Dow Jones Market Data Preparation "
    "and Validation System"
)

DEFAULT_START_DATE = "2010-01-01"


# ------------------------------------------------------------
# LATEST COMPLETED NEW YORK STOCK EXCHANGE SESSION
# ------------------------------------------------------------

def get_last_completed_new_york_session() -> str:
    """
    Returns the latest fully completed regular trading session
    of the New York stock exchanges.

    The XNYS calendar is used as a common reference
    because NYSE and Nasdaq share the primary calendar
    and regular trading hours.
    """

    new_york_timezone = ZoneInfo(
        "America/New_York"
    )

    now_new_york = datetime.now(
        new_york_timezone
    )

    calendar = mcal.get_calendar(
        "XNYS"
    )

    schedule_start = (
        now_new_york.date()
        - timedelta(days=15)
    )

    schedule_end = now_new_york.date()

    market_schedule = calendar.schedule(
        start_date=schedule_start,
        end_date=schedule_end
    )

    if market_schedule.empty:

        raise RuntimeError(
            "Unable to determine the calendar "
            "of the New York stock exchanges."
        )

    current_timestamp_utc = pd.Timestamp(
        now_new_york
    ).tz_convert(
        "UTC"
    )

    completed_sessions = market_schedule[
        market_schedule["market_close"]
        <= current_timestamp_utc
    ]

    if completed_sessions.empty:

        raise RuntimeError(
            "No completed trading session identified "
            "within the period checked."
        )

    last_completed_session = (
        completed_sessions.index[-1]
    )

    return pd.Timestamp(
        last_completed_session
    ).strftime(
        "%Y-%m-%d"
    )


DEFAULT_END_DATE = (
    get_last_completed_new_york_session()
)

DEFAULT_INTERVAL = "1d"


# ------------------------------------------------------------
# LLM MODELS USED THROUGH NEBIUS
# ------------------------------------------------------------
# NVIDIA Nemotron 3 Ultra 550B:
# - is used as the primary model;
# - interprets the user's request;
# - produces the structured outputs required by the process.
#
# NVIDIA Nemotron 3 Ultra 550B:
# - is also used as the critic model;
# - critically evaluates the outputs of the primary model;
# - identifies errors, inconsistencies, and critical issues.
#
# The primary model is explicitly selected
# and the same model is used as the critic.
# ------------------------------------------------------------

MAIN_MODEL ="nvidia/Nemotron-3-Ultra-550b-a55b"

CRITIC_MODEL = MAIN_MODEL


# ------------------------------------------------------------
# CROSS-CHECK WITH A SECONDARY SOURCE: TWELVE DATA
# ------------------------------------------------------------
# True:
# - performs the comparison between Yahoo Finance and Twelve Data.
#
# False:
# - disables the cross-check with the secondary source.
# ------------------------------------------------------------

ENABLE_CROSS_SOURCE_CHECK = True


# ------------------------------------------------------------
# TWELVE DATA API KEY
# ------------------------------------------------------------

TWELVE_DATA_API_KEY = userdata.get("TWELVE_DATA")


# Maximum number of tickers to verify with Twelve Data.
# The check is limited to reduce:
# - number of API requests;
# - execution time;
# - risk of exceeding the free plan limits.

MAX_CROSS_SOURCE_TICKERS = 5


# Maximum allowed percentage deviation
# between Yahoo Close and Twelve Data Close: 0.1%.

CROSS_SOURCE_TOLERANCE_PERCENT = 0.10


# Number of observations to display
# for each ticker in the comparison between:
# - Yahoo Close;
# - Twelve Data Close.

RANDOM_SAMPLE_ROWS = 5

# ============================================================
# EXECUTION MODE
# ============================================================

# True  -> also runs manual tests of individual agents.
# False -> runs only the complete workflow through LangGraph.

RUN_DEVELOPMENT_TESTS = False

# ------------------------------------------------------------
# QUALITY CONTROL PARAMETERS
# ------------------------------------------------------------

# Maximum tolerated threshold of missing data.

MAX_MISSING_RATIO = 0.01


# Indicative minimum number of required observations.

MINIMUM_OBSERVATIONS = 252


# ------------------------------------------------------------
# CONFIGURATION OUTPUT
# ------------------------------------------------------------

print(PROJECT_NAME)

print(
    "Configuration completed."
)

print(
    f"Default period: "
    f"{DEFAULT_START_DATE} - {DEFAULT_END_DATE}"
)

print(
    "Dataset end date: latest completed "
    "New York stock exchange trading session."
)

print(
    f"Primary model: {MAIN_MODEL}"
)

print(
    f"Critic model: {CRITIC_MODEL}"
)

print(
    f"Twelve Data check enabled: "
    f"{ENABLE_CROSS_SOURCE_CHECK}"
)

print(
    f"Maximum number of tickers checked: "
    f"{MAX_CROSS_SOURCE_TICKERS}"
)

print(
    f"Maximum tolerance: "
    f"{CROSS_SOURCE_TOLERANCE_PERCENT:.2f}%"
)

print(
    f"Rows displayed per ticker: "
    f"{RANDOM_SAMPLE_ROWS}"
)

# ========= ORIGINAL NOTEBOOK CELL 11 =========
# ============================================================
# BOX 2 — NEBIUS + LANGSMITH CONFIGURATION
# ============================================================


# ============================================================
# NEBIUS
# ============================================================

NEBIUS_API_KEY = userdata.get("NEBIUS_API_KEY")

os.environ["NEBIUS_API_KEY"] = NEBIUS_API_KEY

# ============================================================
# LANGSMITH
# ============================================================

LANGSMITH_API_KEY = userdata.get("LANGSMITH_API_KEY")

os.environ["LANGSMITH_TRACING_V2"] = "true"
os.environ["LANGSMITH_API_KEY"] = LANGSMITH_API_KEY
os.environ["LANGSMITH_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGSMITH_PROJECT"] = "Agentic_AI"

# ============================================================
# PRIMARY MODEL
# ============================================================
# Primary LLM model used by the workflow.
# The critic model is instead defined separately
# through the CRITIC_MODEL variable.
# ============================================================

MODEL_NAME = MAIN_MODEL

# ============================================================
# NEBIUS CLIENT
# ============================================================

client = OpenAI(
    api_key=NEBIUS_API_KEY,
    base_url="https://api.tokenfactory.us-central1.nebius.com/v1/"
)

print("Nebius configured correctly.")
print("LangSmith configured correctly.")
print("Selected model:", MODEL_NAME)

# ========= ORIGINAL NOTEBOOK CELL 12 =========
# ============================================================
# BOX 3 — NEBIUS CONNECTION TEST
# ============================================================
# This box:
# - first tries the primary model NVIDIA Nemotron 3 Ultra 550B;
# - if the primary model does not respond or returns an error,
#   automatically tries NVIDIA Nemotron 3 Super 120B as fallback;
# - confirms which model actually responded.
# ============================================================

MODEL_NAME = MAIN_MODEL

FALLBACK_MODEL_NAME = "nvidia/nemotron-3-super-120b-a12b"

MODELS = [
    MODEL_NAME,
    FALLBACK_MODEL_NAME
]

print("Primary model:", MODEL_NAME)
print("Fallback model:", FALLBACK_MODEL_NAME)

if MODEL_NAME == FALLBACK_MODEL_NAME:
    raise ValueError(
        "The primary model and the fallback model "
        "must be different."
    )

response = None
last_error = None

for model in MODELS:

    print(f"\nAttempting with model: {model}")

    try:

        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": "Respond exclusively with the word OK."
                }
            ],
            max_tokens=1024,
            temperature=0,
            timeout=120
        )

        if response is None:
            raise RuntimeError(
                "Nebius did not return any response."
            )

        if not response.choices:

            error_details = getattr(
                response,
                "error",
                None
            )

            if error_details is None:
                error_details = response.model_dump()

            raise RuntimeError(
                "The model did not generate any valid response. "
                f"Details: {error_details}"
            )

        content = response.choices[0].message.content

        if content is None or content.strip() == "":
            raise RuntimeError(
                "The model returned an empty response."
            )

        print("\n✓ Connection to Nebius successful.")
        print("Model used:", model)
        print("Response:", content.strip())

        break

    except Exception as error:

        last_error = error

        print(
            f"❌ The model {model} "
            "did not respond correctly."
        )
        print("Error:", error)

else:

    raise RuntimeError(
        "\nNone of the configured models "
        "responded correctly.\n"
        f"Last error detected: {last_error}"
    )

# ========= ORIGINAL NOTEBOOK CELL 13 =========

# ============================================================
# BOX 4 — DEFINITION AND VALIDATION OF THE DOW JONES UNIVERSE
# ============================================================

from typing import List
from collections import defaultdict
from google.colab import userdata
import requests
import re

# ============================================================
# DOW JONES UNIVERSE
# ============================================================

DOW_JONES_TICKERS = [
    "AAPL", "AMGN", "AMZN", "AXP", "BA",
    "CAT", "CRM", "CSCO", "CVX", "DIS",
    "GS", "HD", "HON", "IBM", "JNJ",
    "JPM", "KO", "MCD", "MMM", "MRK",
    "MSFT", "NKE", "NVDA", "PG", "SHW",
    "TRV", "UNH", "V", "VZ", "WMT",
]

EXPECTED_NUMBER_OF_TICKERS = 30

# ============================================================
# NORMALIZATION
# ============================================================

def normalize_ticker(ticker: str) -> str:
    return str(ticker).strip().upper().replace(".", "-")


def clean_ticker_list(raw_tickers) -> List[str]:
    cleaned_tickers = []

    for ticker in raw_tickers:
        normalized_ticker = normalize_ticker(ticker)

        if normalized_ticker in {"", "NAN", "NONE"}:
            continue

        cleaned_tickers.append(normalized_ticker)

    return list(dict.fromkeys(cleaned_tickers))


# ============================================================
# VALIDATION
# ============================================================

def validate_dow_jones_tickers(
    ticker_list: List[str]
) -> List[str]:

    validated_tickers = clean_ticker_list(ticker_list)

    if len(validated_tickers) != EXPECTED_NUMBER_OF_TICKERS:
        raise ValueError(
            "Invalid Dow Jones universe: "
            f"{len(validated_tickers)} tickers found "
            f"instead of {EXPECTED_NUMBER_OF_TICKERS} expected."
        )

    return validated_tickers


# ============================================================
# FINAL VARIABLE
# ============================================================

tickers = validate_dow_jones_tickers(DOW_JONES_TICKERS)

# ============================================================
# ORIGINAL OUTPUT
# ============================================================

print("Dow Jones universe configured correctly.")
print(f"Number of tickers: {len(tickers)}")
print("\nDow Jones tickers:")
print(", ".join(tickers))

print(
    "\nSubsequent boxes can proceed "
    "with downloading the 30 historical time series."
)

# ========= ORIGINAL NOTEBOOK CELL 14 =========
# ============================================================
# BOX 5 — DEFINITION OF THE SYSTEM'S SHARED STATE
# ============================================================
# LangGraph uses a Python state shared across the different
# nodes of the workflow.
#
# The state progressively collects:
# - the user's original request;
# - parameters interpreted by the LLM model;
# - ticker universe;
# - raw and cleaned financial data;
# - price, volume, and return matrices;
# - reports produced by the agents;
# - errors and final execution status.
#
# This state:
# - exists only during notebook execution;
# - does not require a database;
# - does not use persistent memory.
#
# DataFrames are temporarily stored in the Python state
# and passed between LangGraph nodes.
# ============================================================


class MarketDataState(TypedDict, total=False):

    # ========================================================
    # CONFIGURATION AND EXECUTION
    # ========================================================

    # Name of the OpenRouter model used by the system.
    model_name: str

    # Primary source used for market data.
    data_source: str

    # Current execution status:
    # initialized, running, completed, or failed.
    execution_status: str

    # Name of the last LangGraph node executed.
    current_node: str

    # ========================================================
    # USER REQUEST
    # ========================================================

    # Original request entered by the user.
    user_request: str

    # Request transformed by the LLM model into structured
    # parameters that can be used by the Python agents.
    parsed_request: Dict[str, Any]

    # ========================================================
    # ANALYSIS UNIVERSE
    # ========================================================

    # Final and validated list of tickers to analyze.
    tickers: List[str]

    # ========================================================
    # MARKET DATA
    # ========================================================

    # Raw data returned by the primary source.
    raw_data: Any

    # Cleaned data organized separately by ticker.
    clean_data: Dict[str, pd.DataFrame]

    # Aligned matrix of closing prices.
    aligned_prices: pd.DataFrame

    # Aligned matrix of volumes.
    aligned_volumes: pd.DataFrame

    # Daily simple returns.
    simple_returns: pd.DataFrame

    # Daily logarithmic returns.
    log_returns: pd.DataFrame

    # ========================================================
    # AGENT REPORTS
    # ========================================================

    # Report produced during data cleaning.
    cleaning_report: pd.DataFrame

    # Report related to the temporal alignment of the series.
    alignment_report: Dict[str, Any]

    # Report produced by the Data Quality Validator.
    validation_report: pd.DataFrame

    # Results of the comparison with a secondary data source.
    cross_source_report: pd.DataFrame

    # Details of the monthly Yahoo-Twelve Data samples.
    cross_source_comparison: pd.DataFrame

    # Monthly samples used in the comparison.
    cross_source_monthly_test: pd.DataFrame

    # General summary of the Twelve Data check:
    # availability, latest date, number of samples, and outcome.
    cross_source_summary: Dict[str, Any]

    # Yahoo date used as the reference for the check.
    cross_source_reference_date: Any

    # True only if at least one price exceeds the allowed threshold.
    cross_source_blocking_failure: bool

    # Assessment produced by the Critic Agent.
    critic_report: Dict[str, Any]

    # Final dataset certification.
    certification: Dict[str, Any]

    # ========================================================
    # ERRORS AND ANOMALIES
    # ========================================================

    # Tickers that the data source failed to download.
    failed_tickers: List[str]

    # Error messages collected during execution.
    errors: List[str]


print("Shared state MarketDataState defined correctly.")
print(f"Number of available fields: {len(MarketDataState.__annotations__)}")

# ========= ORIGINAL NOTEBOOK CELL 15 =========
# ============================================================
# BOX 6 — SUPPORT FUNCTIONS FOR THE LLM MODEL
# ============================================================
# These functions allow us to:
# - extract JSON from model responses;
# - handle any Markdown blocks;
# - send requests to Nebius in a centralized way;
# - use MAIN_MODEL as the primary model;
# - use NVIDIA Nemotron 3 Super 120B as the fallback model;
# - try the fallback ONLY if the primary model fails;
# - limit each call through a timeout;
# - disable automatic client retries;
# - perform only one manual retry if Nebius returns
#   an empty response;
# - prevent a transient error from the primary model
#   from immediately interrupting the entire question_graph.
# ============================================================


# ============================================================
# CONFIGURATION
# ============================================================

LLM_TIMEOUT_SECONDS = 60.0

LLM_MAX_RETRIES = 0

LLM_EMPTY_RESPONSE_RETRY = 1

LLM_RETRY_WAIT_SECONDS = 1.0


# ------------------------------------------------------------
# FALLBACK MODEL
# ------------------------------------------------------------
# MAIN_MODEL is defined in the previous boxes.
#
# If BOX 3 has already been executed, the existing
# FALLBACK_MODEL_NAME is reused.
#
# Otherwise, NVIDIA Nemotron 3 Super 120B is used directly.
# ------------------------------------------------------------

LLM_FALLBACK_MODEL = globals().get(
    "FALLBACK_MODEL_NAME",
    "nvidia/nemotron-3-super-120b-a12b"
)


if MAIN_MODEL == LLM_FALLBACK_MODEL:

    raise ValueError(
        "MAIN_MODEL and LLM_FALLBACK_MODEL "
        "must be two different models."
    )


# ============================================================
# JSON EXTRACTION
# ============================================================

def extract_json_from_text(
    text: str
) -> Dict[str, Any]:

    if (
        not isinstance(
            text,
            str
        )
        or not text.strip()
    ):

        raise ValueError(
            "The model response is empty "
            "or is not a string."
        )

    cleaned_text = (
        text
        .strip()
        .replace(
            "```json",
            ""
        )
        .replace(
            "```JSON",
            ""
        )
        .replace(
            "```",
            ""
        )
        .strip()
    )

    try:

        parsed_json = json.loads(
            cleaned_text
        )

    except json.JSONDecodeError:

        start_position = (
            cleaned_text.find(
                "{"
            )
        )

        end_position = (
            cleaned_text.rfind(
                "}"
            )
        )

        if (
            start_position == -1
            or end_position == -1
        ):

            raise ValueError(
                "The model response does not contain "
                "a recognizable JSON object."
            )

        json_text = cleaned_text[
            start_position:
            end_position + 1
        ]

        try:

            parsed_json = json.loads(
                json_text
            )

        except json.JSONDecodeError as error:

            raise ValueError(
                "The model returned JSON-like text, "
                "but with invalid syntax.\n\n"
                f"Response received:\n{cleaned_text}"
            ) from error

    if not isinstance(
        parsed_json,
        dict
    ):

        raise ValueError(
            "The JSON response must be "
            "a Python dictionary."
        )

    return parsed_json


# ============================================================
# SINGLE NEBIUS CALL
# ============================================================

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
            {
                "role": "system",
                "content": system_instruction
            },
            {
                "role": "user",
                "content": user_content
            }
        ]
    )


# ============================================================
# CENTRALIZED MODEL CALL
# ============================================================

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
        + "\n\n"
        + "Return exclusively a single valid JSON object. "
        + "Do not use Markdown blocks, comments, or additional text."
    )


    # --------------------------------------------------------
    # PRIMARY MODEL FOR THE CALL
    # --------------------------------------------------------

    requested_model = (
        model
        if isinstance(
            model,
            str
        )
        and model.strip()
        else MAIN_MODEL
    )


    # --------------------------------------------------------
    # FALLBACK SEQUENCE
    # --------------------------------------------------------
    # Normally:
    #
    # NVIDIA Nemotron 3 Ultra 550B
    #       ↓ if it fails
    # NVIDIA Nemotron 3 Super 120B
    #
    # We still avoid duplication if the caller
    # directly requests the fallback model.
    # --------------------------------------------------------

    models_to_try = [
        requested_model
    ]

    if (
        LLM_FALLBACK_MODEL
        not in models_to_try
    ):

        models_to_try.append(
            LLM_FALLBACK_MODEL
        )


    total_attempts_per_model = (
        1
        + LLM_EMPTY_RESPONSE_RETRY
    )

    model_errors = {}


    # ========================================================
    # PRIMARY → FALLBACK LOOP
    # ========================================================

    for current_model in models_to_try:

        last_model_error = None


        for attempt in range(
            1,
            total_attempts_per_model + 1
        ):

            try:

                response = _call_openrouter_once(
                    system_instruction=(
                        complete_system_instruction
                    ),
                    user_content=(
                        user_content
                    ),
                    model=(
                        current_model
                    ),
                    temperature=(
                        temperature
                    )
                )


                # ------------------------------------------------
                # MISSING RESPONSE
                # ------------------------------------------------

                if response is None:

                    raise RuntimeError(
                        "Nebius did not return "
                        "any response."
                    )


                # ------------------------------------------------
                # RESPONSE WITH CHOICE
                # ------------------------------------------------

                if response.choices:

                    response_text = (
                        response
                        .choices[
                            0
                        ]
                        .message
                        .content
                    )

                    if (
                        response_text
                        is not None
                        and str(
                            response_text
                        ).strip()
                    ):

                        try:

                            parsed_response = (
                                extract_json_from_text(
                                    response_text
                                )
                            )

                        except Exception as error:

                            raise ValueError(
                                "The model responded, "
                                "but did not produce valid JSON. "
                                f"Model: {current_model}. "
                                f"Error: {error}"
                            ) from error


                        # ----------------------------------------
                        # MODEL ACTUALLY USED
                        # ----------------------------------------

                        parsed_response.setdefault(
                            "_llm_model_used",
                            current_model
                        )

                        parsed_response.setdefault(
                            "_llm_fallback_used",
                            (
                                current_model
                                != requested_model
                            )
                        )

                        return parsed_response


                # ------------------------------------------------
                # EMPTY RESPONSE
                # ------------------------------------------------

                last_model_error = RuntimeError(
                    "Nebius returned "
                    "an empty response."
                )


            except Exception as error:

                last_model_error = error


            # ----------------------------------------------------
            # MANUAL RETRY ON THE SAME MODEL
            # ----------------------------------------------------

            if (
                attempt
                < total_attempts_per_model
            ):

                time.sleep(
                    LLM_RETRY_WAIT_SECONDS
                )

                continue


        # ========================================================
        # MODEL FAILED
        # ========================================================

        model_errors[
            current_model
        ] = str(
            last_model_error
        )


        # If another model exists in the loop,
        # execution automatically continues with the fallback.


    # ============================================================
    # ALL MODELS FAILED
    # ============================================================

    error_details = "\n".join(
        [
            f"- {model_name}: {error_message}"
            for model_name, error_message
            in model_errors.items()
        ]
    )

    raise RuntimeError(
        "None of the configured models "
        "completed the call successfully.\n\n"
        f"Primary model: {requested_model}\n"
        f"Fallback model: {LLM_FALLBACK_MODEL}\n\n"
        "Errors detected:\n"
        f"{error_details}"
    )


# ============================================================
# CHECK
# ============================================================

print(
    "Nebius support functions defined correctly."
)

print(
    f"MAIN_MODEL: {MAIN_MODEL}"
)

print(
    f"FALLBACK_MODEL: {LLM_FALLBACK_MODEL}"
)

print(
    f"Timeout per call: {LLM_TIMEOUT_SECONDS:.0f} seconds"
)

print(
    f"Automatic client retries: {LLM_MAX_RETRIES}"
)

print(
    f"Manual retries per model on empty response: "
    f"{LLM_EMPTY_RESPONSE_RETRY}"
)

print(
    "LLM sequence: "
    f"{MAIN_MODEL} → {LLM_FALLBACK_MODEL}"
)

# ========= ORIGINAL NOTEBOOK CELL 16 =========
# ============================================================
# BOX 7 — GENERAL FUNCTION FOR DISPLAYING AGENT OUTPUTS
# ============================================================

def inspect_agent_output(
    agent_name,
    result,
    rows=5
):

    print("\n" + "=" * 80)
    print(f"AGENT OUTPUT: {agent_name}")
    print("=" * 80)

    if result is None:

        print("No result returned.")
        return

    if not isinstance(result, dict):

        print(result)
        return

    for key, value in result.items():

        print("\n" + "-" * 80)
        print(f"OUTPUT: {key}")
        print(f"TYPE: {type(value).__name__}")
        print("-" * 80)

        if isinstance(value, pd.DataFrame):

            print(
                f"Dimensions: "
                f"{value.shape[0]} rows x "
                f"{value.shape[1]} columns"
            )

            if value.empty:

                print("Empty DataFrame.")

            else:

                print(
                    value
                    .head(rows)
                    .to_string()
                )

        elif isinstance(value, pd.Series):

            print(
                f"Number of elements: "
                f"{len(value)}"
            )

            if value.empty:

                print("Empty Series.")

            else:

                print(
                    value
                    .head(rows)
                    .to_string()
                )

        elif isinstance(value, dict):

            print(
                f"Number of elements: "
                f"{len(value)}"
            )

            if len(value) == 0:

                print("Empty dictionary.")

            else:

                for sub_key, sub_value in list(
                    value.items()
                )[:rows]:

                    print(f"\n{sub_key}")

                    if isinstance(
                        sub_value,
                        pd.DataFrame
                    ):

                        if sub_value.empty:

                            print("Empty DataFrame.")

                        else:

                            print(
                                sub_value
                                .head(rows)
                                .to_string()
                            )

                    elif isinstance(
                        sub_value,
                        pd.Series
                    ):

                        if sub_value.empty:

                            print("Empty Series.")

                        else:

                            print(
                                sub_value
                                .head(rows)
                                .to_string()
                            )

                    elif isinstance(
                        sub_value,
                        dict
                    ):

                        print(
                            json.dumps(
                                sub_value,
                                ensure_ascii=False,
                                indent=2,
                                default=str
                            )
                        )

                    else:

                        print(sub_value)

        elif isinstance(value, list):

            print(
                f"Number of elements: "
                f"{len(value)}"
            )

            if len(value) == 0:

                print("Empty list.")

            else:

                for item in value[:rows]:

                    if isinstance(item, dict):

                        print(
                            json.dumps(
                                item,
                                ensure_ascii=False,
                                indent=2,
                                default=str
                            )
                        )

                    else:

                        print(item)

        elif isinstance(value, tuple):

            print(
                f"Number of elements: "
                f"{len(value)}"
            )

            for item in value[:rows]:
                print(item)

        else:

            print(value)

    print("\n" + "=" * 80)
    print(f"END OUTPUT: {agent_name}")
    print("=" * 80)


print(
    "inspect_agent_output function defined."
)


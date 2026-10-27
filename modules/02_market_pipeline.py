# Original Colab cells, unchanged and in their original execution order.
# Run via run.py to preserve the notebook shared namespace.

# ========= ORIGINAL NOTEBOOK CELL 17 =========
# ============================================================
# BOX 8 — AGENT 1: REQUEST INTERPRETATION
# ============================================================
# This agent receives a natural-language request
# and transforms it into structured parameters.
#
# The LLM model is used exclusively to:
# - identify the user's intent;
# - identify the requested tickers;
# - interpret the time period;
# - define the required frequency and fields.
#
# The model must not:
# - download data;
# - perform financial calculations;
# - comment on the markets;
# - provide financial advice;
# - invent tickers.
#
# Dow Jones securities are traded partly on the NYSE
# and partly on Nasdaq. Both exchanges follow the same
# primary calendar and the same regular New York trading hours.
#
# The expressions "today", "up to today", "current date", and
# "up to now" are therefore interpreted as the latest
# fully completed New York stock exchange trading session,
# already calculated in BOX 1 and stored in DEFAULT_END_DATE.
#
# If the request concerns the entire Dow Jones, the
# "tickers" field must contain:
#
#       "all"
# ============================================================

def request_interpreter_agent(
    state: MarketDataState
) -> Dict[str, Any]:
    """
    Interprets the user's request and returns
    a structured configuration for subsequent nodes.

    If the model is unavailable or returns
    invalid output, a default configuration
    consistent with the project is applied.
    """

    # --------------------------------------------------------
    # ORIGINAL REQUEST
    # --------------------------------------------------------

    user_request = state.get(
        "user_request",
        "Retrieve and prepare the Dow Jones historical time series "
        "from 2010 to today."
    )

    # Uses the tickers already retrieved and validated in BOX 4.
    available_tickers = state.get(
        "tickers",
        tickers
    )

    # --------------------------------------------------------
    # MODEL INSTRUCTIONS
    # --------------------------------------------------------

    system_instruction = """
You are the Request Interpreter of a quantitative financial system.

The domain is limited to Dow Jones Industrial Average securities.

You must transform the user's request into a single JSON object.

You must not:
- perform calculations;
- comment on the markets;
- provide financial advice;
- invent tickers;
- invent dates;
- add text outside the JSON.

The JSON must follow this structure:

{
    "intent": "prepare_market_dataset",
    "universe": "dow_jones",
    "tickers": "all",
    "start_date": "YYYY-MM-DD",
    "end_date": "YYYY-MM-DD",
    "interval": "1d",
    "fields": [
        "Open",
        "High",
        "Low",
        "Close",
        "Adj Close",
        "Volume"
    ]
}

Rules:

1. The "intent" field must be:
   "prepare_market_dataset".

2. The "universe" field must be:
   "dow_jones".

3. If the user requests all Dow Jones securities,
   the "tickers" field must be the string:
   "all".

4. If the user specifies particular tickers,
   the "tickers" field must be a list of strings.

5. You may use only tickers present in the list
   of available tickers provided in the request content.

6. If the user does not specify a start date,
   use:
   "2010-01-01".

7. If the user uses expressions such as:
   - today;
   - current date;
   - up to now;
   - up to today;

   use the latest fully completed New York stock exchange
   trading session provided in the request content.

8. If the user does not specify an end date,
   use the latest fully completed New York stock exchange
   trading session provided in the request content.

9. The end date cannot be later than the latest fully completed
   New York stock exchange trading session provided.

10. If the user does not specify a frequency,
    use:
    "1d".

11. The "fields" field must always contain:
    "Open",
    "High",
    "Low",
    "Close",
    "Adj Close",
    "Volume".
"""

    # --------------------------------------------------------
    # CONTENT SENT TO THE MODEL
    # --------------------------------------------------------

    user_content = json.dumps(
        {
            "last_completed_new_york_session": DEFAULT_END_DATE,
            "available_dow_jones_tickers": available_tickers,
            "user_request": user_request
        },
        ensure_ascii=False
    )

    # --------------------------------------------------------
    # FALLBACK CONFIGURATION
    # --------------------------------------------------------

    fallback_request = {
        "intent": "prepare_market_dataset",
        "universe": "dow_jones",
        "tickers": "all",
        "start_date": DEFAULT_START_DATE,
        "end_date": DEFAULT_END_DATE,
        "interval": DEFAULT_INTERVAL,
        "fields": [
            "Open",
            "High",
            "Low",
            "Close",
            "Adj Close",
            "Volume"
        ]
    }

    # --------------------------------------------------------
    # OPENROUTER MODEL CALL
    # --------------------------------------------------------

    try:

        parsed_request = call_llm_json(
            system_instruction=system_instruction,
            user_content=user_content
        )

        # ----------------------------------------------------
        # MINIMAL RESPONSE VALIDATION
        # ----------------------------------------------------

        required_fields = {
            "intent",
            "universe",
            "tickers",
            "start_date",
            "end_date",
            "interval",
            "fields"
        }

        missing_fields = required_fields.difference(
            parsed_request.keys()
        )

        if missing_fields:
            raise ValueError(
                "The model did not return the required fields: "
                f"{sorted(missing_fields)}"
            )

        # Prevents the model from modifying the domain.
        parsed_request["intent"] = "prepare_market_dataset"
        parsed_request["universe"] = "dow_jones"

        # Prevents the end date from exceeding the latest
        # fully completed New York stock exchange trading session.
        parsed_end_date = pd.Timestamp(
            parsed_request["end_date"]
        ).normalize()

        maximum_end_date = pd.Timestamp(
            DEFAULT_END_DATE
        ).normalize()

        if parsed_end_date > maximum_end_date:
            parsed_request["end_date"] = DEFAULT_END_DATE

        # Normalization of specific tickers.
        requested_tickers = parsed_request.get("tickers")

        if isinstance(requested_tickers, list):

            normalized_requested_tickers = [
                normalize_ticker(ticker)
                for ticker in requested_tickers
            ]

            invalid_tickers = [
                ticker
                for ticker in normalized_requested_tickers
                if ticker not in available_tickers
            ]

            if invalid_tickers:
                raise ValueError(
                    "The model returned tickers that do not belong "
                    "to the Dow Jones universe: "
                    f"{invalid_tickers}"
                )

            parsed_request["tickers"] = list(
                dict.fromkeys(normalized_requested_tickers)
            )

        elif requested_tickers != "all":

            raise ValueError(
                'The "tickers" field must be "all" '
                "or a list of tickers."
            )

        # Ensures that the financial fields are always those
        # required by the project.
        parsed_request["fields"] = [
            "Open",
            "High",
            "Low",
            "Close",
            "Adj Close",
            "Volume"
        ]

        return {
            "parsed_request": parsed_request,
            "current_node": "request_interpreter_agent",
            "execution_status": "running",
            "errors": state.get("errors", [])
        }

    # --------------------------------------------------------
    # FALLBACK IN CASE OF ERROR
    # --------------------------------------------------------

    except Exception as error:

        errors = state.get(
            "errors",
            []
        ).copy()

        errors.append(
            "Request Interpreter unavailable or response "
            f"invalid: {error}. "
            "Default request applied."
        )

        return {
            "parsed_request": fallback_request,
            "current_node": "request_interpreter_agent",
            "execution_status": "running",
            "errors": errors
        }


print("Request Interpreter Agent defined correctly.")

# ========= ORIGINAL NOTEBOOK CELL 18 =========
# ============================================================
# BOX 9 — AGENT 2: TICKER RESOLUTION AND VALIDATION
# ============================================================
# This node:
# - reads the tickers interpreted by the Request Interpreter;
# - transforms the "all" request into the complete list;
# - normalizes tickers into Yahoo Finance format;
# - verifies that they belong to the Dow Jones;
# - removes duplicates;
# - records any invalid tickers;
# - applies the entire Dow Jones universe as fallback
#   if no valid ticker is identified.
#
# This agent does not use the LLM model.
# The check is performed entirely in Python.
# ============================================================

def ticker_resolution_agent(
    state: MarketDataState
) -> Dict[str, Any]:
    """
    Resolves and validates the tickers requested by the user.

    Returns in the state:
    - the final list of tickers to analyze;
    - any error messages;
    - the name of the current node;
    - the execution status.
    """

    # --------------------------------------------------------
    # RETRIEVAL OF THE STRUCTURED REQUEST
    # --------------------------------------------------------

    parsed_request = state.get(
        "parsed_request",
        {}
    )

    # Uses the universe already retrieved and validated in BOX 4.
    available_tickers = state.get(
        "tickers",
        tickers
    )

    available_tickers = clean_ticker_list(
        available_tickers
    )

    if len(available_tickers) == 0:
        raise ValueError(
            "The available ticker universe is empty."
        )

    requested_tickers = parsed_request.get(
        "tickers",
        "all"
    )

    errors = state.get(
        "errors",
        []
    ).copy()

    invalid_tickers = []

    # --------------------------------------------------------
    # CASE 1 — ENTIRE DOW JONES UNIVERSE
    # --------------------------------------------------------

    if requested_tickers == "all":

        selected_tickers = available_tickers.copy()

    # --------------------------------------------------------
    # CASE 2 — LIST OF SPECIFIC TICKERS
    # --------------------------------------------------------

    elif isinstance(requested_tickers, list):

        normalized_requested = clean_ticker_list(
            requested_tickers
        )

        selected_tickers = [
            ticker
            for ticker in normalized_requested
            if ticker in available_tickers
        ]

        invalid_tickers = [
            ticker
            for ticker in normalized_requested
            if ticker not in available_tickers
        ]

    # --------------------------------------------------------
    # CASE 3 — SINGLE TICKER AS A STRING
    # --------------------------------------------------------

    elif isinstance(requested_tickers, str):

        normalized_ticker = normalize_ticker(
            requested_tickers
        )

        if normalized_ticker in available_tickers:

            selected_tickers = [
                normalized_ticker
            ]

        else:

            selected_tickers = []
            invalid_tickers = [
                normalized_ticker
            ]

    # --------------------------------------------------------
    # CASE 4 — INVALID FORMAT
    # --------------------------------------------------------

    else:

        selected_tickers = []

        errors.append(
            'Invalid format for the "tickers" field. '
            'Only "all", a string, '
            "or a list of tickers are accepted."
        )

    # --------------------------------------------------------
    # RECORDING INVALID TICKERS
    # --------------------------------------------------------

    if invalid_tickers:

        errors.append(
            "Tickers excluded because they do not belong "
            f"to the Dow Jones universe: {invalid_tickers}"
        )

    # --------------------------------------------------------
    # REMOVAL OF ANY DUPLICATES
    # --------------------------------------------------------

    selected_tickers = list(
        dict.fromkeys(selected_tickers)
    )

    # --------------------------------------------------------
    # FALLBACK
    # --------------------------------------------------------

    if len(selected_tickers) == 0:

        errors.append(
            "No valid ticker identified. "
            "The entire Dow Jones universe will be used."
        )

        selected_tickers = available_tickers.copy()

    # --------------------------------------------------------
    # STATE UPDATE
    # --------------------------------------------------------

    return {
        "tickers": selected_tickers,
        "current_node": "ticker_resolution_agent",
        "execution_status": "running",
        "errors": errors
    }


print("Ticker Resolution Agent defined correctly.")

# ========= ORIGINAL NOTEBOOK CELL 19 =========
# ============================================================
# BOX 10 — AGENT 3: HISTORICAL TIME SERIES DOWNLOAD
# ============================================================
# This agent:
# - downloads Open, High, Low, Close, Adj Close, and Volume;
# - uses Yahoo Finance through yfinance;
# - keeps the raw data without cleaning or transforming it;
# - performs up to three attempts in case of error;
# - correctly handles the end date;
# - limits the download to the latest completed trading session
#   of the New York stock exchanges, already defined in BOX 1;
# - excludes any rows after that session;
# - verifies which tickers actually contain data;
# - records missing tickers and errors;
# - updates the shared LangGraph state.
#
# The dataset uses DEFAULT_END_DATE as its maximum limit,
# corresponding to the latest fully completed trading session
# of the New York stock exchanges.
#
# No value is yet removed, interpolated,
# aligned, or transformed, except for the exclusion of any
# dates after the established time limit.
# ============================================================


def market_data_collector_agent(
    state: MarketDataState
) -> Dict[str, Any]:
    """
    Downloads from Yahoo Finance the historical time series
    of the tickers selected by the previous node.

    Returns:
    - raw data;
    - tickers without data;
    - data source;
    - node status;
    - any errors.
    """

    # --------------------------------------------------------
    # RETRIEVAL OF PARAMETERS FROM THE STATE
    # --------------------------------------------------------

    parsed_request = state.get(
        "parsed_request",
        {}
    )

    selected_tickers = state.get(
        "tickers",
        []
    )

    errors = state.get(
        "errors",
        []
    ).copy()

    if not selected_tickers:
        raise ValueError(
            "The list of tickers to download is empty."
        )

    start_date = parsed_request.get(
        "start_date",
        DEFAULT_START_DATE
    )

    requested_end_date = parsed_request.get(
        "end_date",
        DEFAULT_END_DATE
    )

    interval = parsed_request.get(
        "interval",
        DEFAULT_INTERVAL
    )

    # --------------------------------------------------------
    # DATE VALIDATION
    # --------------------------------------------------------

    try:

        start_datetime = pd.to_datetime(
            start_date,
            format="%Y-%m-%d"
        ).normalize()

        requested_end_datetime = pd.to_datetime(
            requested_end_date,
            format="%Y-%m-%d"
        ).normalize()

        last_completed_session = pd.to_datetime(
            DEFAULT_END_DATE,
            format="%Y-%m-%d"
        ).normalize()

    except Exception as error:

        raise ValueError(
            "Dates must be expressed in YYYY-MM-DD format."
        ) from error

    # The actual end date cannot exceed the latest
    # completed trading session of the New York stock exchanges.
    end_datetime = min(
        requested_end_datetime,
        last_completed_session
    )

    if start_datetime >= end_datetime:

        raise ValueError(
            "The start date must be earlier "
            "than the end date."
        )

    if requested_end_datetime > last_completed_session:

        errors.append(
            "The requested end date was later than the latest "
            "completed trading session of the New York stock exchanges "
            f"and has been limited to {DEFAULT_END_DATE}."
        )

    # --------------------------------------------------------
    # END DATE ADJUSTMENT
    # --------------------------------------------------------
    # In yfinance, the end parameter is exclusive.
    #
    # To include end_datetime in the requested period,
    # the following day is therefore passed to yfinance.
    # end_datetime is already limited to the latest completed
    # trading session of the New York stock exchanges.
    # --------------------------------------------------------

    download_end_date = (
        end_datetime + timedelta(days=1)
    ).strftime("%Y-%m-%d")

    # --------------------------------------------------------
    # DOWNLOAD WITH A MAXIMUM OF THREE ATTEMPTS
    # --------------------------------------------------------

    raw_data = None
    maximum_attempts = 3

    for attempt in range(1, maximum_attempts + 1):

        try:

            raw_data = yf.download(
                tickers=selected_tickers,
                start=start_datetime.strftime("%Y-%m-%d"),
                end=download_end_date,
                interval=interval,
                group_by="ticker",
                auto_adjust=False,
                actions=False,
                progress=False,
                threads=True
            )

            if (
                raw_data is not None
                and isinstance(raw_data, pd.DataFrame)
                and not raw_data.empty
            ):
                break

            errors.append(
                f"Download attempt {attempt}: "
                "Yahoo Finance returned an empty DataFrame."
            )

        except Exception as error:

            errors.append(
                f"Download attempt {attempt} failed: "
                f"{type(error).__name__}: {error}"
            )

        if attempt < maximum_attempts:
            time.sleep(2)

    # --------------------------------------------------------
    # OVERALL RESULT CHECK
    # --------------------------------------------------------

    if (
        raw_data is None
        or not isinstance(raw_data, pd.DataFrame)
        or raw_data.empty
    ):

        raise RuntimeError(
            "Yahoo Finance did not return any data "
            "after three attempts."
        )

    # Sorts the index chronologically without modifying
    # the downloaded values.
    raw_data = raw_data.sort_index()

    # --------------------------------------------------------
    # LIMIT TO THE LATEST COMPLETED TRADING SESSION
    # --------------------------------------------------------
    # Any rows after the actual end date
    # are excluded before continuing the workflow.
    # --------------------------------------------------------

    normalized_index = pd.to_datetime(
        raw_data.index
    )

    if normalized_index.tz is not None:
        normalized_index = (
            normalized_index
            .tz_convert("America/New_York")
            .tz_localize(None)
        )

    raw_data.index = normalized_index

    raw_data = raw_data.loc[
        raw_data.index.normalize() <= end_datetime
    ].copy()

    if raw_data.empty:

        raise RuntimeError(
            "The dataset is empty after applying the limit "
            "corresponding to the latest completed trading session "
            "of the New York stock exchanges."
        )

    downloaded_last_date = pd.Timestamp(
        raw_data.index.max()
    ).normalize()

    # The maximum date present can never be later
    # than the actual end date.
    if downloaded_last_date > end_datetime:

        raise RuntimeError(
            "The dataset contains a date later "
            "than the latest allowed trading session."
        )

    # --------------------------------------------------------
    # IDENTIFICATION OF TICKERS WITH ACTUAL DATA
    # --------------------------------------------------------

    downloaded_tickers = []
    failed_tickers = []

    if len(selected_tickers) == 1:

        # With a single ticker, yfinance may return simple
        # columns instead of a MultiIndex.
        ticker = selected_tickers[0]

        if raw_data.dropna(how="all").empty:
            failed_tickers.append(ticker)
        else:
            downloaded_tickers.append(ticker)

    elif isinstance(raw_data.columns, pd.MultiIndex):

        first_level_values = set(
            str(value)
            for value in raw_data.columns.get_level_values(0)
        )

        second_level_values = set(
            str(value)
            for value in raw_data.columns.get_level_values(1)
        )

        for ticker in selected_tickers:

            ticker_frame = None

            # Case group_by="ticker":
            # first level = ticker
            # second level = field.
            if ticker in first_level_values:

                try:
                    ticker_frame = raw_data[ticker]
                except Exception:
                    ticker_frame = None

            # Defensive handling of the opposite format:
            # first level = field
            # second level = ticker.
            elif ticker in second_level_values:

                try:
                    ticker_frame = raw_data.xs(
                        ticker,
                        axis=1,
                        level=1
                    )
                except Exception:
                    ticker_frame = None

            if (
                ticker_frame is None
                or ticker_frame.empty
                or ticker_frame.dropna(how="all").empty
            ):
                failed_tickers.append(ticker)
            else:
                downloaded_tickers.append(ticker)

    else:

        # Unexpected format: the anomaly is recorded.
        errors.append(
            "Yahoo Finance returned non-MultiIndex columns "
            "for a request with multiple tickers. "
            "The structure will be verified in subsequent nodes."
        )

        downloaded_tickers = selected_tickers.copy()

    # --------------------------------------------------------
    # RECORDING TICKERS WITHOUT DATA
    # --------------------------------------------------------

    if failed_tickers:

        errors.append(
            "Yahoo Finance did not return usable data "
            f"for the following tickers: {failed_tickers}"
        )

    if len(downloaded_tickers) == 0:

        raise RuntimeError(
            "None of the requested tickers contains usable data."
        )

    # --------------------------------------------------------
    # VERIFICATION OUTPUT
    # --------------------------------------------------------

    print(
        "Requested end date:",
        requested_end_datetime.strftime("%Y-%m-%d")
    )

    print(
        "Latest completed trading session of the New York stock exchanges:",
        last_completed_session.strftime("%Y-%m-%d")
    )

    print(
        "Actual download end date:",
        end_datetime.strftime("%Y-%m-%d")
    )

    print(
        "Latest date present in the Yahoo dataset:",
        downloaded_last_date.strftime("%Y-%m-%d")
    )

    print(
        "Tickers with data:",
        len(downloaded_tickers)
    )

    print(
        "Tickers without data:",
        len(failed_tickers)
    )

    # --------------------------------------------------------
    # STATE UPDATE
    # --------------------------------------------------------

    return {
        "raw_data": raw_data,
        "failed_tickers": failed_tickers,
        "data_source": "Yahoo Finance via yfinance",
        "current_node": "market_data_collector_agent",
        "execution_status": "running",
        "errors": errors
    }


print("Market Data Collector Agent defined correctly.")

# ========= ORIGINAL NOTEBOOK CELL 20 =========
# ============================================================
# BOX 11 — FUNCTION FOR EXTRACTING DATA FOR A SINGLE TICKER
# ============================================================
# yfinance may return different structures:
#
# 1. MultiIndex columns when multiple tickers are downloaded;
# 2. simple columns when a single ticker is downloaded;
# 3. MultiIndex organized as:
#
#       ticker -> field
#
#    or, in some cases:
#
#       field -> ticker
#
# This function standardizes these structures and returns
# a DataFrame for a single ticker.
#
# The function:
# - does not clean values;
# - does not interpolate missing data;
# - does not modify prices or volumes;
# - does not add missing columns.
#
# Cleaning and validation operations are performed
# in subsequent nodes.
# ============================================================

EXPECTED_COLUMNS = [
    "Open",
    "High",
    "Low",
    "Close",
    "Adj Close",
    "Volume"
]


def extract_single_ticker_dataframe(
    raw_data: pd.DataFrame,
    ticker: str,
    total_tickers: int
) -> pd.DataFrame:
    """
    Extracts from the raw dataset the DataFrame related
    to a single ticker.

    Parameters
    ----------
    raw_data:
        Raw DataFrame returned by yfinance.

    ticker:
        Ticker to extract.

    total_tickers:
        Total number of tickers requested in the download.

    Returns
    -------
    pd.DataFrame
        DataFrame for the single ticker or an empty DataFrame
        if the ticker is not present.
    """

    # --------------------------------------------------------
    # PRELIMINARY CHECKS
    # --------------------------------------------------------

    if raw_data is None:
        return pd.DataFrame()

    if not isinstance(raw_data, pd.DataFrame):
        return pd.DataFrame()

    if raw_data.empty:
        return pd.DataFrame()

    normalized_ticker = normalize_ticker(ticker)

    ticker_data = None

    # --------------------------------------------------------
    # CASE 1 — MULTIINDEX COLUMNS
    # --------------------------------------------------------

    if isinstance(raw_data.columns, pd.MultiIndex):

        level_zero = [
            str(value).strip()
            for value in raw_data.columns.get_level_values(0)
        ]

        level_one = [
            str(value).strip()
            for value in raw_data.columns.get_level_values(1)
        ]

        # Expected structure with group_by="ticker":
        #
        # level 0 = ticker
        # level 1 = field
        if normalized_ticker in level_zero:

            try:

                ticker_data = raw_data.xs(
                    normalized_ticker,
                    axis=1,
                    level=0
                ).copy()

            except (KeyError, ValueError):
                ticker_data = None

        # Alternative structure:
        #
        # level 0 = field
        # level 1 = ticker
        elif normalized_ticker in level_one:

            try:

                ticker_data = raw_data.xs(
                    normalized_ticker,
                    axis=1,
                    level=1
                ).copy()

            except (KeyError, ValueError):
                ticker_data = None

        else:

            return pd.DataFrame()

    # --------------------------------------------------------
    # CASE 2 — SIMPLE COLUMNS
    # --------------------------------------------------------

    else:

        # Simple columns are considered valid only
        # when the download concerned a single ticker.
        if total_tickers != 1:
            return pd.DataFrame()

        ticker_data = raw_data.copy()

    # --------------------------------------------------------
    # RESULT CHECK
    # --------------------------------------------------------

    if ticker_data is None:
        return pd.DataFrame()

    if ticker_data.empty:
        return pd.DataFrame()

    # --------------------------------------------------------
    # REMOVAL OF ANY RESIDUAL LEVELS
    # --------------------------------------------------------

    if isinstance(ticker_data.columns, pd.MultiIndex):

        ticker_data.columns = [
            " ".join(
                str(value).strip()
                for value in column
                if str(value).strip()
            )
            for column in ticker_data.columns
        ]

    else:

        ticker_data.columns = [
            str(column).strip()
            for column in ticker_data.columns
        ]

    # --------------------------------------------------------
    # COLUMN NAME NORMALIZATION
    # --------------------------------------------------------

    column_mapping = {
        "AdjClose": "Adj Close",
        "Adj_Close": "Adj Close",
        "Adjusted Close": "Adj Close"
    }

    ticker_data = ticker_data.rename(
        columns=column_mapping
    )

    # Removes any duplicate columns, keeping
    # the first occurrence.
    ticker_data = ticker_data.loc[
        :,
        ~ticker_data.columns.duplicated()
    ]

    # Removes only completely empty columns.
    # Rows with missing values are not removed.
    ticker_data = ticker_data.dropna(
        axis=1,
        how="all"
    )

    # Sorts the index chronologically without altering values.
    ticker_data = ticker_data.sort_index()

    return ticker_data


print(
    "Function for extracting data for a single ticker "
    "defined correctly."
)

# ========= ORIGINAL NOTEBOOK CELL 21 =========
# ============================================================
# BOX 12 — AGENT 4: DATA CLEANING
# ============================================================
# This agent performs, for each ticker:
#
# 1. conversion of the index into date format;
# 2. chronological sorting;
# 3. exclusion of rows after the latest completed trading session
#    of the New York stock exchanges;
# 4. removal of duplicates;
# 5. checking and standardization of columns;
# 6. conversion of columns to numeric format;
# 7. replacement of infinities with temporary NA values;
# 8. removal of completely empty rows and any
#    incomplete trailing rows;
# 9. replacement of the remaining missing values with the
#    previous value from the same column or, if unavailable
#    (e.g. first dataset row), with the next value;
# 10. removal of null or negative prices;
# 11. removal of negative volumes;
# 12. verification of the absence of NA values;
# 13. recording of every intervention performed.
#
# No interpolation is used.
# The only rows removed because of missing values are those
# that are completely empty or any incomplete trailing rows,
# which do not represent consolidated trading sessions.
# ============================================================

def data_cleaning_agent(
    state: MarketDataState
) -> Dict[str, Any]:

    raw_data = state["raw_data"]
    selected_tickers = state["tickers"]

    clean_data = {}
    report_rows = []
    errors = state.get("errors", []).copy()

    # --------------------------------------------------------
    # ACTUAL DATASET END DATE
    # --------------------------------------------------------

    parsed_request = state.get(
        "parsed_request",
        {}
    )

    requested_end_date = parsed_request.get(
        "end_date",
        DEFAULT_END_DATE
    )

    try:

        requested_end_datetime = pd.to_datetime(
            requested_end_date,
            format="%Y-%m-%d"
        ).normalize()

        last_completed_session = pd.to_datetime(
            DEFAULT_END_DATE,
            format="%Y-%m-%d"
        ).normalize()

    except Exception as error:

        raise ValueError(
            "The end date must be expressed "
            "in YYYY-MM-DD format."
        ) from error

    expected_end_datetime = min(
        requested_end_datetime,
        last_completed_session
    )

    for ticker in selected_tickers:

        ticker_df = extract_single_ticker_dataframe(
            raw_data=raw_data,
            ticker=ticker,
            total_tickers=len(selected_tickers)
        )

        if ticker_df.empty:

            errors.append(
                f"{ticker}: no data available."
            )

            continue

        original_rows = len(ticker_df)

        # ----------------------------------------------------
        # DATE CONVERSION AND SORTING
        # ----------------------------------------------------

        ticker_df.index = pd.to_datetime(
            ticker_df.index,
            errors="coerce"
        )

        # If the index contains a time zone, the dates are
        # converted to New York time before removing it.
        if ticker_df.index.tz is not None:

            ticker_df.index = (
                ticker_df.index
                .tz_convert("America/New_York")
                .tz_localize(None)
            )

        invalid_dates = int(
            ticker_df.index.isna().sum()
        )

        ticker_df = ticker_df[
            ~ticker_df.index.isna()
        ]

        ticker_df = ticker_df.sort_index()

        # ----------------------------------------------------
        # EXCLUSION OF DATES AFTER THE LATEST COMPLETED
        # TRADING SESSION OF THE NEW YORK STOCK EXCHANGES
        # ----------------------------------------------------

        rows_after_end_date_mask = (
            ticker_df.index.normalize()
            > expected_end_datetime
        )

        rows_after_end_date_removed = int(
            rows_after_end_date_mask.sum()
        )

        ticker_df = ticker_df.loc[
            ~rows_after_end_date_mask
        ].copy()

        if ticker_df.empty:

            errors.append(
                f"{ticker}: no rows available up to "
                f"the end date {expected_end_datetime.date()}."
            )

            continue

        # ----------------------------------------------------
        # DUPLICATE REMOVAL
        # ----------------------------------------------------

        duplicate_count = int(
            ticker_df.index.duplicated(
                keep="first"
            ).sum()
        )

        ticker_df = ticker_df[
            ~ticker_df.index.duplicated(
                keep="first"
            )
        ]

        # ----------------------------------------------------
        # COLUMN CHECKING AND STANDARDIZATION
        # ----------------------------------------------------

        missing_columns = [
            column
            for column in EXPECTED_COLUMNS
            if column not in ticker_df.columns
        ]

        if missing_columns:

            errors.append(
                f"{ticker}: missing columns added with NA values: "
                f"{missing_columns}"
            )

            for column in missing_columns:
                ticker_df[column] = np.nan

        ticker_df = ticker_df[EXPECTED_COLUMNS]

        # ----------------------------------------------------
        # NUMERIC CONVERSION
        # ----------------------------------------------------

        non_numeric_values = 0

        for column in EXPECTED_COLUMNS:

            original_non_null = int(
                ticker_df[column].notna().sum()
            )

            ticker_df[column] = pd.to_numeric(
                ticker_df[column],
                errors="coerce"
            )

            converted_non_null = int(
                ticker_df[column].notna().sum()
            )

            non_numeric_values += (
                original_non_null - converted_non_null
            )

        # ----------------------------------------------------
        # REPLACEMENT OF INFINITIES
        # ----------------------------------------------------
        # Infinities are temporarily converted into NA values
        # so they can be treated as missing values.
        # ----------------------------------------------------

        infinite_values = int(
            np.isinf(
                ticker_df.select_dtypes(
                    include=[np.number]
                )
            ).sum().sum()
        )

        ticker_df = ticker_df.replace(
            [np.inf, -np.inf],
            np.nan
        )

        missing_before = int(
            ticker_df.isna().sum().sum()
        )

        # ----------------------------------------------------
        # REMOVAL OF COMPLETELY EMPTY ROWS
        # ----------------------------------------------------
        # A completely empty row does not represent an
        # available trading session and must not be reconstructed
        # artificially through ffill or bfill.
        # ----------------------------------------------------

        completely_empty_mask = (
            ticker_df.isna().all(axis=1)
        )

        completely_empty_rows = int(
            completely_empty_mask.sum()
        )

        ticker_df = ticker_df.loc[
            ~completely_empty_mask
        ].copy()

        if ticker_df.empty:

            errors.append(
                f"{ticker}: all rows are empty."
            )

            continue

        # ----------------------------------------------------
        # REMOVAL OF ANY INCOMPLETE TRAILING ROWS
        # ----------------------------------------------------
        # Only incomplete rows located at the end of the
        # series are removed, because they may represent
        # data that have not yet been consolidated.
        #
        # Historical partially incomplete rows continue
        # instead to be handled using the original
        # missing-value replacement logic.
        # ----------------------------------------------------

        trailing_incomplete_rows_removed = 0

        while (
            not ticker_df.empty
            and ticker_df.iloc[-1][
                EXPECTED_COLUMNS
            ].isna().any()
        ):

            ticker_df = ticker_df.iloc[:-1].copy()

            trailing_incomplete_rows_removed += 1

        if ticker_df.empty:

            errors.append(
                f"{ticker}: no complete trading session available "
                "after excluding incomplete trailing rows."
            )

            continue

        # ----------------------------------------------------
        # REPLACEMENT OF REMAINING MISSING VALUES
        # ----------------------------------------------------
        # Each historical NA value is replaced with the exact
        # previous value from the same column.
        #
        # If no previous value exists, as in the first
        # row of the dataset, the exact next value
        # from the same column is used.
        #
        # Completely empty rows and any incomplete trailing rows
        # are not reconstructed.
        # ----------------------------------------------------

        ticker_df = ticker_df.ffill().bfill()

        remaining_missing_values = int(
            ticker_df.isna().sum().sum()
        )

        if remaining_missing_values > 0:

            errors.append(
                f"{ticker}: unable to replace "
                f"{remaining_missing_values} NA values because "
                f"the corresponding column contains no valid value."
            )

            continue

        # ----------------------------------------------------
        # PRICE CHECK
        # ----------------------------------------------------

        price_columns = [
            "Open",
            "High",
            "Low",
            "Close",
            "Adj Close"
        ]

        non_positive_price_mask = (
            ticker_df[price_columns]
            .le(0)
            .any(axis=1)
        )

        non_positive_price_rows = int(
            non_positive_price_mask.sum()
        )

        ticker_df = ticker_df.loc[
            ~non_positive_price_mask
        ]

        # ----------------------------------------------------
        # VOLUME CHECK
        # ----------------------------------------------------

        negative_volume_mask = (
            ticker_df["Volume"] < 0
        )

        negative_volume_rows = int(
            negative_volume_mask.sum()
        )

        ticker_df = ticker_df.loc[
            ~negative_volume_mask
        ]

        # ----------------------------------------------------
        # CLOSING PRICE CHECK
        # ----------------------------------------------------
        # After replacement, there must be no missing values
        # in the Close column.
        # ----------------------------------------------------

        missing_close_rows = int(
            ticker_df["Close"].isna().sum()
        )

        ticker_df.index.name = "Date"

        # ----------------------------------------------------
        # FINAL RESULT CHECK
        # ----------------------------------------------------

        final_rows = len(ticker_df)

        if ticker_df.empty:

            errors.append(
                f"{ticker}: no valid rows after cleaning."
            )

            continue

        final_last_date = pd.Timestamp(
            ticker_df.index.max()
        ).normalize()

        if final_last_date > expected_end_datetime:

            errors.append(
                f"{ticker}: the cleaned end date "
                f"{final_last_date.date()} exceeds the limit "
                f"{expected_end_datetime.date()}."
            )

            continue

        total_cells = max(
            final_rows * len(EXPECTED_COLUMNS),
            1
        )

        final_missing_values = int(
            ticker_df.isna().sum().sum()
        )

        missing_ratio = (
            final_missing_values / total_cells
        )

        clean_data[ticker] = ticker_df

        # ----------------------------------------------------
        # CLEANING OPERATIONS REPORT
        # ----------------------------------------------------

        report_rows.append(
            {
                "Ticker": ticker,
                "Original_Rows": original_rows,
                "Final_Rows": final_rows,
                "Removed_Rows": original_rows - final_rows,
                "Invalid_Dates": invalid_dates,
                "Rows_After_End_Date_Removed":
                    rows_after_end_date_removed,
                "Trailing_Incomplete_Rows_Removed":
                    trailing_incomplete_rows_removed,
                "Duplicates_Removed": duplicate_count,
                "Missing_Columns": missing_columns,
                "Non_Numeric_Values": non_numeric_values,
                "Infinite_Values": infinite_values,
                "Empty_Rows_Removed": completely_empty_rows,
                "Non_Positive_Price_Rows": non_positive_price_rows,
                "Negative_Volume_Rows": negative_volume_rows,
                "Missing_Close_Rows": missing_close_rows,
                "Missing_Values_Before": missing_before,
                "Missing_Values_After": final_missing_values,
                "Missing_Ratio": missing_ratio,
                "Expected_Last_Date": expected_end_datetime,
                "First_Date": ticker_df.index.min(),
                "Last_Date": ticker_df.index.max()
            }
        )

    cleaning_report = pd.DataFrame(
        report_rows
    )

    return {
        "clean_data": clean_data,
        "cleaning_report": cleaning_report,
        "current_node": "data_cleaning_agent",
        "execution_status": "running",
        "errors": errors
    }


print("Data Cleaning Agent defined.")

# ========= ORIGINAL NOTEBOOK CELL 22 =========
# ============================================================
# BOX 13 — AGENT 5: HISTORICAL TIME SERIES ALIGNMENT
# ============================================================
# This agent creates:
#
# - a matrix of adjusted closing prices;
# - a volume matrix;
# - a version aligned on common dates;
# - a report on the loss of observations;
# - a verification of the alignment of all tickers
#   to the expected final date.
#
# For comparisons across securities, only dates
# simultaneously available for all tickers are retained.
#
# The expected final date corresponds to the latest fully
# completed trading session of the New York stock exchanges,
# defined in BOX 1 and stored in DEFAULT_END_DATE.
#
# If one or more tickers do not reach the expected final date,
# the anomaly is recorded without silently moving back
# the dataset reference date.
# ============================================================

def data_alignment_agent(
    state: MarketDataState
) -> Dict[str, Any]:

    clean_data = state["clean_data"]
    errors = state.get("errors", []).copy()

    price_series = {}
    volume_series = {}

    # --------------------------------------------------------
    # EXPECTED DATASET END DATE
    # --------------------------------------------------------

    parsed_request = state.get(
        "parsed_request",
        {}
    )

    requested_end_date = parsed_request.get(
        "end_date",
        DEFAULT_END_DATE
    )

    try:

        requested_end_datetime = pd.to_datetime(
            requested_end_date,
            format="%Y-%m-%d"
        ).normalize()

        last_completed_session = pd.to_datetime(
            DEFAULT_END_DATE,
            format="%Y-%m-%d"
        ).normalize()

    except Exception as error:

        raise ValueError(
            "The end date must be expressed "
            "in YYYY-MM-DD format."
        ) from error

    expected_end_datetime = min(
        requested_end_datetime,
        last_completed_session
    )

    # --------------------------------------------------------
    # SERIES PREPARATION
    # --------------------------------------------------------

    ticker_last_dates = {}
    tickers_missing_expected_date = []

    for ticker, ticker_df in clean_data.items():

        if ticker_df.empty:

            errors.append(
                f"{ticker}: no data available "
                f"for alignment."
            )

            continue

        ticker_df = ticker_df.sort_index()

        ticker_last_date = pd.Timestamp(
            ticker_df.index.max()
        ).normalize()

        ticker_last_dates[ticker] = (
            ticker_last_date
        )

        if expected_end_datetime not in (
            ticker_df.index.normalize()
        ):

            tickers_missing_expected_date.append(
                ticker
            )

        # We use Adj Close when available.
        # If unavailable, we use Close.
        adjusted_close = ticker_df[
            "Adj Close"
        ].copy()

        if adjusted_close.isna().all():

            adjusted_close = ticker_df[
                "Close"
            ].copy()

        price_series[ticker] = adjusted_close
        volume_series[ticker] = ticker_df[
            "Volume"
        ]

    if len(price_series) == 0:

        raise ValueError(
            "No valid series are available for alignment."
        )

    # --------------------------------------------------------
    # CREATION OF COMPLETE MATRICES
    # --------------------------------------------------------

    all_prices = pd.concat(
        price_series,
        axis=1
    ).sort_index()

    all_volumes = pd.concat(
        volume_series,
        axis=1
    ).sort_index()

    rows_before_alignment = len(
        all_prices
    )

    # --------------------------------------------------------
    # ALIGNMENT ON COMMON DATES
    # --------------------------------------------------------

    # We retain only dates common to all tickers.
    aligned_prices = all_prices.dropna(
        how="any"
    )

    aligned_volumes = all_volumes.reindex(
        aligned_prices.index
    )

    rows_after_alignment = len(
        aligned_prices
    )

    removed_rows = (
        rows_before_alignment
        -
        rows_after_alignment
    )

    loss_ratio = (
        removed_rows / rows_before_alignment
        if rows_before_alignment > 0
        else 0
    )

    # --------------------------------------------------------
    # VERIFICATION OF THE FINAL COMMON DATE
    # --------------------------------------------------------

    last_common_date = (
        pd.Timestamp(
            aligned_prices.index.max()
        ).normalize()
        if not aligned_prices.empty
        else None
    )

    expected_date_available_for_all = (
        not tickers_missing_expected_date
    )

    last_common_date_matches_expected = (
        last_common_date
        == expected_end_datetime
        if last_common_date is not None
        else False
    )

    temporal_alignment_passed = (
        expected_date_available_for_all
        and last_common_date_matches_expected
    )

    if tickers_missing_expected_date:

        errors.append(
            "The following tickers do not have data "
            f"for the expected final date "
            f"{expected_end_datetime.strftime('%Y-%m-%d')}: "
            f"{tickers_missing_expected_date}"
        )

    if (
        last_common_date is not None
        and not last_common_date_matches_expected
    ):

        errors.append(
            "The final common date of the dataset "
            f"({last_common_date.strftime('%Y-%m-%d')}) "
            "does not match the expected final date "
            f"({expected_end_datetime.strftime('%Y-%m-%d')})."
        )

    if aligned_prices.empty:

        errors.append(
            "No dates are common to all tickers."
        )

    # --------------------------------------------------------
    # ALIGNMENT REPORT
    # --------------------------------------------------------

    alignment_report = {
        "rows_before_alignment":
            rows_before_alignment,

        "rows_after_alignment":
            rows_after_alignment,

        "removed_rows":
            removed_rows,

        "alignment_loss_ratio":
            loss_ratio,

        "number_of_requested_tickers":
            len(clean_data),

        "number_of_aligned_tickers":
            aligned_prices.shape[1],

        "expected_last_date":
            expected_end_datetime.strftime(
                "%Y-%m-%d"
            ),

        "first_common_date": (
            str(
                aligned_prices.index.min().date()
            )
            if not aligned_prices.empty
            else None
        ),

        "last_common_date": (
            str(
                aligned_prices.index.max().date()
            )
            if not aligned_prices.empty
            else None
        ),

        "tickers_missing_expected_date":
            tickers_missing_expected_date,

        "number_of_tickers_missing_expected_date":
            len(
                tickers_missing_expected_date
            ),

        "expected_date_available_for_all":
            expected_date_available_for_all,

        "last_common_date_matches_expected":
            last_common_date_matches_expected,

        "temporal_alignment_passed":
            temporal_alignment_passed,

        "ticker_last_dates": {
            ticker: ticker_date.strftime(
                "%Y-%m-%d"
            )
            for ticker, ticker_date
            in ticker_last_dates.items()
        }
    }

    # --------------------------------------------------------
    # VERIFICATION OUTPUT
    # --------------------------------------------------------

    print(
        "Expected final date:",
        alignment_report[
            "expected_last_date"
        ]
    )

    print(
        "Latest common date:",
        alignment_report[
            "last_common_date"
        ]
    )

    print(
        "Tickers missing the expected date:",
        alignment_report[
            "number_of_tickers_missing_expected_date"
        ]
    )

    if tickers_missing_expected_date:

        print(
            "List of unaligned tickers:",
            tickers_missing_expected_date
        )

    print(
        "Temporal alignment passed:",
        alignment_report[
            "temporal_alignment_passed"
        ]
    )

    return {
        "aligned_prices": aligned_prices,
        "aligned_volumes": aligned_volumes,
        "alignment_report": alignment_report,
        "current_node": "data_alignment_agent",
        "execution_status": "running",
        "errors": errors
    }


print("Data Alignment Agent defined.")


# ============================================================
# DATA ALIGNMENT AGENT DEVELOPMENT TEST
# ============================================================
# This section is used exclusively to manually verify
# the operation of the agent.
#
# With RUN_DEVELOPMENT_TESTS = False:
# - the agent is defined;
# - the test is not executed;
# - the node will be executed only by the LangGraph workflow.
#
# With RUN_DEVELOPMENT_TESTS = True:
# - the test is executed;
# - the output is displayed;
# - the development state is updated.
# ============================================================

if RUN_DEVELOPMENT_TESTS:

    # --------------------------------------------------------
    # DATA ALIGNMENT AGENT EXECUTION
    # --------------------------------------------------------

    alignment_result = data_alignment_agent(
        state
    )

    state.update(
        alignment_result
    )

    # --------------------------------------------------------
    # OUTPUT DISPLAY
    # --------------------------------------------------------

    inspect_agent_output(
        agent_name="Data Alignment Agent",
        result=alignment_result,
        rows=5
    )

    # --------------------------------------------------------
    # VERIFICATION OF THE STATE UPDATE
    # --------------------------------------------------------

    print(
        "\nalignment_report present in state:",
        "alignment_report" in state
    )

    print(
        "Expected final date:",
        state["alignment_report"].get(
            "expected_last_date"
        )
    )

    print(
        "Latest common date:",
        state["alignment_report"].get(
            "last_common_date"
        )
    )

    print(
        "Temporal alignment passed:",
        state["alignment_report"].get(
            "temporal_alignment_passed"
        )
    )

else:

    print(
        "Data Alignment Agent development test "
        "not executed."
    )

# ========= ORIGINAL NOTEBOOK CELL 23 =========
# ============================================================
# BOX 14 — AGENT 6: PREPARATION OF COMMON VARIABLES
# ============================================================
# This agent prepares the variables that will be used
# by subsequent quantitative analyses:
#
# - simple return;
# - logarithmic return.
#
# Simple return formula:
#
#       P_t / P_(t-1) - 1
#
# Logarithmic return formula:
#
#       ln(P_t / P_(t-1))
#
# Returns are not interpreted by the LLM.
# They are calculated exclusively with Python.
# ============================================================

def feature_preparation_agent(
    state: MarketDataState
) -> Dict[str, Any]:

    aligned_prices = state["aligned_prices"]
    errors = state.get("errors", []).copy()

    if aligned_prices.empty:

        raise ValueError(
            "The aligned price matrix is empty."
        )

    # --------------------------------------------------------
    # SIMPLE RETURNS
    # --------------------------------------------------------

    simple_returns = (
        aligned_prices
        .pct_change(fill_method=None)
        .replace([np.inf, -np.inf], np.nan)
        .dropna(how="all")
    )

    # --------------------------------------------------------
    # LOGARITHMIC RETURNS
    # --------------------------------------------------------

    log_returns = (
        np.log(
            aligned_prices /
            aligned_prices.shift(1)
        )
        .replace([np.inf, -np.inf], np.nan)
        .dropna(how="all")
    )

    # --------------------------------------------------------
    # REPORT
    # --------------------------------------------------------

    feature_report = {
        "number_of_assets": aligned_prices.shape[1],
        "number_of_observations": aligned_prices.shape[0],
        "simple_returns_rows": simple_returns.shape[0],
        "log_returns_rows": log_returns.shape[0],
        "first_return_date": (
            str(simple_returns.index.min().date())
            if not simple_returns.empty
            else None
        ),
        "last_return_date": (
            str(simple_returns.index.max().date())
            if not simple_returns.empty
            else None
        )
    }

    return {
        "simple_returns": simple_returns,
        "log_returns": log_returns,
        "feature_report": feature_report,
        "current_node": "feature_preparation_agent",
        "execution_status": "running",
        "errors": errors
    }


print("Feature Preparation Agent defined.")


# ============================================================
# FEATURE PREPARATION AGENT DEVELOPMENT TEST
# ============================================================
# This section is used exclusively to manually check
# the operation of the agent.
#
# With RUN_DEVELOPMENT_TESTS = False:
# - the agent is defined;
# - the test is not executed;
# - the node will be executed only by the LangGraph workflow.
#
# With RUN_DEVELOPMENT_TESTS = True:
# - the test is executed;
# - the output is displayed;
# - the development state is updated.
# ============================================================

if RUN_DEVELOPMENT_TESTS:

    # --------------------------------------------------------
    # FEATURE PREPARATION AGENT EXECUTION
    # --------------------------------------------------------

    feature_result = feature_preparation_agent(
        state
    )

    state.update(
        feature_result
    )

    # --------------------------------------------------------
    # OUTPUT DISPLAY
    # --------------------------------------------------------

    inspect_agent_output(
        agent_name="Feature Preparation Agent",
        result=feature_result,
        rows=5
    )

    # --------------------------------------------------------
    # VERIFICATION OF THE STATE UPDATE
    # --------------------------------------------------------

    print(
        "\nlog_returns present in state:",
        "log_returns" in state
    )

else:

    print(
        "Feature Preparation Agent development test "
        "not executed."
    )

# ========= ORIGINAL NOTEBOOK CELL 24 =========
# ============================================================
# BOX 15 — AGENT 7: QUALITY VALIDATION
# ============================================================
# This agent checks each ticker based on deterministic rules.
#
# Checks performed:
#
# - minimum number of observations;
# - presence of duplicates;
# - null or negative prices;
# - negative volumes;
# - percentage of missing data;
# - availability of a start and end date;
# - correspondence of the actual end date with the latest
#   completed trading session of the New York stock exchanges,
#   defined in BOX 1 and stored in DEFAULT_END_DATE.
#
# Each ticker receives:
#
# - PASS;
# - WARNING;
# - FAIL;
# - a score from 0 to 100.
# ============================================================

def data_quality_validator_agent(
    state: MarketDataState
) -> Dict[str, Any]:

    clean_data = state["clean_data"]
    cleaning_report = state["cleaning_report"]
    errors = state.get("errors", []).copy()

    validation_rows = []

    if cleaning_report.empty:

        raise ValueError(
            "The cleaning report is empty."
        )

    # --------------------------------------------------------
    # EXPECTED DATASET END DATE
    # --------------------------------------------------------

    parsed_request = state.get(
        "parsed_request",
        {}
    )

    requested_end_date = parsed_request.get(
        "end_date",
        DEFAULT_END_DATE
    )

    try:

        requested_end_datetime = pd.to_datetime(
            requested_end_date,
            format="%Y-%m-%d"
        ).normalize()

        last_completed_session = pd.to_datetime(
            DEFAULT_END_DATE,
            format="%Y-%m-%d"
        ).normalize()

    except Exception as error:

        raise ValueError(
            "The end date must be expressed "
            "in YYYY-MM-DD format."
        ) from error

    expected_end_datetime = min(
        requested_end_datetime,
        last_completed_session
    )

    for _, cleaning_row in cleaning_report.iterrows():

        ticker = cleaning_row["Ticker"]

        ticker_df = clean_data.get(
            ticker,
            pd.DataFrame()
        )

        actual_last_date = (
            pd.Timestamp(
                ticker_df.index.max()
            ).normalize()
            if not ticker_df.empty
            else None
        )

        expected_last_date_check = (
            actual_last_date
            == expected_end_datetime
            if actual_last_date is not None
            else False
        )

        checks = {
            "minimum_observations": (
                len(ticker_df) >= MINIMUM_OBSERVATIONS
            ),
            "no_duplicates": (
                cleaning_row["Duplicates_Removed"] == 0
            ),
            "no_non_positive_prices": (
                cleaning_row["Non_Positive_Price_Rows"] == 0
            ),
            "no_negative_volumes": (
                cleaning_row["Negative_Volume_Rows"] == 0
            ),
            "acceptable_missing_ratio": (
                cleaning_row["Missing_Ratio"]
                <= MAX_MISSING_RATIO
            ),
            "valid_period": (
                pd.notna(
                    cleaning_row["First_Date"]
                )
                and
                pd.notna(
                    cleaning_row["Last_Date"]
                )
            ),
            "expected_last_date": (
                expected_last_date_check
            )
        }

        passed_checks = sum(
            bool(value)
            for value in checks.values()
        )

        total_checks = len(checks)

        quality_score = round(
            100 * passed_checks / total_checks,
            2
        )

        critical_failure = (
            not checks[
                "minimum_observations"
            ]
            or
            not checks[
                "valid_period"
            ]
            or
            not checks[
                "expected_last_date"
            ]
        )

        if critical_failure:

            status = "FAIL"

        elif quality_score < 100:

            status = "WARNING"

        else:

            status = "PASS"

        failed_checks = [
            check_name
            for check_name, check_value
            in checks.items()
            if not check_value
        ]

        if status != "PASS":

            errors.append(
                f"{ticker}: quality validation {status}. "
                f"Failed checks: {failed_checks}"
            )

        validation_rows.append(
            {
                "Ticker": ticker,
                "Status": status,
                "Quality_Score": quality_score,
                "Observations": len(ticker_df),
                "Missing_Ratio":
                    cleaning_row[
                        "Missing_Ratio"
                    ],
                "First_Date":
                    cleaning_row[
                        "First_Date"
                    ],
                "Last_Date":
                    cleaning_row[
                        "Last_Date"
                    ],
                "Expected_Last_Date":
                    expected_end_datetime,
                "Minimum_Observations_Check":
                    checks[
                        "minimum_observations"
                    ],
                "Duplicates_Check":
                    checks[
                        "no_duplicates"
                    ],
                "Prices_Check":
                    checks[
                        "no_non_positive_prices"
                    ],
                "Volumes_Check":
                    checks[
                        "no_negative_volumes"
                    ],
                "Missing_Ratio_Check":
                    checks[
                        "acceptable_missing_ratio"
                    ],
                "Valid_Period_Check":
                    checks[
                        "valid_period"
                    ],
                "Expected_Last_Date_Check":
                    checks[
                        "expected_last_date"
                    ],
                "Failed_Checks":
                    ", ".join(
                        failed_checks
                    )
            }
        )

    validation_report = pd.DataFrame(
        validation_rows
    )

    status_summary = (
        validation_report["Status"]
        .value_counts()
        .to_dict()
        if not validation_report.empty
        else {}
    )

    temporally_aligned_tickers = (
        int(
            validation_report[
                "Expected_Last_Date_Check"
            ].sum()
        )
        if not validation_report.empty
        else 0
    )

    validation_summary = {
        "total_tickers":
            len(validation_report),

        "pass_tickers":
            status_summary.get(
                "PASS",
                0
            ),

        "warning_tickers":
            status_summary.get(
                "WARNING",
                0
            ),

        "fail_tickers":
            status_summary.get(
                "FAIL",
                0
            ),

        "average_quality_score": (
            round(
                validation_report[
                    "Quality_Score"
                ].mean(),
                2
            )
            if not validation_report.empty
            else 0
        ),

        "expected_last_date":
            expected_end_datetime.strftime(
                "%Y-%m-%d"
            ),

        "temporally_aligned_tickers":
            temporally_aligned_tickers,

        "temporally_not_aligned_tickers": (
            len(validation_report)
            - temporally_aligned_tickers
        ),

        "temporal_alignment_passed": (
            temporally_aligned_tickers
            == len(validation_report)
            and not validation_report.empty
        )
    }

    # --------------------------------------------------------
    # VERIFICATION OUTPUT
    # --------------------------------------------------------

    print(
        "Expected final date:",
        validation_summary[
            "expected_last_date"
        ]
    )

    print(
        "Tickers aligned to the expected date:",
        validation_summary[
            "temporally_aligned_tickers"
        ]
    )

    print(
        "Tickers not aligned to the expected date:",
        validation_summary[
            "temporally_not_aligned_tickers"
        ]
    )

    print(
        "Temporal validation passed:",
        validation_summary[
            "temporal_alignment_passed"
        ]
    )

    return {
        "validation_report":
            validation_report,

        "validation_summary":
            validation_summary,

        "current_node":
            "data_quality_validator_agent",

        "execution_status":
            "running",

        "errors":
            errors
    }


print("Data Quality Validator Agent defined.")


# ============================================================
# DATA QUALITY VALIDATOR AGENT DEVELOPMENT TEST
# ============================================================
# This section is used exclusively to manually check
# the operation of the agent.
#
# With RUN_DEVELOPMENT_TESTS = False:
# - the agent is defined;
# - the test is not executed;
# - the node will be executed only by the LangGraph workflow.
#
# With RUN_DEVELOPMENT_TESTS = True:
# - the test is executed;
# - the output is displayed;
# - the development state is updated.
# ============================================================

if RUN_DEVELOPMENT_TESTS:

    # --------------------------------------------------------
    # BOX 15 EXECUTION
    # --------------------------------------------------------

    validation_result = (
        data_quality_validator_agent(
            state
        )
    )

    state.update(
        validation_result
    )

    # --------------------------------------------------------
    # DISPLAY OF BOX 15 OUTPUT
    # --------------------------------------------------------

    inspect_agent_output(
        agent_name=(
            "Data Quality Validator Agent"
        ),
        result=validation_result,
        rows=5
    )

    print(
        "\nExpected final date:",
        state[
            "validation_summary"
        ].get(
            "expected_last_date"
        )
    )

    print(
        "Tickers aligned to the expected date:",
        state[
            "validation_summary"
        ].get(
            "temporally_aligned_tickers"
        )
    )

    print(
        "Temporal validation passed:",
        state[
            "validation_summary"
        ].get(
            "temporal_alignment_passed"
        )
    )

else:

    print(
        "Data Quality Validator Agent development test "
        "not executed."
    )

# ========= ORIGINAL NOTEBOOK CELL 25 =========
# ============================================================
# BOX 16 — AGENT 8: YAHOO CLOSE VS TWELVE DATA CLOSE CHECK
# WITH VISIBLE VERIFICATION ON MONTHLY SAMPLES
# ============================================================
# This agent:
#
# - checks whether Twelve Data responds;
# - checks whether Twelve Data returns usable data;
# - identifies the latest date available in Yahoo Finance;
# - identifies the latest date available in Twelve Data;
# - reports whether Twelve Data is up to date or delayed;
# - aligns the two sources on common dates;
# - selects the first common trading session of each month;
# - compares Close prices over the entire available period;
# - applies the CROSS_SOURCE_TOLERANCE_PERCENT threshold;
# - makes only deviations above the threshold on actually
#   comparable prices blocking;
# - prints all checks during workflow execution;
# - stores reports, samples, and outcome in the state.
#
# Missing data, delayed updates, or failure of Twelve Data
# to respond are reported as diagnostic conditions and do not
# by themselves invalidate the Yahoo dataset.
# ============================================================

def cross_source_checker_agent(
    state: MarketDataState
) -> Dict[str, Any]:

    errors = state.get(
        "errors",
        []
    ).copy()

    # --------------------------------------------------------
    # ACTIVATION CHECK
    # --------------------------------------------------------

    if not ENABLE_CROSS_SOURCE_CHECK:

        cross_source_summary = {
            "enabled": False,
            "twelve_data_responding": False,
            "twelve_data_has_data": False,
            "latest_yahoo_date": None,
            "latest_twelve_data_date": None,
            "sampling_method": (
                "first common trading session of each month"
            ),
            "monthly_samples_tested": 0,
            "samples_above_tolerance": 0,
            "tolerance_percent":
                CROSS_SOURCE_TOLERANCE_PERCENT,
            "blocking_failure": False,
            "overall_status": "DISABLED"
        }

        print("\n" + "=" * 80)
        print("TWELVE DATA TEST")
        print("=" * 80)
        print("Twelve Data check enabled: False")
        print("=" * 80)

        return {
            "cross_source_report":
                pd.DataFrame(),

            "cross_source_comparison":
                pd.DataFrame(),

            "cross_source_monthly_test":
                pd.DataFrame(),

            "cross_source_summary":
                cross_source_summary,

            "cross_source_reference_date":
                None,

            "cross_source_blocking_failure":
                False,

            "current_node":
                "cross_source_checker_agent",

            "execution_status":
                "running",

            "errors":
                errors
        }

    # --------------------------------------------------------
    # YAHOO DATA CHECK
    # --------------------------------------------------------

    clean_data = state.get(
        "clean_data",
        {}
    )

    if not clean_data:

        raise ValueError(
            "state['clean_data'] is not available or is empty."
        )

    selected_tickers = list(
        clean_data.keys()
    )[:MAX_CROSS_SOURCE_TICKERS]

    report_rows = []
    monthly_test_tables = []

    # --------------------------------------------------------
    # TWELVE DATA DOWNLOAD
    # --------------------------------------------------------

    def download_twelve_data_close(
        ticker: str,
        start_date: pd.Timestamp,
        end_date: pd.Timestamp
    ) -> Dict[str, Any]:

        url = (
            "https://api.twelvedata.com/time_series"
        )

        params = {
            "symbol": ticker,
            "interval": "1day",
            "start_date": start_date.strftime(
                "%Y-%m-%d"
            ),
            "end_date": end_date.strftime(
                "%Y-%m-%d"
            ),
            "outputsize": 5000,
            "format": "JSON",
            "timezone": "America/New_York",
            "apikey": TWELVE_DATA_API_KEY
        }

        try:

            response = requests.get(
                url,
                params=params,
                timeout=30
            )

            response.raise_for_status()

            payload = response.json()

        except Exception as error:

            return {
                "responding": False,
                "has_data": False,
                "series": pd.Series(
                    dtype=float,
                    name="Twelve_Data_Close"
                ),
                "message": (
                    f"{type(error).__name__}: {error}"
                )
            }

        if payload.get("status") == "error":

            return {
                "responding": True,
                "has_data": False,
                "series": pd.Series(
                    dtype=float,
                    name="Twelve_Data_Close"
                ),
                "message": (
                    f"Twelve Data error "
                    f"{payload.get('code', 'UNKNOWN')}: "
                    f"{payload.get('message', '')}"
                )
            }

        values = payload.get(
            "values",
            []
        )

        if not values:

            return {
                "responding": True,
                "has_data": False,
                "series": pd.Series(
                    dtype=float,
                    name="Twelve_Data_Close"
                ),
                "message": (
                    "Twelve Data did not return any data."
                )
            }

        twelve_df = pd.DataFrame(
            values
        )

        if (
            "datetime" not in twelve_df.columns
            or "close" not in twelve_df.columns
        ):

            return {
                "responding": True,
                "has_data": False,
                "series": pd.Series(
                    dtype=float,
                    name="Twelve_Data_Close"
                ),
                "message": (
                    "The Twelve Data response does not contain "
                    "the datetime and close columns."
                )
            }

        twelve_df["Date"] = pd.to_datetime(
            twelve_df["datetime"],
            errors="coerce"
        )

        twelve_df[
            "Twelve_Data_Close"
        ] = pd.to_numeric(
            twelve_df["close"],
            errors="coerce"
        )

        twelve_df = (
            twelve_df
            .dropna(
                subset=[
                    "Date",
                    "Twelve_Data_Close"
                ]
            )
            .drop_duplicates(
                subset="Date",
                keep="last"
            )
            .set_index("Date")
            .sort_index()
        )

        if twelve_df.index.tz is not None:

            twelve_df.index = (
                twelve_df.index
                .tz_convert(
                    "America/New_York"
                )
                .tz_localize(None)
            )

        twelve_df.index = (
            twelve_df.index.normalize()
        )

        series = (
            twelve_df[
                "Twelve_Data_Close"
            ]
            .astype(float)
            .rename(
                "Twelve_Data_Close"
            )
        )

        return {
            "responding": True,
            "has_data": not series.empty,
            "series": series,
            "message": ""
        }

    # --------------------------------------------------------
    # MONTHLY SAMPLING
    # --------------------------------------------------------

    def first_common_session_per_month(
        comparison_df: pd.DataFrame
    ) -> pd.DataFrame:
        """
        Selects the first available common trading session
        for each month over the entire overlapping period.
        """

        if comparison_df.empty:

            return comparison_df.copy()

        return (
            comparison_df
            .sort_index()
            .groupby(
                comparison_df.index.to_period(
                    "M"
                )
            )
            .head(1)
            .copy()
        )

    # --------------------------------------------------------
    # TICKER-BY-TICKER COMPARISON
    # --------------------------------------------------------

    for ticker in selected_tickers:

        ticker_df = clean_data.get(
            ticker,
            pd.DataFrame()
        )

        if (
            ticker_df is None
            or ticker_df.empty
            or "Close" not in ticker_df.columns
        ):

            errors.append(
                f"{ticker}: Yahoo data not available."
            )

            report_rows.append(
                {
                    "Ticker": ticker,
                    "Yahoo_Last_Date": None,
                    "Twelve_Responding": False,
                    "Twelve_Has_Data": False,
                    "Twelve_Last_Date": None,
                    "Update_Status": "YAHOO_DATA_ERROR",
                    "Monthly_Samples": 0,
                    "Samples_Above_Tolerance": 0,
                    "Maximum_Difference_Percent": np.nan,
                    "Average_Difference_Percent": np.nan,
                    "Status": "NOT_COMPARABLE",
                    "Blocking_Failure": False
                }
            )

            continue

        yahoo_close = pd.to_numeric(
            ticker_df["Close"],
            errors="coerce"
        )

        yahoo_close.index = pd.to_datetime(
            yahoo_close.index,
            errors="coerce"
        )

        if yahoo_close.index.tz is not None:

            yahoo_close.index = (
                yahoo_close.index
                .tz_convert(
                    "America/New_York"
                )
                .tz_localize(None)
            )

        yahoo_close.index = (
            yahoo_close.index.normalize()
        )

        yahoo_close = (
            yahoo_close[
                ~yahoo_close.index.isna()
            ]
            .dropna()
            .groupby(level=0)
            .last()
            .sort_index()
            .astype(float)
            .rename("Yahoo_Close")
        )

        if yahoo_close.empty:

            errors.append(
                f"{ticker}: Yahoo Close series is empty."
            )

            continue

        yahoo_first_date = (
            yahoo_close.index.min()
        )

        yahoo_last_date = (
            yahoo_close.index.max()
        )

        twelve_result = (
            download_twelve_data_close(
                ticker=ticker,
                start_date=yahoo_first_date,
                end_date=yahoo_last_date
            )
        )

        twelve_responding = (
            twelve_result[
                "responding"
            ]
        )

        twelve_has_data = (
            twelve_result[
                "has_data"
            ]
        )

        twelve_close = (
            twelve_result[
                "series"
            ]
        )

        twelve_message = (
            twelve_result[
                "message"
            ]
        )

        if not twelve_responding:

            report_rows.append(
                {
                    "Ticker": ticker,
                    "Yahoo_Last_Date":
                        yahoo_last_date,
                    "Twelve_Responding": False,
                    "Twelve_Has_Data": False,
                    "Twelve_Last_Date": None,
                    "Update_Status":
                        "APPLICATION_NOT_RESPONDING",
                    "Monthly_Samples": 0,
                    "Samples_Above_Tolerance": 0,
                    "Maximum_Difference_Percent": np.nan,
                    "Average_Difference_Percent": np.nan,
                    "Status": "NOT_COMPARABLE",
                    "Blocking_Failure": False
                }
            )

            errors.append(
                f"{ticker}: {twelve_message}"
            )

            continue

        if not twelve_has_data:

            report_rows.append(
                {
                    "Ticker": ticker,
                    "Yahoo_Last_Date":
                        yahoo_last_date,
                    "Twelve_Responding": True,
                    "Twelve_Has_Data": False,
                    "Twelve_Last_Date": None,
                    "Update_Status":
                        "NO_DATA_AVAILABLE",
                    "Monthly_Samples": 0,
                    "Samples_Above_Tolerance": 0,
                    "Maximum_Difference_Percent": np.nan,
                    "Average_Difference_Percent": np.nan,
                    "Status": "NOT_COMPARABLE",
                    "Blocking_Failure": False
                }
            )

            continue

        twelve_last_date = (
            twelve_close.index.max()
        )

        if twelve_last_date < yahoo_last_date:

            update_status = (
                "AVAILABLE_BUT_NOT_UPDATED"
            )

        elif twelve_last_date == yahoo_last_date:

            update_status = (
                "AVAILABLE_AND_UPDATED"
            )

        else:

            update_status = (
                "AVAILABLE_WITH_LATER_DATE"
            )

        comparison_df = pd.concat(
            [
                yahoo_close,
                twelve_close
            ],
            axis=1,
            join="inner"
        ).dropna()

        monthly_test = (
            first_common_session_per_month(
                comparison_df
            )
        )

        if monthly_test.empty:

            report_rows.append(
                {
                    "Ticker": ticker,
                    "Yahoo_Last_Date":
                        yahoo_last_date,
                    "Twelve_Responding": True,
                    "Twelve_Has_Data": True,
                    "Twelve_Last_Date":
                        twelve_last_date,
                    "Update_Status":
                        update_status,
                    "Monthly_Samples": 0,
                    "Samples_Above_Tolerance": 0,
                    "Maximum_Difference_Percent": np.nan,
                    "Average_Difference_Percent": np.nan,
                    "Status": "NOT_COMPARABLE",
                    "Blocking_Failure": False
                }
            )

            continue

        monthly_test[
            "Difference_Percent"
        ] = (
            (
                monthly_test[
                    "Yahoo_Close"
                ]
                - monthly_test[
                    "Twelve_Data_Close"
                ]
            ).abs()
            / monthly_test[
                "Yahoo_Close"
            ].abs()
            * 100
        )

        monthly_test[
            "Within_Tolerance"
        ] = (
            monthly_test[
                "Difference_Percent"
            ]
            <= CROSS_SOURCE_TOLERANCE_PERCENT
        )

        monthly_test.insert(
            0,
            "Ticker",
            ticker
        )

        monthly_test_tables.append(
            monthly_test.copy()
        )

        samples_above = int(
            (
                ~monthly_test[
                    "Within_Tolerance"
                ]
            ).sum()
        )

        blocking_failure = (
            samples_above > 0
        )

        report_rows.append(
            {
                "Ticker": ticker,
                "Yahoo_Last_Date":
                    yahoo_last_date,
                "Twelve_Responding": True,
                "Twelve_Has_Data": True,
                "Twelve_Last_Date":
                    twelve_last_date,
                "Update_Status":
                    update_status,
                "Monthly_Samples":
                    len(monthly_test),
                "Samples_Above_Tolerance":
                    samples_above,
                "Maximum_Difference_Percent":
                    float(
                        monthly_test[
                            "Difference_Percent"
                        ].max()
                    ),
                "Average_Difference_Percent":
                    float(
                        monthly_test[
                            "Difference_Percent"
                        ].mean()
                    ),
                "Status": (
                    "FAIL"
                    if blocking_failure
                    else "PASS"
                ),
                "Blocking_Failure":
                    blocking_failure
            }
        )

    # --------------------------------------------------------
    # OUTPUT CONSTRUCTION
    # --------------------------------------------------------

    cross_source_report = pd.DataFrame(
        report_rows
    )

    if monthly_test_tables:

        cross_source_monthly_test = pd.concat(
            monthly_test_tables,
            axis=0
        )

        cross_source_monthly_test.index.name = (
            "Date"
        )

    else:

        cross_source_monthly_test = pd.DataFrame(
            columns=[
                "Ticker",
                "Yahoo_Close",
                "Twelve_Data_Close",
                "Difference_Percent",
                "Within_Tolerance"
            ]
        )

    cross_source_comparison = (
        cross_source_monthly_test.copy()
    )

    twelve_data_responding = bool(
        cross_source_report[
            "Twelve_Responding"
        ].any()
        if not cross_source_report.empty
        else False
    )

    twelve_data_has_data = bool(
        cross_source_report[
            "Twelve_Has_Data"
        ].any()
        if not cross_source_report.empty
        else False
    )

    latest_yahoo_date = (
        pd.to_datetime(
            cross_source_report[
                "Yahoo_Last_Date"
            ],
            errors="coerce"
        ).max()
        if not cross_source_report.empty
        else pd.NaT
    )

    latest_twelve_data_date = (
        pd.to_datetime(
            cross_source_report[
                "Twelve_Last_Date"
            ],
            errors="coerce"
        ).max()
        if not cross_source_report.empty
        else pd.NaT
    )

    monthly_samples_tested = int(
        cross_source_report[
            "Monthly_Samples"
        ].fillna(0).sum()
        if not cross_source_report.empty
        else 0
    )

    samples_above_tolerance = int(
        cross_source_report[
            "Samples_Above_Tolerance"
        ].fillna(0).sum()
        if not cross_source_report.empty
        else 0
    )

    blocking_failure = bool(
        cross_source_report[
            "Blocking_Failure"
        ].fillna(False).any()
        if not cross_source_report.empty
        else False
    )

    if blocking_failure:

        overall_status = "FAIL"

    elif monthly_samples_tested > 0:

        overall_status = "PASS"

    else:

        overall_status = "NOT_COMPARABLE"

    cross_source_summary = {
        "enabled": True,
        "twelve_data_responding":
            twelve_data_responding,
        "twelve_data_has_data":
            twelve_data_has_data,
        "latest_yahoo_date": (
            latest_yahoo_date.strftime(
                "%Y-%m-%d"
            )
            if pd.notna(
                latest_yahoo_date
            )
            else None
        ),
        "latest_twelve_data_date": (
            latest_twelve_data_date.strftime(
                "%Y-%m-%d"
            )
            if pd.notna(
                latest_twelve_data_date
            )
            else None
        ),
        "sampling_method": (
            "first common trading session of each month"
        ),
        "monthly_samples_tested":
            monthly_samples_tested,
        "samples_above_tolerance":
            samples_above_tolerance,
        "tolerance_percent":
            CROSS_SOURCE_TOLERANCE_PERCENT,
        "blocking_failure":
            blocking_failure,
        "overall_status":
            overall_status
    }

    # --------------------------------------------------------
    # All outcomes are stored in the state.
    # The single, concise visualization is delegated to BOX 20.

    return {
        "cross_source_report":
            cross_source_report,

        "cross_source_comparison":
            cross_source_comparison,

        "cross_source_monthly_test":
            cross_source_monthly_test,

        "cross_source_summary":
            cross_source_summary,

        "cross_source_reference_date":
            latest_yahoo_date,

        "cross_source_blocking_failure":
            blocking_failure,

        "current_node":
            "cross_source_checker_agent",

        "execution_status":
            "running",

        "errors":
            errors
    }


print(
    "Cross-Source Checker Agent defined."
)


# ============================================================
# BOX 16 DEVELOPMENT TEST
# ============================================================
# Checks are printed when BOX 16
# is executed by the complete workflow in BOX 20.
# ============================================================

if RUN_DEVELOPMENT_TESTS:

    cross_source_result = (
        cross_source_checker_agent(
            state
        )
    )

    state.update(
        cross_source_result
    )

    inspect_agent_output(
        agent_name=(
            "Cross-Source Checker Agent"
        ),
        result=cross_source_result,
        rows=5
    )

else:

    print(
        "Dataset Certification Agent development test "
        "not executed."
    )

# ========= ORIGINAL NOTEBOOK CELL 26 =========
# ============================================================
# BOX 17 — AGENT 9: CRITIC AGENT BASED ON OPENROUTER
# ============================================================

def critic_agent(
    state: MarketDataState
) -> Dict[str, Any]:

    cleaning_report = state["cleaning_report"]
    validation_report = state["validation_report"]
    alignment_report = state["alignment_report"]
    cross_source_report = state["cross_source_report"]

    critic_input = {
        "cleaning_report": (
            cleaning_report
            .replace({np.nan: None})
            .to_dict(orient="records")
        ),
        "validation_report": (
            validation_report
            .replace({np.nan: None})
            .to_dict(orient="records")
        ),
        "alignment_report": alignment_report,
        "cross_source_report": (
            cross_source_report
            .replace({np.nan: None})
            .to_dict(orient="records")
        )
    }

    system_instruction = """
You are the Critic Agent of a quantitative financial system.

You must evaluate exclusively the technical reports received.

You must not:
- recalculate the data;
- invent information;
- formulate financial forecasts;
- provide advice;
- modify Python results;
- add text outside the JSON.

The primary dataset is the one produced by Yahoo Finance.

Twelve Data is used exclusively as a secondary source
for validation and challenge.

Failure of Twelve Data to respond, absence of Twelve Data data,
or a Twelve Data end date earlier than Yahoo Finance
are exclusively diagnostic conditions.

These conditions:
- do NOT constitute warnings on the primary dataset;
- do NOT constitute limitations of the primary dataset;
- must NOT modify critic_status;
- must NOT be included in warnings;
- must NOT be included in recommended_actions;
- must NOT make dataset_ready false.

In the cross-source check, only price consistency
on actually comparable dates is relevant.

A cross-source issue is critical only if
Blocking_Failure is true, meaning that one or more compared prices
exceed the CROSS_SOURCE_TOLERANCE_PERCENT threshold.

You must return exactly one JSON object with this structure:

{
    "critic_status": "PASSED",
    "dataset_ready": true,
    "critical_issues": [],
    "warnings": [],
    "recommended_actions": [],
    "reasoning_summary": "brief technical explanation"
}

Use critic_status exclusively as:
- PASSED if the dataset can be used;
- FAILED if critical issues exist that prevent its use.

Do not use APPROVED_WITH_WARNINGS.

If:
- deterministic checks are passed;
- there are no FAIL tickers;
- temporal alignment is valid;
- the price comparison on common dates does not show
  Blocking_Failure;

then the dataset must be classified as PASSED,
even if Twelve Data is less up to date than Yahoo Finance.
"""

    print("\n" + "=" * 80)
    print("INPUT SENT TO THE CRITIC AGENT")
    print("=" * 80)

    print(
        json.dumps(
            critic_input,
            ensure_ascii=False,
            indent=2,
            default=str
        )
    )

    try:

        critic_report = call_llm_json(
            system_instruction=system_instruction,
            user_content=json.dumps(
                critic_input,
                ensure_ascii=False,
                default=str
            ),
            model=CRITIC_MODEL
        )

        # ----------------------------------------------------
        # DETERMINISTIC NORMALIZATION OF THE CRITIC STATUS
        # ----------------------------------------------------
        # Diagnostic conditions from the secondary source
        # cannot transform a valid dataset into
        # PASSED WITH WARNINGS.
        # ----------------------------------------------------

        failed_tickers = validation_report.loc[
            validation_report["Status"] == "FAIL",
            "Ticker"
        ].tolist()

        cross_source_blocking_failure = bool(
            state.get(
                "cross_source_blocking_failure",
                False
            )
        )

        deterministic_pass = bool(
            len(failed_tickers) == 0
            and not cross_source_blocking_failure
        )

        if deterministic_pass:

            critic_report["critic_status"] = "PASSED"
            critic_report["dataset_ready"] = True
            critic_report["critical_issues"] = []
            critic_report["warnings"] = []
            critic_report["recommended_actions"] = []

        else:

            critic_report["critic_status"] = "FAILED"
            critic_report["dataset_ready"] = False

        print("\n" + "=" * 80)
        print("CRITIC AGENT OUTPUT")
        print("=" * 80)

        print(
            json.dumps(
                critic_report,
                ensure_ascii=False,
                indent=2,
                default=str
            )
        )

    except Exception as error:

        failed_tickers = validation_report.loc[
            validation_report["Status"] == "FAIL",
            "Ticker"
        ].tolist()

        cross_source_blocking_failure = bool(
            state.get(
                "cross_source_blocking_failure",
                False
            )
        )

        dataset_ready = bool(
            len(failed_tickers) == 0
            and not cross_source_blocking_failure
        )

        critic_report = {
            "critic_status": (
                "PASSED"
                if dataset_ready
                else "FAILED"
            ),
            "dataset_ready":
                dataset_ready,
            "critical_issues": (
                []
                if dataset_ready
                else failed_tickers
            ),
            "warnings": [],
            "recommended_actions": [],
            "reasoning_summary": (
                "OpenRouter Critic Agent unavailable. "
                "Deterministic check applied."
            ),
            "openrouter_error":
                str(error)
        }

        print("\n" + "=" * 80)
        print("CRITIC AGENT ERROR")
        print("=" * 80)

        print(str(error))

        print("\n" + "=" * 80)
        print("DETERMINISTIC CHECK OUTPUT")
        print("=" * 80)

        print(
            json.dumps(
                critic_report,
                ensure_ascii=False,
                indent=2,
                default=str
            )
        )

    return {
        "critic_report": critic_report,
        "current_node": "critic_agent",
        "execution_status": "running"
    }


print("Critic Agent defined.")


# ============================================================
# BOX 17 DEVELOPMENT TEST
# ============================================================

if RUN_DEVELOPMENT_TESTS:

    # ========================================================
    # BOX 17 EXECUTION
    # ========================================================

    critic_result = critic_agent(state)

    state.update(critic_result)

    # ========================================================
    # DISPLAY OF BOX 17 OUTPUT
    # ========================================================

    inspect_agent_output(
        agent_name="Critic Agent",
        result=critic_result,
        rows=5
    )

    # ========================================================
    # VERIFICATION OF THE STATE UPDATE
    # ========================================================

    print(
        "\ncritic_report present in state:",
        "critic_report" in state
    )

else:

    print(
        "Critic Agent development test "
        "not executed."
    )

# ========= ORIGINAL NOTEBOOK CELL 27 =========
# ============================================================
# BOX 18 — AGENT 10: FINAL DATASET CERTIFICATION
# ============================================================
# This agent combines:
# - deterministic results;
# - Critic Agent assessment;
# - matrix availability;
# - temporal validation and alignment;
# - cross-source check produced by BOX 16.
#
# Failure of Twelve Data to respond or update
# is diagnostic and non-blocking and does not constitute
# a limitation of the primary dataset.
#
# Only a price deviation above the
# CROSS_SOURCE_TOLERANCE_PERCENT threshold is blocking.
# ============================================================

def dataset_certification_agent(
    state: MarketDataState
) -> Dict[str, Any]:

    validation_report = state["validation_report"]
    critic_report = state["critic_report"]
    aligned_prices = state["aligned_prices"]
    log_returns = state["log_returns"]
    alignment_report = state.get(
        "alignment_report",
        {}
    )

    cross_source_summary = state.get(
        "cross_source_summary",
        {}
    )

    cross_source_blocking_failure = bool(
        state.get(
            "cross_source_blocking_failure",
            cross_source_summary.get(
                "blocking_failure",
                False
            )
        )
    )

    passed_tickers = validation_report.loc[
        validation_report["Status"] == "PASS",
        "Ticker"
    ].tolist()

    warning_tickers = validation_report.loc[
        validation_report["Status"] == "WARNING",
        "Ticker"
    ].tolist()

    failed_tickers = validation_report.loc[
        validation_report["Status"] == "FAIL",
        "Ticker"
    ].tolist()

    average_quality_score = (
        float(
            validation_report[
                "Quality_Score"
            ].mean()
        )
        if not validation_report.empty
        else 0.0
    )

    temporal_alignment_ready = bool(
        alignment_report.get(
            "temporal_alignment_passed",
            False
        )
    )

    deterministic_ready = bool(
        not aligned_prices.empty
        and not log_returns.empty
        and len(failed_tickers) == 0
        and temporal_alignment_ready
        and not cross_source_blocking_failure
    )

    critic_ready = bool(
        critic_report.get(
            "dataset_ready",
            False
        )
    )

    dataset_ready = bool(
        deterministic_ready
        and critic_ready
    )

    usable_for = []

    if dataset_ready:

        usable_for.extend(
            [
                "financial_metrics",
                "sharpe_ratio",
                "momentum",
                "dollar_volume",
                "cross_sectional_momentum",
                "capm"
            ]
        )

        if aligned_prices.shape[1] >= 2:

            usable_for.extend(
                [
                    "correlation"
                ]
            )

    certification = {
        "project":
            PROJECT_NAME,
        "certification_timestamp":
            datetime.now().isoformat(),
        "dataset_ready":
            dataset_ready,
        "deterministic_ready":
            deterministic_ready,
        "critic_ready":
            critic_ready,
        "temporal_alignment_ready":
            temporal_alignment_ready,
        "cross_source_blocking_failure":
            cross_source_blocking_failure,
        "cross_source_summary":
            cross_source_summary,
        "average_quality_score":
            round(
                average_quality_score,
                2
            ),
        "total_tickers":
            len(
                validation_report
            ),
        "passed_tickers":
            passed_tickers,
        "warning_tickers":
            warning_tickers,
        "failed_tickers":
            failed_tickers,
        "aligned_observations":
            len(
                aligned_prices
            ),
        "usable_for":
            usable_for,
        "critic_status":
            (
                "PASSED"
                if dataset_ready
                else "FAILED"
            ),
        "limitations":
            (
                []
                if dataset_ready
                else critic_report.get(
                    "critical_issues",
                    []
                )
            )
    }

    return {
        "certification":
            certification,
        "current_node":
            "dataset_certification_agent",
        "execution_status":
            "completed"
    }


print(
    "Dataset Certification Agent defined."
)


if RUN_DEVELOPMENT_TESTS:

    certification_result = (
        dataset_certification_agent(
            state
        )
    )

    state.update(
        certification_result
    )

else:

    print(
        "Dataset Certification Agent development test "
        "not executed."
    )

# ========= ORIGINAL NOTEBOOK CELL 28 =========
# ============================================================
# BOX 19 — LANGGRAPH GRAPH CONSTRUCTION
# ============================================================
# Execution order:
#
# 1. request interpretation;
# 2. ticker validation;
# 3. Yahoo Finance download;
# 4. cleaning;
# 5. alignment;
# 6. return preparation;
# 7. validation;
# 8. secondary-source check;
# 9. Critic Agent check;
# 10. final certification.
# ============================================================

graph_builder = StateGraph(
    MarketDataState
)

graph_builder.add_node(
    "request_interpreter",
    request_interpreter_agent
)

graph_builder.add_node(
    "ticker_resolution",
    ticker_resolution_agent
)

graph_builder.add_node(
    "market_data_collector",
    market_data_collector_agent
)

graph_builder.add_node(
    "data_cleaning",
    data_cleaning_agent
)

graph_builder.add_node(
    "data_alignment",
    data_alignment_agent
)

graph_builder.add_node(
    "feature_preparation",
    feature_preparation_agent
)

graph_builder.add_node(
    "data_quality_validator",
    data_quality_validator_agent
)

graph_builder.add_node(
    "cross_source_checker",
    cross_source_checker_agent
)

graph_builder.add_node(
    "critic_agent",
    critic_agent
)

graph_builder.add_node(
    "dataset_certification",
    dataset_certification_agent
)

# ------------------------------------------------------------
# NODE CONNECTIONS
# ------------------------------------------------------------

graph_builder.add_edge(
    START,
    "request_interpreter"
)

graph_builder.add_edge(
    "request_interpreter",
    "ticker_resolution"
)

graph_builder.add_edge(
    "ticker_resolution",
    "market_data_collector"
)

graph_builder.add_edge(
    "market_data_collector",
    "data_cleaning"
)

graph_builder.add_edge(
    "data_cleaning",
    "data_alignment"
)

graph_builder.add_edge(
    "data_alignment",
    "feature_preparation"
)

graph_builder.add_edge(
    "feature_preparation",
    "data_quality_validator"
)

graph_builder.add_edge(
    "data_quality_validator",
    "cross_source_checker"
)

graph_builder.add_edge(
    "cross_source_checker",
    "critic_agent"
)

graph_builder.add_edge(
    "critic_agent",
    "dataset_certification"
)

graph_builder.add_edge(
    "dataset_certification",
    END
)

market_data_graph = graph_builder.compile()

print("LangGraph graph compiled successfully.")

# ========= ORIGINAL NOTEBOOK CELL 29 =========
# ============================================================
# BOX 20 — EXECUTION OF THE COMPLETE PROCESS
# ============================================================
# The workflow is executed in its entirety.
#
# NOTE ON EXECUTION TIMES:
# this box may take a few minutes because it executes the entire
# data preparation and validation pipeline and also includes
# a cross-check with an independent external source
# (Twelve Data).
#
# The cross-check requires API calls and the download of the
# historical series required for comparison with Yahoo Finance;
# execution times therefore also depend on provider latency
# and limits.
#
# The cross-source check is intended to strengthen the reliability
# of the dataset before final certification.
#
# The output shows:
# - all main checks along the workflow;
# - whether Yahoo Finance downloaded the data and the latest date;
# - whether Twelve Data downloaded the data and the latest date;
# - whether Twelve Data is updated relative to Yahoo;
# - the number of sampled prices;
# - the outcome of the 0.10% threshold;
# - a single overall verification for each ticker.
# ============================================================

USER_REQUEST = """
Prepare and validate the daily historical time series of all
Dow Jones stocks from 2010 to today.
"""

initial_state: MarketDataState = {
    "user_request":
        USER_REQUEST,
    "tickers":
        tickers,
    "errors":
        []
}

_internal_output = io.StringIO()

with contextlib.redirect_stdout(
    _internal_output
):

    final_state = market_data_graph.invoke(
        initial_state
    )


# ============================================================
# OUTPUT RETRIEVAL
# ============================================================

clean_data = final_state.get(
    "clean_data",
    {}
)

cleaning_report = final_state.get(
    "cleaning_report",
    pd.DataFrame()
)

validation_report = final_state.get(
    "validation_report",
    pd.DataFrame()
)

alignment_report = final_state.get(
    "alignment_report",
    {}
)

cross_source_report = final_state.get(
    "cross_source_report",
    pd.DataFrame()
)

cross_source_summary = final_state.get(
    "cross_source_summary",
    {}
)

critic_report = final_state.get(
    "critic_report",
    {}
)

certification = final_state.get(
    "certification",
    {}
)

requested_tickers = final_state.get(
    "tickers",
    tickers
)


# ============================================================
# GENERAL CHECKS
# ============================================================

graph_verified = bool(
    final_state
    and final_state.get(
        "execution_status"
    ) == "completed"
)

yahoo_downloaded = bool(
    clean_data
)

yahoo_last_dates = [
    pd.Timestamp(
        ticker_df.index.max()
    ).normalize()
    for ticker_df in clean_data.values()
    if (
        isinstance(
            ticker_df,
            pd.DataFrame
        )
        and not ticker_df.empty
    )
]

yahoo_last_date = (
    max(
        yahoo_last_dates
    ).strftime(
        "%Y-%m-%d"
    )
    if yahoo_last_dates
    else None
)

cleaning_verified = bool(
    isinstance(
        cleaning_report,
        pd.DataFrame
    )
    and not cleaning_report.empty
)

validation_verified = bool(
    isinstance(
        validation_report,
        pd.DataFrame
    )
    and not validation_report.empty
    and "Status"
    in validation_report.columns
    and not validation_report[
        "Status"
    ]
    .astype(str)
    .str.upper()
    .eq("FAIL")
    .any()
)

alignment_verified = bool(
    alignment_report.get(
        "temporal_alignment_passed",
        False
    )
)

twelve_downloaded = bool(
    cross_source_summary.get(
        "twelve_data_responding",
        False
    )
    and cross_source_summary.get(
        "twelve_data_has_data",
        False
    )
)

twelve_last_date = (
    cross_source_summary.get(
        "latest_twelve_data_date"
    )
)

twelve_updated = bool(
    twelve_downloaded
    and yahoo_last_date
    and twelve_last_date
    and twelve_last_date == yahoo_last_date
)

monthly_samples_tested = int(
    cross_source_summary.get(
        "monthly_samples_tested",
        0
    )
)

samples_above_tolerance = int(
    cross_source_summary.get(
        "samples_above_tolerance",
        0
    )
)

cross_source_blocking_failure = bool(
    cross_source_summary.get(
        "blocking_failure",
        final_state.get(
            "cross_source_blocking_failure",
            False
        )
    )
)

price_comparison_confirmed = bool(
    monthly_samples_tested > 0
    and not cross_source_blocking_failure
)

critic_verified = bool(
    critic_report.get(
        "dataset_ready",
        False
    )
)

certification_verified = bool(
    certification.get(
        "dataset_ready",
        False
    )
)


# ============================================================
# A SINGLE OVERALL VERIFICATION FOR EACH TICKER
# ============================================================

validation_by_ticker = {}

if (
    isinstance(
        validation_report,
        pd.DataFrame
    )
    and not validation_report.empty
):

    validation_by_ticker = {
        str(row["Ticker"]): (
            str(
                row["Status"]
            ).upper()
            != "FAIL"
        )
        for _, row
        in validation_report.iterrows()
    }

cross_source_by_ticker = {}

if (
    isinstance(
        cross_source_report,
        pd.DataFrame
    )
    and not cross_source_report.empty
):

    cross_source_by_ticker = {
        str(row["Ticker"]): (
            not bool(
                row.get(
                    "Blocking_Failure",
                    False
                )
            )
        )
        for _, row
        in cross_source_report.iterrows()
    }

ticker_last_dates = alignment_report.get(
    "ticker_last_dates",
    {}
)

expected_last_date = alignment_report.get(
    "expected_last_date"
)

ticker_results = {}

for ticker in requested_tickers:

    ticker = str(
        ticker
    )

    downloaded = bool(
        ticker in clean_data
        and isinstance(
            clean_data.get(
                ticker
            ),
            pd.DataFrame
        )
        and not clean_data[
            ticker
        ].empty
    )

    validated = validation_by_ticker.get(
        ticker,
        False
    )

    aligned = bool(
        ticker_last_dates.get(
            ticker
        )
        == expected_last_date
    )

    cross_source_ok = (
        cross_source_by_ticker.get(
            ticker,
            True
        )
    )

    ticker_results[ticker] = bool(
        downloaded
        and validated
        and aligned
        and cross_source_ok
    )


# ============================================================
# FINAL OUTPUT
# ============================================================

print("\n" + "=" * 60)
print("WORKFLOW CHECKS")
print("=" * 60)

print(
    "LangGraph graph:",
    "VERIFIED"
    if graph_verified
    else "NOT VERIFIED"
)

print(
    "Yahoo Finance:",
    (
        f"CONFIRMED — data download YES — "
        f"30 tickers — latest date {yahoo_last_date}"
        if yahoo_downloaded
        else "NOT CONFIRMED — data download NO"
    )
)

if twelve_downloaded:

    print(
        "Twelve Data:",
        (
            f"data download YES — latest date "
            f"{twelve_last_date} — "
            f"{'UPDATED' if twelve_updated else 'NOT UPDATED — non-blocking'}"
        )
    )

else:

    print(
        "Twelve Data:",
        "data download NO — latest date unavailable — non-blocking"
    )

print(
    "Price sampling:",
    (
        f"{monthly_samples_tested} sampled prices — "
        f"{samples_above_tolerance} above threshold "
        f"{CROSS_SOURCE_TOLERANCE_PERCENT:.2f}% — "
        f"{'CONFIRMED' if price_comparison_confirmed else 'NOT CONFIRMED'}"
    )
)

print(
    "Data cleaning:",
    "VERIFIED"
    if cleaning_verified
    else "NOT VERIFIED"
)

print(
    "Data validation:",
    "VERIFIED"
    if validation_verified
    else "NOT VERIFIED"
)

print(
    "Temporal alignment:",
    "VERIFIED"
    if alignment_verified
    else "NOT VERIFIED"
)

print(
    "Critic Agent:",
    "VERIFIED"
    if critic_verified
    else "NOT VERIFIED"
)

print(
    "Final certification:",
    "VERIFIED"
    if certification_verified
    else "NOT VERIFIED"
)


# ============================================================
# TICKER OUTCOME — SIX TICKERS PER ROW
# ============================================================

print("\nTICKER OUTCOME")

ticker_output = [
    (
        f"{str(ticker):<6} "
        f"{'VERIFIED' if ticker_results[str(ticker)] else 'NOT VERIFIED'}"
    )
    for ticker in requested_tickers
]

for start_index in range(
    0,
    len(ticker_output),
    6
):

    print(
        " | ".join(
            ticker_output[
                start_index:
                start_index + 6
            ]
        )
    )


# ============================================================
# FINAL OUTCOME
# ============================================================

workflow_verified = bool(
    graph_verified
    and yahoo_downloaded
    and cleaning_verified
    and validation_verified
    and alignment_verified
    and critic_verified
    and certification_verified
    and not cross_source_blocking_failure
    and all(
        ticker_results.values()
    )
)

print("\n" + "=" * 60)

print(
    "FINAL OUTCOME:",
    "PROCEED"
    if workflow_verified
    else "ISSUE"
)

print("=" * 60)

# ========= ORIGINAL NOTEBOOK CELL 30 =========
# ============================================================
# BOX 21 - DISPLAY OF THE FINAL CLEAN DATASET
# ============================================================
# This box:
# - does NOT execute agents;
# - does NOT invoke LangGraph;
# - does NOT modify final_state;
# - does NOT perform cleaning or recalculations;
# - reads exclusively the dataset already produced by the workflow;
# - shows, for each ticker, the first 10 and last 10 trading sessions.
#
# Numerical convention used in the display:
# - comma as the thousands separator;
# - period as the decimal separator;
# - prices displayed with 3 decimal places;
# - volumes displayed as integers.
#
# Formatting applies exclusively to the displayed output:
# the original numerical values in the dataset are not modified.
# ============================================================

clean_dataset = final_state.get(
    "clean_data",
    {}
)

if not clean_dataset:

    raise ValueError(
        "The clean dataset is not available in final_state."
    )


# ============================================================
# OVERALL DATASET TIME RANGE
# ============================================================

dataset_start_dates = [
    pd.Timestamp(
        ticker_df.index.min()
    )
    for ticker_df in clean_dataset.values()
    if (
        isinstance(
            ticker_df,
            pd.DataFrame
        )
        and not ticker_df.empty
    )
]

dataset_end_dates = [
    pd.Timestamp(
        ticker_df.index.max()
    )
    for ticker_df in clean_dataset.values()
    if (
        isinstance(
            ticker_df,
            pd.DataFrame
        )
        and not ticker_df.empty
    )
]

dataset_start_date = (
    min(
        dataset_start_dates
    ).strftime(
        "%Y-%m-%d"
    )
    if dataset_start_dates
    else "N/A"
)

dataset_end_date = (
    max(
        dataset_end_dates
    ).strftime(
        "%Y-%m-%d"
    )
    if dataset_end_dates
    else "N/A"
)


# ============================================================
# GENERAL LEGEND
# ============================================================

print("\n" + "=" * 110)
print("FINAL CLEAN DATASET — DOW JONES INDUSTRIAL AVERAGE")
print("=" * 110)

print(
    f"Overall time range: "
    f"{dataset_start_date} → {dataset_end_date}"
)

print(
    f"Tickers included: {len(clean_dataset)}"
)

print(
    "Display: first 10 trading sessions and last 10 trading sessions "
    "available for each ticker."
)

print(
    "Prices: displayed with 3 decimal places according to the English convention "
    "(comma for thousands and period for decimals); "
    "the values used by the system remain those contained "
    "in the certified dataset."
)

print(
    "Volume: displayed as an integer with comma as the thousands separator "
    "according to the English convention."
)

print(
    "Dates: explicitly reported in the Date column "
    "in YYYY-MM-DD format."
)

print("=" * 110)


# ============================================================
# NUMERIC FORMATTING FUNCTION
# ============================================================

def format_number_italian(
    value,
    decimals=3
):

    if pd.isna(value):

        return ""

    formatted_value = f"{float(value):,.{decimals}f}"

    return formatted_value


# ============================================================
# FORMATTING FUNCTION FOR DISPLAY ONLY
# ============================================================

def format_dataset_for_print(
    ticker_df
):

    display_df = ticker_df.copy()

    display_df = display_df.reset_index()

    if "Date" not in display_df.columns:

        display_df = display_df.rename(
            columns={
                display_df.columns[0]:
                    "Date"
            }
        )

    display_df["Date"] = pd.to_datetime(
        display_df["Date"]
    ).dt.strftime(
        "%Y-%m-%d"
    )

    price_columns = [
        "Open",
        "High",
        "Low",
        "Close",
        "Adj Close"
    ]

    for column in price_columns:

        if column in display_df.columns:

            display_df[column] = display_df[
                column
            ].map(
                lambda value:
                format_number_italian(
                    value,
                    decimals=3
                )
            )

    if "Volume" in display_df.columns:

        display_df["Volume"] = display_df[
            "Volume"
        ].map(
            lambda value:
            (
                f"{int(value):,}"
                if pd.notna(value)
                else ""
            )
        )

    return display_df


# ============================================================
# DISPLAY BY TICKER
# ============================================================

for ticker, ticker_df in clean_dataset.items():

    if (
        not isinstance(
            ticker_df,
            pd.DataFrame
        )
        or ticker_df.empty
    ):

        continue

    ticker_start_date = pd.Timestamp(
        ticker_df.index.min()
    ).strftime(
        "%Y-%m-%d"
    )

    ticker_end_date = pd.Timestamp(
        ticker_df.index.max()
    ).strftime(
        "%Y-%m-%d"
    )

    observations = len(
        ticker_df
    )

    display_df = format_dataset_for_print(
        ticker_df
    )

    first_rows = display_df.head(
        10
    )

    last_rows = display_df.tail(
        10
    )

    first_period_start = first_rows[
        "Date"
    ].iloc[0]

    first_period_end = first_rows[
        "Date"
    ].iloc[-1]

    last_period_start = last_rows[
        "Date"
    ].iloc[0]

    last_period_end = last_rows[
        "Date"
    ].iloc[-1]

    print("\n" + "=" * 110)

    print(
        f"{ticker} — CLEAN DATASET"
    )

    print(
        f"Full period: "
        f"{ticker_start_date} → {ticker_end_date}"
        f" | Observations: {observations}"
    )

    print("=" * 110)

    print(
        f"\nFIRST 10 TRADING SESSIONS "
        f"({first_period_start} → {first_period_end})\n"
    )

    print(
        first_rows.to_string(
            index=False
        )
    )

    print(
        f"\nLAST 10 TRADING SESSIONS "
        f"({last_period_start} → {last_period_end})\n"
    )

    print(
        last_rows.to_string(
            index=False
        )
    )


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n" + "=" * 110)

print(
    f"TICKERS DISPLAYED: {len(clean_dataset)}"
)

print(
    f"OVERALL TIME RANGE: "
    f"{dataset_start_date} → {dataset_end_date}"
)

print("=" * 110)

# ========= ORIGINAL NOTEBOOK CELL 31 =========
# ============================================================
# BOX 22 — DISPLAY OF THE INTERPRETED REQUEST
# ============================================================

print("ORIGINAL REQUEST")
print(final_state["user_request"])

print("\nREQUEST INTERPRETED BY THE LLM")
print(
    json.dumps(
        final_state["parsed_request"],
        indent=4,
        ensure_ascii=False
    )
)

# ========= ORIGINAL NOTEBOOK CELL 32 =========
# ============================================================
# BOX 23 — DISPLAY OF THE CLEANING REPORT
# ============================================================

cleaning_report = (
    final_state["cleaning_report"]
    .sort_values("Ticker")
    .reset_index(drop=True)
)

checks = {
    "Rows removed": cleaning_report["Removed_Rows"] > 0,
    "Invalid dates": cleaning_report["Invalid_Dates"] > 0,
    "Rows beyond the end date": cleaning_report[
        "Rows_After_End_Date_Removed"
    ] > 0,
    "Trailing incomplete rows": cleaning_report[
        "Trailing_Incomplete_Rows_Removed"
    ] > 0,
    "Duplicates removed": cleaning_report["Duplicates_Removed"] > 0,
    "Missing columns": cleaning_report[
        "Missing_Columns"
    ].apply(len) > 0,
    "Non-numeric values": cleaning_report[
        "Non_Numeric_Values"
    ] > 0,
    "Infinite values": cleaning_report["Infinite_Values"] > 0,
    "Completely empty rows": cleaning_report[
        "Empty_Rows_Removed"
    ] > 0,
    "Zero or negative prices": cleaning_report[
        "Non_Positive_Price_Rows"
    ] > 0,
    "Negative volumes": cleaning_report[
        "Negative_Volume_Rows"
    ] > 0,
    "Final missing values": cleaning_report[
        "Missing_Values_After"
    ] > 0
}

print("=" * 100)
print("DATA CLEANING REPORT")
print("=" * 100)

for check_name, mask in checks.items():

    affected_tickers = cleaning_report.loc[
        mask,
        "Ticker"
    ].tolist()

    result = (
        ", ".join(affected_tickers)
        if affected_tickers
        else "NO OCCURRENCES"
    )

    print(
        f"{check_name:<35} {result}"
    )

print("=" * 100)

# ========= ORIGINAL NOTEBOOK CELL 33 =========
# ============================================================
# BOX 24 — DISPLAY OF THE ALIGNMENT REPORT
# ============================================================

print(
    json.dumps(
        final_state["alignment_report"],
        indent=4,
        ensure_ascii=False,
        default=str
    )
)

# ========= ORIGINAL NOTEBOOK CELL 34 =========
# ============================================================
# BOX 25 — DISPLAY OF THE VALIDATION REPORT
# ============================================================

validation_report = final_state[
    "validation_report"
].copy()

checks = {
    "Minimum number of observations":
        "Minimum_Observations_Check",

    "No duplicates":
        "Duplicates_Check",

    "No zero or negative prices":
        "Prices_Check",

    "No negative volumes":
        "Volumes_Check",

    "Acceptable percentage of missing data":
        "Missing_Ratio_Check",

    "Valid time period":
        "Valid_Period_Check",

    "Correct end date":
        "Expected_Last_Date_Check"
}

print("=" * 100)
print("DATA QUALITY VALIDATION REPORT")
print("=" * 100)

for check_name, column_name in checks.items():

    affected_tickers = validation_report.loc[
        ~validation_report[column_name],
        "Ticker"
    ].tolist()

    result = (
        ", ".join(affected_tickers)
        if affected_tickers
        else "VERIFIED FOR ALL TICKERS"
    )

    print(
        f"{check_name:<45} {result}"
    )

print("-" * 100)

for status in [
    "FAIL",
    "WARNING"
]:

    affected_tickers = validation_report.loc[
        validation_report["Status"] == status,
        "Ticker"
    ].tolist()

    result = (
        ", ".join(affected_tickers)
        if affected_tickers
        else "NO TICKERS"
    )

    print(
        f"Tickers with status {status:<27} {result}"
    )

print("=" * 100)

# ========= ORIGINAL NOTEBOOK CELL 35 =========
# ============================================================
# BOX 26 — DISPLAY OF THE CROSS-SOURCE CHECK
# ============================================================

cross_source_report = final_state[
    "cross_source_report"
].copy()

checks = {
    "Twelve Data not responding":
        ~cross_source_report["Twelve_Responding"],

    "Twelve Data with no data":
        ~cross_source_report["Twelve_Has_Data"],

    "Twelve Data not updated":
        cross_source_report["Update_Status"]
        != "UPDATED",

    "No monthly samples available":
        cross_source_report["Monthly_Samples"]
        == 0,

    "Samples above tolerance":
        cross_source_report[
            "Samples_Above_Tolerance"
        ] > 0,

    "Comparison not passed":
        cross_source_report["Status"]
        != "PASS",

    "Blocking failure":
        cross_source_report[
            "Blocking_Failure"
        ].fillna(False)
}

print("=" * 100)
print("YAHOO FINANCE VS TWELVE DATA CROSS-SOURCE CHECK REPORT")
print("=" * 100)

for check_name, mask in checks.items():

    affected_tickers = cross_source_report.loc[
        mask,
        "Ticker"
    ].tolist()

    result = (
        ", ".join(affected_tickers)
        if affected_tickers
        else "NO TICKERS"
    )

    print(
        f"{check_name:<45} {result}"
    )

print("-" * 100)

print(
    f"{'Monthly samples analyzed':<45} "
    f"{int(cross_source_report['Monthly_Samples'].sum()):,}"
)

print(
    f"{'Total samples above tolerance':<45} "
    f"{int(cross_source_report['Samples_Above_Tolerance'].sum()):,}"
)

print(
    f"{'Maximum difference detected':<45} "
    f"{cross_source_report['Maximum_Difference_Percent'].max():,.4f}%"
)

print(
    f"{'Average difference detected':<45} "
    f"{cross_source_report['Average_Difference_Percent'].mean():,.4f}%"
)

print("=" * 100)

# ========= ORIGINAL NOTEBOOK CELL 36 =========
# ============================================================
# BOX 27 — DISPLAY OF THE CRITIC AGENT ASSESSMENT
# ============================================================

print(
    json.dumps(
        final_state["critic_report"],
        indent=4,
        ensure_ascii=False,
        default=str
    )
)

# ========= ORIGINAL NOTEBOOK CELL 37 =========
# ============================================================
# BOX 28 — FINAL DATASET CERTIFICATION
# ============================================================

print(
    json.dumps(
        final_state["certification"],
        indent=4,
        ensure_ascii=False,
        default=str
    )
)

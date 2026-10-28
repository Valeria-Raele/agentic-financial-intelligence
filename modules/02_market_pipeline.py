def request_interpreter_agent(state: MarketDataState) -> Dict[str, Any]:
    """
    Interprets the user's request and returns
    a structured configuration for subsequent nodes.

    If the model is unavailable or returns
    invalid output, a default configuration
    consistent with the project is applied.
    """
    user_request = state.get('user_request', 'Retrieve and prepare the Dow Jones historical time series from 2010 to today.')
    available_tickers = state.get('tickers', tickers)
    system_instruction = '\nYou are the Request Interpreter of a quantitative financial system.\n\nThe domain is limited to Dow Jones Industrial Average securities.\n\nYou must transform the user\'s request into a single JSON object.\n\nYou must not:\n- perform calculations;\n- comment on the markets;\n- provide financial advice;\n- invent tickers;\n- invent dates;\n- add text outside the JSON.\n\nThe JSON must follow this structure:\n\n{\n    "intent": "prepare_market_dataset",\n    "universe": "dow_jones",\n    "tickers": "all",\n    "start_date": "YYYY-MM-DD",\n    "end_date": "YYYY-MM-DD",\n    "interval": "1d",\n    "fields": [\n        "Open",\n        "High",\n        "Low",\n        "Close",\n        "Adj Close",\n        "Volume"\n    ]\n}\n\nRules:\n\n1. The "intent" field must be:\n   "prepare_market_dataset".\n\n2. The "universe" field must be:\n   "dow_jones".\n\n3. If the user requests all Dow Jones securities,\n   the "tickers" field must be the string:\n   "all".\n\n4. If the user specifies particular tickers,\n   the "tickers" field must be a list of strings.\n\n5. You may use only tickers present in the list\n   of available tickers provided in the request content.\n\n6. If the user does not specify a start date,\n   use:\n   "2010-01-01".\n\n7. If the user uses expressions such as:\n   - today;\n   - current date;\n   - up to now;\n   - up to today;\n\n   use the latest fully completed New York stock exchange\n   trading session provided in the request content.\n\n8. If the user does not specify an end date,\n   use the latest fully completed New York stock exchange\n   trading session provided in the request content.\n\n9. The end date cannot be later than the latest fully completed\n   New York stock exchange trading session provided.\n\n10. If the user does not specify a frequency,\n    use:\n    "1d".\n\n11. The "fields" field must always contain:\n    "Open",\n    "High",\n    "Low",\n    "Close",\n    "Adj Close",\n    "Volume".\n'
    user_content = json.dumps({'last_completed_new_york_session': DEFAULT_END_DATE, 'available_dow_jones_tickers': available_tickers, 'user_request': user_request}, ensure_ascii=False)
    fallback_request = {'intent': 'prepare_market_dataset', 'universe': 'dow_jones', 'tickers': 'all', 'start_date': DEFAULT_START_DATE, 'end_date': DEFAULT_END_DATE, 'interval': DEFAULT_INTERVAL, 'fields': ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']}
    try:
        parsed_request = call_llm_json(system_instruction=system_instruction, user_content=user_content)
        required_fields = {'intent', 'universe', 'tickers', 'start_date', 'end_date', 'interval', 'fields'}
        missing_fields = required_fields.difference(parsed_request.keys())
        if missing_fields:
            raise ValueError(f'The model did not return the required fields: {sorted(missing_fields)}')
        parsed_request['intent'] = 'prepare_market_dataset'
        parsed_request['universe'] = 'dow_jones'
        parsed_end_date = pd.Timestamp(parsed_request['end_date']).normalize()
        maximum_end_date = pd.Timestamp(DEFAULT_END_DATE).normalize()
        if parsed_end_date > maximum_end_date:
            parsed_request['end_date'] = DEFAULT_END_DATE
        requested_tickers = parsed_request.get('tickers')
        if isinstance(requested_tickers, list):
            normalized_requested_tickers = [normalize_ticker(ticker) for ticker in requested_tickers]
            invalid_tickers = [ticker for ticker in normalized_requested_tickers if ticker not in available_tickers]
            if invalid_tickers:
                raise ValueError(f'The model returned tickers that do not belong to the Dow Jones universe: {invalid_tickers}')
            parsed_request['tickers'] = list(dict.fromkeys(normalized_requested_tickers))
        elif requested_tickers != 'all':
            raise ValueError('The "tickers" field must be "all" or a list of tickers.')
        parsed_request['fields'] = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
        return {'parsed_request': parsed_request, 'current_node': 'request_interpreter_agent', 'execution_status': 'running', 'errors': state.get('errors', [])}
    except Exception as error:
        errors = state.get('errors', []).copy()
        errors.append(f'Request Interpreter unavailable or response invalid: {error}. Default request applied.')
        return {'parsed_request': fallback_request, 'current_node': 'request_interpreter_agent', 'execution_status': 'running', 'errors': errors}

def ticker_resolution_agent(state: MarketDataState) -> Dict[str, Any]:
    """
    Resolves and validates the tickers requested by the user.

    Returns in the state:
    - the final list of tickers to analyze;
    - any error messages;
    - the name of the current node;
    - the execution status.
    """
    parsed_request = state.get('parsed_request', {})
    available_tickers = state.get('tickers', tickers)
    available_tickers = clean_ticker_list(available_tickers)
    if len(available_tickers) == 0:
        raise ValueError('The available ticker universe is empty.')
    requested_tickers = parsed_request.get('tickers', 'all')
    errors = state.get('errors', []).copy()
    invalid_tickers = []
    if requested_tickers == 'all':
        selected_tickers = available_tickers.copy()
    elif isinstance(requested_tickers, list):
        normalized_requested = clean_ticker_list(requested_tickers)
        selected_tickers = [ticker for ticker in normalized_requested if ticker in available_tickers]
        invalid_tickers = [ticker for ticker in normalized_requested if ticker not in available_tickers]
    elif isinstance(requested_tickers, str):
        normalized_ticker = normalize_ticker(requested_tickers)
        if normalized_ticker in available_tickers:
            selected_tickers = [normalized_ticker]
        else:
            selected_tickers = []
            invalid_tickers = [normalized_ticker]
    else:
        selected_tickers = []
        errors.append('Invalid format for the "tickers" field. Only "all", a string, or a list of tickers are accepted.')
    if invalid_tickers:
        errors.append(f'Tickers excluded because they do not belong to the Dow Jones universe: {invalid_tickers}')
    selected_tickers = list(dict.fromkeys(selected_tickers))
    if len(selected_tickers) == 0:
        errors.append('No valid ticker identified. The entire Dow Jones universe will be used.')
        selected_tickers = available_tickers.copy()
    return {'tickers': selected_tickers, 'current_node': 'ticker_resolution_agent', 'execution_status': 'running', 'errors': errors}

def market_data_collector_agent(state: MarketDataState) -> Dict[str, Any]:
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
    parsed_request = state.get('parsed_request', {})
    selected_tickers = state.get('tickers', [])
    errors = state.get('errors', []).copy()
    if not selected_tickers:
        raise ValueError('The list of tickers to download is empty.')
    start_date = parsed_request.get('start_date', DEFAULT_START_DATE)
    requested_end_date = parsed_request.get('end_date', DEFAULT_END_DATE)
    interval = parsed_request.get('interval', DEFAULT_INTERVAL)
    try:
        start_datetime = pd.to_datetime(start_date, format='%Y-%m-%d').normalize()
        requested_end_datetime = pd.to_datetime(requested_end_date, format='%Y-%m-%d').normalize()
        last_completed_session = pd.to_datetime(DEFAULT_END_DATE, format='%Y-%m-%d').normalize()
    except Exception as error:
        raise ValueError('Dates must be expressed in YYYY-MM-DD format.') from error
    end_datetime = min(requested_end_datetime, last_completed_session)
    if start_datetime >= end_datetime:
        raise ValueError('The start date must be earlier than the end date.')
    if requested_end_datetime > last_completed_session:
        errors.append(f'The requested end date was later than the latest completed trading session of the New York stock exchanges and has been limited to {DEFAULT_END_DATE}.')
    download_end_date = (end_datetime + timedelta(days=1)).strftime('%Y-%m-%d')
    raw_data = None
    maximum_attempts = 3
    for attempt in range(1, maximum_attempts + 1):
        try:
            raw_data = yf.download(tickers=selected_tickers, start=start_datetime.strftime('%Y-%m-%d'), end=download_end_date, interval=interval, group_by='ticker', auto_adjust=False, actions=False, progress=False, threads=True)
            if raw_data is not None and isinstance(raw_data, pd.DataFrame) and (not raw_data.empty):
                break
            errors.append(f'Download attempt {attempt}: Yahoo Finance returned an empty DataFrame.')
        except Exception as error:
            errors.append(f'Download attempt {attempt} failed: {type(error).__name__}: {error}')
        if attempt < maximum_attempts:
            time.sleep(2)
    if raw_data is None or not isinstance(raw_data, pd.DataFrame) or raw_data.empty:
        raise RuntimeError('Yahoo Finance did not return any data after three attempts.')
    raw_data = raw_data.sort_index()
    normalized_index = pd.to_datetime(raw_data.index)
    if normalized_index.tz is not None:
        normalized_index = normalized_index.tz_convert('America/New_York').tz_localize(None)
    raw_data.index = normalized_index
    raw_data = raw_data.loc[raw_data.index.normalize() <= end_datetime].copy()
    if raw_data.empty:
        raise RuntimeError('The dataset is empty after applying the limit corresponding to the latest completed trading session of the New York stock exchanges.')
    downloaded_last_date = pd.Timestamp(raw_data.index.max()).normalize()
    if downloaded_last_date > end_datetime:
        raise RuntimeError('The dataset contains a date later than the latest allowed trading session.')
    downloaded_tickers = []
    failed_tickers = []
    if len(selected_tickers) == 1:
        ticker = selected_tickers[0]
        if raw_data.dropna(how='all').empty:
            failed_tickers.append(ticker)
        else:
            downloaded_tickers.append(ticker)
    elif isinstance(raw_data.columns, pd.MultiIndex):
        first_level_values = set((str(value) for value in raw_data.columns.get_level_values(0)))
        second_level_values = set((str(value) for value in raw_data.columns.get_level_values(1)))
        for ticker in selected_tickers:
            ticker_frame = None
            if ticker in first_level_values:
                try:
                    ticker_frame = raw_data[ticker]
                except Exception:
                    ticker_frame = None
            elif ticker in second_level_values:
                try:
                    ticker_frame = raw_data.xs(ticker, axis=1, level=1)
                except Exception:
                    ticker_frame = None
            if ticker_frame is None or ticker_frame.empty or ticker_frame.dropna(how='all').empty:
                failed_tickers.append(ticker)
            else:
                downloaded_tickers.append(ticker)
    else:
        errors.append('Yahoo Finance returned non-MultiIndex columns for a request with multiple tickers. The structure will be verified in subsequent nodes.')
        downloaded_tickers = selected_tickers.copy()
    if failed_tickers:
        errors.append(f'Yahoo Finance did not return usable data for the following tickers: {failed_tickers}')
    if len(downloaded_tickers) == 0:
        raise RuntimeError('None of the requested tickers contains usable data.')
    return {'raw_data': raw_data, 'failed_tickers': failed_tickers, 'data_source': 'Yahoo Finance via yfinance', 'current_node': 'market_data_collector_agent', 'execution_status': 'running', 'errors': errors}
EXPECTED_COLUMNS = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']

def extract_single_ticker_dataframe(raw_data: pd.DataFrame, ticker: str, total_tickers: int) -> pd.DataFrame:
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
    if raw_data is None:
        return pd.DataFrame()
    if not isinstance(raw_data, pd.DataFrame):
        return pd.DataFrame()
    if raw_data.empty:
        return pd.DataFrame()
    normalized_ticker = normalize_ticker(ticker)
    ticker_data = None
    if isinstance(raw_data.columns, pd.MultiIndex):
        level_zero = [str(value).strip() for value in raw_data.columns.get_level_values(0)]
        level_one = [str(value).strip() for value in raw_data.columns.get_level_values(1)]
        if normalized_ticker in level_zero:
            try:
                ticker_data = raw_data.xs(normalized_ticker, axis=1, level=0).copy()
            except (KeyError, ValueError):
                ticker_data = None
        elif normalized_ticker in level_one:
            try:
                ticker_data = raw_data.xs(normalized_ticker, axis=1, level=1).copy()
            except (KeyError, ValueError):
                ticker_data = None
        else:
            return pd.DataFrame()
    else:
        if total_tickers != 1:
            return pd.DataFrame()
        ticker_data = raw_data.copy()
    if ticker_data is None:
        return pd.DataFrame()
    if ticker_data.empty:
        return pd.DataFrame()
    if isinstance(ticker_data.columns, pd.MultiIndex):
        ticker_data.columns = [' '.join((str(value).strip() for value in column if str(value).strip())) for column in ticker_data.columns]
    else:
        ticker_data.columns = [str(column).strip() for column in ticker_data.columns]
    column_mapping = {'AdjClose': 'Adj Close', 'Adj_Close': 'Adj Close', 'Adjusted Close': 'Adj Close'}
    ticker_data = ticker_data.rename(columns=column_mapping)
    ticker_data = ticker_data.loc[:, ~ticker_data.columns.duplicated()]
    ticker_data = ticker_data.dropna(axis=1, how='all')
    ticker_data = ticker_data.sort_index()
    return ticker_data

def data_cleaning_agent(state: MarketDataState) -> Dict[str, Any]:
    raw_data = state['raw_data']
    selected_tickers = state['tickers']
    clean_data = {}
    report_rows = []
    errors = state.get('errors', []).copy()
    parsed_request = state.get('parsed_request', {})
    requested_end_date = parsed_request.get('end_date', DEFAULT_END_DATE)
    try:
        requested_end_datetime = pd.to_datetime(requested_end_date, format='%Y-%m-%d').normalize()
        last_completed_session = pd.to_datetime(DEFAULT_END_DATE, format='%Y-%m-%d').normalize()
    except Exception as error:
        raise ValueError('The end date must be expressed in YYYY-MM-DD format.') from error
    expected_end_datetime = min(requested_end_datetime, last_completed_session)
    for ticker in selected_tickers:
        ticker_df = extract_single_ticker_dataframe(raw_data=raw_data, ticker=ticker, total_tickers=len(selected_tickers))
        if ticker_df.empty:
            errors.append(f'{ticker}: no data available.')
            continue
        original_rows = len(ticker_df)
        ticker_df.index = pd.to_datetime(ticker_df.index, errors='coerce')
        if ticker_df.index.tz is not None:
            ticker_df.index = ticker_df.index.tz_convert('America/New_York').tz_localize(None)
        invalid_dates = int(ticker_df.index.isna().sum())
        ticker_df = ticker_df[~ticker_df.index.isna()]
        ticker_df = ticker_df.sort_index()
        rows_after_end_date_mask = ticker_df.index.normalize() > expected_end_datetime
        rows_after_end_date_removed = int(rows_after_end_date_mask.sum())
        ticker_df = ticker_df.loc[~rows_after_end_date_mask].copy()
        if ticker_df.empty:
            errors.append(f'{ticker}: no rows available up to the end date {expected_end_datetime.date()}.')
            continue
        duplicate_count = int(ticker_df.index.duplicated(keep='first').sum())
        ticker_df = ticker_df[~ticker_df.index.duplicated(keep='first')]
        missing_columns = [column for column in EXPECTED_COLUMNS if column not in ticker_df.columns]
        if missing_columns:
            errors.append(f'{ticker}: missing columns added with NA values: {missing_columns}')
            for column in missing_columns:
                ticker_df[column] = np.nan
        ticker_df = ticker_df[EXPECTED_COLUMNS]
        non_numeric_values = 0
        for column in EXPECTED_COLUMNS:
            original_non_null = int(ticker_df[column].notna().sum())
            ticker_df[column] = pd.to_numeric(ticker_df[column], errors='coerce')
            converted_non_null = int(ticker_df[column].notna().sum())
            non_numeric_values += original_non_null - converted_non_null
        infinite_values = int(np.isinf(ticker_df.select_dtypes(include=[np.number])).sum().sum())
        ticker_df = ticker_df.replace([np.inf, -np.inf], np.nan)
        missing_before = int(ticker_df.isna().sum().sum())
        completely_empty_mask = ticker_df.isna().all(axis=1)
        completely_empty_rows = int(completely_empty_mask.sum())
        ticker_df = ticker_df.loc[~completely_empty_mask].copy()
        if ticker_df.empty:
            errors.append(f'{ticker}: all rows are empty.')
            continue
        trailing_incomplete_rows_removed = 0
        while not ticker_df.empty and ticker_df.iloc[-1][EXPECTED_COLUMNS].isna().any():
            ticker_df = ticker_df.iloc[:-1].copy()
            trailing_incomplete_rows_removed += 1
        if ticker_df.empty:
            errors.append(f'{ticker}: no complete trading session available after excluding incomplete trailing rows.')
            continue
        ticker_df = ticker_df.ffill().bfill()
        remaining_missing_values = int(ticker_df.isna().sum().sum())
        if remaining_missing_values > 0:
            errors.append(f'{ticker}: unable to replace {remaining_missing_values} NA values because the corresponding column contains no valid value.')
            continue
        price_columns = ['Open', 'High', 'Low', 'Close', 'Adj Close']
        non_positive_price_mask = ticker_df[price_columns].le(0).any(axis=1)
        non_positive_price_rows = int(non_positive_price_mask.sum())
        ticker_df = ticker_df.loc[~non_positive_price_mask]
        negative_volume_mask = ticker_df['Volume'] < 0
        negative_volume_rows = int(negative_volume_mask.sum())
        ticker_df = ticker_df.loc[~negative_volume_mask]
        missing_close_rows = int(ticker_df['Close'].isna().sum())
        ticker_df.index.name = 'Date'
        final_rows = len(ticker_df)
        if ticker_df.empty:
            errors.append(f'{ticker}: no valid rows after cleaning.')
            continue
        final_last_date = pd.Timestamp(ticker_df.index.max()).normalize()
        if final_last_date > expected_end_datetime:
            errors.append(f'{ticker}: the cleaned end date {final_last_date.date()} exceeds the limit {expected_end_datetime.date()}.')
            continue
        total_cells = max(final_rows * len(EXPECTED_COLUMNS), 1)
        final_missing_values = int(ticker_df.isna().sum().sum())
        missing_ratio = final_missing_values / total_cells
        clean_data[ticker] = ticker_df
        report_rows.append({'Ticker': ticker, 'Original_Rows': original_rows, 'Final_Rows': final_rows, 'Removed_Rows': original_rows - final_rows, 'Invalid_Dates': invalid_dates, 'Rows_After_End_Date_Removed': rows_after_end_date_removed, 'Trailing_Incomplete_Rows_Removed': trailing_incomplete_rows_removed, 'Duplicates_Removed': duplicate_count, 'Missing_Columns': missing_columns, 'Non_Numeric_Values': non_numeric_values, 'Infinite_Values': infinite_values, 'Empty_Rows_Removed': completely_empty_rows, 'Non_Positive_Price_Rows': non_positive_price_rows, 'Negative_Volume_Rows': negative_volume_rows, 'Missing_Close_Rows': missing_close_rows, 'Missing_Values_Before': missing_before, 'Missing_Values_After': final_missing_values, 'Missing_Ratio': missing_ratio, 'Expected_Last_Date': expected_end_datetime, 'First_Date': ticker_df.index.min(), 'Last_Date': ticker_df.index.max()})
    cleaning_report = pd.DataFrame(report_rows)
    return {'clean_data': clean_data, 'cleaning_report': cleaning_report, 'current_node': 'data_cleaning_agent', 'execution_status': 'running', 'errors': errors}

def data_alignment_agent(state: MarketDataState) -> Dict[str, Any]:
    clean_data = state['clean_data']
    errors = state.get('errors', []).copy()
    price_series = {}
    volume_series = {}
    parsed_request = state.get('parsed_request', {})
    requested_end_date = parsed_request.get('end_date', DEFAULT_END_DATE)
    try:
        requested_end_datetime = pd.to_datetime(requested_end_date, format='%Y-%m-%d').normalize()
        last_completed_session = pd.to_datetime(DEFAULT_END_DATE, format='%Y-%m-%d').normalize()
    except Exception as error:
        raise ValueError('The end date must be expressed in YYYY-MM-DD format.') from error
    expected_end_datetime = min(requested_end_datetime, last_completed_session)
    ticker_last_dates = {}
    tickers_missing_expected_date = []
    for ticker, ticker_df in clean_data.items():
        if ticker_df.empty:
            errors.append(f'{ticker}: no data available for alignment.')
            continue
        ticker_df = ticker_df.sort_index()
        ticker_last_date = pd.Timestamp(ticker_df.index.max()).normalize()
        ticker_last_dates[ticker] = ticker_last_date
        if expected_end_datetime not in ticker_df.index.normalize():
            tickers_missing_expected_date.append(ticker)
        adjusted_close = ticker_df['Adj Close'].copy()
        if adjusted_close.isna().all():
            adjusted_close = ticker_df['Close'].copy()
        price_series[ticker] = adjusted_close
        volume_series[ticker] = ticker_df['Volume']
    if len(price_series) == 0:
        raise ValueError('No valid series are available for alignment.')
    all_prices = pd.concat(price_series, axis=1).sort_index()
    all_volumes = pd.concat(volume_series, axis=1).sort_index()
    rows_before_alignment = len(all_prices)
    aligned_prices = all_prices.dropna(how='any')
    aligned_volumes = all_volumes.reindex(aligned_prices.index)
    rows_after_alignment = len(aligned_prices)
    removed_rows = rows_before_alignment - rows_after_alignment
    loss_ratio = removed_rows / rows_before_alignment if rows_before_alignment > 0 else 0
    last_common_date = pd.Timestamp(aligned_prices.index.max()).normalize() if not aligned_prices.empty else None
    expected_date_available_for_all = not tickers_missing_expected_date
    last_common_date_matches_expected = last_common_date == expected_end_datetime if last_common_date is not None else False
    temporal_alignment_passed = expected_date_available_for_all and last_common_date_matches_expected
    if tickers_missing_expected_date:
        errors.append(f"The following tickers do not have data for the expected final date {expected_end_datetime.strftime('%Y-%m-%d')}: {tickers_missing_expected_date}")
    if last_common_date is not None and (not last_common_date_matches_expected):
        errors.append(f"The final common date of the dataset ({last_common_date.strftime('%Y-%m-%d')}) does not match the expected final date ({expected_end_datetime.strftime('%Y-%m-%d')}).")
    if aligned_prices.empty:
        errors.append('No dates are common to all tickers.')
    alignment_report = {'rows_before_alignment': rows_before_alignment, 'rows_after_alignment': rows_after_alignment, 'removed_rows': removed_rows, 'alignment_loss_ratio': loss_ratio, 'number_of_requested_tickers': len(clean_data), 'number_of_aligned_tickers': aligned_prices.shape[1], 'expected_last_date': expected_end_datetime.strftime('%Y-%m-%d'), 'first_common_date': str(aligned_prices.index.min().date()) if not aligned_prices.empty else None, 'last_common_date': str(aligned_prices.index.max().date()) if not aligned_prices.empty else None, 'tickers_missing_expected_date': tickers_missing_expected_date, 'number_of_tickers_missing_expected_date': len(tickers_missing_expected_date), 'expected_date_available_for_all': expected_date_available_for_all, 'last_common_date_matches_expected': last_common_date_matches_expected, 'temporal_alignment_passed': temporal_alignment_passed, 'ticker_last_dates': {ticker: ticker_date.strftime('%Y-%m-%d') for ticker, ticker_date in ticker_last_dates.items()}}
    if tickers_missing_expected_date:
        pass
    return {'aligned_prices': aligned_prices, 'aligned_volumes': aligned_volumes, 'alignment_report': alignment_report, 'current_node': 'data_alignment_agent', 'execution_status': 'running', 'errors': errors}

def feature_preparation_agent(state: MarketDataState) -> Dict[str, Any]:
    aligned_prices = state['aligned_prices']
    errors = state.get('errors', []).copy()
    if aligned_prices.empty:
        raise ValueError('The aligned price matrix is empty.')
    simple_returns = aligned_prices.pct_change(fill_method=None).replace([np.inf, -np.inf], np.nan).dropna(how='all')
    log_returns = np.log(aligned_prices / aligned_prices.shift(1)).replace([np.inf, -np.inf], np.nan).dropna(how='all')
    feature_report = {'number_of_assets': aligned_prices.shape[1], 'number_of_observations': aligned_prices.shape[0], 'simple_returns_rows': simple_returns.shape[0], 'log_returns_rows': log_returns.shape[0], 'first_return_date': str(simple_returns.index.min().date()) if not simple_returns.empty else None, 'last_return_date': str(simple_returns.index.max().date()) if not simple_returns.empty else None}
    return {'simple_returns': simple_returns, 'log_returns': log_returns, 'feature_report': feature_report, 'current_node': 'feature_preparation_agent', 'execution_status': 'running', 'errors': errors}

def data_quality_validator_agent(state: MarketDataState) -> Dict[str, Any]:
    clean_data = state['clean_data']
    cleaning_report = state['cleaning_report']
    errors = state.get('errors', []).copy()
    validation_rows = []
    if cleaning_report.empty:
        raise ValueError('The cleaning report is empty.')
    parsed_request = state.get('parsed_request', {})
    requested_end_date = parsed_request.get('end_date', DEFAULT_END_DATE)
    try:
        requested_end_datetime = pd.to_datetime(requested_end_date, format='%Y-%m-%d').normalize()
        last_completed_session = pd.to_datetime(DEFAULT_END_DATE, format='%Y-%m-%d').normalize()
    except Exception as error:
        raise ValueError('The end date must be expressed in YYYY-MM-DD format.') from error
    expected_end_datetime = min(requested_end_datetime, last_completed_session)
    for _, cleaning_row in cleaning_report.iterrows():
        ticker = cleaning_row['Ticker']
        ticker_df = clean_data.get(ticker, pd.DataFrame())
        actual_last_date = pd.Timestamp(ticker_df.index.max()).normalize() if not ticker_df.empty else None
        expected_last_date_check = actual_last_date == expected_end_datetime if actual_last_date is not None else False
        checks = {'minimum_observations': len(ticker_df) >= MINIMUM_OBSERVATIONS, 'no_duplicates': cleaning_row['Duplicates_Removed'] == 0, 'no_non_positive_prices': cleaning_row['Non_Positive_Price_Rows'] == 0, 'no_negative_volumes': cleaning_row['Negative_Volume_Rows'] == 0, 'acceptable_missing_ratio': cleaning_row['Missing_Ratio'] <= MAX_MISSING_RATIO, 'valid_period': pd.notna(cleaning_row['First_Date']) and pd.notna(cleaning_row['Last_Date']), 'expected_last_date': expected_last_date_check}
        passed_checks = sum((bool(value) for value in checks.values()))
        total_checks = len(checks)
        quality_score = round(100 * passed_checks / total_checks, 2)
        critical_failure = not checks['minimum_observations'] or not checks['valid_period'] or (not checks['expected_last_date'])
        if critical_failure:
            status = 'FAIL'
        elif quality_score < 100:
            status = 'WARNING'
        else:
            status = 'PASS'
        failed_checks = [check_name for check_name, check_value in checks.items() if not check_value]
        if status != 'PASS':
            errors.append(f'{ticker}: quality validation {status}. Failed checks: {failed_checks}')
        validation_rows.append({'Ticker': ticker, 'Status': status, 'Quality_Score': quality_score, 'Observations': len(ticker_df), 'Missing_Ratio': cleaning_row['Missing_Ratio'], 'First_Date': cleaning_row['First_Date'], 'Last_Date': cleaning_row['Last_Date'], 'Expected_Last_Date': expected_end_datetime, 'Minimum_Observations_Check': checks['minimum_observations'], 'Duplicates_Check': checks['no_duplicates'], 'Prices_Check': checks['no_non_positive_prices'], 'Volumes_Check': checks['no_negative_volumes'], 'Missing_Ratio_Check': checks['acceptable_missing_ratio'], 'Valid_Period_Check': checks['valid_period'], 'Expected_Last_Date_Check': checks['expected_last_date'], 'Failed_Checks': ', '.join(failed_checks)})
    validation_report = pd.DataFrame(validation_rows)
    status_summary = validation_report['Status'].value_counts().to_dict() if not validation_report.empty else {}
    temporally_aligned_tickers = int(validation_report['Expected_Last_Date_Check'].sum()) if not validation_report.empty else 0
    validation_summary = {'total_tickers': len(validation_report), 'pass_tickers': status_summary.get('PASS', 0), 'warning_tickers': status_summary.get('WARNING', 0), 'fail_tickers': status_summary.get('FAIL', 0), 'average_quality_score': round(validation_report['Quality_Score'].mean(), 2) if not validation_report.empty else 0, 'expected_last_date': expected_end_datetime.strftime('%Y-%m-%d'), 'temporally_aligned_tickers': temporally_aligned_tickers, 'temporally_not_aligned_tickers': len(validation_report) - temporally_aligned_tickers, 'temporal_alignment_passed': temporally_aligned_tickers == len(validation_report) and (not validation_report.empty)}
    return {'validation_report': validation_report, 'validation_summary': validation_summary, 'current_node': 'data_quality_validator_agent', 'execution_status': 'running', 'errors': errors}

def cross_source_checker_agent(state: MarketDataState) -> Dict[str, Any]:
    errors = state.get('errors', []).copy()
    if not ENABLE_CROSS_SOURCE_CHECK:
        cross_source_summary = {'enabled': False, 'twelve_data_responding': False, 'twelve_data_has_data': False, 'latest_yahoo_date': None, 'latest_twelve_data_date': None, 'sampling_method': 'first common trading session of each month', 'monthly_samples_tested': 0, 'samples_above_tolerance': 0, 'tolerance_percent': CROSS_SOURCE_TOLERANCE_PERCENT, 'blocking_failure': False, 'overall_status': 'DISABLED'}
        return {'cross_source_report': pd.DataFrame(), 'cross_source_comparison': pd.DataFrame(), 'cross_source_monthly_test': pd.DataFrame(), 'cross_source_summary': cross_source_summary, 'cross_source_reference_date': None, 'cross_source_blocking_failure': False, 'current_node': 'cross_source_checker_agent', 'execution_status': 'running', 'errors': errors}
    clean_data = state.get('clean_data', {})
    if not clean_data:
        raise ValueError("state['clean_data'] is not available or is empty.")
    selected_tickers = list(clean_data.keys())[:MAX_CROSS_SOURCE_TICKERS]
    report_rows = []
    monthly_test_tables = []

    def download_twelve_data_close(ticker: str, start_date: pd.Timestamp, end_date: pd.Timestamp) -> Dict[str, Any]:
        url = 'https://api.twelvedata.com/time_series'
        params = {'symbol': ticker, 'interval': '1day', 'start_date': start_date.strftime('%Y-%m-%d'), 'end_date': end_date.strftime('%Y-%m-%d'), 'outputsize': 5000, 'format': 'JSON', 'timezone': 'America/New_York', 'apikey': TWELVE_DATA_API_KEY}
        try:
            response = requests.get(url, params=params, timeout=30)
            response.raise_for_status()
            payload = response.json()
        except Exception as error:
            return {'responding': False, 'has_data': False, 'series': pd.Series(dtype=float, name='Twelve_Data_Close'), 'message': f'{type(error).__name__}: {error}'}
        if payload.get('status') == 'error':
            return {'responding': True, 'has_data': False, 'series': pd.Series(dtype=float, name='Twelve_Data_Close'), 'message': f"Twelve Data error {payload.get('code', 'UNKNOWN')}: {payload.get('message', '')}"}
        values = payload.get('values', [])
        if not values:
            return {'responding': True, 'has_data': False, 'series': pd.Series(dtype=float, name='Twelve_Data_Close'), 'message': 'Twelve Data did not return any data.'}
        twelve_df = pd.DataFrame(values)
        if 'datetime' not in twelve_df.columns or 'close' not in twelve_df.columns:
            return {'responding': True, 'has_data': False, 'series': pd.Series(dtype=float, name='Twelve_Data_Close'), 'message': 'The Twelve Data response does not contain the datetime and close columns.'}
        twelve_df['Date'] = pd.to_datetime(twelve_df['datetime'], errors='coerce')
        twelve_df['Twelve_Data_Close'] = pd.to_numeric(twelve_df['close'], errors='coerce')
        twelve_df = twelve_df.dropna(subset=['Date', 'Twelve_Data_Close']).drop_duplicates(subset='Date', keep='last').set_index('Date').sort_index()
        if twelve_df.index.tz is not None:
            twelve_df.index = twelve_df.index.tz_convert('America/New_York').tz_localize(None)
        twelve_df.index = twelve_df.index.normalize()
        series = twelve_df['Twelve_Data_Close'].astype(float).rename('Twelve_Data_Close')
        return {'responding': True, 'has_data': not series.empty, 'series': series, 'message': ''}

    def first_common_session_per_month(comparison_df: pd.DataFrame) -> pd.DataFrame:
        """
        Selects the first available common trading session
        for each month over the entire overlapping period.
        """
        if comparison_df.empty:
            return comparison_df.copy()
        return comparison_df.sort_index().groupby(comparison_df.index.to_period('M')).head(1).copy()
    for ticker in selected_tickers:
        ticker_df = clean_data.get(ticker, pd.DataFrame())
        if ticker_df is None or ticker_df.empty or 'Close' not in ticker_df.columns:
            errors.append(f'{ticker}: Yahoo data not available.')
            report_rows.append({'Ticker': ticker, 'Yahoo_Last_Date': None, 'Twelve_Responding': False, 'Twelve_Has_Data': False, 'Twelve_Last_Date': None, 'Update_Status': 'YAHOO_DATA_ERROR', 'Monthly_Samples': 0, 'Samples_Above_Tolerance': 0, 'Maximum_Difference_Percent': np.nan, 'Average_Difference_Percent': np.nan, 'Status': 'NOT_COMPARABLE', 'Blocking_Failure': False})
            continue
        yahoo_close = pd.to_numeric(ticker_df['Close'], errors='coerce')
        yahoo_close.index = pd.to_datetime(yahoo_close.index, errors='coerce')
        if yahoo_close.index.tz is not None:
            yahoo_close.index = yahoo_close.index.tz_convert('America/New_York').tz_localize(None)
        yahoo_close.index = yahoo_close.index.normalize()
        yahoo_close = yahoo_close[~yahoo_close.index.isna()].dropna().groupby(level=0).last().sort_index().astype(float).rename('Yahoo_Close')
        if yahoo_close.empty:
            errors.append(f'{ticker}: Yahoo Close series is empty.')
            continue
        yahoo_first_date = yahoo_close.index.min()
        yahoo_last_date = yahoo_close.index.max()
        twelve_result = download_twelve_data_close(ticker=ticker, start_date=yahoo_first_date, end_date=yahoo_last_date)
        twelve_responding = twelve_result['responding']
        twelve_has_data = twelve_result['has_data']
        twelve_close = twelve_result['series']
        twelve_message = twelve_result['message']
        if not twelve_responding:
            report_rows.append({'Ticker': ticker, 'Yahoo_Last_Date': yahoo_last_date, 'Twelve_Responding': False, 'Twelve_Has_Data': False, 'Twelve_Last_Date': None, 'Update_Status': 'APPLICATION_NOT_RESPONDING', 'Monthly_Samples': 0, 'Samples_Above_Tolerance': 0, 'Maximum_Difference_Percent': np.nan, 'Average_Difference_Percent': np.nan, 'Status': 'NOT_COMPARABLE', 'Blocking_Failure': False})
            errors.append(f'{ticker}: {twelve_message}')
            continue
        if not twelve_has_data:
            report_rows.append({'Ticker': ticker, 'Yahoo_Last_Date': yahoo_last_date, 'Twelve_Responding': True, 'Twelve_Has_Data': False, 'Twelve_Last_Date': None, 'Update_Status': 'NO_DATA_AVAILABLE', 'Monthly_Samples': 0, 'Samples_Above_Tolerance': 0, 'Maximum_Difference_Percent': np.nan, 'Average_Difference_Percent': np.nan, 'Status': 'NOT_COMPARABLE', 'Blocking_Failure': False})
            continue
        twelve_last_date = twelve_close.index.max()
        if twelve_last_date < yahoo_last_date:
            update_status = 'AVAILABLE_BUT_NOT_UPDATED'
        elif twelve_last_date == yahoo_last_date:
            update_status = 'AVAILABLE_AND_UPDATED'
        else:
            update_status = 'AVAILABLE_WITH_LATER_DATE'
        comparison_df = pd.concat([yahoo_close, twelve_close], axis=1, join='inner').dropna()
        monthly_test = first_common_session_per_month(comparison_df)
        if monthly_test.empty:
            report_rows.append({'Ticker': ticker, 'Yahoo_Last_Date': yahoo_last_date, 'Twelve_Responding': True, 'Twelve_Has_Data': True, 'Twelve_Last_Date': twelve_last_date, 'Update_Status': update_status, 'Monthly_Samples': 0, 'Samples_Above_Tolerance': 0, 'Maximum_Difference_Percent': np.nan, 'Average_Difference_Percent': np.nan, 'Status': 'NOT_COMPARABLE', 'Blocking_Failure': False})
            continue
        monthly_test['Difference_Percent'] = (monthly_test['Yahoo_Close'] - monthly_test['Twelve_Data_Close']).abs() / monthly_test['Yahoo_Close'].abs() * 100
        monthly_test['Within_Tolerance'] = monthly_test['Difference_Percent'] <= CROSS_SOURCE_TOLERANCE_PERCENT
        monthly_test.insert(0, 'Ticker', ticker)
        monthly_test_tables.append(monthly_test.copy())
        samples_above = int((~monthly_test['Within_Tolerance']).sum())
        blocking_failure = samples_above > 0
        report_rows.append({'Ticker': ticker, 'Yahoo_Last_Date': yahoo_last_date, 'Twelve_Responding': True, 'Twelve_Has_Data': True, 'Twelve_Last_Date': twelve_last_date, 'Update_Status': update_status, 'Monthly_Samples': len(monthly_test), 'Samples_Above_Tolerance': samples_above, 'Maximum_Difference_Percent': float(monthly_test['Difference_Percent'].max()), 'Average_Difference_Percent': float(monthly_test['Difference_Percent'].mean()), 'Status': 'FAIL' if blocking_failure else 'PASS', 'Blocking_Failure': blocking_failure})
    cross_source_report = pd.DataFrame(report_rows)
    if monthly_test_tables:
        cross_source_monthly_test = pd.concat(monthly_test_tables, axis=0)
        cross_source_monthly_test.index.name = 'Date'
    else:
        cross_source_monthly_test = pd.DataFrame(columns=['Ticker', 'Yahoo_Close', 'Twelve_Data_Close', 'Difference_Percent', 'Within_Tolerance'])
    cross_source_comparison = cross_source_monthly_test.copy()
    twelve_data_responding = bool(cross_source_report['Twelve_Responding'].any() if not cross_source_report.empty else False)
    twelve_data_has_data = bool(cross_source_report['Twelve_Has_Data'].any() if not cross_source_report.empty else False)
    latest_yahoo_date = pd.to_datetime(cross_source_report['Yahoo_Last_Date'], errors='coerce').max() if not cross_source_report.empty else pd.NaT
    latest_twelve_data_date = pd.to_datetime(cross_source_report['Twelve_Last_Date'], errors='coerce').max() if not cross_source_report.empty else pd.NaT
    monthly_samples_tested = int(cross_source_report['Monthly_Samples'].fillna(0).sum() if not cross_source_report.empty else 0)
    samples_above_tolerance = int(cross_source_report['Samples_Above_Tolerance'].fillna(0).sum() if not cross_source_report.empty else 0)
    blocking_failure = bool(cross_source_report['Blocking_Failure'].fillna(False).any() if not cross_source_report.empty else False)
    if blocking_failure:
        overall_status = 'FAIL'
    elif monthly_samples_tested > 0:
        overall_status = 'PASS'
    else:
        overall_status = 'NOT_COMPARABLE'
    cross_source_summary = {'enabled': True, 'twelve_data_responding': twelve_data_responding, 'twelve_data_has_data': twelve_data_has_data, 'latest_yahoo_date': latest_yahoo_date.strftime('%Y-%m-%d') if pd.notna(latest_yahoo_date) else None, 'latest_twelve_data_date': latest_twelve_data_date.strftime('%Y-%m-%d') if pd.notna(latest_twelve_data_date) else None, 'sampling_method': 'first common trading session of each month', 'monthly_samples_tested': monthly_samples_tested, 'samples_above_tolerance': samples_above_tolerance, 'tolerance_percent': CROSS_SOURCE_TOLERANCE_PERCENT, 'blocking_failure': blocking_failure, 'overall_status': overall_status}
    return {'cross_source_report': cross_source_report, 'cross_source_comparison': cross_source_comparison, 'cross_source_monthly_test': cross_source_monthly_test, 'cross_source_summary': cross_source_summary, 'cross_source_reference_date': latest_yahoo_date, 'cross_source_blocking_failure': blocking_failure, 'current_node': 'cross_source_checker_agent', 'execution_status': 'running', 'errors': errors}

def critic_agent(state: MarketDataState) -> Dict[str, Any]:
    cleaning_report = state['cleaning_report']
    validation_report = state['validation_report']
    alignment_report = state['alignment_report']
    cross_source_report = state['cross_source_report']
    critic_input = {'cleaning_report': cleaning_report.replace({np.nan: None}).to_dict(orient='records'), 'validation_report': validation_report.replace({np.nan: None}).to_dict(orient='records'), 'alignment_report': alignment_report, 'cross_source_report': cross_source_report.replace({np.nan: None}).to_dict(orient='records')}
    system_instruction = '\nYou are the Critic Agent of a quantitative financial system.\n\nYou must evaluate exclusively the technical reports received.\n\nYou must not:\n- recalculate the data;\n- invent information;\n- formulate financial forecasts;\n- provide advice;\n- modify Python results;\n- add text outside the JSON.\n\nThe primary dataset is the one produced by Yahoo Finance.\n\nTwelve Data is used exclusively as a secondary source\nfor validation and challenge.\n\nFailure of Twelve Data to respond, absence of Twelve Data data,\nor a Twelve Data end date earlier than Yahoo Finance\nare exclusively diagnostic conditions.\n\nThese conditions:\n- do NOT constitute warnings on the primary dataset;\n- do NOT constitute limitations of the primary dataset;\n- must NOT modify critic_status;\n- must NOT be included in warnings;\n- must NOT be included in recommended_actions;\n- must NOT make dataset_ready false.\n\nIn the cross-source check, only price consistency\non actually comparable dates is relevant.\n\nA cross-source issue is critical only if\nBlocking_Failure is true, meaning that one or more compared prices\nexceed the CROSS_SOURCE_TOLERANCE_PERCENT threshold.\n\nYou must return exactly one JSON object with this structure:\n\n{\n    "critic_status": "PASSED",\n    "dataset_ready": true,\n    "critical_issues": [],\n    "warnings": [],\n    "recommended_actions": [],\n    "reasoning_summary": "brief technical explanation"\n}\n\nUse critic_status exclusively as:\n- PASSED if the dataset can be used;\n- FAILED if critical issues exist that prevent its use.\n\nDo not use APPROVED_WITH_WARNINGS.\n\nIf:\n- deterministic checks are passed;\n- there are no FAIL tickers;\n- temporal alignment is valid;\n- the price comparison on common dates does not show\n  Blocking_Failure;\n\nthen the dataset must be classified as PASSED,\neven if Twelve Data is less up to date than Yahoo Finance.\n'
    try:
        critic_report = call_llm_json(system_instruction=system_instruction, user_content=json.dumps(critic_input, ensure_ascii=False, default=str), model=CRITIC_MODEL)
        failed_tickers = validation_report.loc[validation_report['Status'] == 'FAIL', 'Ticker'].tolist()
        cross_source_blocking_failure = bool(state.get('cross_source_blocking_failure', False))
        deterministic_pass = bool(len(failed_tickers) == 0 and (not cross_source_blocking_failure))
        if deterministic_pass:
            critic_report['critic_status'] = 'PASSED'
            critic_report['dataset_ready'] = True
            critic_report['critical_issues'] = []
            critic_report['warnings'] = []
            critic_report['recommended_actions'] = []
        else:
            critic_report['critic_status'] = 'FAILED'
            critic_report['dataset_ready'] = False
    except Exception as error:
        failed_tickers = validation_report.loc[validation_report['Status'] == 'FAIL', 'Ticker'].tolist()
        cross_source_blocking_failure = bool(state.get('cross_source_blocking_failure', False))
        dataset_ready = bool(len(failed_tickers) == 0 and (not cross_source_blocking_failure))
        critic_report = {'critic_status': 'PASSED' if dataset_ready else 'FAILED', 'dataset_ready': dataset_ready, 'critical_issues': [] if dataset_ready else failed_tickers, 'warnings': [], 'recommended_actions': [], 'reasoning_summary': 'OpenRouter Critic Agent unavailable. Deterministic check applied.', 'openrouter_error': str(error)}
    return {'critic_report': critic_report, 'current_node': 'critic_agent', 'execution_status': 'running'}

def dataset_certification_agent(state: MarketDataState) -> Dict[str, Any]:
    validation_report = state['validation_report']
    critic_report = state['critic_report']
    aligned_prices = state['aligned_prices']
    log_returns = state['log_returns']
    alignment_report = state.get('alignment_report', {})
    cross_source_summary = state.get('cross_source_summary', {})
    cross_source_blocking_failure = bool(state.get('cross_source_blocking_failure', cross_source_summary.get('blocking_failure', False)))
    passed_tickers = validation_report.loc[validation_report['Status'] == 'PASS', 'Ticker'].tolist()
    warning_tickers = validation_report.loc[validation_report['Status'] == 'WARNING', 'Ticker'].tolist()
    failed_tickers = validation_report.loc[validation_report['Status'] == 'FAIL', 'Ticker'].tolist()
    average_quality_score = float(validation_report['Quality_Score'].mean()) if not validation_report.empty else 0.0
    temporal_alignment_ready = bool(alignment_report.get('temporal_alignment_passed', False))
    deterministic_ready = bool(not aligned_prices.empty and (not log_returns.empty) and (len(failed_tickers) == 0) and temporal_alignment_ready and (not cross_source_blocking_failure))
    critic_ready = bool(critic_report.get('dataset_ready', False))
    dataset_ready = bool(deterministic_ready and critic_ready)
    usable_for = []
    if dataset_ready:
        usable_for.extend(['financial_metrics', 'sharpe_ratio', 'momentum', 'dollar_volume', 'cross_sectional_momentum', 'capm'])
        if aligned_prices.shape[1] >= 2:
            usable_for.extend(['correlation'])
    certification = {'project': PROJECT_NAME, 'certification_timestamp': datetime.now().isoformat(), 'dataset_ready': dataset_ready, 'deterministic_ready': deterministic_ready, 'critic_ready': critic_ready, 'temporal_alignment_ready': temporal_alignment_ready, 'cross_source_blocking_failure': cross_source_blocking_failure, 'cross_source_summary': cross_source_summary, 'average_quality_score': round(average_quality_score, 2), 'total_tickers': len(validation_report), 'passed_tickers': passed_tickers, 'warning_tickers': warning_tickers, 'failed_tickers': failed_tickers, 'aligned_observations': len(aligned_prices), 'usable_for': usable_for, 'critic_status': 'PASSED' if dataset_ready else 'FAILED', 'limitations': [] if dataset_ready else critic_report.get('critical_issues', [])}
    return {'certification': certification, 'current_node': 'dataset_certification_agent', 'execution_status': 'completed'}
graph_builder = StateGraph(MarketDataState)
graph_builder.add_node('request_interpreter', request_interpreter_agent)
graph_builder.add_node('ticker_resolution', ticker_resolution_agent)
graph_builder.add_node('market_data_collector', market_data_collector_agent)
graph_builder.add_node('data_cleaning', data_cleaning_agent)
graph_builder.add_node('data_alignment', data_alignment_agent)
graph_builder.add_node('feature_preparation', feature_preparation_agent)
graph_builder.add_node('data_quality_validator', data_quality_validator_agent)
graph_builder.add_node('cross_source_checker', cross_source_checker_agent)
graph_builder.add_node('critic_agent', critic_agent)
graph_builder.add_node('dataset_certification', dataset_certification_agent)
graph_builder.add_edge(START, 'request_interpreter')
graph_builder.add_edge('request_interpreter', 'ticker_resolution')
graph_builder.add_edge('ticker_resolution', 'market_data_collector')
graph_builder.add_edge('market_data_collector', 'data_cleaning')
graph_builder.add_edge('data_cleaning', 'data_alignment')
graph_builder.add_edge('data_alignment', 'feature_preparation')
graph_builder.add_edge('feature_preparation', 'data_quality_validator')
graph_builder.add_edge('data_quality_validator', 'cross_source_checker')
graph_builder.add_edge('cross_source_checker', 'critic_agent')
graph_builder.add_edge('critic_agent', 'dataset_certification')
graph_builder.add_edge('dataset_certification', END)
market_data_graph = graph_builder.compile()
USER_REQUEST = '\nPrepare and validate the daily historical time series of all\nDow Jones stocks from 2010 to today.\n'
initial_state: MarketDataState = {'user_request': USER_REQUEST, 'tickers': tickers, 'errors': []}
_internal_output = io.StringIO()
with contextlib.redirect_stdout(_internal_output):
    final_state = market_data_graph.invoke(initial_state)
clean_data = final_state.get('clean_data', {})
cleaning_report = final_state.get('cleaning_report', pd.DataFrame())
validation_report = final_state.get('validation_report', pd.DataFrame())
alignment_report = final_state.get('alignment_report', {})
cross_source_report = final_state.get('cross_source_report', pd.DataFrame())
cross_source_summary = final_state.get('cross_source_summary', {})
critic_report = final_state.get('critic_report', {})
certification = final_state.get('certification', {})



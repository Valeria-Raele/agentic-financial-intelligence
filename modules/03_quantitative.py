clean_data = final_state['clean_data']
aligned_prices = final_state['aligned_prices']
aligned_volumes = final_state['aligned_volumes']
simple_returns = final_state['simple_returns']
log_returns = final_state['log_returns']

def financial_metrics_tool(state: MarketDataState, risk_free_rate: float=0.03, start_date: str=None, end_date: str=None, period_type: str=None) -> Dict[str, Any]:
    start_time = time.perf_counter()
    calculation_errors = []
    log_returns = state['log_returns'].copy()
    normalized_period_type = str(period_type).strip().lower() if period_type is not None else None
    if normalized_period_type == 'rolling' and (not (start_date and end_date)):
        raise ValueError("financial_metrics_tool received period_type='rolling' without start_date/end_date. calendar_year execution blocked.")
    exact_period_mode = bool(start_date or end_date)
    if exact_period_mode:
        if not (start_date and end_date):
            raise ValueError('start_date and end_date must be provided together.')
        start_ts = pd.Timestamp(start_date).normalize()
        end_ts = pd.Timestamp(end_date).normalize()
        if start_ts > end_ts:
            raise ValueError('start_date cannot be later than end_date.')
        log_returns = log_returns.loc[(log_returns.index >= start_ts) & (log_returns.index <= end_ts)].copy()
        if log_returns.empty:
            raise ValueError('No log returns available within the requested interval.')
        normalized_start_date = start_ts.strftime('%Y-%m-%d')
        normalized_end_date = end_ts.strftime('%Y-%m-%d')
    else:
        normalized_start_date = None
        normalized_end_date = None
    if log_returns.empty:
        raise ValueError('The log_returns matrix is empty.')

    def compute_year_metrics(log_r: pd.Series) -> pd.Series:
        log_r = log_r.dropna()
        if log_r.empty:
            raise ValueError('No log returns available.')
        annualized_return = np.exp(log_r.mean() * 252) - 1
        log_return_std = log_r.std()
        if pd.isna(log_return_std) or not np.isfinite(log_return_std) or log_return_std <= 0:
            raise ValueError('Standard deviation of log returns is missing, non-finite, or equal to zero.')
        vol = log_return_std * np.sqrt(252)
        rr = annualized_return / vol
        daily_rf = np.log(1 + risk_free_rate) / 252
        sharpe = (log_r.mean() - daily_rf) / log_return_std * np.sqrt(252)
        return pd.Series({'Annual Return (%)': annualized_return * 100, 'Annualized Volatility (%)': vol * 100, 'Return-to-Risk Ratio (raw)': rr, 'Sharpe Ratio': sharpe})
    results = []
    for ticker in log_returns.columns:
        ticker_log_returns = log_returns[ticker].dropna()
        if exact_period_mode:
            try:
                metrics = compute_year_metrics(ticker_log_returns)
                metrics.name = f'{ticker}_{normalized_start_date}_{normalized_end_date}'
                results.append(metrics)
            except Exception as error:
                calculation_errors.append({'Ticker': ticker, 'Start Date': normalized_start_date, 'End Date': normalized_end_date, 'Error': str(error)})
        else:
            for year, group in ticker_log_returns.groupby(ticker_log_returns.index.year):
                try:
                    metrics = compute_year_metrics(group)
                    metrics.name = f'{ticker}_{year}'
                    results.append(metrics)
                except Exception as error:
                    calculation_errors.append({'Ticker': ticker, 'Year': int(year), 'Error': str(error)})
    final_table = pd.DataFrame(results)
    if final_table.empty:
        raise ValueError('The tool did not produce valid results.')
    if exact_period_mode:
        final_table['Ticker'] = [str(index_value).split('_', 1)[0] for index_value in final_table.index]
        final_table = final_table.sort_values(by=['Ticker']).drop(columns=['Ticker']).round(2)
    else:
        final_table['Ticker'] = final_table.index.str.rsplit('_', n=1).str[0]
        final_table['Year'] = final_table.index.str.rsplit('_', n=1).str[1].astype(int)
        final_table = final_table.sort_values(by=['Ticker', 'Year'])
        final_table = final_table.drop(columns=['Ticker', 'Year']).round(2)
    if final_table.empty:
        raise ValueError('The tool produced an empty table.')
    if final_table.isna().any().any():
        invalid_rows = final_table[final_table.isna().any(axis=1)].index.tolist()
        raise ValueError(f'The tool produced NA values or incomplete rows: {invalid_rows}')
    numeric_values = final_table.to_numpy(dtype=float)
    if not np.isfinite(numeric_values).all():
        raise ValueError('The tool produced infinite values or invalid numbers.')
    if not (final_table['Annualized Volatility (%)'] > 0).all():
        raise ValueError('The tool produced zero or negative annualized volatility values.')
    if not final_table['Annual Return (%)'].between(-100, 100000).all():
        raise ValueError('The tool produced annual returns outside the plausibility range.')
    if not final_table['Return-to-Risk Ratio (raw)'].between(-1000, 1000).all():
        raise ValueError('The tool produced Return-to-Risk Ratio values outside the plausibility range.')
    if not final_table['Sharpe Ratio'].between(-100, 100).all():
        raise ValueError('The tool produced Sharpe Ratio values outside the plausibility range.')
    coherence_check = 'passed'
    execution_time = time.perf_counter() - start_time
    tool_report = {'tool_name': 'financial_metrics_tool', 'execution_timestamp': datetime.now().isoformat(), 'execution_time_seconds': round(execution_time, 4), 'execution_status': 'completed' if not calculation_errors else 'completed_with_errors', 'coherence_check': coherence_check, 'tickers_analyzed': int(log_returns.shape[1]), 'ticker_year_rows': int(len(final_table)), 'period_mode': 'exact_interval' if exact_period_mode else 'calendar_year', 'start_date': normalized_start_date, 'end_date': normalized_end_date, 'calculation_errors': calculation_errors}
    return {'financial_metrics': final_table, 'financial_metrics_report': tool_report, 'current_node': 'financial_metrics_tool', 'execution_status': 'completed'}
financial_metrics_output = financial_metrics_tool(state=final_state, risk_free_rate=0.03)
final_state.update(financial_metrics_output)
final_state.setdefault('response_display_formats', {})
final_state['response_display_formats']['financial_metrics'] = {'Annual Return (%)': 'percent_points_2', 'Annualized Volatility (%)': 'percent_points_2', 'Return-to-Risk Ratio (raw)': 'number_2', 'Sharpe Ratio': 'number_2'}

def pearson_correlation_tool(state: MarketDataState, correlation_threshold: float=0.75, start_date: Any=None, end_date: Any=None) -> Dict[str, Any]:
    start_time = time.perf_counter()
    calculation_errors = []
    if not isinstance(correlation_threshold, (int, float, np.integer, np.floating)):
        raise TypeError('correlation_threshold must be a number.')
    if not np.isfinite(correlation_threshold):
        raise ValueError('correlation_threshold must be a finite value.')
    if not -1.0 <= correlation_threshold < 1.0:
        raise ValueError('correlation_threshold must be within the interval [-1, 1).')
    if 'log_returns' not in state:
        raise KeyError('The log_returns variable is not present in final_state.')
    log_returns = state['log_returns'].copy()
    start_date = None
    end_date = None
    if not isinstance(log_returns, pd.DataFrame):
        raise TypeError('log_returns must be a pandas DataFrame.')
    if log_returns.empty:
        raise ValueError('The log_returns table is empty.')
    if log_returns.shape[1] < 2:
        raise ValueError('At least two tickers are required to calculate a correlation table.')
    if log_returns.columns.duplicated().any():
        duplicated_columns = log_returns.columns[log_returns.columns.duplicated()].tolist()
        raise ValueError(f'Duplicate tickers are present in log_returns: {duplicated_columns}')
    non_numeric_columns = log_returns.select_dtypes(exclude=[np.number]).columns.tolist()
    if non_numeric_columns:
        raise TypeError(f'log_returns contains non-numeric columns: {non_numeric_columns}')
    input_numeric_values = log_returns.to_numpy(dtype=float)
    if np.isinf(input_numeric_values).any():
        raise ValueError('log_returns contains infinite values.')
    valid_observations = log_returns.notna().sum()
    insufficient_tickers = valid_observations[valid_observations < 2].index.tolist()
    if insufficient_tickers:
        raise ValueError(f'The following tickers do not have at least two valid observations: {insufficient_tickers}')
    try:
        correlation_values = log_returns.corr(method='pearson', min_periods=2)
    except Exception as error:
        calculation_errors.append({'Stage': 'correlation_calculation', 'Error': str(error)})
        raise RuntimeError('Error while calculating the correlation table.') from error
    correlation_values = correlation_values.round(4)
    if correlation_values.empty:
        raise ValueError('The tool produced an empty correlation table.')
    if correlation_values.shape[0] != correlation_values.shape[1]:
        raise ValueError('The correlation table is not square.')
    if not correlation_values.index.equals(correlation_values.columns):
        raise ValueError('The rows and columns of the correlation table do not match.')
    if correlation_values.isna().any().any():
        invalid_tickers = correlation_values.index[correlation_values.isna().any(axis=1)].tolist()
        raise ValueError(f'The correlation table contains NaN values. Tickers involved: {invalid_tickers}')
    correlation_numeric_values = correlation_values.to_numpy(dtype=float)
    if not np.isfinite(correlation_numeric_values).all():
        raise ValueError('The correlation table contains infinite or invalid values.')
    tolerance = 0.0001
    if not ((correlation_numeric_values >= -1.0 - tolerance) & (correlation_numeric_values <= 1.0 + tolerance)).all():
        raise ValueError('The table contains correlation coefficients outside the interval [-1, 1].')
    if not np.allclose(correlation_numeric_values, correlation_numeric_values.T, atol=tolerance, rtol=0):
        raise ValueError('The correlation table is not symmetric.')
    diagonal_values = np.diag(correlation_numeric_values)
    if not np.allclose(diagonal_values, np.ones_like(diagonal_values), atol=tolerance, rtol=0):
        raise ValueError('The diagonal of the correlation table does not contain only values equal to 1.')
    tickers = correlation_values.columns.tolist()
    all_unique_pairs = []
    for first_position in range(len(tickers)):
        for second_position in range(first_position + 1, len(tickers)):
            ticker_1 = tickers[first_position]
            ticker_2 = tickers[second_position]
            correlation_value = float(correlation_values.loc[ticker_1, ticker_2])
            all_unique_pairs.append({'Ticker 1': ticker_1, 'Ticker 2': ticker_2, 'Correlation': correlation_value})
    all_correlation_pairs = pd.DataFrame(all_unique_pairs)
    all_correlation_pairs = all_correlation_pairs.sort_values(by='Correlation', ascending=False).reset_index(drop=True)
    if all_correlation_pairs.empty:
        raise ValueError('It was not possible to build the list of unique pairs.')
    expected_pair_count = int(len(tickers) * (len(tickers) - 1) / 2)
    if len(all_correlation_pairs) != expected_pair_count:
        raise ValueError(f'The number of unique pairs produced does not match the theoretically expected number. Expected: {expected_pair_count}; produced: {len(all_correlation_pairs)}.')
    if all_correlation_pairs[['Ticker 1', 'Ticker 2']].isna().any().any():
        raise ValueError('The pair list contains missing tickers.')
    if all_correlation_pairs['Correlation'].isna().any():
        raise ValueError('The pair list contains NaN correlations.')
    if not np.isfinite(all_correlation_pairs['Correlation'].to_numpy(dtype=float)).all():
        raise ValueError('The pair list contains infinite or invalid correlations.')
    if not all_correlation_pairs['Correlation'].between(-1.0, 1.0, inclusive='both').all():
        raise ValueError('The pair list contains correlations outside the interval [-1, 1].')
    duplicated_pairs = all_correlation_pairs[['Ticker 1', 'Ticker 2']].duplicated().any()
    if duplicated_pairs:
        raise ValueError('The list contains duplicate pairs.')
    same_ticker_pairs = (all_correlation_pairs['Ticker 1'] == all_correlation_pairs['Ticker 2']).any()
    if same_ticker_pairs:
        raise ValueError('The list contains at least one pair formed by the same ticker.')
    high_correlation_pairs = all_correlation_pairs[all_correlation_pairs['Correlation'] > correlation_threshold].copy()
    high_correlation_pairs = high_correlation_pairs.sort_values(by='Correlation', ascending=False).reset_index(drop=True)
    high_correlation_pairs.insert(0, 'Rank', np.arange(1, len(high_correlation_pairs) + 1))
    if not high_correlation_pairs.empty:
        if high_correlation_pairs.isna().any().any():
            raise ValueError('The table of pairs above the threshold contains NaN values.')
        high_pair_numeric_values = high_correlation_pairs[['Rank', 'Correlation']].to_numpy(dtype=float)
        if not np.isfinite(high_pair_numeric_values).all():
            raise ValueError('The table of pairs above the threshold contains infinite or invalid values.')
        if not (high_correlation_pairs['Correlation'] > correlation_threshold).all():
            raise ValueError('The table contains one or more pairs that do not exceed the defined threshold.')
        if not high_correlation_pairs['Correlation'].between(-1.0, 1.0, inclusive='both').all():
            raise ValueError('The table of pairs above the threshold contains correlations outside [-1, 1].')
        if not high_correlation_pairs['Correlation'].is_monotonic_decreasing:
            raise ValueError('The pairs above the threshold are not ordered from highest to lowest correlation.')
        expected_ranks = np.arange(1, len(high_correlation_pairs) + 1)
        if not np.array_equal(high_correlation_pairs['Rank'].to_numpy(), expected_ranks):
            raise ValueError('The pair ranking is not sequential.')
    unique_correlations = all_correlation_pairs['Correlation'].to_numpy(dtype=float)
    correlation_statistics = {'minimum_correlation': round(float(np.min(unique_correlations)), 4), 'maximum_correlation': round(float(np.max(unique_correlations)), 4), 'mean_correlation': round(float(np.mean(unique_correlations)), 4), 'median_correlation': round(float(np.median(unique_correlations)), 4)}
    selected_pair_count = int(len(high_correlation_pairs))
    selected_pair_percentage = selected_pair_count / expected_pair_count * 100
    pair_selection_statistics = {'correlation_threshold': float(correlation_threshold), 'total_unique_pairs': expected_pair_count, 'selected_pairs': selected_pair_count, 'excluded_pairs': int(expected_pair_count - selected_pair_count), 'selected_pairs_percentage': round(float(selected_pair_percentage), 2)}
    coherence_checks = {'matrix_not_empty': True, 'matrix_is_square': True, 'matching_index_and_columns': True, 'no_nan_in_matrix': True, 'no_infinite_values_in_matrix': True, 'correlations_within_minus_one_and_one': True, 'matrix_is_symmetric': True, 'diagonal_equals_one': True, 'correct_unique_pair_count': True, 'no_duplicate_pairs': True, 'no_same_ticker_pairs': True, 'no_nan_in_pairs': True, 'no_infinite_values_in_pairs': True, 'selected_pairs_above_threshold': True, 'selected_pairs_correctly_ranked': True}
    coherence_check = 'passed'
    execution_time = time.perf_counter() - start_time
    tool_report = {'tool_name': 'pearson_correlation_tool', 'execution_timestamp': datetime.now().isoformat(), 'execution_time_seconds': round(execution_time, 4), 'execution_status': 'completed' if not calculation_errors else 'completed_with_errors', 'coherence_check': coherence_check, 'coherence_checks': coherence_checks, 'correlation_method': 'pearson', 'input_variable': 'log_returns', 'tickers_analyzed': int(correlation_values.shape[1]), 'observations_analyzed': int(len(log_returns)), 'unique_pairs_available': expected_pair_count, 'correlation_statistics': correlation_statistics, 'pair_selection_statistics': pair_selection_statistics, 'calculation_errors': calculation_errors}
    return {'all_correlation_pairs': all_correlation_pairs, 'high_correlation_pairs': high_correlation_pairs, 'correlation_report': tool_report, 'current_node': 'pearson_correlation_tool', 'execution_status': 'completed'}
correlation_output = pearson_correlation_tool(state=final_state, correlation_threshold=0.75)
final_state.update(correlation_output)
final_state.setdefault('response_display_formats', {})
final_state['response_display_formats']['pearson_correlation'] = {'Correlation': 'number_4', 'correlation_threshold': 'coefficient_and_percent', 'Rank': 'integer'}

def momentum_tool(state: Dict[str, Any], formation_period_months: int=12, dollar_volume_window: int=20, display_output: bool=False) -> Dict[str, Any]:
    calculation_errors = []
    integer_parameters = {'formation_period_months': formation_period_months, 'dollar_volume_window': dollar_volume_window}
    for parameter_name, parameter_value in integer_parameters.items():
        if not isinstance(parameter_value, (int, np.integer)):
            raise TypeError(f'{parameter_name} must be an integer.')
        if parameter_value <= 0:
            raise ValueError(f'{parameter_name} must be greater than zero.')
    if formation_period_months < 2:
        raise ValueError('formation_period_months must be at least equal to 2.')
    if 'aligned_prices' not in state:
        raise KeyError('The aligned_prices variable is not present in final_state.')
    if 'aligned_volumes' not in state:
        raise KeyError('The aligned_volumes variable is not present in final_state.')
    aligned_prices = state['aligned_prices'].copy()
    aligned_volumes = state['aligned_volumes'].copy()
    if not isinstance(aligned_prices, pd.DataFrame):
        raise TypeError('aligned_prices must be a pandas DataFrame.')
    if not isinstance(aligned_volumes, pd.DataFrame):
        raise TypeError('aligned_volumes must be a pandas DataFrame.')
    if aligned_prices.empty:
        raise ValueError('aligned_prices is an empty DataFrame.')
    if aligned_volumes.empty:
        raise ValueError('aligned_volumes is an empty DataFrame.')
    if aligned_prices.shape[1] == 0:
        raise ValueError('aligned_prices does not contain any tickers.')
    if aligned_volumes.shape[1] == 0:
        raise ValueError('aligned_volumes does not contain any tickers.')
    if aligned_prices.columns.duplicated().any():
        duplicated_tickers = aligned_prices.columns[aligned_prices.columns.duplicated()].tolist()
        raise ValueError(f'aligned_prices contains duplicate tickers: {duplicated_tickers}')
    if aligned_volumes.columns.duplicated().any():
        duplicated_tickers = aligned_volumes.columns[aligned_volumes.columns.duplicated()].tolist()
        raise ValueError(f'aligned_volumes contains duplicate tickers: {duplicated_tickers}')
    if not isinstance(aligned_prices.index, pd.DatetimeIndex):
        raise TypeError('The aligned_prices index must be a DatetimeIndex.')
    if not isinstance(aligned_volumes.index, pd.DatetimeIndex):
        raise TypeError('The aligned_volumes index must be a DatetimeIndex.')
    if aligned_prices.index.has_duplicates:
        raise ValueError('aligned_prices contains duplicate dates.')
    if aligned_volumes.index.has_duplicates:
        raise ValueError('aligned_volumes contains duplicate dates.')
    if not aligned_prices.index.is_monotonic_increasing:
        aligned_prices = aligned_prices.sort_index()
    if not aligned_volumes.index.is_monotonic_increasing:
        aligned_volumes = aligned_volumes.sort_index()
    common_tickers = aligned_prices.columns.intersection(aligned_volumes.columns).tolist()
    if not common_tickers:
        raise ValueError('aligned_prices and aligned_volumes do not share any tickers.')
    missing_price_tickers = sorted(set(aligned_volumes.columns) - set(aligned_prices.columns))
    missing_volume_tickers = sorted(set(aligned_prices.columns) - set(aligned_volumes.columns))
    if missing_price_tickers or missing_volume_tickers:
        raise ValueError(f'The columns of aligned_prices and aligned_volumes do not match. Tickers present only in volumes: {missing_price_tickers}; tickers present only in prices: {missing_volume_tickers}.')
    if not aligned_prices.index.equals(aligned_volumes.index):
        raise ValueError('aligned_prices and aligned_volumes do not share the same time index.')
    aligned_prices = aligned_prices[common_tickers].apply(pd.to_numeric, errors='coerce')
    aligned_volumes = aligned_volumes[common_tickers].apply(pd.to_numeric, errors='coerce')
    if aligned_prices.isna().any().any():
        invalid_tickers = aligned_prices.columns[aligned_prices.isna().any(axis=0)].tolist()
        raise ValueError(f'aligned_prices contains missing values. Tickers involved: {invalid_tickers}')
    if aligned_volumes.isna().any().any():
        invalid_tickers = aligned_volumes.columns[aligned_volumes.isna().any(axis=0)].tolist()
        raise ValueError(f'aligned_volumes contains missing values. Tickers involved: {invalid_tickers}')
    price_values = aligned_prices.to_numpy(dtype=float)
    volume_values = aligned_volumes.to_numpy(dtype=float)
    if not np.isfinite(price_values).all():
        raise ValueError('aligned_prices contains infinite or invalid values.')
    if not np.isfinite(volume_values).all():
        raise ValueError('aligned_volumes contains infinite or invalid values.')
    if (price_values <= 0).any():
        raise ValueError('aligned_prices contains prices lower than or equal to zero.')
    if (volume_values < 0).any():
        raise ValueError('aligned_volumes contains negative volumes.')
    if len(aligned_prices) < dollar_volume_window:
        raise ValueError(f'The available observations are fewer than the requested Dollar Volume window. Available observations: {len(aligned_prices)}; required observations: {dollar_volume_window}.')
    try:
        monthly_prices = aligned_prices.resample('ME').last().dropna(how='all')
    except Exception as error:
        calculation_errors.append({'Stage': 'monthly_price_resampling', 'Error': str(error)})
        raise RuntimeError('Error while constructing monthly prices.') from error
    if len(monthly_prices) < formation_period_months + 1:
        raise ValueError(f'The available monthly prices are insufficient to calculate Momentum. Available months: {len(monthly_prices)}; minimum required months: {formation_period_months + 1}.')
    try:
        monthly_returns = monthly_prices.pct_change(fill_method=None)
        cumulative_momentum = (1 + monthly_returns).rolling(window=formation_period_months, min_periods=formation_period_months).apply(lambda values: np.prod(values) - 1, raw=True)
    except Exception as error:
        calculation_errors.append({'Stage': 'momentum_calculation', 'Error': str(error)})
        raise RuntimeError('Error while calculating Momentum.') from error
    valid_momentum_dates = cumulative_momentum.dropna(how='all').index
    if len(valid_momentum_dates) == 0:
        raise ValueError('The calculation did not produce any date with valid Momentum values.')
    measurement_date = valid_momentum_dates[-1]
    latest_momentum = cumulative_momentum.loc[measurement_date].dropna()
    if latest_momentum.empty:
        raise ValueError('No valid Momentum values are available on the latest measurement date.')
    excluded_tickers = sorted(set(common_tickers) - set(latest_momentum.index))
    if excluded_tickers:
        raise ValueError(f'Some tickers do not have sufficient observations for Momentum: {excluded_tickers}')
    try:
        daily_dollar_volume = aligned_prices * aligned_volumes
        average_dollar_volume = daily_dollar_volume.tail(dollar_volume_window).mean()
    except Exception as error:
        calculation_errors.append({'Stage': 'dollar_volume_calculation', 'Error': str(error)})
        raise RuntimeError('Error while calculating Dollar Volume.') from error
    if average_dollar_volume.isna().any():
        invalid_tickers = average_dollar_volume[average_dollar_volume.isna()].index.tolist()
        raise ValueError(f'Average Dollar Volume contains missing values. Tickers involved: {invalid_tickers}')
    if not np.isfinite(average_dollar_volume.to_numpy(dtype=float)).all():
        raise ValueError('Average Dollar Volume contains infinite or invalid values.')
    momentum_results = pd.DataFrame({'Ticker': latest_momentum.index, 'Momentum': latest_momentum.values, 'Average Dollar Volume': average_dollar_volume.reindex(latest_momentum.index).values})
    momentum_results = momentum_results.sort_values(by=['Momentum', 'Average Dollar Volume', 'Ticker'], ascending=[False, False, True]).reset_index(drop=True)
    momentum_results.insert(0, 'Rank', np.arange(1, len(momentum_results) + 1))
    expected_columns = ['Rank', 'Ticker', 'Momentum', 'Average Dollar Volume']
    if momentum_results.columns.tolist() != expected_columns:
        raise ValueError('momentum_results does not contain the expected columns.')
    if momentum_results.empty:
        raise ValueError('momentum_results is an empty DataFrame.')
    if momentum_results.isna().any().any():
        raise ValueError('momentum_results contains missing values.')
    if momentum_results['Ticker'].duplicated().any():
        duplicated_tickers = momentum_results.loc[momentum_results['Ticker'].duplicated(), 'Ticker'].tolist()
        raise ValueError(f'momentum_results contains duplicate tickers: {duplicated_tickers}')
    expected_ranks = np.arange(1, len(momentum_results) + 1)
    if not np.array_equal(momentum_results['Rank'].to_numpy(), expected_ranks):
        raise ValueError('The Rank column does not contain a correct sequential ranking.')
    if not momentum_results['Momentum'].is_monotonic_decreasing:
        raise ValueError('momentum_results is not sorted in descending order of Momentum.')
    if not np.isfinite(momentum_results[['Momentum', 'Average Dollar Volume']].to_numpy(dtype=float)).all():
        raise ValueError('momentum_results contains infinite or invalid numeric values.')
    formatted_table = momentum_results.copy()
    formatted_table['Momentum'] = formatted_table['Momentum'].map(lambda value: f'{value * 100:,.2f}%')
    formatted_table['Average Dollar Volume'] = formatted_table['Average Dollar Volume'].map(lambda value: f'$ {value:,.0f}')
    formatted_table = formatted_table.set_index('Rank')
    if display_output:
        pass
    momentum_context = {'formation_period_months': int(formation_period_months), 'time_horizon': f'{int(formation_period_months)}M', 'measurement_date': measurement_date, 'dollar_volume_window': int(dollar_volume_window)}
    return {'momentum_results': momentum_results, 'momentum_context': momentum_context}
momentum_output = momentum_tool(state=final_state, display_output=False)
final_state.update(momentum_output)
final_state.setdefault('response_display_formats', {})
final_state['response_display_formats']['momentum'] = {'Rank': 'integer', 'Momentum': 'percent_fraction_2', 'Average Dollar Volume': 'usd_0'}
BENCHMARK_TICKER = '^DJI'

def build_benchmark_log_returns(state: MarketDataState, benchmark_ticker: str=BENCHMARK_TICKER) -> pd.Series:
    if 'log_returns' not in state:
        raise KeyError('final_state does not contain log_returns.')
    log_returns = state['log_returns'].copy()
    if not isinstance(log_returns, pd.DataFrame):
        raise TypeError("final_state['log_returns'] must be a pandas DataFrame.")
    if log_returns.empty:
        raise ValueError('The log_returns matrix is empty.')
    if not isinstance(log_returns.index, pd.DatetimeIndex):
        raise TypeError('The log_returns index must be a DatetimeIndex.')
    valid_dates = log_returns.dropna(how='all').index
    if valid_dates.empty:
        raise ValueError('No valid dates are available in log_returns.')
    start_date = valid_dates.min().normalize()
    end_date = valid_dates.max().normalize()
    download_end_date = end_date + pd.Timedelta(days=1)
    benchmark_download = yf.download(tickers=benchmark_ticker, start=start_date.strftime('%Y-%m-%d'), end=download_end_date.strftime('%Y-%m-%d'), auto_adjust=False, progress=False)
    if benchmark_download.empty:
        raise ValueError(f'No data available for benchmark {benchmark_ticker}.')
    if isinstance(benchmark_download.columns, pd.MultiIndex):
        level_zero = benchmark_download.columns.get_level_values(0)
        if 'Adj Close' in level_zero:
            benchmark_prices = benchmark_download['Adj Close']
        elif 'Close' in level_zero:
            benchmark_prices = benchmark_download['Close']
        else:
            raise KeyError('The benchmark does not contain Adj Close or Close.')
        if isinstance(benchmark_prices, pd.DataFrame):
            benchmark_prices = benchmark_prices.iloc[:, 0]
    elif 'Adj Close' in benchmark_download.columns:
        benchmark_prices = benchmark_download['Adj Close']
    elif 'Close' in benchmark_download.columns:
        benchmark_prices = benchmark_download['Close']
    else:
        raise KeyError('The benchmark does not contain Adj Close or Close.')
    benchmark_prices = pd.to_numeric(benchmark_prices, errors='coerce').replace([np.inf, -np.inf], np.nan).dropna().sort_index()
    if benchmark_prices.empty:
        raise ValueError('The benchmark price series is empty.')
    benchmark_log_returns = np.log(benchmark_prices / benchmark_prices.shift(1)).replace([np.inf, -np.inf], np.nan).dropna().rename(benchmark_ticker)
    if benchmark_log_returns.empty:
        raise ValueError('benchmark_log_returns is empty.')
    return benchmark_log_returns
benchmark_log_returns = build_benchmark_log_returns(state=final_state, benchmark_ticker=BENCHMARK_TICKER)
final_state['benchmark_log_returns'] = benchmark_log_returns
RISK_FREE_RATE = 0.03
TRADING_DAYS = 252

def format_number(value, decimals=4):
    if pd.isna(value):
        return 'N/A'
    return f'{value:,.{decimals}f}'

def format_percentage(value, decimals=2):
    if pd.isna(value):
        return 'N/A'
    return f'{value * 100:,.{decimals}f}%'

def capm_tool(state: Dict[str, Any], tickers: Optional[Sequence[str]]=None, start_date: str=None, end_date: str=None, period_type: str=None, benchmark_ticker: str=BENCHMARK_TICKER, risk_free_rate: float=RISK_FREE_RATE, trading_days: int=TRADING_DAYS) -> Dict[str, Any]:
    start_time = time.perf_counter()
    calculation_errors = []
    if not isinstance(risk_free_rate, (int, float, np.integer, np.floating)):
        raise TypeError('risk_free_rate must be numeric.')
    if not np.isfinite(risk_free_rate):
        raise ValueError('risk_free_rate must be a finite value.')
    if risk_free_rate <= -1:
        raise ValueError('risk_free_rate must be greater than -1.')
    if not isinstance(trading_days, (int, np.integer)):
        raise TypeError('trading_days must be an integer.')
    if trading_days <= 1:
        raise ValueError('trading_days must be greater than 1.')
    if 'log_returns' not in state:
        raise KeyError('final_state does not contain log_returns.')
    if 'benchmark_log_returns' not in state:
        raise KeyError('final_state does not contain benchmark_log_returns. Run BOX 34 first.')
    stock_returns = state['log_returns'].copy()
    benchmark_returns = state['benchmark_log_returns'].copy()
    if not isinstance(stock_returns, pd.DataFrame):
        raise TypeError("final_state['log_returns'] must be a pandas DataFrame.")
    if stock_returns.empty:
        raise ValueError('The log_returns matrix is empty.')
    if not isinstance(stock_returns.index, pd.DatetimeIndex):
        raise TypeError('The log_returns index must be a DatetimeIndex.')
    stock_returns = stock_returns.sort_index().apply(pd.to_numeric, errors='coerce').replace([np.inf, -np.inf], np.nan)
    if isinstance(benchmark_returns, pd.DataFrame):
        if benchmark_returns.shape[1] != 1:
            raise ValueError('benchmark_log_returns must contain a single column.')
        benchmark_returns = benchmark_returns.iloc[:, 0]
    if not isinstance(benchmark_returns, pd.Series):
        raise TypeError('benchmark_log_returns must be a pandas Series.')
    if not isinstance(benchmark_returns.index, pd.DatetimeIndex):
        raise TypeError('The benchmark_log_returns index must be a DatetimeIndex.')
    benchmark_returns = pd.to_numeric(benchmark_returns, errors='coerce').replace([np.inf, -np.inf], np.nan).dropna().sort_index().rename('Market_Return')
    if tickers is None:
        selected_tickers = list(stock_returns.columns)
    else:
        selected_tickers = []
        for ticker in tickers:
            ticker_value = str(ticker).strip().upper()
            if ticker_value and ticker_value not in selected_tickers:
                selected_tickers.append(ticker_value)
        if not selected_tickers:
            raise ValueError('No valid tickers requested.')
        missing_tickers = [ticker for ticker in selected_tickers if ticker not in stock_returns.columns]
        if missing_tickers:
            raise ValueError(f'Tickers not present in log_returns: {missing_tickers}.')
    stock_returns = stock_returns.loc[:, selected_tickers].copy()
    exact_period_mode = bool(start_date or end_date)
    if exact_period_mode:
        if not (start_date and end_date):
            raise ValueError('start_date and end_date must be provided together.')
        start_ts = pd.Timestamp(start_date).normalize()
        end_ts = pd.Timestamp(end_date).normalize()
        if start_ts > end_ts:
            raise ValueError('start_date cannot be later than end_date.')
        stock_returns = stock_returns.loc[(stock_returns.index >= start_ts) & (stock_returns.index <= end_ts)].copy()
        benchmark_returns = benchmark_returns.loc[(benchmark_returns.index >= start_ts) & (benchmark_returns.index <= end_ts)].copy()
        normalized_start_date = start_ts.strftime('%Y-%m-%d')
        normalized_end_date = end_ts.strftime('%Y-%m-%d')
        normalized_period_type = period_type if period_type else 'exact_date_range'
    else:
        common_start = max(stock_returns.dropna(how='all').index.min(), benchmark_returns.index.min())
        common_end = min(stock_returns.dropna(how='all').index.max(), benchmark_returns.index.max())
        normalized_start_date = common_start.strftime('%Y-%m-%d')
        normalized_end_date = common_end.strftime('%Y-%m-%d')
        normalized_period_type = period_type if period_type else 'available_data_range'
    if stock_returns.dropna(how='all').empty:
        raise ValueError('No log returns are available within the requested interval.')
    if benchmark_returns.empty:
        raise ValueError('No benchmark returns are available within the requested interval.')
    market_mean_daily_log_return = benchmark_returns.mean()
    market_annual_return = np.exp(market_mean_daily_log_return * trading_days) - 1
    market_annual_volatility = benchmark_returns.std(ddof=1) * np.sqrt(trading_days)
    capm_records = []
    for ticker in selected_tickers:
        try:
            combined_returns = pd.concat([stock_returns[ticker].rename('Stock_Return'), benchmark_returns], axis=1, join='inner').dropna()
            if len(combined_returns) < 2:
                raise ValueError('Insufficient common observations for CAPM regression.')
            stock_series = combined_returns['Stock_Return']
            market_series = combined_returns['Market_Return']
            market_variance = market_series.var(ddof=1)
            if not np.isfinite(market_variance) or market_variance <= 0:
                raise ValueError('Benchmark variance is not valid.')
            regression_matrix = np.column_stack([np.ones(len(combined_returns)), market_series.to_numpy()])
            regression_coefficients = np.linalg.lstsq(regression_matrix, stock_series.to_numpy(), rcond=None)[0]
            alpha_daily_log = regression_coefficients[0]
            beta = regression_coefficients[1]
            predicted_returns = alpha_daily_log + beta * market_series
            residuals = stock_series - predicted_returns
            total_sum_of_squares = np.sum((stock_series - stock_series.mean()) ** 2)
            residual_sum_of_squares = np.sum(residuals ** 2)
            if total_sum_of_squares > 0:
                r_squared = 1 - residual_sum_of_squares / total_sum_of_squares
            else:
                r_squared = np.nan
            stock_annual_return = np.exp(stock_series.mean() * trading_days) - 1
            alpha_annual = np.exp(alpha_daily_log * trading_days) - 1
            expected_capm_return = risk_free_rate + beta * (market_annual_return - risk_free_rate)
            return_difference = stock_annual_return - expected_capm_return
            capm_records.append({'Ticker': str(ticker), 'Benchmark': benchmark_ticker, 'Beta': beta, 'Annual_Alpha': alpha_annual, 'R_Squared': r_squared, 'Observed_Annual_Return': stock_annual_return, 'CAPM_Annual_Return': expected_capm_return, 'Return_Difference': return_difference})
        except Exception as error:
            calculation_errors.append({'Ticker': str(ticker), 'Error': str(error)})
    capm_results = pd.DataFrame(capm_records)
    if capm_results.empty:
        raise ValueError('CAPM was not calculated for any security.')
    capm_results = capm_results.sort_values(by='Beta', ascending=False).reset_index(drop=True)
    execution_time = time.perf_counter() - start_time
    capm_metadata = {'tickers': list(capm_results['Ticker'].astype(str)), 'start_date': normalized_start_date, 'end_date': normalized_end_date, 'time_periods': [f'{normalized_start_date}/{normalized_end_date}'], 'period_type': normalized_period_type, 'benchmark_ticker': benchmark_ticker, 'risk_free_rate': float(risk_free_rate), 'trading_days': int(trading_days)}
    capm_report = {'tool': 'capm_tool', 'status': 'COMPLETED' if not calculation_errors else 'COMPLETED_WITH_WARNINGS', 'benchmark': benchmark_ticker, 'tickers_received': int(len(selected_tickers)), 'tickers_calculated': int(capm_results.shape[0]), 'tickers_with_errors': int(len(calculation_errors)), 'start_date': normalized_start_date, 'end_date': normalized_end_date, 'period_type': normalized_period_type, 'annual_risk_free_rate': float(risk_free_rate), 'annual_market_return': float(market_annual_return), 'annual_market_volatility': float(market_annual_volatility), 'execution_time_seconds': round(execution_time, 6), 'errors': calculation_errors}
    return {'capm_results': capm_results, 'capm_metadata': capm_metadata, 'capm_report': capm_report}

def _capm_atomic_tool_output(state: Dict[str, Any], metric_column: str, output_field: str, metric_name: str, **kwargs) -> Dict[str, Any]:
    base_output = capm_tool(state=state, **kwargs)
    base_results = base_output['capm_results'].copy()
    keep_columns = [column for column in ['Ticker', 'Benchmark', metric_column] if column in base_results.columns]
    atomic_results = base_results[keep_columns].copy()
    atomic_metadata = dict(base_output.get('capm_metadata', {}))
    atomic_metadata['metric'] = metric_name
    atomic_metadata['source_tool'] = output_field.replace('_results', '')
    return {output_field: atomic_results, f'{output_field}_metadata': atomic_metadata, f'{output_field}_report': base_output.get('capm_report', {})}

def capm_beta_tool(state: Dict[str, Any], tickers: Optional[Sequence[str]]=None, start_date: str=None, end_date: str=None, period_type: str=None, benchmark_ticker: str=BENCHMARK_TICKER, risk_free_rate: float=RISK_FREE_RATE, trading_days: int=TRADING_DAYS) -> Dict[str, Any]:
    return _capm_atomic_tool_output(state=state, metric_column='Beta', output_field='capm_beta_results', metric_name='capm_beta', tickers=tickers, start_date=start_date, end_date=end_date, period_type=period_type, benchmark_ticker=benchmark_ticker, risk_free_rate=risk_free_rate, trading_days=trading_days)

def capm_alpha_tool(state: Dict[str, Any], tickers: Optional[Sequence[str]]=None, start_date: str=None, end_date: str=None, period_type: str=None, benchmark_ticker: str=BENCHMARK_TICKER, risk_free_rate: float=RISK_FREE_RATE, trading_days: int=TRADING_DAYS) -> Dict[str, Any]:
    return _capm_atomic_tool_output(state=state, metric_column='Annual_Alpha', output_field='capm_alpha_results', metric_name='capm_alpha', tickers=tickers, start_date=start_date, end_date=end_date, period_type=period_type, benchmark_ticker=benchmark_ticker, risk_free_rate=risk_free_rate, trading_days=trading_days)

def capm_expected_return_tool(state: Dict[str, Any], tickers: Optional[Sequence[str]]=None, start_date: str=None, end_date: str=None, period_type: str=None, benchmark_ticker: str=BENCHMARK_TICKER, risk_free_rate: float=RISK_FREE_RATE, trading_days: int=TRADING_DAYS) -> Dict[str, Any]:
    return _capm_atomic_tool_output(state=state, metric_column='CAPM_Annual_Return', output_field='capm_expected_return_results', metric_name='capm_expected_return', tickers=tickers, start_date=start_date, end_date=end_date, period_type=period_type, benchmark_ticker=benchmark_ticker, risk_free_rate=risk_free_rate, trading_days=trading_days)
capm_output = capm_tool(state=final_state, benchmark_ticker=BENCHMARK_TICKER, risk_free_rate=RISK_FREE_RATE, trading_days=TRADING_DAYS)
capm_results = capm_output['capm_results']
capm_metadata = capm_output['capm_metadata']
capm_report = capm_output['capm_report']
final_state.update({'capm_results': capm_results, 'capm_metadata': capm_metadata, 'capm_report': capm_report})
final_state.update({'capm_beta_results': capm_results[['Ticker', 'Benchmark', 'Beta']].copy(), 'capm_alpha_results': capm_results[['Ticker', 'Benchmark', 'Annual_Alpha']].copy(), 'capm_expected_return_results': capm_results[['Ticker', 'Benchmark', 'CAPM_Annual_Return']].copy()})
final_state.setdefault('response_display_formats', {})
final_state['response_display_formats']['capm'] = {'Beta': 'number_4', 'Annual_Alpha': 'percent_fraction_2', 'R_Squared': 'number_4', 'Observed_Annual_Return': 'percent_fraction_2', 'CAPM_Annual_Return': 'percent_fraction_2', 'Return_Difference': 'percent_fraction_2'}

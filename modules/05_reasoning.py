_BaseMarketDataState = MarketDataState

class MarketDataState(_BaseMarketDataState, total=False):
    user_question: str
    question_id: str
    conversation_id: str
    conversation_turn: int
    question_analysis: Dict[str, Any]
    question_intent: str
    extracted_entities: Dict[str, Any]
    detected_ambiguities: List[Dict[str, Any]]
    interpretation_confidence: float
    sub_questions: List[Dict[str, Any]]
    required_components: List[Dict[str, Any]]
    matched_components: List[Dict[str, Any]]
    components_to_execute: List[Dict[str, Any]]
    component_evidence: List[Dict[str, Any]]
    task_dependencies: List[Dict[str, Any]]
    execution_plan: List[Dict[str, Any]]
    execution_plan_version: int
    planning_summary: Dict[str, Any]
    selected_agents: List[str]
    selected_tools: List[str]
    agent_assignments: List[Dict[str, Any]]
    tool_parameters: Dict[str, Dict[str, Any]]
    tool_execution_status: Dict[str, str]
    primary_llm_name: str
    critic_llm_name: str
    llm_role_assignment: Dict[str, str]
    llm_generation_parameters: Dict[str, Dict[str, Any]]
    llm_raw_responses: Dict[str, Any]
    llm_errors: List[Dict[str, Any]]
    llm_call_count: int
    normalized_question: str
    question_embedding: Any
    retrieved_similar_requests: List[Dict[str, Any]]
    retrieved_previous_flows: List[Dict[str, Any]]
    retrieval_context: List[Dict[str, Any]]
    retrieval_report: Dict[str, Any]
    retrieval_similarity_threshold: float
    reusable_flow_detected: bool
    reused_flow_id: Optional[str]
    benchmark_log_returns: pd.Series
    capm_results: pd.DataFrame
    capm_metadata: Dict[str, Any]
    tool_results: Dict[str, Any]
    capm_beta_results: Any
    capm_alpha_results: Any
    capm_expected_return_results: Any
    tool_results_by_key: Dict[str, Any]
    tool_result_keys_by_step: Dict[str, str]
    tool_results_by_step: Dict[str, Any]
    tool_output_history: Dict[str, Any]
    press_release_query: Dict[str, Any]
    press_release_result: Any
    press_release_catalog_index: Dict[str, Any]
    press_release_information_catalog: Dict[str, Any]
    press_release_search_catalog: Dict[str, Any]
    press_release_section_catalog: Dict[str, Any]
    press_release_semantic_kpi_families: Dict[str, Any]
    press_release_tool_contract: Dict[str, Any]
    agent_results: Dict[str, Any]
    selected_evidence: List[Dict[str, Any]]
    missing_information: List[Dict[str, Any]]
    normalized_tool_results: Dict[str, Any]
    draft_answer: str
    answer_versions: List[str]
    final_answer: str
    expected_answer_format: Dict[str, Any]
    answer_sources: List[Dict[str, Any]]
    validation_result: Dict[str, Any]
    question_answer_alignment: Dict[str, Any]
    unsupported_claims: List[Dict[str, Any]]
    missing_answer_components: List[Dict[str, Any]]
    numerical_inconsistencies: List[Dict[str, Any]]
    requires_revision: bool
    revision_count: int
    maximum_revisions: int
    answer_validation_status: str
    executed_tests: List[Dict[str, Any]]
    functional_test_results: Dict[str, Any]
    semantic_test_results: Dict[str, Any]
    decomposition_test_results: Dict[str, Any]
    routing_test_results: Dict[str, Any]
    retrieval_test_results: Dict[str, Any]
    answer_test_results: Dict[str, Any]
    overall_test_status: str
    total_execution_time_seconds: float
    agent_execution_times: Dict[str, float]
    tool_execution_times: Dict[str, float]
    llm_execution_times: Dict[str, float]
    retrieval_execution_time_seconds: float
    token_usage: Dict[str, Any]
    performance_metrics: Dict[str, Any]
    performance_history: List[Dict[str, Any]]
    agentic_execution_report: Dict[str, Any]
    current_question_node: str
    question_workflow_status: str
    next_node: str
    stop_workflow: bool
    agentic_errors: List[Dict[str, Any]]
agentic_state_defaults = {'user_question': '', 'question_id': '', 'conversation_id': '', 'conversation_turn': 0, 'question_analysis': {}, 'question_intent': '', 'extracted_entities': {}, 'detected_ambiguities': [], 'interpretation_confidence': 0.0, 'sub_questions': [], 'required_components': [], 'matched_components': [], 'components_to_execute': [], 'component_evidence': [], 'task_dependencies': [], 'execution_plan': [], 'execution_plan_version': 0, 'planning_summary': {}, 'selected_agents': [], 'selected_tools': [], 'agent_assignments': [], 'tool_parameters': {}, 'tool_execution_status': {}, 'primary_llm_name': '', 'critic_llm_name': '', 'llm_role_assignment': {}, 'llm_generation_parameters': {}, 'llm_raw_responses': {}, 'llm_errors': [], 'llm_call_count': 0, 'normalized_question': '', 'question_embedding': None, 'retrieved_similar_requests': [], 'retrieved_previous_flows': [], 'retrieval_context': [], 'retrieval_report': {}, 'retrieval_similarity_threshold': 0.75, 'reusable_flow_detected': False, 'reused_flow_id': None, 'tool_results': {}, 'tool_results_by_key': {}, 'tool_result_keys_by_step': {}, 'tool_results_by_step': {}, 'tool_output_history': {}, 'agent_results': {}, 'press_release_query': {}, 'press_release_result': {}, 'press_release_catalog_index': {}, 'press_release_information_catalog': {}, 'press_release_search_catalog': {}, 'press_release_section_catalog': {}, 'press_release_semantic_kpi_families': {}, 'press_release_tool_contract': {}, 'selected_evidence': [], 'missing_information': [], 'normalized_tool_results': {}, 'draft_answer': '', 'answer_versions': [], 'final_answer': '', 'expected_answer_format': {}, 'answer_sources': [], 'validation_result': {}, 'question_answer_alignment': {}, 'unsupported_claims': [], 'missing_answer_components': [], 'numerical_inconsistencies': [], 'requires_revision': False, 'revision_count': 0, 'maximum_revisions': 2, 'answer_validation_status': 'not_started', 'executed_tests': [], 'functional_test_results': {}, 'semantic_test_results': {}, 'decomposition_test_results': {}, 'routing_test_results': {}, 'retrieval_test_results': {}, 'answer_test_results': {}, 'overall_test_status': 'not_started', 'total_execution_time_seconds': 0.0, 'agent_execution_times': {}, 'tool_execution_times': {}, 'llm_execution_times': {}, 'retrieval_execution_time_seconds': 0.0, 'token_usage': {}, 'performance_metrics': {}, 'performance_history': [], 'agentic_execution_report': {}, 'current_question_node': '', 'question_workflow_status': 'initialized', 'next_node': '', 'stop_workflow': False, 'agentic_errors': []}
for field_name, default_value in agentic_state_defaults.items():
    final_state.setdefault(field_name, default_value)
original_state_fields = set(_BaseMarketDataState.__annotations__.keys())
extended_state_fields = set(MarketDataState.__annotations__.keys())
required_agentic_fields = {'user_question', 'question_analysis', 'sub_questions', 'required_components', 'matched_components', 'components_to_execute', 'component_evidence', 'execution_plan', 'selected_agents', 'selected_tools', 'primary_llm_name', 'critic_llm_name', 'retrieval_context', 'tool_results', 'draft_answer', 'validation_result', 'final_answer', 'performance_metrics'}
missing_type_fields = required_agentic_fields - extended_state_fields
missing_state_fields = required_agentic_fields - set(final_state.keys())
original_fields_preserved = original_state_fields.issubset(extended_state_fields)
existing_results_preserved = all((field_name in final_state for field_name in ['financial_metrics', 'all_correlation_pairs', 'high_correlation_pairs', 'momentum_results', 'capm_results']))
_PreviousMarketDataState = MarketDataState

class MarketDataState(_PreviousMarketDataState, total=False):
    current_conversation_history: List[Dict[str, Any]]
    retrieval_context: Dict[str, Any]
    resolved_slots: Dict[str, Any]
    retrieved_current_flow: List[Dict[str, Any]]
    available_results: Dict[str, Any]
    required_components: List[Dict[str, Any]]
    matched_components: List[Dict[str, Any]]
    components_to_execute: List[Dict[str, Any]]
    component_evidence: List[Dict[str, Any]]
    question_analysis_status: str
    question_analysis_error: Optional[str]
    question_analysis_execution_time_seconds: float
    question_analysis_model: str
    question_analysis_self_check: Dict[str, Any]
    planning_status: str
    planning_error: Optional[str]
    planning_execution_time_seconds: float
    planning_model: str
    planning_source: str
    execution_summary: Dict[str, Any]
    execution_trace: List[Dict[str, Any]]
    tool_execution_errors: List[Dict[str, Any]]
    tool_result_signatures: Dict[str, Any]
    tool_results_by_key: Dict[str, Any]
    tool_result_keys_by_step: Dict[str, str]
    tool_results_by_step: Dict[str, Any]
    tool_output_history: Dict[str, Any]
    evidence_normalization_summary: Dict[str, Any]
    answer_synthesis_status: str
    answer_synthesis_error: Optional[str]
    answer_synthesis_execution_time_seconds: float
    answer_synthesis_model: str
    answer_synthesis_used_evidence_ids: List[str]
    answer_synthesis_reported_missing_information: List[Any]
    answer_validation_error: Optional[str]
    answer_validation_execution_time_seconds: float
    answer_validation_model: str
    revision_instructions: List[Any]
    revision_actions: List[Any]
    revision_status: str
    revision_limit_reached: bool
    revision_execution_time_seconds: float

def build_registry_entry(name: str, function: Callable, component_type: str, description: str, required_state_fields: List[str], output_fields: List[str], uses_llm: bool=False, uses_external_source: bool=False, produced_metrics: Optional[List[str]]=None) -> Dict[str, Any]:
    """
    Creates and validates a standard registry entry.
    """
    if not callable(function):
        raise TypeError(f"The function associated with '{name}' is not executable.")
    signature = inspect.signature(function)
    return {'name': name, 'function': function, 'function_name': function.__name__, 'component_type': component_type, 'description': description, 'required_state_fields': required_state_fields, 'output_fields': output_fields, 'result_identity_dimensions': ['tool_name', 'tickers', 'time_periods', 'metric', 'result_selection'] if component_type in {'quantitative_tool', 'fundamental_tool'} else ['tool_name'], 'produced_metrics': list(produced_metrics or []), 'uses_llm': uses_llm, 'uses_external_source': uses_external_source, 'signature': str(signature), 'available': True}
AGENT_REGISTRY = {'request_interpreter': build_registry_entry(name='request_interpreter', function=request_interpreter_agent, component_type='llm_agent', description='Interprets the initial request and converts it into structured parameters.', required_state_fields=['user_request', 'tickers'], output_fields=['parsed_request', 'current_node', 'execution_status', 'errors'], uses_llm=True), 'ticker_resolution': build_registry_entry(name='ticker_resolution', function=ticker_resolution_agent, component_type='deterministic_agent', description='Normalizes and validates the requested tickers against the Dow Jones universe.', required_state_fields=['parsed_request', 'tickers'], output_fields=['tickers', 'current_node', 'execution_status', 'errors']), 'market_data_collector': build_registry_entry(name='market_data_collector', function=market_data_collector_agent, component_type='data_agent', description='Retrieves through APIs the historical time series of the selected tickers.', required_state_fields=['parsed_request', 'tickers'], output_fields=['raw_data', 'failed_tickers', 'data_source', 'current_node', 'execution_status', 'errors'], uses_external_source=True), 'data_cleaning': build_registry_entry(name='data_cleaning', function=data_cleaning_agent, component_type='deterministic_agent', description='Cleans and standardizes the collected historical time series.', required_state_fields=['raw_data', 'tickers', 'parsed_request'], output_fields=['clean_data', 'cleaning_report', 'current_node', 'execution_status', 'errors']), 'data_alignment': build_registry_entry(name='data_alignment', function=data_alignment_agent, component_type='deterministic_agent', description='Temporally aligns the historical time series of the different tickers.', required_state_fields=['clean_data', 'parsed_request'], output_fields=['aligned_prices', 'aligned_volumes', 'alignment_report', 'current_node', 'execution_status', 'errors']), 'feature_preparation': build_registry_entry(name='feature_preparation', function=feature_preparation_agent, component_type='deterministic_agent', description='Prepares prices, volumes, returns, and variables required by the quantitative tools.', required_state_fields=['aligned_prices'], output_fields=['simple_returns', 'log_returns', 'feature_report', 'current_node', 'execution_status', 'errors']), 'data_quality_validator': build_registry_entry(name='data_quality_validator', function=data_quality_validator_agent, component_type='validation_agent', description='Verifies completeness, consistency, and quality of the prepared dataset.', required_state_fields=['clean_data', 'cleaning_report', 'parsed_request'], output_fields=['validation_report', 'validation_summary', 'current_node', 'execution_status', 'errors']), 'cross_source_checker': build_registry_entry(name='cross_source_checker', function=cross_source_checker_agent, component_type='validation_agent', description='Compares the primary data with a second independent source.', required_state_fields=['clean_data'], output_fields=['cross_source_report', 'cross_source_comparison', 'cross_source_monthly_test', 'cross_source_summary', 'cross_source_reference_date', 'cross_source_blocking_failure', 'current_node', 'execution_status', 'errors'], uses_external_source=True), 'critic': build_registry_entry(name='critic', function=critic_agent, component_type='llm_critic_agent', description='Critically reviews the pipeline results and identifies anomalies or inconsistencies.', required_state_fields=['validation_report', 'cross_source_report'], output_fields=['critic_report', 'current_node', 'execution_status'], uses_llm=True), 'dataset_certification': build_registry_entry(name='dataset_certification', function=dataset_certification_agent, component_type='certification_agent', description='Produces the final dataset certification and consolidates final_state.', required_state_fields=['validation_report', 'cross_source_report', 'critic_report'], output_fields=['certification', 'current_node', 'execution_status'])}
TOOL_REGISTRY = {'financial_metrics': build_registry_entry(name='financial_metrics', function=financial_metrics_tool, component_type='quantitative_tool', description='Calculates annualized return, volatility, Return-to-Risk Ratio, and Sharpe Ratio.', required_state_fields=['log_returns'], output_fields=['financial_metrics', 'financial_metrics_report', 'current_node', 'execution_status']), 'pearson_correlation': build_registry_entry(name='pearson_correlation', function=pearson_correlation_tool, component_type='quantitative_tool', description='Calculates Pearson correlation on log returns and identifies pairs above the selected threshold.', required_state_fields=['log_returns'], output_fields=['all_correlation_pairs', 'high_correlation_pairs', 'correlation_report', 'current_node', 'execution_status']), 'momentum': build_registry_entry(name='momentum', function=momentum_tool, component_type='quantitative_tool', description='Calculates Momentum, Dollar Volume, and stock rankings.', required_state_fields=['aligned_prices', 'aligned_volumes'], output_fields=['momentum_results', 'momentum_context']), 'capm_beta': build_registry_entry(name='capm_beta', function=capm_beta_tool, component_type='quantitative_tool', description='Calculates only the CAPM Beta for the requested tickers and time interval.', required_state_fields=['log_returns', 'benchmark_log_returns'], output_fields=['capm_beta_results'], uses_external_source=False, produced_metrics=['capm_beta']), 'capm_alpha': build_registry_entry(name='capm_alpha', function=capm_alpha_tool, component_type='quantitative_tool', description='Calculates only the CAPM Alpha for the requested tickers and time interval.', required_state_fields=['log_returns', 'benchmark_log_returns'], output_fields=['capm_alpha_results'], uses_external_source=False, produced_metrics=['capm_alpha']), 'capm_expected_return': build_registry_entry(name='capm_expected_return', function=capm_expected_return_tool, component_type='quantitative_tool', description='Calculates only the expected annual return according to CAPM for the requested tickers and time interval.', required_state_fields=['log_returns', 'benchmark_log_returns'], output_fields=['capm_expected_return_results'], uses_external_source=False, produced_metrics=['capm_expected_return']), 'press_release_fy2025': build_registry_entry(name='press_release_fy2025', function=press_release_agentic_tool, component_type='fundamental_tool', description="Queries the companies' FY2025 Press Releases through KPIs, synonyms, and thematic areas.", required_state_fields=[], output_fields=['press_release_query', 'press_release_result'], uses_external_source=True)}
TOOL_REGISTRY['financial_metrics']['produced_metrics'] = ['annual_return', 'annualized_volatility', 'return_to_risk_ratio', 'sharpe_ratio']
TOOL_REGISTRY['pearson_correlation']['produced_metrics'] = ['correlation']
TOOL_REGISTRY['momentum']['produced_metrics'] = ['momentum', 'dollar_volume', 'momentum_rank']
TOOL_REGISTRY['press_release_fy2025']['produced_metrics'] = sorted([metric for metric in (globals().get('PRESS_RELEASE_SEARCH_CATALOG', {}) or final_state.get('press_release_search_catalog', {})).keys() if str(metric).strip().upper() != 'GENERAL_FUNDAMENTAL'])
TOOL_REGISTRY['financial_metrics']['optional_parameters'] = {'risk_free_rate': 0.03, 'start_date': None, 'end_date': None}
TOOL_REGISTRY['pearson_correlation']['optional_parameters'] = {'correlation_threshold': 0.75, 'start_date': None, 'end_date': None}
TOOL_REGISTRY['momentum']['optional_parameters'] = {'formation_period_months': 12, 'dollar_volume_window': 20}
for _capm_tool_name in ['capm_beta', 'capm_alpha', 'capm_expected_return']:
    TOOL_REGISTRY[_capm_tool_name]['optional_parameters'] = {'tickers': None, 'start_date': None, 'end_date': None, 'period_type': None, 'benchmark_ticker': BENCHMARK_TICKER, 'risk_free_rate': RISK_FREE_RATE, 'trading_days': TRADING_DAYS}
TOOL_REGISTRY['press_release_fy2025']['optional_parameters'] = {'company': None, 'question': None, 'force_refresh': False, 'ticker': None, 'tickers': None, 'time_period': None, 'time_periods': None, 'metric': None, 'component_id': None}
final_state['agent_registry'] = AGENT_REGISTRY
final_state['tool_registry'] = TOOL_REGISTRY
required_agents = {'request_interpreter', 'ticker_resolution', 'market_data_collector', 'data_cleaning', 'data_alignment', 'feature_preparation', 'data_quality_validator', 'cross_source_checker', 'critic', 'dataset_certification'}
required_tools = {'financial_metrics', 'pearson_correlation', 'momentum', 'capm_beta', 'capm_alpha', 'capm_expected_return', 'press_release_fy2025'}
missing_agents = required_agents - set(AGENT_REGISTRY.keys())
missing_tools = required_tools - set(TOOL_REGISTRY.keys())
invalid_agent_functions = [name for name, metadata in AGENT_REGISTRY.items() if not callable(metadata.get('function'))]
invalid_tool_functions = [name for name, metadata in TOOL_REGISTRY.items() if not callable(metadata.get('function'))]
invalid_tool_inputs = {tool_name: [field_name for field_name in metadata['required_state_fields'] if field_name not in final_state] for tool_name, metadata in TOOL_REGISTRY.items()}
ATOMIC_IDENTITY_FIELDS = ('tool_name', 'tickers', 'metric', 'time_period')
RESULT_SIGNATURE_IDENTITY_FIELDS = ('tool_name', 'tickers', 'metric', 'time_periods', 'effective_start_date', 'effective_end_date', 'result_selection', 'parameters')
MAX_OUTPUT_ROWS = None
MAX_OUTPUT_COLUMNS = None
MAX_TEXT_LENGTH = None
MAX_JSON_CHARACTERS = None
DEFAULT_DECIMALS = 6

def normalize_scalar(value: Any, decimals: int=DEFAULT_DECIMALS) -> Any:
    """
    Converts a scalar value into a format compatible
    with JSON serialization.
    """
    if value is None:
        return None
    if value is pd.NA:
        return None
    if isinstance(value, (datetime, date, pd.Timestamp)):
        return value.isoformat()
    if isinstance(value, np.datetime64):
        return pd.Timestamp(value).isoformat()
    if isinstance(value, (np.bool_, bool)):
        return bool(value)
    if isinstance(value, (np.integer,)):
        return int(value)
    if isinstance(value, (np.floating, float)):
        if pd.isna(value) or np.isinf(value):
            return None
        return round(float(value), decimals)
    if isinstance(value, (int, str)):
        return value
    return value

def truncate_text(text: Any, max_length: int=MAX_TEXT_LENGTH) -> str:
    """
    Limits the length of a text without modifying
    its initial content.
    """
    normalized_text = str(text if text is not None else '')
    if max_length is None or len(normalized_text) <= max_length:
        return normalized_text
    return normalized_text[:max_length] + '\n...[text truncated]'

def select_dataframe_content(dataframe: pd.DataFrame, tickers: Optional[Sequence[str]]=None, columns: Optional[Sequence[str]]=None, max_rows: int=MAX_OUTPUT_ROWS, max_columns: int=MAX_OUTPUT_COLUMNS, sort_by: Optional[str]=None, ascending: bool=False) -> pd.DataFrame:
    """
    Selects only the relevant rows and columns
    of a DataFrame without modifying the original object.
    """
    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError('The received object is not a DataFrame.')
    selected = dataframe.copy()
    if selected.empty:
        return selected
    if tickers:
        normalized_tickers = {str(ticker).strip().upper() for ticker in tickers}
        ticker_columns = [column for column in selected.columns if str(column).lower() in {'ticker', 'symbol', 'company_ticker'}]
        if ticker_columns:
            ticker_column = ticker_columns[0]
            selected = selected[selected[ticker_column].astype(str).str.upper().isin(normalized_tickers)]
        else:
            normalized_index = selected.index.astype(str).str.upper()
            if any((ticker in set(normalized_index) for ticker in normalized_tickers)):
                selected = selected[normalized_index.isin(normalized_tickers)]
            else:
                matching_columns = [column for column in selected.columns if str(column).upper() in normalized_tickers]
                if matching_columns:
                    selected = selected[matching_columns]
    if columns:
        available_columns = [column for column in columns if column in selected.columns]
        if available_columns:
            selected = selected[available_columns]
    if sort_by is not None and sort_by in selected.columns:
        selected = selected.sort_values(by=sort_by, ascending=ascending)
    if max_columns is not None and selected.shape[1] > max_columns:
        selected = selected.iloc[:, :max_columns]
    if max_rows is not None and selected.shape[0] > max_rows:
        selected = selected.head(max_rows)
    return selected

def dataframe_to_records(dataframe: pd.DataFrame, tickers: Optional[Sequence[str]]=None, columns: Optional[Sequence[str]]=None, max_rows: int=MAX_OUTPUT_ROWS, max_columns: int=MAX_OUTPUT_COLUMNS, sort_by: Optional[str]=None, ascending: bool=False) -> Dict[str, Any]:
    """
    Converts a DataFrame into a compact JSON structure,
    while retaining dimension information.
    """
    selected = select_dataframe_content(dataframe=dataframe, tickers=tickers, columns=columns, max_rows=max_rows, max_columns=max_columns, sort_by=sort_by, ascending=ascending)
    normalized_records = []
    for record in selected.reset_index().to_dict(orient='records'):
        normalized_records.append({str(key): normalize_for_json(value) for key, value in record.items()})
    return {'object_type': 'DataFrame', 'original_shape': [int(dataframe.shape[0]), int(dataframe.shape[1])], 'returned_shape': [int(selected.shape[0]), int(selected.shape[1])], 'truncated_rows': dataframe.shape[0] > selected.shape[0], 'truncated_columns': dataframe.shape[1] > selected.shape[1], 'records': normalized_records}

def normalize_for_json(value: Any, max_rows: int=MAX_OUTPUT_ROWS, max_columns: int=MAX_OUTPUT_COLUMNS, max_text_length: int=MAX_TEXT_LENGTH) -> Any:
    """
    Recursively converts a Python object into a
    JSON-compatible structure.
    """
    if isinstance(value, pd.DataFrame):
        return dataframe_to_records(dataframe=value, max_rows=max_rows, max_columns=max_columns)
    if isinstance(value, pd.Series):
        selected_series = value if max_rows is None else value.head(max_rows)
        return {'object_type': 'Series', 'name': str(value.name) if value.name is not None else None, 'original_length': int(len(value)), 'values': {str(index): normalize_for_json(item) for index, item in selected_series.items()}, 'truncated': False if max_rows is None else len(value) > max_rows}
    if isinstance(value, pd.Index):
        selected_index = value if max_rows is None else value[:max_rows]
        return [normalize_scalar(item) for item in selected_index]
    if isinstance(value, np.ndarray):
        limited_value = value
        if max_rows is not None or max_columns is not None:
            if value.ndim == 1:
                limited_value = value if max_rows is None else value[:max_rows]
            elif value.ndim >= 2:
                limited_value = value[:max_rows if max_rows is not None else None, :max_columns if max_columns is not None else None]
        return normalize_for_json(limited_value.tolist(), max_rows=max_rows, max_columns=max_columns, max_text_length=max_text_length)
    if isinstance(value, dict):
        return {str(key): normalize_for_json(item, max_rows=max_rows, max_columns=max_columns, max_text_length=max_text_length) for key, item in value.items()}
    if isinstance(value, (list, tuple, set)):
        selected_values = list(value) if max_rows is None else list(value)[:max_rows]
        normalized_list = [normalize_for_json(item, max_rows=max_rows, max_columns=max_columns, max_text_length=max_text_length) for item in selected_values]
        if max_rows is not None and len(value) > max_rows:
            normalized_list.append({'_truncated_items': len(value) - max_rows})
        return normalized_list
    if isinstance(value, str):
        return truncate_text(value, max_length=max_text_length)
    normalized_scalar = normalize_scalar(value)
    if normalized_scalar is value:
        return truncate_text(repr(value), max_length=max_text_length)
    return normalized_scalar

def serialize_to_json(value: Any, indent: Optional[int]=2, max_characters: int=MAX_JSON_CHARACTERS) -> str:
    """
    Normalizes and serializes an object into JSON,
    applying a maximum limit to the final length.
    """
    normalized_value = normalize_for_json(value)
    serialized_value = json.dumps(normalized_value, ensure_ascii=False, indent=indent, allow_nan=False)
    if max_characters is None or len(serialized_value) <= max_characters:
        return serialized_value
    return serialized_value[:max_characters] + '\n"...[JSON output truncated]"'

def is_json_serializable(value: Any) -> bool:
    """
    Checks whether an object can be normalized and
    correctly serialized into JSON.
    """
    try:
        json.dumps(normalize_for_json(value), ensure_ascii=False, allow_nan=False)
        return True
    except (TypeError, ValueError, OverflowError):
        return False

def get_available_state_outputs(state: Dict[str, Any], exclude_empty: bool=True) -> Dict[str, Dict[str, Any]]:
    """
    Returns a concise catalog of the outputs available
    in the state, without copying their full content.
    """
    available_outputs = {}
    for field_name, value in state.items():
        is_empty = False
        if value is None:
            is_empty = True
        elif isinstance(value, (str, list, tuple, set, dict, pd.DataFrame, pd.Series)):
            is_empty = len(value) == 0
        if exclude_empty and is_empty:
            continue
        output_metadata = {'type': type(value).__name__, 'json_serializable': is_json_serializable(value)}
        if isinstance(value, pd.DataFrame):
            output_metadata.update({'rows': int(value.shape[0]), 'columns': int(value.shape[1]), 'column_names': [str(column) for column in value.columns[:MAX_OUTPUT_COLUMNS]]})
        elif isinstance(value, pd.Series):
            output_metadata['length'] = int(len(value))
        elif hasattr(value, '__len__'):
            try:
                output_metadata['length'] = int(len(value))
            except TypeError:
                pass
        available_outputs[field_name] = output_metadata
    return available_outputs

def select_state_outputs(state: Dict[str, Any], field_names: Sequence[str], tickers: Optional[Sequence[str]]=None, columns_by_field: Optional[Dict[str, Sequence[str]]]=None, max_rows: int=MAX_OUTPUT_ROWS) -> Dict[str, Any]:
    """
    Retrieves and normalizes only the outputs requested
    by the agentic workflow.
    """
    selected_outputs = {}
    missing_fields = []
    columns_by_field = columns_by_field if columns_by_field is not None else {}
    for field_name in field_names:
        if field_name not in state:
            missing_fields.append(field_name)
            continue
        value = state[field_name]
        if isinstance(value, pd.DataFrame):
            selected_outputs[field_name] = dataframe_to_records(dataframe=value, tickers=tickers, columns=columns_by_field.get(field_name), max_rows=max_rows)
        else:
            selected_outputs[field_name] = normalize_for_json(value, max_rows=max_rows)
    return {'selected_outputs': selected_outputs, 'missing_fields': missing_fields, 'requested_fields': list(field_names)}

def build_compact_evidence_package(state: Dict[str, Any], field_names: Sequence[str], tickers: Optional[Sequence[str]]=None, columns_by_field: Optional[Dict[str, Sequence[str]]]=None, max_rows: int=MAX_OUTPUT_ROWS, max_characters: int=MAX_JSON_CHARACTERS) -> Dict[str, Any]:
    """
    Builds the compact evidence package to be provided
    to the LLM agents.
    """
    selection_result = select_state_outputs(state=state, field_names=field_names, tickers=tickers, columns_by_field=columns_by_field, max_rows=max_rows)
    evidence_package = {'requested_fields': selection_result['requested_fields'], 'missing_fields': selection_result['missing_fields'], 'evidence': selection_result['selected_outputs']}
    evidence_json = serialize_to_json(evidence_package, indent=2, max_characters=max_characters)
    return {'package': evidence_package, 'json': evidence_json, 'character_count': len(evidence_json), 'within_size_limit': True if max_characters is None else len(evidence_json) <= max_characters}

def _format_english_number(value: Any, decimals: int) -> str:
    numeric_value = float(value)
    return f'{numeric_value:,.{decimals}f}'

def _get_response_display_rule(field_name: str) -> Optional[str]:
    display_formats = final_state.get('response_display_formats', {})
    for tool_formats in display_formats.values():
        if not isinstance(tool_formats, dict):
            continue
        if field_name in tool_formats:
            return tool_formats[field_name]
    return None

def format_financial_response_value(value: Any, field_name: Optional[str]=None) -> Any:
    """
    Applies only the presentation format defined
    for the metric, without modifying the computational value.
    """
    if value is None:
        return None
    if field_name is None:
        return value
    rule = _get_response_display_rule(str(field_name))
    if rule is None:
        return value
    if isinstance(value, (bool, np.bool_)):
        return bool(value)
    if not isinstance(value, (int, float, np.integer, np.floating)):
        return value
    if pd.isna(value):
        return 'N/A'
    if rule == 'number_2':
        return _format_english_number(value, 2)
    if rule == 'number_4':
        return _format_english_number(value, 4)
    if rule == 'percent_points_2':
        return _format_english_number(value, 2) + '%'
    if rule == 'percent_fraction_2':
        return _format_english_number(float(value) * 100.0, 2) + '%'
    if rule == 'usd_2':
        return '$ ' + _format_english_number(value, 2)
    if rule == 'usd_0':
        return '$ ' + _format_english_number(value, 0)
    if rule == 'integer':
        return f'{int(round(float(value))):,}'
    if rule == 'coefficient_and_percent':
        coefficient = _format_english_number(value, 2)
        percentage = _format_english_number(float(value) * 100.0, 0)
        return f'{coefficient} ({percentage}%)'
    return value

def format_financial_response_structure(value: Any, field_name: Optional[str]=None) -> Any:
    """
    Recursively formats only the representation intended
    for the response, preserving the evidence structure.
    """
    if isinstance(value, dict):
        return {str(key): format_financial_response_structure(item, field_name=str(key)) for key, item in value.items()}
    if isinstance(value, list):
        return [format_financial_response_structure(item, field_name=field_name) for item in value]
    if isinstance(value, tuple):
        return [format_financial_response_structure(item, field_name=field_name) for item in value]
    return format_financial_response_value(value, field_name=field_name)
OUTPUT_UTILITY_REGISTRY = {'normalize_scalar': normalize_scalar, 'truncate_text': truncate_text, 'select_dataframe_content': select_dataframe_content, 'dataframe_to_records': dataframe_to_records, 'normalize_for_json': normalize_for_json, 'serialize_to_json': serialize_to_json, 'is_json_serializable': is_json_serializable, 'get_available_state_outputs': get_available_state_outputs, 'select_state_outputs': select_state_outputs, 'build_compact_evidence_package': build_compact_evidence_package, 'format_financial_response_value': format_financial_response_value, 'format_financial_response_structure': format_financial_response_structure}
available_state_outputs = get_available_state_outputs(final_state)
final_state['output_utility_registry'] = {utility_name: utility_function.__name__ for utility_name, utility_function in OUTPUT_UTILITY_REGISTRY.items()}
final_state['available_results'] = available_state_outputs
final_state['output_normalization_config'] = {'max_output_rows': MAX_OUTPUT_ROWS, 'max_output_columns': MAX_OUTPUT_COLUMNS, 'max_text_length': MAX_TEXT_LENGTH, 'max_json_characters': MAX_JSON_CHARACTERS, 'default_decimals': DEFAULT_DECIMALS}
required_utilities = {'normalize_scalar', 'truncate_text', 'select_dataframe_content', 'dataframe_to_records', 'normalize_for_json', 'serialize_to_json', 'is_json_serializable', 'get_available_state_outputs', 'select_state_outputs', 'build_compact_evidence_package', 'format_financial_response_value', 'format_financial_response_structure'}
missing_utilities = required_utilities - set(OUTPUT_UTILITY_REGISTRY.keys())

def canonical_identity_text(value: Any) -> str:
    return re.sub('[^a-z0-9]+', '_', str(value or '').strip().lower()).strip('_')

def canonical_time_period(value: Any) -> str:
    if value is None:
        return ''
    if isinstance(value, dict):
        ptype = str(value.get('period_type', value.get('type', '')) or '').lower()
        raw = value.get('time_value', value.get('value'))
        unit = str(value.get('time_unit', value.get('unit', '')) or '').upper()
        if ptype == 'rolling' and raw is not None:
            if isinstance(raw, str) and re.fullmatch('\\d+(?:M|Y|W|D)', raw.upper()):
                return raw.upper()
            umap = {'MONTH': 'M', 'MONTHS': 'M', 'MESE': 'M', 'MESI': 'M', 'YEAR': 'Y', 'YEARS': 'Y', 'ANNO': 'Y', 'ANNI': 'Y', 'WEEK': 'W', 'WEEKS': 'W', 'DAY': 'D', 'DAYS': 'D'}
            u = umap.get(unit, unit)
            if u in {'M', 'Y', 'W', 'D'}:
                return f'{raw}{u}'.upper()
        return json.dumps(value, ensure_ascii=False, sort_keys=True, default=str)
    text = str(value).strip().upper().replace(' ', '')
    aliases = {'24M': '2Y', '1Y': '12M', '0.5Y': '6M'}
    return aliases.get(text, text)

def canonical_metric_name(value: Any) -> str:
    key = canonical_identity_text(value)
    aliases = {'annual_return': 'annualized_return', 'annualized_return': 'annualized_return', 'annualized_volatility': 'annualized_volatility', 'volatility': 'annualized_volatility', 'sharpe': 'sharpe_ratio', 'sharpe_ratio': 'sharpe_ratio', 'beta': 'capm_beta', 'capm_beta': 'capm_beta'}
    return aliases.get(key, key)

def build_atomic_id(tool_name: Any, tickers: Any, metric: Any, time_period: Any) -> str:
    ts = sorted({str(x).strip().upper() for x in tickers or [] if str(x).strip()})
    payload = {'tool_name': str(tool_name or '').strip(), 'tickers': ts, 'metric': canonical_metric_name(metric), 'time_period': canonical_time_period(time_period)}
    return 'ATOM::' + hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(',', ':'), default=str).encode()).hexdigest()[:24]

def canonicalize_result_parameters(parameters: Any) -> Dict[str, Any]:
    p = copy.deepcopy(parameters) if isinstance(parameters, dict) else {}
    p.pop('period_type', None)
    return {str(k): p[k] for k in sorted(p) if p[k] is not None}

def build_canonical_result_signature(tool_name: Any, tickers: Any, time_periods: Any, metric: Any='', result_selection: Any=None, parameters: Any=None, effective_start_date: Any=None, effective_end_date: Any=None) -> Dict[str, Any]:
    periods = sorted({canonical_time_period(x) for x in time_periods or [] if canonical_time_period(x)})
    ts = sorted({str(x).strip().upper() for x in tickers or [] if str(x).strip()})
    sel = result_selection if isinstance(result_selection, dict) else {'type': 'all', 'size': None}
    p = canonicalize_result_parameters(parameters)
    start = effective_start_date or p.get('start_date')
    end = effective_end_date or p.get('end_date')
    return {'tool_name': str(tool_name or '').strip(), 'tickers': ts, 'metric': canonical_metric_name(metric), 'time_periods': periods, 'effective_start_date': str(start) if start else None, 'effective_end_date': str(end) if end else None, 'result_selection': {'type': sel.get('type', 'all'), 'size': sel.get('size')}, 'parameters': p}

def canonical_result_signature_id(signature: Dict[str, Any]) -> str:
    canonical = build_canonical_result_signature(**{k: signature.get(k) for k in ['tool_name', 'tickers', 'time_periods', 'metric', 'result_selection', 'parameters', 'effective_start_date', 'effective_end_date']})
    return 'SIG::' + hashlib.sha256(json.dumps(canonical, sort_keys=True, separators=(',', ':'), default=str).encode()).hexdigest()[:32]

def canonical_result_signatures_match(a: Dict[str, Any], b: Dict[str, Any]) -> bool:
    ca = build_canonical_result_signature(**{k: a.get(k) for k in ['tool_name', 'tickers', 'time_periods', 'metric', 'result_selection', 'parameters', 'effective_start_date', 'effective_end_date']})
    cb = build_canonical_result_signature(**{k: b.get(k) for k in ['tool_name', 'tickers', 'time_periods', 'metric', 'result_selection', 'parameters', 'effective_start_date', 'effective_end_date']})
    if ca['tool_name'] != cb['tool_name'] or ca['metric'] != cb['metric'] or ca['time_periods'] != cb['time_periods']:
        return False
    if ca['tickers'] and cb['tickers'] and (not set(ca['tickers']).issubset(set(cb['tickers']))) and (not set(cb['tickers']).issubset(set(ca['tickers']))):
        return False
    if ca['effective_start_date'] and cb['effective_start_date'] and (ca['effective_start_date'] != cb['effective_start_date']):
        return False
    if ca['effective_end_date'] and cb['effective_end_date'] and (ca['effective_end_date'] != cb['effective_end_date']):
        return False
    return ca['result_selection'] == cb['result_selection'] and ca['parameters'] == cb['parameters']

def build_requirement_id(ticker: Any, metric: Any, time_period: Any) -> str:
    payload = {'ticker': str(ticker or '').strip().upper(), 'metric': canonical_metric_name(metric), 'time_period': canonical_time_period(time_period)}
    canonical = json.dumps(payload, sort_keys=True, separators=(',', ':'), default=str)
    return 'REQ::' + hashlib.sha256(canonical.encode('utf-8')).hexdigest()[:24]

def build_requirement_atom(ticker: Any, metric: Any, time_period: Any, component_id: Any=None) -> Dict[str, Any]:
    ticker_value = str(ticker or '').strip().upper()
    metric_value = canonical_metric_name(metric)
    period_value = canonical_time_period(time_period)
    return {'requirement_id': build_requirement_id(ticker_value, metric_value, period_value), 'ticker': ticker_value or None, 'metric': metric_value, 'time_period': period_value or None, 'component_id': component_id}

def reusable_signature_covers_request(requested, stored):
    """A stored calculation must cover the requested ticker set, not vice versa."""
    if not isinstance(requested, dict) or not isinstance(stored, dict):
        return False
    if not canonical_result_signatures_match(requested, stored):
        return False
    req = build_canonical_result_signature(**{k: requested.get(k) for k in ['tool_name', 'tickers', 'time_periods', 'metric', 'result_selection', 'parameters', 'effective_start_date', 'effective_end_date']})
    got = build_canonical_result_signature(**{k: stored.get(k) for k in ['tool_name', 'tickers', 'time_periods', 'metric', 'result_selection', 'parameters', 'effective_start_date', 'effective_end_date']})
    return not req['tickers'] or bool(got['tickers'] and set(req['tickers']).issubset(got['tickers']))
MAX_CONVERSATION_TURNS = 20
MAX_RETRIEVED_TURNS = 5
FOLLOW_UP_EXPRESSIONS = {'and among these', 'and among these', 'among these', 'among these', 'of these', 'of these', 'which of them', 'among these', 'among these', 'the same', 'the same', 'these stocks', 'these companies', 'these results', 'instead', 'also', 'then', 'now compare them', 'compare them', 'rank them', 'show them'}
CONTEXTUAL_PRONOUNS = {'these', 'these', 'those', 'those', 'that', 'that', 'those', 'those', 'them', 'they', 'they', 'them', 'them', 'both', 'all', 'same', 'same'}
FINANCIAL_CONCEPT_ALIASES = {'risk': {'risk', 'risky', 'risky', 'volatility', 'volatile', 'stability'}, 'return': {'return', 'returns', 'performance', 'performance', 'growth'}, 'momentum': {'momentum', 'strength', 'annual performance', '12m'}, 'correlation': {'correlation', 'correlated', 'correlated', 'relationship'}, 'volume': {'volume', 'volumes', 'liquidity', 'dollar volume'}, 'capm': {'capm', 'beta', 'alpha', 'market sensitivity', 'r-squared', 'r2'}, 'fundamental': {'fundamentals', 'company results', 'earnings', 'revenue', 'margins', 'guidance', 'press release', 'fy2025 results'}}
FINANCIAL_METRIC_ALIASES = {'annualized_volatility': {'annualized volatility', 'annualized volatility', 'volatility', 'volatility'}, 'annual_return': {'annual return', 'annual return', 'return', 'returns', 'performance'}, 'return_to_risk_ratio': {'return-to-risk', 'return to risk', 'return-to-risk ratio', 'return to risk ratio'}, 'sharpe_ratio': {'sharpe ratio', 'sharpe'}, 'correlation': {'correlation', 'correlation'}, 'momentum': {'momentum', 'momentum'}, 'capm_beta': {'beta capm', 'beta'}, 'capm_alpha': {'alpha capm', 'alpha'}, 'capm_expected_return': {'capm return', 'capm expected return', 'annual capm return', 'expected return capm', 'capm expected return'}}

def normalize_retrieval_text(text: Any) -> str:
    """
    Normalizes text for comparison within
    the same conversational flow.
    """
    normalized = str(text if text is not None else '').lower()
    normalized = re.sub('[^\\w\\s%-]', ' ', normalized)
    normalized = re.sub('\\s+', ' ', normalized).strip()
    return normalized

def tokenize_retrieval_text(text: Any) -> Set[str]:
    """
    Extracts meaningful terms from the normalized text.
    """
    normalized = normalize_retrieval_text(text)
    stopwords = {'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'how', 'in', 'into', 'is', 'it', 'of', 'on', 'or', 'that', 'the', 'their', 'them', 'these', 'this', 'those', 'to', 'what', 'which', 'who', 'with'}
    return {token for token in normalized.split() if token not in stopwords and len(token) > 1}

def extract_retrieval_concepts(text: Any) -> List[str]:
    """
    Identifies the financial concepts present in the question.
    """
    normalized_text = normalize_retrieval_text(text)
    detected_concepts = []
    for concept, aliases in FINANCIAL_CONCEPT_ALIASES.items():
        if any((alias in normalized_text for alias in aliases)):
            detected_concepts.append(concept)
    return detected_concepts

def extract_retrieval_metrics(text: Any) -> List[str]:
    """Extracts all explicit financial metrics from the question."""
    normalized_text = normalize_retrieval_text(text)
    matches = []
    for metric, aliases in FINANCIAL_METRIC_ALIASES.items():
        best_alias_length = 0
        for alias in aliases:
            normalized_alias = normalize_retrieval_text(alias)
            if normalized_alias and normalized_alias in normalized_text:
                best_alias_length = max(best_alias_length, len(normalized_alias))
        if best_alias_length:
            matches.append((best_alias_length, metric))
    matches.sort(key=lambda item: (-item[0], item[1]))
    return [metric for _, metric in matches]

def extract_retrieval_metric(text: Any) -> Optional[str]:
    """Compatibility: returns the first metric, if present."""
    metrics = extract_retrieval_metrics(text)
    return metrics[0] if metrics else None

def extract_retrieval_time_period(text: Any) -> Optional[Dict[str, Any]]:
    """
    Extracts the explicit time constraint without converting it into dates.
    The final start_date/end_date conversion remains the responsibility
    of the box dedicated to time resolution.
    """
    normalized = normalize_retrieval_text(text)
    relative_match = re.search('\\b(?:last|past|previous)\\s+(\\d+)\\s+(day|days|week|weeks|month|months|year|years)\\b', normalized)
    if relative_match:
        value = int(relative_match.group(1))
        unit_raw = relative_match.group(2)
        if unit_raw.startswith('day'):
            unit = 'days'
        elif unit_raw.startswith('week'):
            unit = 'weeks'
        elif unit_raw.startswith('month'):
            unit = 'months'
        else:
            unit = 'years'
        return {'type': 'rolling', 'value': value, 'unit': unit, 'label': relative_match.group(0)}
    if re.search('\\blast\\s+year\\b', normalized):
        return {'type': 'rolling', 'value': 1, 'unit': 'years', 'label': 'last year'}
    if re.search('\\blast\\s+12\\s+months\\b|\\btwelve\\s+months\\b', normalized):
        return {'type': 'rolling', 'value': 12, 'unit': 'months', 'label': 'last 12 months'}
    year_match = re.search('\\b((?:19|20)\\d{2})\\b', normalized)
    if year_match:
        return {'type': 'calendar_year', 'value': int(year_match.group(1)), 'unit': 'year', 'label': year_match.group(1)}
    return None

def extract_question_tickers(text: Any, known_tickers: Optional[Sequence[str]]=None) -> List[str]:
    """Extracts explicit tickers from the question even when written in lowercase."""
    known = {str(t).upper() for t in known_tickers or []}
    tokens = re.findall('\\b[A-Za-z]{1,5}\\b', str(text or ''))
    detected = {token.upper() for token in tokens if token.upper() in known}
    return sorted(detected)

def extract_question_company_tickers(text: Any, known_tickers: Optional[Sequence[str]]=None) -> List[str]:
    """Extracts explicitly named companies using COMPANY_ALIASES already defined in the project."""
    known = {str(t).upper() for t in known_tickers or []}
    normalized_text = normalize_text(text) if 'normalize_text' in globals() else str(text or '').lower()
    aliases = globals().get('COMPANY_ALIASES', {}) or {}
    detected = set()
    for alias, ticker in sorted(aliases.items(), key=lambda item: len(str(item[0])), reverse=True):
        ticker = str(ticker).upper()
        if known and ticker not in known:
            continue
        normalized_alias = str(alias).strip().lower()
        if not normalized_alias:
            continue
        if re.search(f'(?<![a-z0-9]){re.escape(normalized_alias)}(?![a-z0-9])', normalized_text):
            detected.add(ticker)
    return sorted(detected)
GLOBAL_TICKER_SCOPE_PATTERNS = ['^\\s*which\\s+(?:stock|company|share|component)\\b', '^\\s*which\\s+are\\s+(?:the\\s+)?(?:stocks|companies|shares|components)\\b', '^\\s*what\\s+is\\s+the\\s+(?:stock|company|share|component)\\b', '^\\s*what\\s+is\\s+the\\s+most\\b', '^\\s*which\\s+has\\s+the\\s+highest\\s+value\\b', '\\b(?:stock|stocks|company|companies|share|shares|component|components)\\b.*\\b(?:dow jones|djia|dow)\\b', '\\b(?:dow jones|djia|dow)\\b.*\\b(?:stock|stocks|company|companies|share|shares|component|components)\\b', '\\bamong\\s+all\\b', '\\ball\\s+(?:the\\s+)?(?:stocks|companies|shares|components)\\b', '\\bentire\\s+(?:dow jones|djia|dow|index|universe)\\b', '\\b(?:ranking|rank|top|bottom)\\b.*\\b(?:stocks|companies|shares|components|dow jones|djia|dow)\\b']

def is_global_ticker_scope(question: Any, explicit_current_tickers: Optional[Sequence[str]]=None) -> bool:
    """
    Recognizes a request for the entire universe only when the current
    question does NOT explicitly restrict a subset of tickers/companies.
    """
    if explicit_current_tickers:
        return False
    normalized = normalize_text(question) if 'normalize_text' in globals() else str(question or '').lower()
    return any((re.search(pattern, normalized, flags=re.IGNORECASE) for pattern in GLOBAL_TICKER_SCOPE_PATTERNS))

def extract_question_slots(question: Any, known_tickers: Optional[Sequence[str]]=None) -> Dict[str, Any]:
    """Extracts the three main slots explicitly present in the question."""
    return {'ticker': sorted(set(extract_question_tickers(question, known_tickers) + extract_question_company_tickers(question, known_tickers))), 'metric': extract_retrieval_metric(question), 'metrics': extract_retrieval_metrics(question), 'concepts': extract_retrieval_concepts(question), 'time_period': extract_retrieval_time_period(question)}

def extract_turn_effective_time_period(turn: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """
    Retrieves the effective period preserved in the turn plan.

    Priority:
    1. step execution_scope;
    2. step time_periods;
    3. step tool_parameters.

    The function is used only as a fallback when the current question
    does not already contain an explicit time period.
    """
    if not isinstance(turn, dict):
        return None
    execution_plan = turn.get('execution_plan', [])
    if not isinstance(execution_plan, list):
        return None
    for step in execution_plan:
        if not isinstance(step, dict):
            continue
        execution_scope = step.get('execution_scope', {})
        if not isinstance(execution_scope, dict):
            execution_scope = {}
        start_date = execution_scope.get('start_date')
        end_date = execution_scope.get('end_date')
        if start_date and end_date:
            return {'type': 'exact_date_range', 'value': f'{start_date}/{end_date}', 'unit': 'date_range', 'label': f'{start_date}/{end_date}'}
        candidate_periods = []
        candidate_periods.extend(execution_scope.get('time_periods', []) or [])
        candidate_periods.extend(step.get('time_periods', []) or [])
        tool_parameters = step.get('tool_parameters', {})
        if isinstance(tool_parameters, dict):
            candidate_periods.extend(tool_parameters.get('time_periods', []) or [])
            formation_period_months = tool_parameters.get('formation_period_months')
            if formation_period_months is not None and (not candidate_periods):
                try:
                    months = int(formation_period_months)
                except (TypeError, ValueError):
                    months = None
                if months and months > 0:
                    return {'type': 'rolling', 'value': months, 'unit': 'months', 'label': f'{months} months'}
        for candidate in candidate_periods:
            if candidate is None:
                continue
            if isinstance(candidate, dict):
                candidate_type = str(candidate.get('type', '')).strip().lower()
                if candidate_type in {'rolling', 'calendar_year', 'full_available_dataset'}:
                    return copy.deepcopy(candidate)
                continue
            candidate_text = str(candidate).strip()
            if not candidate_text:
                continue
            parsed_candidate = extract_retrieval_time_period(candidate_text)
            if parsed_candidate is not None:
                return parsed_candidate
            exact_match = re.fullmatch('\\s*(\\d{4}-\\d{2}-\\d{2})\\s*/\\s*(\\d{4}-\\d{2}-\\d{2})\\s*', candidate_text)
            if exact_match:
                return {'type': 'exact_date_range', 'value': f'{exact_match.group(1)}/{exact_match.group(2)}', 'unit': 'date_range', 'label': candidate_text}
            rolling_match = re.fullmatch('\\s*(\\d+)\\s+(days|day|weeks|week|months|month|years|year)\\s*', candidate_text.lower())
            if rolling_match:
                value = int(rolling_match.group(1))
                unit_text = rolling_match.group(2)
                if unit_text.startswith('day'):
                    unit = 'days'
                elif unit_text.startswith('week'):
                    unit = 'weeks'
                elif unit_text.startswith('month'):
                    unit = 'months'
                else:
                    unit = 'years'
                return {'type': 'rolling', 'value': value, 'unit': unit, 'label': candidate_text}
    return None

def resolve_conversational_slots(question: str, conversation_history: Sequence[Dict[str, Any]], known_tickers: Optional[Sequence[str]]=None) -> Dict[str, Any]:
    """
    Resolves TICKER, METRIC, and PERIOD with priority given to the current question.
    For each slot, it first exhausts the information and references present
    in the current question; only slots that remain genuinely unresolved
    may be searched backward through the conversation, from the previous turn
    toward more distant ones. Anaphoric references that cannot be resolved
    deterministically in this box remain empty and are delegated to the semantic
    analysis of BOX 40 before any inheritance from the current flow.
    """
    current = extract_question_slots(question, known_tickers)
    correlation_question = 'correlation' in current.get('concepts', []) or current.get('metric') == 'correlation'
    scope_question = re.sub('\\b(?:dow\\s+jones(?:\\s+industrial\\s+average)?|djia)\\b', ' ', str(question or ''), flags=re.IGNORECASE)
    explicit_scope_tickers = sorted(set(extract_question_tickers(scope_question, known_tickers) + extract_question_company_tickers(scope_question, known_tickers)))
    global_ticker_scope = is_global_ticker_scope(question=question, explicit_current_tickers=explicit_scope_tickers)
    if global_ticker_scope:
        current['ticker'] = sorted({str(ticker).upper() for ticker in known_tickers or [] if str(ticker).strip()})
    resolved = {'ticker': {'value': list(current['ticker']), 'source': 'current_question_global_universe' if global_ticker_scope else 'current_question' if current['ticker'] else None, 'turn_number': None}, 'metric': {'value': current['metric'], 'source': 'current_question' if current['metric'] else None, 'turn_number': None}, 'concepts': {'value': list(current['concepts']), 'source': 'current_question' if current['concepts'] else None, 'turn_number': None}, 'time_period': {'value': copy.deepcopy(current['time_period']), 'source': 'current_question' if current['time_period'] else None, 'turn_number': None}}
    has_at_least_one_current_slot = bool(current['ticker'] or current['metric'] or current['concepts'] or current['time_period'])
    same_period_reference = bool(re.search('\\b(?:in|over|during)\\s+the\\s+same\\s+period\\b|\\bsame\\s+period\\b', normalize_retrieval_text(question)))
    ordered_history = sorted(list(conversation_history), key=lambda turn: int((turn or {}).get('turn_number', 0) or 0), reverse=True)
    if has_at_least_one_current_slot:
        for turn in ordered_history:
            previous_question = turn.get('question', '')
            previous_slots = extract_question_slots(previous_question, known_tickers)
            previous_effective_time_period = extract_turn_effective_time_period(turn)
            previous_time_period = previous_effective_time_period if previous_effective_time_period is not None else previous_slots['time_period']
            turn_number = turn.get('turn_number')
            if not resolved['ticker']['value']:
                candidate = list(turn.get('selected_tickers', []) or previous_slots['ticker'])
                candidate = [str(t).upper() for t in candidate if str(t).upper() in set(known_tickers or candidate)]
                if candidate:
                    resolved['ticker'] = {'value': sorted(set(candidate)), 'source': 'conversation_history', 'turn_number': turn_number}
            if resolved['metric']['value'] is None and previous_slots['metric'] is not None:
                resolved['metric'] = {'value': previous_slots['metric'], 'source': 'conversation_history', 'turn_number': turn_number}
            if not resolved['concepts']['value']:
                candidate_concepts = list(turn.get('concepts', []) or previous_slots['concepts'])
                if candidate_concepts:
                    resolved['concepts'] = {'value': candidate_concepts, 'source': 'conversation_history', 'turn_number': turn_number}
            if not correlation_question and resolved['time_period']['value'] is None and (previous_time_period is not None):
                resolved['time_period'] = {'value': copy.deepcopy(previous_time_period), 'source': 'conversation_history_execution_scope' if previous_effective_time_period is not None else 'conversation_history', 'turn_number': turn_number}
            if resolved['ticker']['value'] and resolved['metric']['value'] is not None and (resolved['time_period']['value'] is not None):
                break
    if correlation_question and (not same_period_reference) and (current['time_period'] is None):
        resolved['time_period'] = {'value': {'type': 'full_available_dataset', 'value': None, 'unit': None, 'label': 'full available dataset'}, 'source': 'correlation_default_full_dataset', 'turn_number': None}
    resolved['has_current_slot'] = has_at_least_one_current_slot
    resolved['inherited_any'] = any((str(resolved[name].get('source', '') or '').startswith('conversation_history') for name in ('ticker', 'metric', 'concepts', 'time_period')))
    return resolved

def extract_tickers_from_context(value: Any, known_tickers: Optional[Sequence[str]]=None) -> List[str]:
    """
    Retrieves tickers present in texts, lists, dictionaries,
    or structures produced by previous boxes.
    """
    detected_tickers = set()
    normalized_known_tickers = {str(ticker).upper() for ticker in known_tickers or []}

    def inspect_value(current_value: Any) -> None:
        if current_value is None:
            return
        if isinstance(current_value, str):
            uppercase_tokens = re.findall('\\b[A-Z]{1,5}\\b', current_value)
            for token in uppercase_tokens:
                if not normalized_known_tickers or token in normalized_known_tickers:
                    detected_tickers.add(token)
            return
        if isinstance(current_value, dict):
            for key, item in current_value.items():
                inspect_value(key)
                inspect_value(item)
            return
        if isinstance(current_value, (list, tuple, set, pd.Index)):
            for item in current_value:
                inspect_value(item)
            return
        if isinstance(current_value, pd.DataFrame):
            ticker_columns = [column for column in current_value.columns if str(column).lower() in {'ticker', 'symbol', 'company_ticker'}]
            for column in ticker_columns:
                detected_tickers.update(current_value[column].dropna().astype(str).str.upper().tolist())
            index_values = current_value.index.astype(str).str.upper().tolist()
            for index_value in index_values:
                if not normalized_known_tickers or index_value in normalized_known_tickers:
                    detected_tickers.add(index_value)
    inspect_value(value)
    if normalized_known_tickers:
        detected_tickers = {ticker for ticker in detected_tickers if ticker in normalized_known_tickers}
    return sorted(detected_tickers)

def detect_follow_up_question(question: str, conversation_history: Sequence[Dict[str, Any]], known_tickers: Optional[Sequence[str]]=None) -> Dict[str, Any]:
    """
    Checks whether the question depends on previous context.

    In addition to follow-up pronouns/expressions, a question is considered
    contextual when it contains at least one slot among ticker, metric, and period
    but omits one or more of them: in that case the missing slots can be
    deterministically retrieved from previous turns.
    """
    normalized_question = normalize_retrieval_text(question)
    question_tokens = tokenize_retrieval_text(question)
    matched_expressions = sorted((expression for expression in FOLLOW_UP_EXPRESSIONS if expression in normalized_question))
    matched_pronouns = sorted(question_tokens & CONTEXTUAL_PRONOUNS)
    short_contextual_question = len(question_tokens) <= 6 and bool(conversation_history) and (normalized_question.startswith('and ') or normalized_question.startswith('then ') or normalized_question.startswith('instead '))
    current_slots = extract_question_slots(question, known_tickers)
    slot_presence = {'ticker': bool(current_slots['ticker']), 'metric': current_slots['metric'] is not None or bool(current_slots['concepts']), 'time_period': current_slots['time_period'] is not None}
    partial_slot_question = bool(conversation_history) and any(slot_presence.values()) and (not all(slot_presence.values()))
    is_follow_up = bool(conversation_history and (matched_expressions or matched_pronouns or short_contextual_question or partial_slot_question))
    return {'is_follow_up': is_follow_up, 'matched_expressions': matched_expressions, 'matched_pronouns': matched_pronouns, 'short_contextual_question': short_contextual_question, 'partial_slot_question': partial_slot_question, 'current_slot_presence': slot_presence}

def build_available_result_semantic_descriptor(state: Dict[str, Any], tool_name: str, metadata: Dict[str, Any]) -> Dict[str, Any]:
    """
    Builds a compact semantic description of the already available
    result component.

    The description is used to recognize the result, not to
    validate it. It does not use tickers contained in the result as
    the primary identity key.
    """
    signatures = state.get('tool_result_signatures', {})
    stored_signature = {}
    if isinstance(signatures, dict):
        stored_signature = signatures.get(tool_name, {}) or {}
    parameters = stored_signature.get('parameters', {}) if isinstance(stored_signature, dict) else {}
    time_periods = stored_signature.get('time_periods', []) if isinstance(stored_signature, dict) else []
    semantic_time_period = None
    formation_months = parameters.get('formation_period_months') if isinstance(parameters, dict) else None
    if formation_months is not None:
        try:
            semantic_time_period = f'{int(formation_months)}M'
        except (TypeError, ValueError):
            semantic_time_period = str(formation_months)
    elif time_periods:
        semantic_time_period = str(time_periods[0])
    elif isinstance(parameters, dict) and parameters.get('start_date') and parameters.get('end_date'):
        semantic_time_period = f"{parameters.get('start_date')}/{parameters.get('end_date')}"
    return {'tool_name': tool_name, 'result_kind': 'ranking' if tool_name == 'momentum' else 'tool_result', 'output_fields': list(metadata.get('output_fields', [])), 'time_period': semantic_time_period}

def build_available_results_catalog(state: Dict[str, Any], tool_registry: Optional[Dict[str, Dict[str, Any]]]=None) -> Dict[str, Dict[str, Any]]:
    """
    Links outputs present in final_state to the tools
    registered in BOX 37.
    """
    registry = tool_registry if tool_registry is not None else state.get('tool_registry', {})
    available_results = {}
    for tool_name, metadata in registry.items():
        expected_outputs = metadata.get('output_fields', [])
        available_output_fields = []
        missing_output_fields = []
        for output_field in expected_outputs:
            if output_field in state and (not _is_empty_retrieval_value(state[output_field])):
                available_output_fields.append(output_field)
            else:
                missing_output_fields.append(output_field)
        available_results[tool_name] = {'tool_name': tool_name, 'expected_outputs': expected_outputs, 'available_outputs': available_output_fields, 'missing_outputs': missing_output_fields, 'produced_metrics': list(metadata.get('produced_metrics', []) or []), 'result_keys': [result_key for result_key, result_entry in (state.get('tool_results_by_key', {}) if isinstance(state.get('tool_results_by_key', {}), dict) else {}).items() if isinstance(result_entry, dict) and result_entry.get('tool_name') == tool_name], 'reusable': bool(available_output_fields or any((isinstance(result_entry, dict) and result_entry.get('tool_name') == tool_name for result_entry in (state.get('tool_results_by_key', {}) if isinstance(state.get('tool_results_by_key', {}), dict) else {}).values()))), 'complete': bool(expected_outputs) and (not missing_output_fields), 'semantic_descriptor': build_available_result_semantic_descriptor(state=state, tool_name=tool_name, metadata=metadata)}
    return available_results

def _is_empty_retrieval_value(value: Any) -> bool:
    """
    Checks whether an output should be considered empty.
    """
    if value is None:
        return True
    if isinstance(value, (str, list, tuple, set, dict, pd.DataFrame, pd.Series)):
        return len(value) == 0
    return False

def create_conversation_turn(state: Dict[str, Any], question: str, answer: str='', execution_plan: Optional[List[Dict[str, Any]]]=None, selected_tools: Optional[Sequence[str]]=None, selected_tickers: Optional[Sequence[str]]=None, concepts: Optional[Sequence[str]]=None) -> Dict[str, Any]:
    """
    Creates a compact representation of a turn
    in the current conversation.
    """
    conversation_history = state.get('current_conversation_history', [])
    turn_number = len(conversation_history) + 1
    return {'turn_id': str(uuid.uuid4()), 'turn_number': turn_number, 'timestamp': datetime.now().isoformat(timespec='seconds'), 'question': question, 'normalized_question': normalize_retrieval_text(question), 'answer': answer, 'execution_plan': copy.deepcopy(execution_plan if execution_plan is not None else state.get('execution_plan', [])), 'selected_tools': list(selected_tools if selected_tools is not None else state.get('selected_tools', [])), 'selected_tickers': list(selected_tickers if selected_tickers is not None else state.get('selected_tickers', [])), 'concepts': list(concepts if concepts is not None else extract_retrieval_concepts(question))}

def append_conversation_turn(state: Dict[str, Any], turn: Dict[str, Any], max_turns: int=MAX_CONVERSATION_TURNS) -> List[Dict[str, Any]]:
    """
    Adds a turn to the history of the current session.
    """
    conversation_history = list(state.get('current_conversation_history', []))
    conversation_history.append(copy.deepcopy(turn))
    if len(conversation_history) > max_turns:
        conversation_history = conversation_history[-max_turns:]
    state['current_conversation_history'] = conversation_history
    return conversation_history

def _retrieval_time_signature(question: str) -> Dict[str, Any]:
    """Distinguishes generic rolling periods, calendar years, and the absence of a time constraint."""
    period = extract_retrieval_time_period(question)
    if period is None:
        return {'time_mode': 'no_time_constraint', 'calendar_year': None, 'rolling_value': None, 'rolling_unit': None}
    if period['type'] == 'calendar_year':
        return {'time_mode': 'calendar_year', 'calendar_year': int(period['value']), 'rolling_value': None, 'rolling_unit': None}
    return {'time_mode': 'rolling', 'calendar_year': None, 'rolling_value': int(period['value']), 'rolling_unit': period['unit']}

def _retrieval_time_compatible(current_signature: Dict[str, Any], stored_signature: Dict[str, Any]) -> bool:
    current_mode = current_signature.get('time_mode', 'no_time_constraint')
    stored_mode = stored_signature.get('time_mode', 'no_time_constraint')
    if current_mode == 'no_time_constraint':
        return True
    if current_mode != stored_mode:
        return False
    if current_mode == 'calendar_year':
        return current_signature.get('calendar_year') == stored_signature.get('calendar_year')
    return True

def retrieve_current_flow_context(question: str, conversation_history: Sequence[Dict[str, Any]], known_tickers: Optional[Sequence[str]]=None, max_turns: int=MAX_RETRIEVED_TURNS) -> Dict[str, Any]:
    """
    Retrieves only relevant turns belonging
    to the current conversation.
    """
    current_time_signature = _retrieval_time_signature(question)
    follow_up_report = detect_follow_up_question(question=question, conversation_history=conversation_history, known_tickers=known_tickers)
    current_concepts = set(extract_retrieval_concepts(question))
    current_tokens = tokenize_retrieval_text(question)
    scored_turns = []
    for turn in conversation_history:
        previous_question = turn.get('question', '')
        candidate_time_signature = _retrieval_time_signature(previous_question)
        if not follow_up_report['is_follow_up'] and (not _retrieval_time_compatible(current_time_signature, candidate_time_signature)):
            continue
        previous_tokens = tokenize_retrieval_text(previous_question)
        previous_concepts = set(turn.get('concepts', extract_retrieval_concepts(previous_question)))
        token_union = current_tokens | previous_tokens
        token_overlap_score = len(current_tokens & previous_tokens) / len(token_union) if token_union else 0.0
        concept_union = current_concepts | previous_concepts
        concept_overlap_score = len(current_concepts & previous_concepts) / len(concept_union) if concept_union else 0.0
        recency_score = turn.get('turn_number', 0) / max(len(conversation_history), 1)
        contextual_bonus = 0.5 if follow_up_report['is_follow_up'] else 0.0
        retrieval_score = round(0.35 * token_overlap_score + 0.35 * concept_overlap_score + 0.3 * recency_score + contextual_bonus, 6)
        scored_turns.append({**copy.deepcopy(turn), 'retrieval_score': retrieval_score, 'token_overlap': round(token_overlap_score, 6), 'concept_overlap': round(concept_overlap_score, 6)})
    scored_turns = sorted(scored_turns, key=lambda item: (item['retrieval_score'], item.get('turn_number', 0)), reverse=True)
    if follow_up_report['is_follow_up']:
        retrieved_turns = scored_turns[:max_turns]
    else:
        retrieved_turns = [turn for turn in scored_turns if turn['token_overlap'] > 0 or turn['concept_overlap'] > 0][:max_turns]
    resolved_slots = resolve_conversational_slots(question=question, conversation_history=conversation_history, known_tickers=known_tickers)
    follow_up_report['resolved_slots'] = copy.deepcopy(resolved_slots)
    return {'follow_up_report': follow_up_report, 'resolved_slots': resolved_slots, 'retrieved_turns': retrieved_turns, 'retrieved_turn_count': len(retrieved_turns), 'current_concepts': sorted(current_concepts)}

def build_retrieval_context(state: Dict[str, Any], question: Optional[str]=None) -> Dict[str, Any]:
    """
    Builds the context to provide to subsequent agents.
    """
    current_question = question if question is not None else state.get('user_question', '')
    conversation_history = state.get('current_conversation_history', [])
    known_tickers = state.get('dow_tickers', state.get('tickers', state.get('selected_tickers', [])))
    current_flow = retrieve_current_flow_context(question=current_question, conversation_history=conversation_history, known_tickers=known_tickers)
    available_results = build_available_results_catalog(state=state, tool_registry=state.get('tool_registry', TOOL_REGISTRY if 'TOOL_REGISTRY' in globals() else {}))
    resolved_slots = current_flow.get('resolved_slots', {})
    retrieved_tickers = list(resolved_slots.get('ticker', {}).get('value', []))
    if not retrieved_tickers:
        retrieved_tickers = extract_tickers_from_context(current_flow['retrieved_turns'], known_tickers=known_tickers)
    reusable_tools = [tool_name for tool_name, metadata in available_results.items() if metadata['reusable']]
    context = {'question': current_question, 'normalized_question': normalize_retrieval_text(current_question), 'is_follow_up': current_flow['follow_up_report']['is_follow_up'], 'follow_up_indicators': current_flow['follow_up_report'], 'retrieved_current_flow': current_flow['retrieved_turns'], 'retrieved_tickers': retrieved_tickers, 'current_concepts': resolved_slots.get('concepts', {}).get('value', []) or current_flow['current_concepts'], 'resolved_slots': copy.deepcopy(resolved_slots), 'available_results': available_results, 'press_release_catalog_index': copy.deepcopy(state.get('press_release_catalog_index', {})), 'press_release_search_catalog': copy.deepcopy(state.get('press_release_search_catalog', {})), 'press_release_information_catalog': copy.deepcopy(state.get('press_release_information_catalog', {})), 'press_release_semantic_kpi_families': copy.deepcopy(state.get('press_release_semantic_kpi_families', {})), 'press_release_tool_contract': copy.deepcopy(state.get('press_release_tool_contract', {})), 'reusable_tools': reusable_tools, 'reusable_flow_detected': bool(current_flow['retrieved_turns']), 'persistent_memory_used': False, 'retrieval_scope': 'current_conversation_and_final_state'}
    return context

def retrieval_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Deterministic node that prepares the context of the
    current conversation and reusable outputs.
    """
    start_time = datetime.now()
    retrieval_context = build_retrieval_context(state=state)
    elapsed_time = (datetime.now() - start_time).total_seconds()
    return {'normalized_question': retrieval_context['normalized_question'], 'retrieval_context': retrieval_context, 'resolved_slots': retrieval_context.get('resolved_slots', {}), 'retrieved_current_flow': retrieval_context['retrieved_current_flow'], 'available_results': retrieval_context['available_results'], 'reusable_flow_detected': retrieval_context['reusable_flow_detected'], 'retrieval_execution_time_seconds': elapsed_time, 'current_question_node': 'retrieval', 'question_workflow_status': 'retrieving', 'next_node': 'question_analysis'}
final_state.setdefault('current_conversation_history', [])
final_state.setdefault('retrieved_current_flow', [])
final_state.setdefault('available_results', {})
final_state.setdefault('retrieval_context', {})
final_state.setdefault('reusable_flow_detected', False)
_original_build_available_results_catalog_box40 = build_available_results_catalog

def build_available_results_catalog(state: Dict[str, Any], tool_registry: Optional[Dict[str, Dict[str, Any]]]=None) -> Dict[str, Dict[str, Any]]:
    catalog = _original_build_available_results_catalog_box40(state=state, tool_registry=tool_registry)
    for tool_name, item in catalog.items():
        if not isinstance(item, dict):
            continue
        sig = item.get('result_signature') or {}
        if isinstance(sig, dict) and sig:
            metric = item.get('metric') or sig.get('metric', '')
            cs = build_canonical_result_signature(sig.get('tool_name', item.get('tool_name', tool_name)), sig.get('tickers', item.get('tickers', [])), sig.get('time_periods', item.get('time_periods', [])), metric, sig.get('result_selection', item.get('result_selection')), sig.get('parameters', {}), sig.get('effective_start_date'), sig.get('effective_end_date'))
            item['canonical_result_signature'] = cs
            item['canonical_signature_id'] = canonical_result_signature_id(cs)
    return catalog

def extract_retrieval_time_periods(text: Any) -> List[Dict[str, Any]]:
    """Returns ALL explicit rolling horizons in the question, in question order."""
    normalized = normalize_retrieval_text(text)
    found = []
    occupied = []
    unit_map = {'day': 'days', 'days': 'days', 'week': 'weeks', 'weeks': 'weeks', 'month': 'months', 'months': 'months', 'year': 'years', 'years': 'years'}

    def _append(value, unit_raw, label):
        unit = unit_map.get(str(unit_raw).lower())
        if unit:
            found.append({'type': 'rolling', 'value': int(value), 'unit': unit, 'label': label})
    for match in re.finditer('\\b(\\d+)\\s*[- ]?\\s*(day|week|month|year)s?\\s+(?:and|&|/|,)\\s+(\\d+)\\s*[- ]?\\s*(day|week|month|year)s?\\b', normalized):
        occupied.append(match.span())
        _append(match.group(1), match.group(2), f'{match.group(1)} {match.group(2)}s')
        _append(match.group(3), match.group(4), f'{match.group(3)} {match.group(4)}s')
    for match in re.finditer('\\b(\\d+)\\s*(?:and|&|/|,)\\s*(\\d+)\\s+(days?|weeks?|months?|years?)\\b', normalized):
        occupied.append(match.span())
        unit_raw = match.group(3)
        _append(match.group(1), unit_raw, f'{match.group(1)} {unit_raw}')
        _append(match.group(2), unit_raw, f'{match.group(2)} {unit_raw}')
    compact_unit_map = {'d': 'days', 'w': 'weeks', 'm': 'months', 'y': 'years'}
    for match in re.finditer('\\b(\\d+)\\s*([dwmy])\\s*(?:and|&|/|,)\\s*(\\d+)\\s*([dwmy])\\b', normalized):
        occupied.append(match.span())
        for value, compact in ((match.group(1), match.group(2)), (match.group(3), match.group(4))):
            unit = compact_unit_map[compact]
            found.append({'type': 'rolling', 'value': int(value), 'unit': unit, 'label': f'{value}{compact.upper()}'})
    for match in re.finditer('\\b(?:last|past|previous)?\\s*(\\d+)\\s*[- ]?\\s*(days?|weeks?|months?|years?)\\b', normalized):
        if any((a <= match.start() and match.end() <= b for a, b in occupied)):
            continue
        _append(match.group(1), match.group(2), match.group(0).strip())
    for match in re.finditer('\\b(\\d+)\\s*([dwmy])\\b', normalized):
        if any((a <= match.start() and match.end() <= b for a, b in occupied)):
            continue
        unit = compact_unit_map[match.group(2)]
        found.append({'type': 'rolling', 'value': int(match.group(1)), 'unit': unit, 'label': match.group(0).upper()})
    unique = []
    seen = set()
    for period in found:
        key = (period.get('type'), period.get('value'), period.get('unit'))
        if key not in seen:
            seen.add(key)
            unique.append(period)
    return unique
_original_resolve_conversational_slots_complete_period_set = resolve_conversational_slots

def resolve_conversational_slots(question, conversation_history, known_tickers=None):
    resolved = _original_resolve_conversational_slots_complete_period_set(question=question, conversation_history=conversation_history, known_tickers=known_tickers)
    explicit_periods = extract_retrieval_time_periods(question)
    if explicit_periods:
        resolved['time_periods'] = {'value': copy.deepcopy(explicit_periods), 'source': 'current_question', 'turn_number': None}
        resolved['time_period'] = {'value': copy.deepcopy(explicit_periods[0]), 'source': 'current_question', 'turn_number': None}
    else:
        inherited = (resolved.get('time_period') or {}).get('value')
        resolved['time_periods'] = {'value': [copy.deepcopy(inherited)] if inherited is not None else [], 'source': (resolved.get('time_period') or {}).get('source'), 'turn_number': (resolved.get('time_period') or {}).get('turn_number')}
    return resolved

def inspect_reuse_inventory(state):
    """Inspect stored reusable outputs independently of conversation text."""
    inventory = []
    for key, entry in (state.get('tool_results_by_key') or {}).items():
        if not isinstance(entry, dict):
            continue
        sig = entry.get('result_signature') or {}
        inventory.append({'result_key': key, 'tickers': sig.get('tickers', entry.get('tickers', [])), 'metric': sig.get('metric', entry.get('metric')), 'validation_status': entry.get('validation_status'), 'has_outputs': bool(entry.get('outputs') or entry.get('result') or entry.get('data'))})
    return inventory
import re
import unicodedata
DUAL_DOMAIN_ENGLISH_ALIASES = {'financial_metrics': {'annual_return': ['annual return', 'annualized return', 'annualised return', 'annual return percentage', 'stock return', 'investment return'], 'annualized_volatility': ['annualized volatility', 'annualised volatility', 'volatility', 'standard deviation of returns', 'return volatility'], 'return_to_risk_ratio': ['return to risk ratio', 'return-to-risk ratio', 'return risk ratio', 'return per unit of risk'], 'sharpe_ratio': ['sharpe ratio', 'sharpe', 'risk adjusted performance', 'risk-adjusted return']}, 'pearson_correlation': {'correlation': ['pearson correlation', 'pearson coefficient', 'pearson r', 'correlation coefficient', 'correlation between', 'most correlated', 'highest correlation']}, 'momentum': {'momentum': ['momentum', 'price momentum', 'six month momentum', 'twelve month momentum', '6-month momentum', '12-month momentum'], 'dollar_volume': ['dollar volume', 'dollar trading volume', 'traded dollar volume', 'volume in dollars'], 'momentum_rank': ['momentum ranking', 'momentum rank', 'ranked by momentum', 'highest momentum', 'top momentum']}, 'capm_beta': {'capm_beta': ['capm beta', 'beta coefficient', 'market beta', 'stock beta', 'beta']}, 'capm_alpha': {'capm_alpha': ['capm alpha', 'jensen alpha', "jensen's alpha", 'alpha coefficient', 'alpha']}, 'capm_expected_return': {'capm_expected_return': ['capm expected return', 'expected return under capm', 'expected return according to capm', 'capm required return', 'capm implied return']}, 'press_release_fy2025': {}}
DUAL_DOMAIN_AMBIGUOUS_TERMS = {'financial_metrics': {'annual_return': {'stock return', 'investment return'}, 'sharpe_ratio': {'risk adjusted performance', 'risk-adjusted return'}}, 'capm_beta': {'capm_beta': {'beta'}}, 'capm_alpha': {'capm_alpha': {'alpha'}}, 'press_release_fy2025': {'FY_RESULTS': {'financial performance', 'annual results'}, 'GUIDANCE_OUTLOOK': {'outlook', 'guidance'}}}

def _dd_norm(value):
    value = unicodedata.normalize('NFKD', str(value).casefold())
    value = ''.join((ch for ch in value if not unicodedata.combining(ch)))
    return re.sub('[^a-z0-9]+', ' ', value).strip()

def _dd_hit(text, term):
    return bool(re.search('(?<!\\w)' + re.escape(_dd_norm(term)) + '(?!\\w)', text))

def build_dual_domain_dictionary(tool_registry=None, press_release_catalog=None):
    registry = tool_registry if tool_registry is not None else globals()['TOOL_REGISTRY']
    press_catalog = press_release_catalog if press_release_catalog is not None else globals().get('PRESS_RELEASE_SEARCH_CATALOG', {})
    output = {}
    for tool, metadata in registry.items():
        domain = 'fundamental' if metadata.get('component_type') == 'fundamental_tool' else 'quantitative'
        metrics = {key: list(aliases) for key, aliases in DUAL_DOMAIN_ENGLISH_ALIASES.get(tool, {}).items()}
        if tool == 'press_release_fy2025':
            for metric, spec in press_catalog.items():
                if not isinstance(spec, dict):
                    continue
                terms = []
                for field in ('aliases_en', 'aliases', 'query_terms', 'document_cues', 'label'):
                    value = spec.get(field, [])
                    terms.extend(value if isinstance(value, list) else [value] if isinstance(value, str) else [])
                metrics[str(metric).strip().upper()] = list(dict.fromkeys((t for t in terms if isinstance(t, str) and t.strip())))
        output[tool] = {'domain': domain, 'metrics': metrics, 'produced_metrics': metadata.get('produced_metrics', []), 'output_fields': metadata.get('output_fields', [])}
    return output

def dual_domain_question_check(question, tool_registry=None, press_release_catalog=None):
    catalog = build_dual_domain_dictionary(tool_registry, press_release_catalog)
    normalized = _dd_norm(question)
    hits = []
    for tool, spec in catalog.items():
        for metric, aliases in spec['metrics'].items():
            matched = [a for a in aliases if _dd_hit(normalized, a)]
            if not matched:
                continue
            ambiguous = DUAL_DOMAIN_AMBIGUOUS_TERMS.get(tool, {}).get(metric, set())
            if all((_dd_norm(a) in {_dd_norm(t) for t in ambiguous} for a in matched)):
                continue
            hits.append({'tool': tool, 'metric': metric, 'domain': spec['domain'], 'matched_terms': matched, 'requested': 1})
    domains = {h['domain'] for h in hits}
    hit_keys = {(h['tool'], h['metric']) for h in hits}
    tool_matrix = [{'tool': tool, 'metric': metric, 'domain': spec['domain'], 'requested': int((tool, metric) in hit_keys)} for tool, spec in catalog.items() for metric in spec['metrics']]
    active = domains == {'quantitative', 'fundamental'}
    return {'active': active, 'quantitative_count': sum((h['domain'] == 'quantitative' for h in hits)), 'fundamental_count': sum((h['domain'] == 'fundamental' for h in hits)), 'hits': hits if active else [], 'tool_request_matrix': tool_matrix if active else [], 'note': 'Lexical routing only: ticker, period, and requirement coverage remain the responsibility of the original BOX 41 atomic requirements.'}

def dual_domain_internal_report(check):
    if not check.get('active'):
        return ''
    lines = ['INTERNAL DUAL-DOMAIN CHECK — DO NOT INCLUDE IN THE USER ANSWER', f"Quantitative requested components: {check['quantitative_count']}", f"Fundamental requested components: {check['fundamental_count']}"]
    lines.extend((f"[{hit['domain']}] {hit['tool']} / {hit['metric']}: requested=1" for hit in check['hits']))
    lines.append('Keep both domains in the original BOX 41 → BOX 42 → BOX 43 → BOX 44 → BOX 45 workflow. Use original requirement_atoms and requirement_id for ticker/time-period-specific coverage. Do not create new tools or a parallel execution plan.')
    return '\n'.join(lines)
QUESTION_ANALYSIS_AGENT_NAME = 'question_analysis_agent'
QUESTION_ANALYSIS_AGENT_NUMBER = 11
QUESTION_ANALYSIS_MODEL = MAIN_MODEL
MAX_SUB_QUESTIONS = None
MAX_QUESTION_LENGTH = None
MAX_RETRIEVAL_ITEMS_FOR_PROMPT = None
MAX_AVAILABLE_RESULTS_FOR_PROMPT = None
ALLOWED_QUESTION_INTENTS = {'single_analysis', 'comparison', 'ranking', 'screening', 'multi_factor_analysis', 'fundamental_analysis', 'data_quality_inquiry', 'follow_up', 'methodology_inquiry', 'unsupported_prediction', 'unsupported_request', 'clarification_required'}
ALLOWED_FINANCIAL_CONCEPTS = {'return', 'risk', 'sharpe', 'correlation', 'trend', 'volume', 'benchmark', 'momentum', 'capm', 'fundamental', 'data_quality'}

def normalize_user_question(question: Any) -> str:
    """
    Normalizes the question without changing its meaning.
    """
    normalized_question = str(question if question is not None else '').strip()
    normalized_question = re.sub('\\s+', ' ', normalized_question)
    if not normalized_question:
        raise ValueError("The user's question is empty.")
    return normalized_question

def prepare_retrieval_context_for_analysis(retrieval_context: Any) -> Dict[str, Any]:
    """
    Reduces the BOX 40 context to only the information
    required for semantic analysis.

    Complete DataFrames and quantitative outputs are not
    sent to the model.
    """
    if not isinstance(retrieval_context, dict):
        return {'is_follow_up': False, 'reusable_flow_detected': False, 'retrieved_tickers': [], 'current_concepts': [], 'resolved_slots': {}, 'retrieved_current_flow': [], 'reusable_tools': [], 'retrieval_scope': 'current_conversation_and_final_state'}
    retrieved_flow = []
    for turn in retrieval_context.get('retrieved_current_flow', []):
        if not isinstance(turn, dict):
            continue
        retrieved_flow.append({'turn_number': turn.get('turn_number'), 'question': turn.get('question', ''), 'answer': turn.get('answer', ''), 'selected_tickers': turn.get('selected_tickers', []), 'selected_tools': turn.get('selected_tools', []), 'retrieval_score': turn.get('retrieval_score')})
    return {'is_follow_up': bool(retrieval_context.get('is_follow_up', False)), 'follow_up_indicators': retrieval_context.get('follow_up_indicators', {}), 'reusable_flow_detected': bool(retrieval_context.get('reusable_flow_detected', False)), 'retrieved_tickers': list(retrieval_context.get('retrieved_tickers', [])), 'current_concepts': list(retrieval_context.get('current_concepts', [])), 'resolved_slots': copy.deepcopy(retrieval_context.get('resolved_slots', {})), 'retrieved_current_flow': retrieved_flow, 'reusable_tools': list(retrieval_context.get('reusable_tools', [])), 'press_release_catalog_index': copy.deepcopy(retrieval_context.get('press_release_catalog_index', {})), 'press_release_search_catalog': copy.deepcopy(retrieval_context.get('press_release_search_catalog', {})), 'press_release_tool_contract': copy.deepcopy(retrieval_context.get('press_release_tool_contract', {})), 'retrieval_scope': retrieval_context.get('retrieval_scope', 'current_conversation_and_final_state')}

def prepare_registry_for_question_analysis(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Prepares a compact description of the tools and agents.

    Agent 11 uses the catalog only to understand
    the informational boundaries of the system. Final selection
    is performed by Agent 12.
    """
    tool_registry = state.get('tool_registry', TOOL_REGISTRY if 'TOOL_REGISTRY' in globals() else {})
    agent_registry = state.get('agent_registry', AGENT_REGISTRY if 'AGENT_REGISTRY' in globals() else {})
    compact_tools = []
    if isinstance(tool_registry, dict):
        for tool_name, metadata in list(tool_registry.items()):
            metadata = metadata if isinstance(metadata, dict) else {}
            compact_tools.append({'tool_name': tool_name, 'description': metadata.get('description', metadata.get('purpose', '')), 'category': metadata.get('category', ''), 'supported_concepts': metadata.get('supported_concepts', metadata.get('concepts', [])), 'output_fields': metadata.get('output_fields', [])})
    compact_agents = []
    if isinstance(agent_registry, dict):
        for agent_name, metadata in agent_registry.items():
            metadata = metadata if isinstance(metadata, dict) else {}
            compact_agents.append({'agent_name': agent_name, 'description': metadata.get('description', metadata.get('purpose', ''))})
    return {'available_tools': compact_tools, 'available_agents': compact_agents}
QUESTION_ANALYSIS_OUTPUT_SCHEMA = {'question_analysis': {'summary': "Faithful summary of the user's request.", 'request_type': 'simple | compound | follow_up | evidence_assessment | ambiguous | unsupported', 'is_supported': True, 'requires_clarification': False, 'clarification_reason': None, 'uses_retrieved_context': False, 'assessment_mode': 'descriptive | comparative | evidence_based_assessment | unsupported_prediction', 'prediction_boundary': 'Distinction between evidence-supported assessment and unsupported prediction.', 'reasoning_summary': 'Concise, non-operational explanation of the interpretation.'}, 'question_intent': 'single_analysis', 'sub_questions': [{'sub_question_id': 'SQ1', 'component_id': 'COMP_1', 'metric': 'annualized_volatility', 'time_periods': [], 'sub_question': 'Independent and semantically complete sub-question.', 'objective': 'Requested informational result.', 'financial_concepts': ['risk'], 'referenced_tickers': ['AAPL'], 'depends_on': [], 'priority': 1, 'is_supported': True}], 'extracted_entities': {'tickers': ['AAPL'], 'company_names': [], 'financial_concepts': ['risk'], 'metrics': ['annualized volatility'], 'time_periods': [], 'start_date': None, 'end_date': None, 'period_type': None, 'comparison_groups': [], 'ranking_direction': None, 'result_selection': {'type': 'all | top_n | bottom_n | winner', 'size': None}, 'thresholds': [], 'benchmark_references': [], 'contextual_references': [], 'corporate_guidance_references': [], 'assessment_targets': [], 'unsupported_elements': []}}
QUESTION_ANALYSIS_SYSTEM_INSTRUCTION = '\nYou are Agent 11 of an agentic system for the analysis of stocks\nin the Dow Jones Industrial Average.\n\nYour sole task is to semantically understand the user\'s question\nand transform it into a JSON structure intended for the\nsubsequent planning agent.\n\nMANDATORY RULES\n\nPEARSON CORRELATION TIME SCOPE: Independently of any period specified\nin the current question or inherited from conversation history, Pearson\ncorrelation uses the full available historical dataset. Preserve the\noriginal wording of the question, but identify the effective Pearson\ncalculation scope as full_available_dataset. Other metrics retain their\nrequested periods. Never claim that a full-history Pearson coefficient\nwas calculated over a shorter requested period.\n\n1. Interpret the question based on its meaning, not through a\n   simple keyword-matching approach.\n\n2. The retrieval_context.resolved_slots field represents the deterministic\n   resolution of the conversational context performed by BOX 40.\n   When a TICKER, METRIC, or TIME PERIOD slot contains a value,\n   consider it an integral part of the current question.\n\n   Mandatory priority for each slot:\n   - explicit value in the current question;\n   - if absent, the most recent value retrieved backward from the\n     conversation and present in resolved_slots.\n\n   Do not declare the question ambiguous and do not request clarification for a\n   slot already populated in resolved_slots. If resolved_slots.inherited_any\n   is true, set uses_retrieved_context = true and consider the request\n   a follow-up when semantically appropriate.\n\n   If resolved_slots.ticker.source = "current_question_global_universe",\n   the current question concerns the entire Dow Jones universe: use all\n   tickers present in resolved_slots.ticker.value and do not restrict the\n   scope to the tickers from the previous conversation or to an inferred subset.\n\n3. Do not select tools, do not assign agents, and do not build an\n   execution plan. These activities belong to Agent 12.\n\n4. When a time period is rolling, set period_type = "rolling"\n    and represent the period in time_periods using a compact canonical form:\n    12M for 12 months, 3Y for 3 years, 2W for 2 weeks, 10D for 10 days.\n    Do not replace a rolling period with a calendar year.\n    If the question contains expressions such as "over the same period",\n    "during the same period", or equivalents, fully inherit the period\n    of the component to which the reference applies and preserve the same\n    period_type and the same time_periods in the dependent sub-questions.\n\n5. Do not perform calculations and do not invent financial values.\n- `GENERAL_FUNDAMENTAL` is not a valid metric: never generate it.\n   For the Press Release tool, use exclusively canonical keys present in the catalog;\n   if no key is unambiguous, leave the component unresolved without creating generic fallbacks.\n\n6. Do not produce the final answer to the user\'s question.\n\n7. Decompose a compound question down to the minimum reusable level.\n   Each quantitative component must be explicitly identified\n   by tool/ticker scope + time period + metric.\n   Ticker cardinality does not determine component cardinality:\n   when multiple instruments share the same metric and the same period,\n   keep them together in the same component through referenced_tickers.\n   Different metrics or periods remain distinct components.\n\n8. Keep together operations that constitute a single\n   logical constraint. Example: "among the least volatile stocks, find\n   those with positive momentum" must preserve the dependency\n   between the risk filter and the momentum filter.\n\n9. Extract only entities explicitly present in the question\n   or retrieved with certainty from the provided context.\n\n10. Do not automatically convert company names into tickers\n   when the association is uncertain. In that case, preserve the\n   name in company_names.\n\n11. Always distinguish between:\n    - unsupported prediction: a request to state with certainty\n      what will happen in the future, for example "Will IBM rise tomorrow?";\n    - evidence-based assessment: a request to verify whether\n      results, prices, guidance, or other available information\n      are consistent with a scenario or with estimates communicated by the\n      company.\n\n12. Evidence-based assessments are supported. They must\n    be classified with assessment_mode =\n    evidence_based_assessment and formulated without turning them into\n    certain predictions.\n\n13. Point predictions about the future must be classified\n    as unsupported_prediction and also reported in\n    unsupported_elements.\n\n14. MANAGEMENT COMMENTARY ABSORPTION RULE.\n    When the question explicitly asks what the CEO\n    and/or CFO stated about guidance, outlook, strategy, targets, milestones, or\n    equivalent topics, the requested information component is the role commentary:\n    CEO_COMMENTARY and/or CFO_COMMENTARY. Guidance, outlook, strategy, targets,\n    and milestones are in this case the topic of the commentary and MUST NOT\n    generate separate documentary components GUIDANCE_OUTLOOK or\n    STRATEGY_MILESTONES for the same ticker and period.\n    If the user instead directly asks for guidance/outlook/strategy without\n    attributing them to statements by the CEO or CFO, preserve the normal dedicated\n    documentary components.\n    When the question uses generic terms such as management, management team,\n    senior management, company leadership, management guidance, management\n    statements, or managerial guidance without specifying CEO or CFO, treat them\n    as a generic management reference. Do not automatically transform them into\n    a separate request for both CEO_COMMENTARY and CFO_COMMENTARY. If these\n    terms are associated with guidance, outlook, expectations, strategy,\n    targets, or future/forward-looking indications, preserve the\n    documentary component GUIDANCE_OUTLOOK, which can represent the\n    management\'s forward-looking indication without necessarily requiring both\n    roles.\n\n15. PRESS RELEASE DOCUMENTARY TAXONOMY.\n    For press release requests, use the following information components\n    without creating semantic duplication:\n    - FY_RESULTS: FY2025 full-year results. Revenue, EPS, cash flow,\n      margins, backlog, and the other KPIs reported in the results belong\n      to FY_RESULTS and must not automatically generate additional\n      documentary components when the user generically requests the results.\n    - RESULT_DRIVERS: insights, causes, drivers, and explanations of why\n      FY2025 results performed in a certain way.\n    - GUIDANCE_OUTLOOK: guidance, outlook, prospects, and targets related\n      to 2026/the future.\n    - CEO_COMMENTARY: CEO statements. The role does not have a\n      mandatory time scope of its own.\n    - CFO_COMMENTARY: CFO statements. The role does not have a\n      mandatory time scope of its own.\n    A compound question may require multiple components only when\n    the user actually requests them. Do not automatically transform FY_RESULTS\n    into REVENUE_SALES or other redundant documentary metrics.\n\n16. Specific terms such as earnings, revenue, margins, guidance, growth\n    estimates, price growth, and EPS must be extracted\n    into metrics, corporate_guidance_references, or assessment_targets.\n    They must also be mapped to one or more permitted general categories,\n    such as fundamental, return, momentum, or benchmark.\n\n17. Comparative expressions such as "best", "worst",\n    "most promising", "least promising", "strongest", or\n    "weakest" must be parameterized. Always extract:\n    - the ranking direction;\n    - the quantitative criterion or criteria;\n    - the time horizon;\n    - the requested number of stocks, if any.\n    If the user specifies a criterion, use that criterion. If they do not\n    specify a single KPI, interpret the request as a multi-factor comparison\n    among independent rankings of Annual Return, Sharpe Ratio,\n    Return-to-Risk Ratio, Volatility, CAPM alpha/\n    expected return, Momentum, trend, and liquidity, limited\n    to the tools actually available. Do not invent an\n    opaque score: the synthesis must be based on the number of appearances\n    in the top or bottom N positions and must highlight both confirmations\n    and conflicts among metrics.\n\n18. The time horizon belongs to the semantics of the question.\n    The expressions "last year", "over the last year", "last 12 months",\n    and equivalent formulations ALWAYS indicate a rolling\n    12-month interval ending on the request date, not the current\n    calendar year. Preserve the user\'s explicit period. If absent, associate\n    each metric with its applicable default horizon: 12 months for Momentum,\n    20 trading sessions for trend and volume. Do not\n    automatically apply the same period to metrics with different characteristics.\n\n19. Documentation is excluded from generic quantitative\n    rankings. Use it only for an explicitly requested documentary KPI\n    or to prospectively assess the consistency of evidence\n    with company guidance, targets, or expectations.\n\n20. For Press Release requests, use exclusively the keys available in\n    retrieval_context.press_release_search_catalog as the CANONICAL\n    vocabulary. Do not create, translate, or paraphrase new metric labels.\n    If the question contains multiple documentary information requests,\n    generate a distinct atomic component for each canonical key. Always\n    preserve ticker + time_period + metric as the component identity.\n\n21. When indispensable elements required to interpret the\n    question are missing, use clarification_required and specify the reason.\n\n22. question_intent must belong exclusively to this list:\n    - single_analysis\n    - comparison\n    - ranking\n    - screening\n    - multi_factor_analysis\n    - fundamental_analysis\n    - data_quality_inquiry\n    - follow_up\n    - methodology_inquiry\n    - unsupported_prediction\n    - unsupported_request\n    - clarification_required\n\n23. The allowed normalized financial concepts are:\n    - return\n    - risk\n    - sharpe\n    - correlation\n    - trend\n    - volume\n    - benchmark\n    - momentum\n    - capm\n    - fundamental\n    - data_quality\n\n24. Create at most eight sub-questions.\n\n25. Return exactly four main fields:\n    - question_analysis\n    - question_intent\n    - sub_questions\n    - extracted_entities\n\n26. Do not add main fields other than those requested.\n\n- In anaphoric follow-ups such as "among the 5 stocks", "among these stocks",\n  "over the same period", or equivalent formulations, ALWAYS resolve\n  the reference first using all information, metrics, instruments, rankings,\n  periods, and constraints present in the current question.\n- Only for slots that remain genuinely unresolved after this analysis\n  of the current question, use retrieved_current_flow/current_conversation_history\n  moving backward: first the relevant previous turn, then more\n  distant ones until the slot is resolved.\n- Information explicitly present or semantically inferable from the\n  current question always has priority over any value from the current flow.\n  Information validly retrieved from the current flow constitutes\n  valid context only for slots that are still missing.\n- "Over the same period" must primarily preserve the horizon of the metric\n  or source instrument identifiable in the current question; only\n  if that horizon cannot be determined from the current question may it be\n  retrieved backward from the current flow.\n\n27. For Momentum, the time horizon is NOT part of the metric name.\n    Preserve the concept "momentum" and treat the period as a separate parameter.\n    Apply this priority:\n    - explicit period in the current question;\n    - if absent, period semantically inferable from a metric,\n      instrument, ranking, or other reference present in the current question;\n    - only if still absent, relevant period retrieved backward from the\n      current flow, starting from the previous turn and continuing toward more\n      distant ones;\n    - only if all previous levels are absent, use the default\n      declared in the tool registry.\n\n\n28. Mandatory operational rule for compound questions and comparisons:\n    - always decompose the question into a distinct sub-question for each\n      required piece of information or result;\n    - if the question requires a comparison between a new result and a\n      result already available in the current flow, still represent\n      both as distinct components of the question;\n    - do not automatically transform an already available component\n      into a new calculation request: first identify what is needed;\n    - for each component, explicitly preserve the scope of the\n      instruments/tickers, the time period, and the metric; these elements\n      identify the reusable information building block. Multiple tickers with\n      the same metric and the same period remain within the same scope. The\n      financial concept and result selection remain additional attributes,\n      but cannot replace the metric;\n    - verify that the union of the components covers 100% of the metrics,\n      instruments, and periods required for the answer;\n    - request clarification only when a component cannot genuinely be\n      identified from the question, the current flow, or the tool registry;\n    - a comparison between two already identifiable rankings does not require\n      clarification: it requires the two rankings as inputs and a final comparison.\n\nADDITIONAL TEMPORAL RULES\n\n- The current_date provided in the payload is the authoritative temporal\n  reference already used by the system.\n- Use current_date exclusively as internal semantic context.\n  Do not report it in the answer and do not independently determine\n  whether a date is future, present, or past.\n- For requests involving forecasts or uncovered periods,\n  consider exclusively the availability of data and calculations\n  in the system dataset/evidence. Do not use the model\'s internal\n  temporal knowledge as a criterion for support or rejection.\n'

def build_question_analysis_prompt(user_question: str, retrieval_context: Dict[str, Any], registry_context: Dict[str, Any]) -> str:
    """
    Builds the content sent to the primary model.
    """
    prompt_payload = {'current_date': datetime.now().date().isoformat(), 'task': 'Semantically analyze the question and return the output according to the required schema.', 'user_question': user_question, 'retrieval_context': retrieval_context, 'system_capabilities': registry_context, 'required_output_schema': QUESTION_ANALYSIS_OUTPUT_SCHEMA}
    return json.dumps(prompt_payload, ensure_ascii=False, indent=2, default=str)

def _ensure_list(value: Any) -> List[Any]:
    """
    Converts a value into a list without introducing null elements.
    """
    if value is None:
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, (tuple, set)):
        return list(value)
    return [value]

def _unique_strings(values: Any, uppercase: bool=False) -> List[str]:
    """
    Normalizes a sequence of strings by removing duplicates.
    """
    normalized_values = []
    seen_values = set()
    for value in _ensure_list(values):
        if value is None:
            continue
        normalized_value = re.sub('\\s+', ' ', str(value).strip())
        if not normalized_value:
            continue
        if uppercase:
            normalized_value = normalized_value.upper()
        comparison_value = normalized_value.lower()
        if comparison_value in seen_values:
            continue
        seen_values.add(comparison_value)
        normalized_values.append(normalized_value)
    return normalized_values

def _normalize_press_release_catalog_term(value: Any) -> str:
    text = str(value or '').strip().lower()
    text = text.replace('_', ' ').replace('-', ' ')
    text = re.sub('[^\\w\\s]', ' ', text, flags=re.UNICODE)
    return re.sub('\\s+', ' ', text).strip()

def _match_press_release_catalog_metric(text: Any, search_catalog: Dict[str, Any]) -> Optional[str]:
    normalized_text = _normalize_press_release_catalog_term(text)
    if not normalized_text or not isinstance(search_catalog, dict):
        return None
    matches = []
    for metric_name, raw_spec in search_catalog.items():
        spec = raw_spec if isinstance(raw_spec, dict) else {}
        terms = [metric_name, spec.get('label_it'), spec.get('label_en')]
        terms.extend(_ensure_list(spec.get('aliases_it', [])))
        terms.extend(_ensure_list(spec.get('aliases_en', [])))
        for term in terms:
            normalized_term = _normalize_press_release_catalog_term(term)
            if not normalized_term:
                continue
            if normalized_text == normalized_term:
                matches.append((3, len(normalized_term), str(metric_name)))
            elif normalized_term in normalized_text:
                matches.append((2, len(normalized_term), str(metric_name)))
    if not matches:
        return None
    matches.sort(reverse=True)
    best = matches[0]
    tied_metrics = {item[2] for item in matches if item[:2] == best[:2]}
    if len(tied_metrics) != 1:
        return None
    return best[2]

def canonicalize_press_release_analysis_metrics(analysis_output: Dict[str, Any], retrieval_context: Dict[str, Any], user_question: str) -> Dict[str, Any]:
    output = copy.deepcopy(analysis_output)
    search_catalog = retrieval_context.get('press_release_search_catalog', {}) if isinstance(retrieval_context, dict) else {}
    if not isinstance(search_catalog, dict) or not search_catalog:
        return output
    canonical_metrics = []
    normalized_sub_questions = []
    for raw_sub_question in _ensure_list(output.get('sub_questions', [])):
        if not isinstance(raw_sub_question, dict):
            normalized_sub_questions.append(raw_sub_question)
            continue
        sub_question = copy.deepcopy(raw_sub_question)
        semantic_text = ' '.join((str(sub_question.get(key, '')) for key in ('sub_question', 'objective', 'metric')))
        canonical_metric = _match_press_release_catalog_metric(semantic_text, search_catalog)
        if canonical_metric:
            sub_question['metric'] = canonical_metric
            canonical_metrics.append(canonical_metric)
        normalized_sub_questions.append(sub_question)
    output['sub_questions'] = normalized_sub_questions
    entities = output.get('extracted_entities', {})
    entities = copy.deepcopy(entities) if isinstance(entities, dict) else {}
    normalized_question = _normalize_press_release_catalog_term(user_question)
    question_hits = []
    for metric_name, raw_spec in search_catalog.items():
        spec = raw_spec if isinstance(raw_spec, dict) else {}
        terms = [metric_name, spec.get('label_it'), spec.get('label_en')]
        terms.extend(_ensure_list(spec.get('aliases_it', [])))
        terms.extend(_ensure_list(spec.get('aliases_en', [])))
        for term in terms:
            normalized_term = _normalize_press_release_catalog_term(term)
            if normalized_term and normalized_term in normalized_question:
                question_hits.append(str(metric_name))
                break
    canonical_metrics = _unique_strings(canonical_metrics + question_hits)
    if canonical_metrics:
        entities['metrics'] = canonical_metrics
        concepts = _unique_strings(entities.get('financial_concepts', []))
        if 'fundamental' not in [item.lower() for item in concepts]:
            concepts.append('fundamental')
        entities['financial_concepts'] = concepts
    output['extracted_entities'] = entities
    return output

def apply_press_release_document_taxonomy(analysis_output: Dict[str, Any], user_question: str) -> Dict[str, Any]:
    """
    Deterministically applies the agreed documentary taxonomy.

    - FY_RESULTS -> FY2025;
    - RESULT_DRIVERS -> FY2025;
    - GUIDANCE_OUTLOOK -> 2026/future;
    - CEO_COMMENTARY / CFO_COMMENTARY -> no mandatory temporal scope;
    - a generic request for "FY2025 results" is not automatically
      duplicated into REVENUE_SALES or other documentary metrics.
    """
    output = copy.deepcopy(analysis_output)
    question_text = _normalize_press_release_catalog_term(user_question)
    entities = output.get('extracted_entities', {})
    entities = copy.deepcopy(entities) if isinstance(entities, dict) else {}
    result_terms = ('earnings', 'financial results')
    explicit_result_patterns = ('\\bresults?\\s+(?:for\\s+)?20\\d{2}\\b', '\\b20\\d{2}\\s+results?\\b', '\\bfy\\s*20\\d{2}\\b', '\\bfull[\\s-]?year(?:\\s+20\\d{2})?\\b')
    driver_terms = ('why', 'why', 'driver', 'drivers', 'reasons', 'causes', 'factors', 'insight', 'insights', 'deep dives')
    guidance_terms = ('guidance', 'outlook', 'prospects', 'targets', 'objectives', '2026', 'future', 'future', 'management guidance', 'management statements', 'managerial guidance', 'management guidance', 'management outlook')
    ceo_terms = ('ceo', 'chief executive officer')
    cfo_terms = ('cfo', 'chief financial officer')
    asks_results = any((term in question_text for term in result_terms)) or any((re.search(pattern, question_text) for pattern in explicit_result_patterns))
    asks_drivers = any((term in question_text for term in driver_terms))
    asks_guidance = any((term in question_text for term in guidance_terms))
    asks_ceo = any((term in question_text for term in ceo_terms))
    asks_cfo = any((term in question_text for term in cfo_terms))
    requested_document_metrics = []
    if asks_results:
        requested_document_metrics.append('FY_RESULTS')
    if asks_drivers:
        requested_document_metrics.append('RESULT_DRIVERS')
    if asks_guidance:
        requested_document_metrics.append('GUIDANCE_OUTLOOK')
    if asks_ceo:
        requested_document_metrics.append('CEO_COMMENTARY')
    if asks_cfo:
        requested_document_metrics.append('CFO_COMMENTARY')
    if (asks_ceo or asks_cfo) and asks_guidance:
        requested_document_metrics = [metric for metric in requested_document_metrics if metric != 'GUIDANCE_OUTLOOK']
    requested_document_metrics = _unique_strings(requested_document_metrics)
    press_release_catalog = globals().get('PRESS_RELEASE_SEARCH_CATALOG', {}) or {}
    catalog_metrics = {str(metric).strip().upper() for metric in press_release_catalog if str(metric).strip()}
    current_metrics = _unique_strings(entities.get('metrics', []))
    if requested_document_metrics:
        non_document_metrics = [metric for metric in current_metrics if str(metric).strip().upper() not in catalog_metrics]
        entities['metrics'] = _unique_strings(non_document_metrics + requested_document_metrics)
        normalized_sub_questions = []
        for sub_question in _ensure_list(output.get('sub_questions', [])):
            if not isinstance(sub_question, dict):
                normalized_sub_questions.append(sub_question)
                continue
            metric_key = str(sub_question.get('metric', '')).strip().upper()
            if metric_key and metric_key in catalog_metrics and (metric_key not in requested_document_metrics):
                continue
            normalized_sub_questions.append(copy.deepcopy(sub_question))
        existing_sub_metrics = {str(item.get('metric', '')).strip().upper() for item in normalized_sub_questions if isinstance(item, dict)}
        entity_tickers = _unique_strings(entities.get('tickers', []), uppercase=True)
        for metric in requested_document_metrics:
            if metric in existing_sub_metrics:
                continue
            if metric in {'FY_RESULTS', 'RESULT_DRIVERS'}:
                metric_periods = ['FY2025']
            elif metric == 'GUIDANCE_OUTLOOK':
                metric_periods = ['2026']
            else:
                metric_periods = []
            normalized_sub_questions.append({'sub_question_id': f'SQ{len(normalized_sub_questions) + 1}', 'component_id': f'COMP_{len(normalized_sub_questions) + 1}', 'metric': metric, 'time_periods': metric_periods, 'sub_question': f'Retrieve {metric} from the press release.', 'objective': f'Obtain the documentary component {metric}.', 'financial_concepts': ['fundamental'], 'referenced_tickers': entity_tickers, 'depends_on': [], 'priority': len(normalized_sub_questions) + 1, 'is_supported': True})
        for sub_question in normalized_sub_questions:
            if not isinstance(sub_question, dict):
                continue
            metric_key = str(sub_question.get('metric', '')).strip().upper()
            if metric_key in {'FY_RESULTS', 'RESULT_DRIVERS'}:
                sub_question['time_periods'] = ['FY2025']
            elif metric_key == 'GUIDANCE_OUTLOOK':
                sub_question['time_periods'] = ['2026']
            elif metric_key in {'CEO_COMMENTARY', 'CFO_COMMENTARY'}:
                sub_question['time_periods'] = []
        output['sub_questions'] = normalized_sub_questions
    output['extracted_entities'] = entities
    return output

def validate_question_analysis_output(raw_output: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validates and normalizes the output returned by the model.
    """
    if not isinstance(raw_output, dict):
        raise TypeError('Agent 11 output must be a dictionary.')
    required_fields = {'question_analysis', 'question_intent', 'sub_questions', 'extracted_entities'}
    missing_fields = required_fields - set(raw_output.keys())
    if missing_fields:
        raise ValueError('Agent 11 output does not contain the required fields: ' + ', '.join(sorted(missing_fields)))
    raw_analysis = raw_output.get('question_analysis', {})
    if not isinstance(raw_analysis, dict):
        raw_analysis = {'summary': str(raw_analysis)}
    question_intent = str(raw_output.get('question_intent', '')).strip()
    if question_intent not in ALLOWED_QUESTION_INTENTS:
        question_intent = 'clarification_required'
    request_type = str(raw_analysis.get('request_type', 'simple')).strip().lower()
    if request_type not in {'simple', 'compound', 'follow_up', 'evidence_assessment', 'ambiguous', 'unsupported'}:
        request_type = 'ambiguous'
    question_analysis = {'summary': str(raw_analysis.get('summary', '')).strip(), 'request_type': request_type, 'is_supported': bool(raw_analysis.get('is_supported', question_intent not in {'unsupported_prediction', 'unsupported_request'})), 'requires_clarification': bool(raw_analysis.get('requires_clarification', question_intent == 'clarification_required')), 'clarification_reason': None if raw_analysis.get('clarification_reason') in {None, '', 'null'} else str(raw_analysis.get('clarification_reason')).strip(), 'uses_retrieved_context': bool(raw_analysis.get('uses_retrieved_context', False)), 'assessment_mode': str(raw_analysis.get('assessment_mode', 'descriptive')).strip() if str(raw_analysis.get('assessment_mode', 'descriptive')).strip() in {'descriptive', 'comparative', 'evidence_based_assessment', 'unsupported_prediction'} else 'descriptive', 'prediction_boundary': str(raw_analysis.get('prediction_boundary', '')).strip(), 'reasoning_summary': str(raw_analysis.get('reasoning_summary', '')).strip()}
    normalized_sub_questions = []
    raw_sub_questions = _ensure_list(raw_output.get('sub_questions', []))
    for position, raw_sub_question in enumerate(raw_sub_questions, start=1):
        if isinstance(raw_sub_question, str):
            raw_sub_question = {'sub_question': raw_sub_question}
        if not isinstance(raw_sub_question, dict):
            continue
        sub_question_text = str(raw_sub_question.get('sub_question', '')).strip()
        if not sub_question_text:
            continue
        financial_concepts = [concept for concept in _unique_strings(raw_sub_question.get('financial_concepts', [])) if concept in ALLOWED_FINANCIAL_CONCEPTS]
        priority = raw_sub_question.get('priority', position)
        try:
            priority = int(priority)
        except (TypeError, ValueError):
            priority = position
        normalized_sub_questions.append({'sub_question_id': f'SQ{position}', 'component_id': str(raw_sub_question.get('component_id', f'COMP_{position}')).strip().upper(), 'metric': str(raw_sub_question.get('metric', '')).strip() or None, 'time_periods': _ensure_list(raw_sub_question.get('time_periods', [])), 'sub_question': sub_question_text, 'objective': str(raw_sub_question.get('objective', '')).strip(), 'financial_concepts': financial_concepts, 'referenced_tickers': _unique_strings(raw_sub_question.get('referenced_tickers', []), uppercase=True), 'depends_on': _unique_strings(raw_sub_question.get('depends_on', []), uppercase=True), 'priority': max(1, priority), 'is_supported': bool(raw_sub_question.get('is_supported', True))})
    if not normalized_sub_questions and question_analysis['is_supported'] and (not question_analysis['requires_clarification']):
        raise ValueError('Agent 11 did not produce any valid sub-question.')
    raw_entities = raw_output.get('extracted_entities', {})
    if not isinstance(raw_entities, dict):
        raw_entities = {}
    financial_concepts = [concept for concept in _unique_strings(raw_entities.get('financial_concepts', [])) if concept in ALLOWED_FINANCIAL_CONCEPTS]
    ranking_direction = raw_entities.get('ranking_direction')
    if ranking_direction not in {'ascending', 'descending', 'highest', 'lowest', 'positive', 'negative', None}:
        ranking_direction = None
    extracted_entities = {'tickers': _unique_strings(raw_entities.get('tickers', []), uppercase=True), 'company_names': _unique_strings(raw_entities.get('company_names', [])), 'financial_concepts': financial_concepts, 'metrics': _unique_strings(raw_entities.get('metrics', [])), 'time_periods': _ensure_list(raw_entities.get('time_periods', [])), 'start_date': str(raw_entities.get('start_date')).strip() if raw_entities.get('start_date') else None, 'end_date': str(raw_entities.get('end_date')).strip() if raw_entities.get('end_date') else None, 'period_type': str(raw_entities.get('period_type')).strip().lower() if raw_entities.get('period_type') else None, 'comparison_groups': _ensure_list(raw_entities.get('comparison_groups', [])), 'ranking_direction': ranking_direction, 'result_selection': raw_entities.get('result_selection', {}) if isinstance(raw_entities.get('result_selection', {}), dict) else {}, 'thresholds': _ensure_list(raw_entities.get('thresholds', [])), 'benchmark_references': _unique_strings(raw_entities.get('benchmark_references', [])), 'contextual_references': _unique_strings(raw_entities.get('contextual_references', [])), 'corporate_guidance_references': _unique_strings(raw_entities.get('corporate_guidance_references', [])), 'assessment_targets': _unique_strings(raw_entities.get('assessment_targets', [])), 'unsupported_elements': _unique_strings(raw_entities.get('unsupported_elements', []))}
    return {'question_analysis': question_analysis, 'question_intent': question_intent, 'sub_questions': normalized_sub_questions, 'extracted_entities': extracted_entities}

def _metric_to_financial_concept(metric: Any) -> str:
    normalized = str(metric or '').strip().lower().replace('-', ' ')
    if 'sharpe' in normalized:
        return 'sharpe'
    if 'volatility' in normalized or normalized in {'risk', 'annualized_volatility'}:
        return 'risk'
    if 'beta' in normalized or 'alpha' in normalized or 'capm return' in normalized or ('capm expected return' in normalized) or ('annual capm return' in normalized) or ('expected return capm' in normalized) or ('capm' in normalized):
        return 'capm'
    if 'momentum' in normalized:
        return 'momentum'
    if 'correlation' in normalized:
        return 'correlation'
    if 'return' in normalized:
        return 'return'
    return 'fundamental' if normalized else 'data_quality'

def build_atomic_required_components(analysis_output: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Builds the instrument/ticker scope + time + metric building blocks."""
    entities = analysis_output.get('extracted_entities', {}) or {}
    tickers = _unique_strings(entities.get('tickers', []), uppercase=True)

    def _canonicalize_quantitative_metric(metric: Any) -> str:
        metric_text = str(metric or '').strip()
        if not metric_text:
            return ''
        normalized_metric = re.sub('[^a-z0-9]+', '_', metric_text.lower()).strip('_')
        canonical_metrics = {}
        for tool_metadata in (globals().get('TOOL_REGISTRY', {}) or {}).values():
            for canonical_metric in tool_metadata.get('produced_metrics', []) or []:
                canonical_text = str(canonical_metric).strip()
                if not canonical_text:
                    continue
                canonical_key = re.sub('[^a-z0-9]+', '_', canonical_text.lower()).strip('_')
                canonical_metrics[canonical_key] = canonical_text
        return canonical_metrics.get(normalized_metric, metric_text)

    def _canonicalize_time_period(period: Any) -> Any:
        if not isinstance(period, dict):
            return period
        period_type = str(period.get('period_type', period.get('type', '')) or '').strip().lower()
        raw_value = period.get('time_value', period.get('value'))
        raw_unit = str(period.get('time_unit', period.get('unit', '')) or '').strip().upper()
        if period_type == 'rolling' and raw_value is not None and raw_unit:
            try:
                numeric_value = int(raw_value)
            except (TypeError, ValueError):
                numeric_value = raw_value
            unit_map = {'MONTH': 'M', 'MONTHS': 'M', 'MESE': 'M', 'MESI': 'M', 'YEAR': 'Y', 'YEARS': 'Y', 'ANNO': 'Y', 'ANNI': 'Y', 'WEEK': 'W', 'WEEKS': 'W', 'SETTIMANA': 'W', 'SETTIMANE': 'W', 'DAY': 'D', 'DAYS': 'D', 'GIORNO': 'D', 'GIORNI': 'D'}
            canonical_unit = unit_map.get(raw_unit, raw_unit)
            if canonical_unit in {'M', 'Y', 'W', 'D'}:
                return f'{numeric_value}{canonical_unit}'
        return period
    metrics = _unique_strings([_canonicalize_quantitative_metric(metric) for metric in _ensure_list(entities.get('metrics', []))])
    periods = [_canonicalize_time_period(period) for period in _ensure_list(entities.get('time_periods', []))]
    grouped_components = {}

    def _period_key(period: Any) -> str:
        period = _canonicalize_time_period(period)
        return json.dumps(period, ensure_ascii=False, sort_keys=True, default=str)

    def _add_component(metric: Any, component_tickers: Sequence[Any], period: Any) -> None:
        metric_text = _canonicalize_quantitative_metric(metric)
        period = _canonicalize_time_period(period)
        if not metric_text:
            return
        scope_tickers = _unique_strings(component_tickers, uppercase=True)
        press_release_metric_names = {str(metric_name).strip().upper() for metric_name in globals().get('PRESS_RELEASE_SEARCH_CATALOG', {}) or {} if str(metric_name).strip()}
        if metric_text.upper() in press_release_metric_names and scope_tickers:
            for single_ticker in scope_tickers:
                key = (metric_text.lower(), _period_key(period), single_ticker)
                if key not in grouped_components:
                    grouped_components[key] = {'metric': metric_text, 'period': period, 'tickers': [single_ticker]}
            return
        key = (metric_text.lower(), _period_key(period))
        if key not in grouped_components:
            grouped_components[key] = {'metric': metric_text, 'period': period, 'tickers': []}
        grouped_components[key]['tickers'] = _unique_strings(grouped_components[key]['tickers'] + scope_tickers, uppercase=True)
    sub_questions = [item for item in _ensure_list(analysis_output.get('sub_questions', [])) if isinstance(item, dict)]
    for sub_question in sub_questions:
        sub_metric = _canonicalize_quantitative_metric(sub_question.get('metric', ''))
        sub_tickers = _unique_strings(sub_question.get('referenced_tickers', []), uppercase=True) or tickers
        sub_metric_key = sub_metric.upper()
        if sub_metric_key in {'CEO_COMMENTARY', 'CFO_COMMENTARY'}:
            sub_periods = [None]
        elif sub_metric_key in {'FY_RESULTS', 'RESULT_DRIVERS'}:
            sub_periods = ['FY2025']
        elif sub_metric_key == 'GUIDANCE_OUTLOOK':
            sub_periods = ['2026']
        else:
            sub_periods = [_canonicalize_time_period(period) for period in _ensure_list(sub_question.get('time_periods', []))] or periods or [None]
        if sub_metric:
            for period in sub_periods:
                _add_component(metric=sub_metric, component_tickers=sub_tickers, period=period)
    covered_components = {(str(item.get('metric', '')).strip().lower(), _period_key(item.get('period'))) for item in grouped_components.values() if str(item.get('metric', '')).strip()}
    target_periods = periods if periods else [None]
    for metric in metrics:
        metric_key = str(metric).strip().upper()
        if metric_key in {'CEO_COMMENTARY', 'CFO_COMMENTARY'}:
            metric_periods = [None]
        elif metric_key in {'FY_RESULTS', 'RESULT_DRIVERS'}:
            metric_periods = ['FY2025']
        elif metric_key == 'GUIDANCE_OUTLOOK':
            metric_periods = ['2026']
        else:
            metric_periods = target_periods
        for period in metric_periods:
            existing_scope_tickers = set()
            for existing_component in grouped_components.values():
                if str(existing_component.get('metric', '')).strip().lower() == str(metric).strip().lower() and _period_key(existing_component.get('period')) == _period_key(period):
                    existing_scope_tickers.update(_unique_strings(existing_component.get('tickers', []), uppercase=True))
            required_scope_tickers = set(_unique_strings(tickers, uppercase=True))
            component_fully_covered = not required_scope_tickers and (str(metric).strip().lower(), _period_key(period)) in covered_components or (bool(required_scope_tickers) and required_scope_tickers.issubset(existing_scope_tickers))
            if component_fully_covered:
                continue
            _add_component(metric=metric, component_tickers=tickers, period=period)
    components = []
    for component_index, component in enumerate(grouped_components.values(), start=1):
        scope_tickers = component['tickers']
        period = component['period']
        metric = component['metric']
        single_ticker = scope_tickers[0] if len(scope_tickers) == 1 else None
        components.append({'component_id': f'COMP_{component_index}', 'ticker': single_ticker, 'referenced_tickers': scope_tickers, 'time_period': period, 'time_periods': [period] if period else [], 'metric': metric, 'financial_concept': _metric_to_financial_concept(metric), 'component_signature': {'ticker': single_ticker, 'time_period': period, 'metric': metric}})
    return components

def enforce_atomic_sub_questions(analysis_output: Dict[str, Any]) -> Dict[str, Any]:
    """Ensures one sub-question for each calculation component."""
    output = copy.deepcopy(analysis_output)
    components = build_atomic_required_components(output)
    output['required_components'] = components
    if not components:
        return output
    atomic_sub_questions = []
    for position, component in enumerate(components, start=1):
        referenced_tickers = component.get('referenced_tickers', [])
        metric = component.get('metric')
        period = component.get('time_period')
        if len(referenced_tickers) == 1:
            target = f' for {referenced_tickers[0]}'
        elif referenced_tickers:
            target = f' for the scope of {len(referenced_tickers)} stocks'
        else:
            target = ''
        horizon = f' over the period {period}' if period else ''
        atomic_sub_questions.append({'sub_question_id': f'SQ{position}', 'component_id': component['component_id'], 'metric': metric, 'time_periods': component.get('time_periods', []), 'sub_question': f'Retrieve or calculate {metric}{target}{horizon}.', 'objective': f'Obtain the atomic component {metric}{target}{horizon}.', 'financial_concepts': [component['financial_concept']], 'referenced_tickers': referenced_tickers, 'depends_on': [], 'priority': position, 'is_supported': True})
    output['sub_questions'] = atomic_sub_questions
    return output

def enrich_analysis_with_retrieval_context(analysis_output: Dict[str, Any], retrieval_context: Dict[str, Any]) -> Dict[str, Any]:
    """
    Deterministically integrates the slots resolved by BOX 40.

    The current question has already been given priority in BOX 40; here
    the context is not reconstructed and textual similarity is not applied.
    Only the values present in resolved_slots are propagated.
    """
    enriched_output = copy.deepcopy(analysis_output)
    question_analysis = enriched_output['question_analysis']
    entities = enriched_output['extracted_entities']
    resolved_slots = retrieval_context.get('resolved_slots', {}) or {}
    inherited_any = bool(resolved_slots.get('inherited_any', False))
    resolved_ticker_slot = resolved_slots.get('ticker', {}) or {}
    resolved_tickers = _unique_strings(resolved_ticker_slot.get('value', []), uppercase=True)
    if not resolved_tickers:
        resolved_tickers = _unique_strings(retrieval_context.get('retrieved_tickers', []), uppercase=True)
    global_ticker_scope = resolved_ticker_slot.get('source') == 'current_question_global_universe'
    if resolved_tickers:
        if global_ticker_scope:
            entities['tickers'] = resolved_tickers.copy()
        else:
            entities['tickers'] = _unique_strings(entities.get('tickers', []) + resolved_tickers, uppercase=True)
    resolved_metric = (resolved_slots.get('metric', {}) or {}).get('value')
    metric_label_map = {'annualized_volatility': 'annualized volatility', 'annual_return': 'annual return', 'return_to_risk_ratio': 'return-to-risk ratio', 'sharpe_ratio': 'sharpe ratio', 'correlation': 'correlation', 'momentum': 'momentum', 'capm_beta': 'beta capm', 'capm_alpha': 'alpha capm', 'capm_expected_return': 'capm expected return'}
    if resolved_metric:
        resolved_metric_label = metric_label_map.get(str(resolved_metric), str(resolved_metric).replace('_', ' '))
        entities['metrics'] = _unique_strings(entities.get('metrics', []) + [resolved_metric_label])
    resolved_concepts = _unique_strings((resolved_slots.get('concepts', {}) or {}).get('value', []))
    correlation_question = 'correlation' in resolved_concepts or str(resolved_metric).strip().lower() == 'correlation'
    if resolved_concepts:
        entities['financial_concepts'] = _unique_strings(entities.get('financial_concepts', []) + resolved_concepts)
    resolved_period = copy.deepcopy((resolved_slots.get('time_period', {}) or {}).get('value'))
    if isinstance(resolved_period, dict):
        period_label = resolved_period.get('label')
        if period_label:
            entities['time_periods'] = _unique_strings(entities.get('time_periods', []) + [period_label])
        if resolved_period.get('type'):
            entities['period_type'] = resolved_period.get('type')
    for sub_question in enriched_output.get('sub_questions', []):
        if resolved_tickers and global_ticker_scope:
            sub_question['referenced_tickers'] = resolved_tickers.copy()
        elif resolved_tickers and (not sub_question.get('referenced_tickers')):
            sub_question['referenced_tickers'] = resolved_tickers.copy()
        if resolved_concepts:
            sub_question['financial_concepts'] = _unique_strings(sub_question.get('financial_concepts', []) + resolved_concepts)
        if 'correlation' in sub_question.get('financial_concepts', []) and isinstance(resolved_period, dict) and (resolved_period.get('type') == 'full_available_dataset'):
            sub_question['time_periods'] = []
            sub_question['period_type'] = 'full_available_dataset'
    if inherited_any:
        question_analysis['uses_retrieved_context'] = True
        core_slots_resolved = bool(resolved_tickers and resolved_metric and (correlation_question or resolved_period))
        if core_slots_resolved:
            question_analysis['requires_clarification'] = False
            question_analysis['clarification_reason'] = None
            if enriched_output.get('question_intent') == 'clarification_required':
                enriched_output['question_intent'] = 'follow_up'
            if question_analysis.get('request_type') == 'ambiguous':
                question_analysis['request_type'] = 'follow_up'
    sub_questions = enriched_output.get('sub_questions', []) or []
    management_commentary_metrics = {'CEO_COMMENTARY', 'CFO_COMMENTARY'}
    absorbed_document_metrics = {'GUIDANCE_OUTLOOK', 'STRATEGY_MILESTONES'}

    def _management_scope_signature(item):
        return (tuple(sorted((str(ticker).strip().upper() for ticker in item.get('referenced_tickers', []) or [] if str(ticker).strip()))), json.dumps(item.get('time_periods', []) or [], ensure_ascii=False, sort_keys=True, default=str))
    management_scopes = {_management_scope_signature(item) for item in sub_questions if str(item.get('metric', '')).strip().upper() in management_commentary_metrics}
    if management_scopes:
        enriched_output['sub_questions'] = [item for item in sub_questions if not (str(item.get('metric', '')).strip().upper() in absorbed_document_metrics and _management_scope_signature(item) in management_scopes)]
    return enriched_output
QUESTION_ANALYSIS_SELF_CHECK_ENABLED = True
QUESTION_ANALYSIS_MAX_RUNS = 3
QUESTION_ANALYSIS_REQUIRED_MAJORITY = 2

def _normalized_sorted_unique(values):
    return sorted({str(value).strip().upper() for value in values or [] if str(value).strip()})

def _normalized_lower_unique(values):
    return sorted({str(value).strip().lower() for value in values or [] if str(value).strip()})

def build_question_analysis_critical_signature(analysis_output: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extracts only the semantically decisive fields.
    Free text does not participate in the vote.
    """
    question_analysis = analysis_output.get('question_analysis', {}) or {}
    entities = analysis_output.get('extracted_entities', {}) or {}
    sub_questions = analysis_output.get('sub_questions', []) or []
    dependencies = sorted([(str(item.get('sub_question_id', '')).strip(), tuple(sorted((str(dep).strip() for dep in item.get('depends_on', []) or [] if str(dep).strip())))) for item in sub_questions])
    return {'question_intent': str(analysis_output.get('question_intent', '')).strip().lower(), 'tickers': _normalized_sorted_unique(entities.get('tickers', [])), 'financial_concepts': _normalized_lower_unique(entities.get('financial_concepts', [])), 'metrics': _normalized_lower_unique(entities.get('metrics', [])), 'time_periods': _normalized_lower_unique(entities.get('time_periods', [])), 'start_date': entities.get('start_date'), 'end_date': entities.get('end_date'), 'period_type': str(entities.get('period_type')).strip().lower() if entities.get('period_type') else None, 'ranking_direction': str(entities.get('ranking_direction')).strip().lower() if entities.get('ranking_direction') is not None else None, 'sub_question_count': len(sub_questions), 'dependencies': dependencies, 'assessment_mode': str(question_analysis.get('assessment_mode', '')).strip().lower(), 'requires_clarification': bool(question_analysis.get('requires_clarification', False)), 'corporate_guidance_references': _normalized_lower_unique(entities.get('corporate_guidance_references', []))}

def compare_question_analysis_signatures(left_signature: Dict[str, Any], right_signature: Dict[str, Any]) -> Dict[str, Any]:
    fields = sorted(set(left_signature) | set(right_signature))
    field_comparison = {field: {'status': 'MATCH' if left_signature.get(field) == right_signature.get(field) else 'DISAGREEMENT', 'left': left_signature.get(field), 'right': right_signature.get(field)} for field in fields}
    return {'all_critical_fields_match': all((item['status'] == 'MATCH' for item in field_comparison.values())), 'field_comparison': field_comparison, 'disagreement_fields': [field for field, item in field_comparison.items() if item['status'] == 'DISAGREEMENT']}

def _signature_key(signature: Dict[str, Any]) -> str:
    """
    Stable representation used exclusively for voting.
    """
    return json.dumps(signature, sort_keys=True, ensure_ascii=False, default=str)

def run_question_analysis_self_consistency(user_prompt: str, compact_retrieval_context: Dict[str, Any]) -> Dict[str, Any]:
    """
    Executes two runs using the same model.
    The third run is triggered only in case of disagreement.
    """
    run_records = []

    def execute_single_run(run_number: int):
        run_start = time.perf_counter()
        raw_output = call_llm_json(system_instruction=QUESTION_ANALYSIS_SYSTEM_INSTRUCTION, user_content=user_prompt, model=QUESTION_ANALYSIS_MODEL, temperature=0.0)
        validated = validate_question_analysis_output(raw_output)
        enriched = enrich_analysis_with_retrieval_context(analysis_output=validated, retrieval_context=compact_retrieval_context)
        signature = build_question_analysis_critical_signature(enriched)
        record = {'run_number': run_number, 'model': QUESTION_ANALYSIS_MODEL, 'status': 'COMPLETED', 'execution_time_seconds': round(time.perf_counter() - run_start, 6), 'signature': signature, 'validated_output': enriched}
        run_records.append(record)
        return record
    run_1 = execute_single_run(1)
    run_2 = execute_single_run(2)
    comparison_1_2 = compare_question_analysis_signatures(run_1['signature'], run_2['signature'])
    comparisons = [{'comparison': 'RUN_1_vs_RUN_2', **comparison_1_2}]
    third_run_triggered = not comparison_1_2['all_critical_fields_match']
    if third_run_triggered:
        run_3 = execute_single_run(3)
        comparisons.extend([{'comparison': 'RUN_1_vs_RUN_3', **compare_question_analysis_signatures(run_1['signature'], run_3['signature'])}, {'comparison': 'RUN_2_vs_RUN_3', **compare_question_analysis_signatures(run_2['signature'], run_3['signature'])}])
    votes = {}
    for record in run_records:
        key = _signature_key(record['signature'])
        votes.setdefault(key, [])
        votes[key].append(record['run_number'])
    winning_key = None
    winning_runs = []
    for key, run_numbers in votes.items():
        if len(run_numbers) >= QUESTION_ANALYSIS_REQUIRED_MAJORITY:
            winning_key = key
            winning_runs = run_numbers
            break
    if winning_key is None:
        raise RuntimeError('Semantic self-check failed: no 2/3 majority on the critical fields.')
    selected_record = next((record for record in run_records if record['run_number'] == winning_runs[0]))
    return {'selected_output': selected_record['validated_output'], 'self_check_report': {'status': 'PASSED', 'model': QUESTION_ANALYSIS_MODEL, 'runs_executed': len(run_records), 'third_run_triggered': third_run_triggered, 'required_majority': QUESTION_ANALYSIS_REQUIRED_MAJORITY, 'winning_runs': winning_runs, 'selected_run': selected_record['run_number'], 'comparisons': comparisons, 'runs': [{'run_number': record['run_number'], 'model': record['model'], 'status': record['status'], 'execution_time_seconds': record['execution_time_seconds'], 'signature': record['signature']} for record in run_records]}}

def resolve_relative_time_periods(user_question: str, analysis_output: Dict[str, Any], reference_date: Any=None) -> Dict[str, Any]:
    """
    Deterministically resolves relative time expressions before
    planning. A rolling interval is represented ONLY ONCE
    through:
        time_periods = ["YYYY-MM-DD/YYYY-MM-DD"]
        start_date
        end_date
        period_type

    Examples:
    - "last year" / "last 12 months" -> rolling 12-month period;
    - "last 3 years" -> rolling 3-year period;
    - "last 2 months" -> rolling 2-month period;
    - "last 2 weeks" -> rolling 2-week period;
    - "last 2 days" -> rolling 2-day period.

    Relative expressions are NOT interpreted as separate calendar years,
    months, or periods.
    """
    output = copy.deepcopy(analysis_output)
    question = str(user_question or '').lower()
    entities = output.setdefault('extracted_entities', {})
    number_words = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12}
    number_pattern = '(?P<value>\\d+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)'
    relative_patterns = [(re.compile(f'\\b(?:over\\s+the|during\\s+the|the)?\\s*last\\s+{number_pattern}\\s+years?\\b'), 'years', 'years'), (re.compile(f'\\b(?:over\\s+the|during\\s+the|the)?\\s*last\\s+{number_pattern}\\s+months?\\b'), 'months', 'months'), (re.compile(f'\\b(?:over\\s+the|during\\s+the|the)?\\s*last\\s+{number_pattern}\\s+weeks?\\b'), 'weeks', 'weeks'), (re.compile(f'\\b(?:over\\s+the|during\\s+the|the)?\\s*last\\s+{number_pattern}\\s+days?\\b'), 'days', 'days')]
    singular_patterns = [(re.compile('\\b(?:over\\s+the\\s+)?last\\s+year\\b'), 1, 'years', 'years'), (re.compile('\\b(?:over\\s+the\\s+)?last\\s+month\\b'), 1, 'months', 'months'), (re.compile('\\b(?:over\\s+the\\s+)?last\\s+week\\b'), 1, 'weeks', 'weeks'), (re.compile('\\b(?:over\\s+the\\s+)?last\\s+day\\b'), 1, 'days', 'days')]
    amount = None
    unit = None
    unit_label = None
    for pattern, candidate_unit, candidate_label in relative_patterns:
        match = pattern.search(question)
        if match:
            raw_value = match.group('value')
            if raw_value.isdigit():
                amount = int(raw_value)
            else:
                amount = number_words.get(raw_value)
            unit = candidate_unit
            unit_label = candidate_label
            break
    if amount is None:
        for pattern, candidate_amount, candidate_unit, candidate_label in singular_patterns:
            if pattern.search(question):
                amount = candidate_amount
                unit = candidate_unit
                unit_label = candidate_label
                break
    if amount is None or unit is None or amount <= 0:
        return output
    end_date = pd.Timestamp(reference_date if reference_date is not None else datetime.now().date()).normalize()
    if unit == 'years':
        start_date = end_date - pd.DateOffset(years=amount)
    elif unit == 'months':
        start_date = end_date - pd.DateOffset(months=amount)
    elif unit == 'weeks':
        start_date = end_date - pd.DateOffset(weeks=amount)
    elif unit == 'days':
        start_date = end_date - pd.DateOffset(days=amount)
    else:
        return output
    start_text = start_date.strftime('%Y-%m-%d')
    end_text = end_date.strftime('%Y-%m-%d')
    canonical_period = f'{start_text}/{end_text}'
    period_type = 'rolling'
    entities['time_periods'] = [canonical_period]
    entities['start_date'] = start_text
    entities['end_date'] = end_text
    entities['period_type'] = period_type
    for sub_question in output.get('sub_questions', []):
        if not isinstance(sub_question, dict):
            continue
        sub_question['time_periods'] = [canonical_period]
        sub_question['start_date'] = start_text
        sub_question['end_date'] = end_text
        sub_question['period_type'] = period_type
    return output

def resolve_result_selection(user_question: str, analysis_output: Dict[str, Any]) -> Dict[str, Any]:
    """Makes the third dimension explicit: all/top_n/bottom_n/winner."""
    output = copy.deepcopy(analysis_output)
    entities = output.setdefault('extracted_entities', {})
    question = str(user_question or '').lower()
    match = re.search('\\btop\\s*(\\d+)\\b|\\b(?:first)\\s+(\\d+)\\b', question)
    if match:
        size = int(next((value for value in match.groups() if value)))
        selection = {'type': 'top_n', 'size': size}
    else:
        match = re.search('\\b(?:last|bottom)\\s*(\\d+)\\b', question)
        if match:
            selection = {'type': 'bottom_n', 'size': int(match.group(1))}
        elif re.search('\\b(?:winner|best|first place|top\\s*1|highest|most correlated)\\b', question):
            selection = {'type': 'winner', 'size': 1}
        else:
            selection = {'type': 'all', 'size': None}
    entities['result_selection'] = selection
    return output

def agent_11_question_analysis(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Semantically analyzes the user's question and produces
    the structure required by the Planner Agent.
    """
    start_time = time.perf_counter()
    user_question = normalize_user_question(state.get('user_question', ''))
    retrieval_context = state.get('retrieval_context', {})
    if not retrieval_context and 'build_retrieval_context' in globals():
        retrieval_context = build_retrieval_context(state=state, question=user_question)
    compact_retrieval_context = prepare_retrieval_context_for_analysis(retrieval_context)
    registry_context = prepare_registry_for_question_analysis(state)
    user_prompt = build_question_analysis_prompt(user_question=user_question, retrieval_context=compact_retrieval_context, registry_context=registry_context)
    try:
        if QUESTION_ANALYSIS_SELF_CHECK_ENABLED:
            self_check_result = run_question_analysis_self_consistency(user_prompt=user_prompt, compact_retrieval_context=compact_retrieval_context)
            validated_output = self_check_result['selected_output']
            self_check_report = self_check_result['self_check_report']
        else:
            raw_output = call_llm_json(system_instruction=QUESTION_ANALYSIS_SYSTEM_INSTRUCTION, user_content=user_prompt, model=QUESTION_ANALYSIS_MODEL, temperature=0.0)
            validated_output = validate_question_analysis_output(raw_output)
            validated_output = enrich_analysis_with_retrieval_context(analysis_output=validated_output, retrieval_context=compact_retrieval_context)
            self_check_report = {'status': 'DISABLED', 'model': QUESTION_ANALYSIS_MODEL, 'runs_executed': 1, 'third_run_triggered': False, 'required_majority': 1, 'winning_runs': [1], 'selected_run': 1, 'comparisons': [], 'runs': []}
        validated_output = resolve_relative_time_periods(user_question=user_question, analysis_output=validated_output)
        validated_output = resolve_result_selection(user_question=user_question, analysis_output=validated_output)
        validated_output = canonicalize_press_release_analysis_metrics(analysis_output=validated_output, retrieval_context=compact_retrieval_context, user_question=user_question)
        validated_output = apply_press_release_document_taxonomy(analysis_output=validated_output, user_question=user_question)
        if isinstance(validated_output, dict):
            _entities = validated_output.get('extracted_entities', {})
            if isinstance(_entities, dict) and isinstance(_entities.get('metrics'), list):
                _entities['metrics'] = [_metric for _metric in _entities['metrics'] if str(_metric).strip().upper() != 'GENERAL_FUNDAMENTAL']
        if isinstance(validated_output, dict):
            _question_lower = str(user_question or '').lower()
            _explicit_compare_across = 'compare' in _question_lower and ('horizon' in _question_lower or 'period' in _question_lower or '6-month' in _question_lower or ('12-month' in _question_lower) or ('2-year' in _question_lower) or ('6 month' in _question_lower) or ('12 month' in _question_lower) or ('2 year' in _question_lower) or ('6m' in _question_lower) or ('12m' in _question_lower) or ('2y' in _question_lower))
            if _explicit_compare_across:
                _entities = validated_output.setdefault('extracted_entities', {})
                _explicit_metric_patterns = {'annualized_return': ('annualized return', 'annualised return'), 'annualized_volatility': ('annualized volatility', 'annualised volatility'), 'sharpe_ratio': ('sharpe ratio',), 'capm_beta': ('capm beta',), 'momentum': ('momentum',)}
                _explicit_metrics = [_metric for _metric, _patterns in _explicit_metric_patterns.items() if any((_pattern in _question_lower for _pattern in _patterns))]
                if len(_explicit_metrics) >= 2:
                    _entities['metrics'] = _unique_strings(_ensure_list(_entities.get('metrics', [])) + _explicit_metrics)
        if isinstance(validated_output, dict):
            _entities = validated_output.setdefault('extracted_entities', {})
            _explicit_periods = extract_retrieval_time_periods(user_question) if 'extract_retrieval_time_periods' in globals() else []
            if _explicit_periods:
                _entities['time_periods'] = _explicit_periods
        validated_output = enforce_atomic_sub_questions(validated_output)
        execution_status = 'completed'
        execution_error = None
    except Exception as error:
        elapsed_time = time.perf_counter() - start_time
        return {'question_analysis': {'summary': '', 'request_type': 'ambiguous', 'is_supported': False, 'requires_clarification': True, 'clarification_reason': 'The semantic analysis was not completed correctly.', 'uses_retrieved_context': False, 'assessment_mode': 'descriptive', 'prediction_boundary': '', 'reasoning_summary': ''}, 'question_intent': 'clarification_required', 'sub_questions': [], 'required_components': [], 'extracted_entities': {'tickers': [], 'company_names': [], 'financial_concepts': [], 'metrics': [], 'time_periods': [], 'comparison_groups': [], 'ranking_direction': None, 'thresholds': [], 'benchmark_references': [], 'contextual_references': [], 'corporate_guidance_references': [], 'assessment_targets': [], 'unsupported_elements': []}, 'question_analysis_status': 'failed', 'question_analysis_error': str(error), 'question_analysis_execution_time_seconds': round(elapsed_time, 6), 'question_analysis_model': QUESTION_ANALYSIS_MODEL, 'question_analysis_self_check': {'status': 'FAILED', 'model': QUESTION_ANALYSIS_MODEL, 'error': str(error), 'runs_executed': 0, 'third_run_triggered': False, 'winning_runs': [], 'comparisons': [], 'runs': []}, 'current_question_node': 'question_analysis', 'question_workflow_status': 'analysis_failed', 'next_node': 'END'}
    elapsed_time = time.perf_counter() - start_time
    return {**validated_output, 'question_analysis_status': execution_status, 'question_analysis_error': execution_error, 'question_analysis_execution_time_seconds': round(elapsed_time, 6), 'question_analysis_model': QUESTION_ANALYSIS_MODEL, 'question_analysis_self_check': self_check_report, 'current_question_node': 'question_analysis', 'question_workflow_status': 'analyzed', 'next_node': 'planning'}
question_analysis_node = agent_11_question_analysis
final_state.setdefault('question_analysis', {})
final_state.setdefault('question_intent', '')
final_state.setdefault('sub_questions', [])
final_state.setdefault('extracted_entities', {})
final_state.setdefault('question_analysis_status', 'not_started')
final_state.setdefault('question_analysis_error', None)
final_state.setdefault('question_analysis_execution_time_seconds', 0.0)
final_state.setdefault('question_analysis_model', QUESTION_ANALYSIS_MODEL)
final_state.setdefault('question_analysis_self_check', {})
_original_build_atomic_required_components_box41 = build_atomic_required_components

def build_atomic_required_components(analysis_output: Dict[str, Any]) -> List[Dict[str, Any]]:
    components = _original_build_atomic_required_components_box41(analysis_output)
    for component in components:
        if not isinstance(component, dict):
            continue
        metric = canonical_metric_name(component.get('metric'))
        period = canonical_time_period(component.get('time_period'))
        tickers = component.get('referenced_tickers') or ([component.get('ticker')] if component.get('ticker') else [])
        component['metric'] = metric
        component['time_period'] = period or component.get('time_period')
        component['time_periods'] = [period] if period else []
        component['atomic_id'] = build_atomic_id('', tickers, metric, period)
        component['atomic_identity'] = {'tickers': sorted({str(x).upper() for x in tickers if x}), 'metric': metric, 'time_period': period}
    return components

def build_requirement_atoms_from_components(required_components: Any) -> List[Dict[str, Any]]:
    atoms = []
    seen = set()
    for component in required_components or []:
        if not isinstance(component, dict):
            continue
        metric = canonical_metric_name(component.get('metric'))
        periods = component.get('time_periods') or ([component.get('time_period')] if component.get('time_period') else [None])
        tickers = component.get('referenced_tickers') or ([component.get('ticker')] if component.get('ticker') else [None])
        for ticker in tickers or [None]:
            for period in periods or [None]:
                atom = build_requirement_atom(ticker, metric, period, component.get('component_id'))
                rid = atom['requirement_id']
                if rid in seen:
                    continue
                seen.add(rid)
                atoms.append(atom)
    return atoms
_original_agent_11_question_analysis_requirement_atoms = agent_11_question_analysis

def agent_11_question_analysis(state: Dict[str, Any]) -> Dict[str, Any]:
    _dd_question = state.get('user_question') or state.get('question') or state.get('normalized_question') or ''
    _dd_check = dual_domain_question_check(_dd_question)
    if _dd_check['active']:
        state['dual_domain_check'] = _dd_check
        state['dual_domain_internal_report'] = dual_domain_internal_report(_dd_check)
    result = _original_agent_11_question_analysis_requirement_atoms(state)
    atoms = build_requirement_atoms_from_components(result.get('required_components') or [])
    result['requirement_atoms'] = atoms
    result['required_requirement_ids'] = [a['requirement_id'] for a in atoms]
    if _dd_check['active']:
        result['dual_domain_check'] = _dd_check
        result['dual_domain_internal_report'] = state['dual_domain_internal_report']
    return result
question_analysis_node = agent_11_question_analysis
if 'AGENT_REGISTRY' in globals() and 'question_analysis_agent' in AGENT_REGISTRY:
    try:
        AGENT_REGISTRY['question_analysis_agent']['function'] = agent_11_question_analysis
    except Exception:
        pass

def dual_domain_post_validation_check(state):
    plan = [s for s in state.get('execution_plan') or [] if isinstance(s, dict)]
    selected = [e for e in state.get('selected_evidence') or [] if isinstance(e, dict)]
    step_tickers = {}
    required = []
    for step in plan:
        if str(step.get('selected_tool') or step.get('tool_name') or '').lower() != 'press_release_fy2025':
            continue
        tickers = step.get('referenced_tickers') or step.get('tickers') or []
        if isinstance(tickers, str):
            tickers = [tickers]
        tickers = [str(t).strip().upper() for t in tickers if str(t).strip()]
        step_tickers[step.get('step_id')] = tickers
        for ticker in tickers:
            if ticker not in required:
                required.append(ticker)
    flags = {ticker: 0 for ticker in required}
    ids = {ticker: [] for ticker in required}
    for ev in selected:
        if str(ev.get('selected_tool') or '').lower() != 'press_release_fy2025' or ev.get('output_name') != 'press_release_result':
            continue
        value = ev.get('value')
        if isinstance(value, dict):
            payload = str(value.get('evidence_text') or '')
            verified = bool(payload.strip())
        else:
            payload = ''
            verified = False
        if not payload.strip() or not verified:
            continue
        tickers = step_tickers.get(ev.get('step_id'), [])
        if not tickers:
            tickers = ev.get('referenced_tickers') or []
        if isinstance(tickers, str):
            tickers = [tickers]
        for ticker in tickers:
            ticker = str(ticker).strip().upper()
            if ticker in flags:
                flags[ticker] = 1
                ids[ticker].append(ev.get('evidence_id'))
    entry = state.get('dual_domain_check') or {}
    requested_matrix = [item for item in entry.get('tool_request_matrix') or [] if isinstance(item, dict) and item.get('requested') == 1] if entry.get('active') else []
    tool_rows = []
    for item in requested_matrix:
        tool = str(item.get('tool') or '')
        metric = str(item.get('metric') or '')
        matched_ids = []
        for ev in selected:
            ev_tool = str(ev.get('selected_tool') or ev.get('tool_name') or ev.get('tool') or '')
            if ev_tool != tool:
                continue
            value = ev.get('value')
            if value is None or value == '' or value == {} or (value == []):
                continue
            if tool == 'press_release_fy2025':
                if ev.get('output_name') != 'press_release_result':
                    continue
                content = [value] if isinstance(value, dict) and str(value.get('evidence_text') or '').strip() else []
                if not content:
                    continue
            evidence_metric = str(ev.get('metric') or ev.get('output_name') or '')
            metric_fields = set()
            if isinstance(value, dict):
                metric_fields.update((str(k).casefold() for k in value))
                for nested_key in ('metrics', 'indicators', 'data', 'results', 'records'):
                    nested = value.get(nested_key)
                    if isinstance(nested, dict):
                        metric_fields.update((str(k).casefold() for k in nested))
                    elif isinstance(nested, list):
                        for record in nested:
                            if isinstance(record, dict):
                                metric_fields.update((str(k).casefold() for k in record))
                                for key in ('metric', 'metric_name', 'indicator', 'name'):
                                    if record.get(key):
                                        metric_fields.add(str(record[key]).casefold())
            metric_match = metric.casefold() == evidence_metric.casefold() or metric.casefold() in metric_fields
            if tool == 'press_release_fy2025':
                canonical = str(metric).strip().upper()
                metric_match = any((canonical in {str(record.get(key) or '').strip().upper() for key in ('requested_metric', 'matched_metric', 'metric', 'category', 'information_type')} for record in content))
            if metric_match:
                matched_ids.append(ev.get('evidence_id') or ev.get('step_id'))
        tool_rows.append({'tool': tool, 'metric': metric, 'domain': item.get('domain'), 'requested': 1, 'retrieved': int(bool(matched_ids)), 'evidence_ids': [v for v in matched_ids if v is not None]})
    coverage = []
    for step in plan:
        tool = str(step.get('selected_tool') or step.get('tool_name') or '')
        if not tool:
            continue
        metric = str(step.get('metric') or (step.get('tool_parameters') or {}).get('metric') or '')
        tickers = step.get('referenced_tickers') or step.get('tickers') or []
        if isinstance(tickers, str):
            tickers = [tickers]
        periods = step.get('time_periods') or [None]
        if not isinstance(periods, list):
            periods = [periods]
        for ticker in tickers:
            ticker = str(ticker).strip().upper()
            if not ticker:
                continue
            for period in periods:
                matches = []
                for ev in selected:
                    if str(ev.get('step_id') or '') != str(step.get('step_id') or ''):
                        continue
                    if str(ev.get('selected_tool') or ev.get('tool_name') or '') != tool:
                        continue
                    value = ev.get('value')
                    if value is None or value == '' or value == {} or (value == []):
                        continue
                    if tool == 'press_release_fy2025':
                        if ev.get('output_name') != 'press_release_result':
                            continue
                        if not (isinstance(value, dict) and str(value.get('evidence_text') or '').strip() and (str(value.get('matched_metric') or '').upper() == metric.upper())):
                            continue
                    matches.append(ev.get('evidence_id') or ev.get('step_id'))
                coverage.append({'step_id': step.get('step_id'), 'ticker': ticker, 'tool': tool, 'metric': metric, 'period': period, 'retrieved': int(bool(matches)), 'evidence_ids': matches})
    return {'ticker_metric_period_coverage': coverage, 'all_ticker_metric_period_retrieved': int(all((r['retrieved'] for r in coverage))) if coverage else None, 'tool_evidence_retrieved': tool_rows, 'all_requested_tools_retrieved': int(all((row['retrieved'] for row in tool_rows))) if tool_rows else None, 'active': bool(required), 'document_retrieved': flags, 'all_documents_retrieved': int(all(flags.values())) if required else None, 'document_evidence_ids': ids, 'checked_tickers': required, 'definition': '1 = non-empty press_release_result evidence selected for the ticker; 0 = absent'}
QUESTION_PLANNING_AGENT_NAME = 'question_planning_agent'
QUESTION_PLANNING_AGENT_NUMBER = 12
QUESTION_PLANNING_MODEL = MAIN_MODEL
DETERMINISTIC_EXECUTOR_NODE_NAME = 'deterministic_tool_executor_node'
MAX_PLAN_STEPS = None
MAX_PLANNING_TOOLS = None
CONCEPT_TOOL_MAP = {'return': ['financial_metrics'], 'risk': ['financial_metrics'], 'sharpe': ['financial_metrics'], 'correlation': ['pearson_correlation'], 'volume': ['momentum'], 'benchmark': ['capm_beta', 'capm_alpha', 'capm_expected_return', 'financial_metrics'], 'momentum': ['momentum'], 'capm': ['capm_beta', 'capm_alpha', 'capm_expected_return'], 'fundamental': ['press_release_fy2025'], 'data_quality': []}
PROMISING_COMPOSITE_CRITERIA = {'criterion_name': 'transparent_multi_metric_consensus', 'description': 'Independent rankings for each metric, followed by consensus and counter-evidence. No opaque composite score.', 'preferred_components': [{'label': 'Annual Return', 'concept': 'return', 'tool': 'financial_metrics', 'metrics': ['annualized_return'], 'default_horizon': '10Y', 'direction': 'higher_is_better'}, {'label': 'Sharpe Ratio', 'concept': 'sharpe', 'tool': 'financial_metrics', 'metrics': ['sharpe_ratio'], 'default_horizon': '10Y', 'direction': 'higher_is_better'}, {'label': 'Return-to-Risk Ratio', 'concept': 'return', 'tool': 'financial_metrics', 'metrics': ['return_to_risk_ratio'], 'default_horizon': '10Y', 'direction': 'higher_is_better'}, {'label': 'Volatility', 'concept': 'risk', 'tool': 'financial_metrics', 'metrics': ['annualized_volatility'], 'default_horizon': '10Y', 'direction': 'lower_is_better'}, {'label': 'CAPM Alpha', 'concept': 'capm', 'tool': 'capm_alpha', 'metrics': ['capm_alpha'], 'default_horizon': '10Y', 'direction': 'higher_is_better'}, {'label': 'CAPM Expected Return', 'concept': 'capm', 'tool': 'capm_expected_return', 'metrics': ['capm_expected_return'], 'default_horizon': '10Y', 'direction': 'higher_is_better'}, {'label': 'Momentum', 'concept': 'momentum', 'tool': 'momentum', 'metrics': ['momentum', 'momentum_rank'], 'default_horizon': '12M', 'direction': 'higher_is_better'}], 'default_selection_size': 3, 'consensus_method': 'count_top_n_occurrences', 'confutation_method': 'report_metric_disagreements', 'documentary_policy': 'Exclude documentary analysis from generic quantitative rankings; allow only explicit documentary KPI or prospective guidance assessment.'}
ORCHESTRATION_PARAMETER_KEYS = {'tickers', 'time_periods', 'start_date', 'end_date', 'period_type', 'evidence_rows', 'top_n', 'ranking_criterion', 'question', 'ticker', 'time_period', 'metric', 'component_id'}

def _planner_ensure_list(value: Any) -> List[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, (tuple, set)):
        return list(value)
    return [value]

def _planner_unique_strings(values: Any, uppercase: bool=False) -> List[str]:
    normalized_values = []
    seen_values = set()
    for value in _planner_ensure_list(values):
        if value is None:
            continue
        normalized_value = re.sub('\\s+', ' ', str(value).strip())
        if not normalized_value:
            continue
        if uppercase:
            normalized_value = normalized_value.upper()
        comparison_value = normalized_value.lower()
        if comparison_value in seen_values:
            continue
        seen_values.add(comparison_value)
        normalized_values.append(normalized_value)
    return normalized_values

def _planner_is_empty_value(value: Any) -> bool:
    if value is None:
        return True
    if isinstance(value, (str, bytes, list, tuple, set, dict)):
        return len(value) == 0
    if hasattr(value, 'empty'):
        try:
            return bool(value.empty)
        except Exception:
            return False
    return False

def normalize_time_periods(values: Any) -> List[str]:
    """
    Normalizes periods without transforming exact intervals into years.
    Supported canonical forms:
      - YYYY
      - YYYY-YYYY
      - YYYY-MM-DD/YYYY-MM-DD
      - other temporal labels already produced by BOX 41
    """
    normalized = []
    for value in _planner_ensure_list(values):
        if value is None:
            continue
        if isinstance(value, dict):
            normalized.append(copy.deepcopy(value))
            continue
        text = re.sub('\\s+', ' ', str(value).strip())
        if not text:
            continue
        exact_match = re.fullmatch('(\\d{4}-\\d{2}-\\d{2})\\s*/\\s*(\\d{4}-\\d{2}-\\d{2})', text)
        if exact_match:
            start = pd.Timestamp(exact_match.group(1)).strftime('%Y-%m-%d')
            end = pd.Timestamp(exact_match.group(2)).strftime('%Y-%m-%d')
            text = f'{start}/{end}'
        if text not in normalized:
            normalized.append(text)
    return normalized

def extract_exact_date_range(time_periods: Sequence[Any], extracted_entities: Dict[str, Any]=None, state: Dict[str, Any]=None) -> Tuple[Optional[str], Optional[str]]:
    """
    Resolves the time interval to pass to the tools.

    Priority:
    1. explicit start_date/end_date;
    2. ISO interval YYYY-MM-DD/YYYY-MM-DD;
    3. structured rolling period retrieved from retrieval;
    4. rolling period expressed in natural language
       (e.g. "last 3 years", "last 2 months").

    For a rolling period, the end date coincides with the latest
    observation available in log_returns.
    """
    entities = extracted_entities if isinstance(extracted_entities, dict) else {}
    working_state = state if isinstance(state, dict) else {}
    start_date = entities.get('start_date')
    end_date = entities.get('end_date')
    if start_date and end_date:
        try:
            start = pd.Timestamp(start_date).normalize()
            end = pd.Timestamp(end_date).normalize()
            if start <= end:
                return (start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d'))
        except Exception:
            pass
    for period in _planner_ensure_list(time_periods):
        match = re.fullmatch('\\s*(\\d{4}-\\d{2}-\\d{2})\\s*/\\s*(\\d{4}-\\d{2}-\\d{2})\\s*', str(period))
        if match:
            start = pd.Timestamp(match.group(1)).normalize()
            end = pd.Timestamp(match.group(2)).normalize()
            if start <= end:
                return (start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d'))
    reference_end = None
    state_log_returns = working_state.get('log_returns')
    if isinstance(state_log_returns, pd.DataFrame) and (not state_log_returns.empty) and isinstance(state_log_returns.index, pd.DatetimeIndex):
        reference_end = pd.Timestamp(state_log_returns.index.max()).normalize()
    if reference_end is None:
        reference_end = pd.Timestamp.now().normalize()
    rolling_candidates = []
    rolling_candidates.extend(_planner_ensure_list(time_periods))
    for key in ['time_period', 'rolling_period']:
        if entities.get(key) is not None:
            rolling_candidates.append(entities.get(key))
    rolling_candidates.extend(_planner_ensure_list(entities.get('time_periods', [])))
    retrieval_context = working_state.get('retrieval_context', {})
    if isinstance(retrieval_context, dict):
        resolved_slots = retrieval_context.get('resolved_slots', {})
        if isinstance(resolved_slots, dict):
            resolved_time_period = resolved_slots.get('time_period', {})
            if isinstance(resolved_time_period, dict):
                resolved_time_period = resolved_time_period.get('value')
            if resolved_time_period is not None and (not (isinstance(resolved_time_period, dict) and resolved_time_period.get('type') == 'full_available_dataset')):
                rolling_candidates.append(resolved_time_period)

    def resolve_rolling_candidate(candidate: Any) -> Optional[Tuple[str, str]]:
        value = None
        unit = None
        if isinstance(candidate, dict):
            candidate_type = str(candidate.get('type', '')).strip().lower()
            if candidate_type and candidate_type != 'rolling':
                return None
            value = candidate.get('value')
            unit = candidate.get('unit')
            if isinstance(value, str):
                compact_value = value.strip().lower()
                compact_match = re.fullmatch('(\\d+)[_\\-\\s]*(years|year|months|month|weeks|week|days|day|y|yr|yrs|mo|mos|m|w|wk|wks|d)', compact_value, flags=re.IGNORECASE)
                if compact_match:
                    value = compact_match.group(1)
                    unit = compact_match.group(2)
        else:
            text = re.sub('\\s+', ' ', str(candidate).strip().lower())
            patterns = ['(?:last|past)\\s+(\\d+)\\s+(years|year|months|month|weeks|week|days|day)', '(?:over\\s+the\\s+last|in\\s+the\\s+last)\\s+(\\d+)\\s+(years|year|months|month|weeks|week|days|day)', '\\b(\\d+)[_\\-\\s]*(years|year|months|month|weeks|week|days|day|y|yr|yrs|mo|mos|m|w|wk|wks|d)\\b']
            match = None
            for pattern in patterns:
                match = re.search(pattern, text, flags=re.IGNORECASE)
                if match:
                    break
            if not match:
                return None
            value = match.group(1)
            unit = match.group(2)
        try:
            value = int(value)
        except (TypeError, ValueError):
            return None
        if value <= 0:
            return None
        unit_text = str(unit).strip().lower()
        if unit_text in {'years', 'year', 'y', 'yr', 'yrs'}:
            offset = pd.DateOffset(years=value)
        elif unit_text in {'months', 'month', 'm', 'mo', 'mos'}:
            offset = pd.DateOffset(months=value)
        elif unit_text in {'weeks', 'week', 'w', 'wk', 'wks'}:
            offset = pd.DateOffset(weeks=value)
        elif unit_text in {'days', 'day', 'd'}:
            offset = pd.DateOffset(days=value)
        else:
            return None
        rolling_start = (reference_end - offset).normalize()
        return (rolling_start.strftime('%Y-%m-%d'), reference_end.strftime('%Y-%m-%d'))
    for candidate in rolling_candidates:
        resolved_range = resolve_rolling_candidate(candidate)
        if resolved_range is not None:
            return resolved_range
    return (None, None)

def build_requested_result_signature(tool_name: str, tickers: Sequence[str], time_periods: Sequence[str], parameters: Dict[str, Any]) -> Dict[str, Any]:
    """
    Builds the signature requested by the plan.
    """
    return {'tool_name': tool_name, 'tickers': sorted(_planner_unique_strings(tickers, uppercase=True)), 'time_periods': sorted(normalize_time_periods(time_periods), key=lambda period: str(period)), 'parameters': {key: parameters[key] for key in sorted(parameters) if key not in {'tickers', 'time_periods'}}}

def get_stored_result_signature(state: Dict[str, Any], tool_name: str, requested_signature: Optional[Dict[str, Any]]=None) -> Dict[str, Any]:
    """
    Retrieves the signature stored by the tool, when available.

    If requested_signature is present, first searches persistent results from the same tool for a signature with the same time horizon and compatible ticker coverage. If no persistent match is found, preserves the historical fallback to final_state["tool_result_signatures"][tool_name].
    """
    if isinstance(requested_signature, dict):
        persistent_results = state.get('tool_results_by_key', {})
        if isinstance(persistent_results, dict):
            requested_period = _planner_semantic_time_period(requested_signature)
            requested_tickers = set(_planner_unique_strings(requested_signature.get('tickers', []), uppercase=True))
            persistent_entries = list(persistent_results.values())
            for entry in reversed(persistent_entries):
                if not isinstance(entry, dict):
                    continue
                if str(entry.get('tool_name', '')).strip() != tool_name:
                    continue
                candidate_signature = entry.get('result_signature', {})
                if not isinstance(candidate_signature, dict) or not candidate_signature:
                    continue
                candidate_period = _planner_semantic_time_period(candidate_signature)
                if requested_period and candidate_period and (requested_period != candidate_period):
                    continue
                candidate_tickers = set(_planner_unique_strings(candidate_signature.get('tickers', []), uppercase=True))
                if requested_tickers and candidate_tickers and (not requested_tickers & candidate_tickers):
                    continue
                return copy.deepcopy(candidate_signature)
    signatures = state.get('tool_result_signatures', {})
    if not isinstance(signatures, dict):
        return {}
    signature = signatures.get(tool_name, {})
    return signature if isinstance(signature, dict) else {}

def build_reuse_instrument_signature(signature: Dict[str, Any]) -> Dict[str, Any]:
    """
    Instrument identity independent of ticker scope.
    """
    return {key: copy.deepcopy(value) for key, value in signature.items() if key != 'tickers'}

def is_result_signature_compatible(requested_signature: Dict[str, Any], stored_signature: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """
    Verifies compatibility of instrument, period, and parameters.
    The ticker scope is decomposable: partial coverage is sufficient
    to reuse the portion already available.
    """
    reasons = []
    if not stored_signature:
        return (False, ['Result signature not available.'])
    requested_instrument_signature = build_reuse_instrument_signature(requested_signature)
    stored_instrument_signature = build_reuse_instrument_signature(stored_signature)
    if requested_instrument_signature != stored_instrument_signature:
        reasons.append('Instrument, period, or parameters are not compatible.')
    requested_tickers = set(requested_signature.get('tickers', []))
    stored_tickers = set(stored_signature.get('tickers', []))
    if requested_tickers and stored_tickers and (not requested_tickers & stored_tickers):
        reasons.append('None of the requested tickers are covered by the stored result.')
    stored_validation = stored_signature.get('validation_status', 'UNKNOWN')
    if stored_validation not in {'PASSED', 'CERTIFIED'}:
        reasons.append('The result is not validated or certified.')
    return (not reasons, reasons)

def _planner_semantic_time_period(signature: Optional[Dict[str, Any]]) -> Optional[str]:
    """
    Normalizes the horizon used for result recognition.
    """
    if not isinstance(signature, dict):
        return None
    parameters = signature.get('parameters', {})
    if not isinstance(parameters, dict):
        parameters = {}
    formation_months = parameters.get('formation_period_months')
    if formation_months is not None:
        try:
            return f'{int(formation_months)}M'
        except (TypeError, ValueError):
            return str(formation_months)
    time_periods = signature.get('time_periods', [])
    if time_periods:
        return _planner_canonical_time_period_value(time_periods[0])
    if parameters.get('start_date') and parameters.get('end_date'):
        return f"{parameters.get('start_date')}/{parameters.get('end_date')}"
    return None

def _planner_semantic_result_match(tool_name: str, requested_signature: Optional[Dict[str, Any]], stored_signature: Optional[Dict[str, Any]], available_outputs: Sequence[str]) -> Tuple[bool, List[str]]:
    """
    Checks whether the requested result is already available.

    Ordinary recognition uses the tool, requested output,
    and time horizon.
    The tickers contained in the ranking and the validation status are not
    used as primary semantic keys.
    """
    if not available_outputs:
        return (False, ['Requested output not available.'])
    if not isinstance(stored_signature, dict) or not stored_signature:
        return (False, ['Description of the previous result not available.'])
    stored_tool = str(stored_signature.get('tool_name', tool_name)).strip()
    if stored_tool and stored_tool != tool_name:
        return (False, ['The tool of the previous result is different.'])
    requested_period = _planner_semantic_time_period(requested_signature)
    stored_period = _planner_semantic_time_period(stored_signature)
    if requested_period and stored_period and (requested_period != stored_period):
        return (False, ['Different time horizon.'])
    return (True, [])

def _planner_canonical_time_period_value(value: Any) -> Optional[str]:
    """
    Canonicalizes rolling periods from both new requests and historical result_signature values.

    Equivalent examples:
      - "6M"
      - {"type": "rolling", "value": 6, "unit": "month"}
      - "{'type': 'rolling', 'value': 6, 'unit': 'month'}"

    all become "6M".
    """
    if value is None:
        return None
    if isinstance(value, dict):
        period_type = str(value.get('period_type') or value.get('type') or '').strip().lower()
        raw_value = value.get('time_value') if value.get('time_value') is not None else value.get('value')
        raw_unit = str(value.get('time_unit') or value.get('unit') or '').strip().lower()
        if period_type == 'rolling' and raw_value is not None:
            unit_map = {'m': 'M', 'month': 'M', 'months': 'M', 'mese': 'M', 'mesi': 'M', 'y': 'Y', 'year': 'Y', 'years': 'Y', 'anno': 'Y', 'anni': 'Y', 'd': 'D', 'day': 'D', 'days': 'D', 'giorno': 'D', 'giorni': 'D'}
            canonical_unit = unit_map.get(raw_unit)
            if canonical_unit:
                try:
                    return f'{int(raw_value)}{canonical_unit}'
                except (TypeError, ValueError):
                    pass
    text = re.sub('\\s+', ' ', str(value).strip())
    if not text:
        return None
    direct_match = re.fullmatch('(\\d+)\\s*([MmYyDd])', text)
    if direct_match:
        return f'{int(direct_match.group(1))}{direct_match.group(2).upper()}'
    rolling_type_match = re.search('[\'\\"](?:period_type|type)[\'\\"]\\s*:\\s*[\'\\"]rolling[\'\\"]', text, flags=re.IGNORECASE)
    value_match = re.search('[\'\\"](?:time_value|value)[\'\\"]\\s*:\\s*(\\d+)', text, flags=re.IGNORECASE)
    unit_match = re.search('[\'\\"](?:time_unit|unit)[\'\\"]\\s*:\\s*[\'\\"]([^\'\\"]+)[\'\\"]', text, flags=re.IGNORECASE)
    if rolling_type_match and value_match and unit_match:
        unit_map = {'m': 'M', 'month': 'M', 'months': 'M', 'mese': 'M', 'mesi': 'M', 'y': 'Y', 'year': 'Y', 'years': 'Y', 'anno': 'Y', 'anni': 'Y', 'd': 'D', 'day': 'D', 'days': 'D', 'giorno': 'D', 'giorni': 'D'}
        canonical_unit = unit_map.get(unit_match.group(1).strip().lower())
        if canonical_unit:
            return f'{int(value_match.group(1))}{canonical_unit}'
    return text

def _planner_semantic_time_period(signature: Optional[Dict[str, Any]]) -> Optional[str]:
    """
    Normalizes the time horizon used for result recognition.
    """
    if not isinstance(signature, dict):
        return None
    parameters = signature.get('parameters', {})
    if not isinstance(parameters, dict):
        parameters = {}
    formation_months = parameters.get('formation_period_months')
    if formation_months is not None:
        try:
            return f'{int(formation_months)}M'
        except (TypeError, ValueError):
            return str(formation_months)
    time_periods = signature.get('time_periods', [])
    if time_periods:
        return _planner_canonical_time_period_value(time_periods[0])
    if parameters.get('start_date') and parameters.get('end_date'):
        return f"{parameters.get('start_date')}/{parameters.get('end_date')}"
    return None

def _planner_semantic_result_match(tool_name: str, requested_signature: Optional[Dict[str, Any]], stored_signature: Optional[Dict[str, Any]], available_outputs: Sequence[str]) -> Tuple[bool, List[str]]:
    """
    Checks whether the requested result is already available.

    Standard matching uses the tool, requested output,
    and time horizon.
    Tickers included in the ranking and validation status are not
    used as primary semantic keys.
    """
    if not available_outputs:
        return (False, ['Requested output unavailable.'])
    if not isinstance(stored_signature, dict) or not stored_signature:
        return (False, ['Previous result description unavailable.'])
    stored_tool = str(stored_signature.get('tool_name', tool_name)).strip()
    if stored_tool and stored_tool != tool_name:
        return (False, ['Previous result uses a different tool.'])
    requested_period = _planner_semantic_time_period(requested_signature)
    stored_period = _planner_semantic_time_period(stored_signature)
    if requested_period and stored_period and (requested_period != stored_period):
        return (False, ['Different time horizon.'])
    return (True, [])

def inspect_tool_output_availability(state: Dict[str, Any], tool_name: str, tool_registry: Dict[str, Dict[str, Any]], requested_signature: Optional[Dict[str, Any]]=None) -> Dict[str, Any]:
    """
    Checks output availability and compatibility.
    """
    metadata = tool_registry.get(tool_name, {})
    output_fields = list(metadata.get('output_fields', []))
    available_outputs = []
    missing_outputs = []
    for output_field in output_fields:
        if output_field in state and (not _planner_is_empty_value(state[output_field])):
            available_outputs.append(output_field)
        else:
            missing_outputs.append(output_field)
    stored_signature = get_stored_result_signature(state=state, tool_name=tool_name, requested_signature=requested_signature)
    signature_compatible = False
    semantic_compatible = False
    incompatibility_reasons = []
    match_source = None
    if requested_signature:
        semantic_compatible, semantic_reasons = _planner_semantic_result_match(tool_name=tool_name, requested_signature=requested_signature, stored_signature=stored_signature, available_outputs=available_outputs)
        if semantic_compatible:
            signature_compatible = True
            incompatibility_reasons = []
            match_source = 'semantic_catalog'
        else:
            signature_compatible, incompatibility_reasons = is_result_signature_compatible(requested_signature=requested_signature, stored_signature=stored_signature)
            if signature_compatible:
                match_source = 'technical_signature'
            elif not incompatibility_reasons:
                incompatibility_reasons = semantic_reasons
    return {'tool_name': tool_name, 'expected_outputs': output_fields, 'available_outputs': available_outputs, 'missing_outputs': missing_outputs, 'all_outputs_available': bool(output_fields) and (not missing_outputs), 'stored_signature': stored_signature, 'signature_compatible': signature_compatible, 'semantic_compatible': semantic_compatible, 'match_source': match_source, 'incompatibility_reasons': incompatibility_reasons, 'reusable': bool(output_fields) and (not missing_outputs) and signature_compatible}

def build_planning_tool_catalog(state: Dict[str, Any], tool_registry: Dict[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
    compact_catalog = []
    for tool_name, metadata in list(tool_registry.items()):
        compact_catalog.append({'tool_name': tool_name, 'component_type': metadata.get('component_type', ''), 'description': metadata.get('description', ''), 'required_state_fields': list(metadata.get('required_state_fields', [])), 'output_fields': list(metadata.get('output_fields', [])), 'optional_parameters': copy.deepcopy(metadata.get('optional_parameters', {})), 'uses_external_source': bool(metadata.get('uses_external_source', False))})
    return compact_catalog

def validate_tool_parameters(tool_name: str, proposed_parameters: Any, tool_registry: Dict[str, Dict[str, Any]]) -> Tuple[Dict[str, Any], List[str]]:
    """
    Keeps only parameters declared by the tool or standard
    orchestration parameters.
    """
    metadata = tool_registry.get(tool_name, {})
    defaults = copy.deepcopy(metadata.get('optional_parameters', {}))
    proposed_parameters = proposed_parameters if isinstance(proposed_parameters, dict) else {}
    allowed_keys = set(defaults) | ORCHESTRATION_PARAMETER_KEYS
    rejected_keys = sorted(set(proposed_parameters) - allowed_keys)
    validated_parameters = {**defaults, **{key: value for key, value in proposed_parameters.items() if key in allowed_keys and (not (key in defaults and defaults.get(key) is not None and (value is None or (isinstance(value, str) and value.strip().lower() in {'', 'none', 'null'}))))}}
    return (validated_parameters, rejected_keys)

def get_allowed_tools_for_concepts(concepts: Sequence[str], tool_registry: Dict[str, Dict[str, Any]]) -> List[str]:
    allowed_tools = []
    for concept in concepts:
        for tool_name in CONCEPT_TOOL_MAP.get(str(concept), []):
            if tool_name in tool_registry and tool_name not in allowed_tools:
                allowed_tools.append(tool_name)
    return allowed_tools

def resolve_tool_routing(proposed_tool: Optional[str], concepts: Sequence[str], tool_registry: Dict[str, Dict[str, Any]]) -> Tuple[Optional[str], Optional[Dict[str, Any]]]:
    """
    Corrects routing without hiding the correction.
    """
    allowed_tools = get_allowed_tools_for_concepts(concepts=concepts, tool_registry=tool_registry)
    if proposed_tool and proposed_tool in allowed_tools:
        return (proposed_tool, None)
    if proposed_tool and proposed_tool in tool_registry and (not allowed_tools):
        return (proposed_tool, None)
    if len(allowed_tools) == 1:
        selected_tool = allowed_tools[0]
        return (selected_tool, {'proposed_tool': proposed_tool, 'selected_tool': selected_tool, 'reason': 'Routing corrected through a unique match between the concept and the registered tool.'})
    return (None, {'proposed_tool': proposed_tool, 'selected_tool': None, 'reason': 'No unique match was found. The step requires review.'})

def resolve_tool_from_required_outputs(required_outputs: Sequence[str], tool_registry: Dict[str, Dict[str, Any]]) -> Tuple[Optional[str], List[str]]:
    """
    Finds the tool that can produce all requested outputs.

    Correction is allowed only when there is a single
    compatible producer in TOOL_REGISTRY.
    """
    requested = set(_planner_unique_strings(required_outputs))
    if not requested:
        return (None, [])
    candidates = []
    for tool_name, metadata in tool_registry.items():
        if not isinstance(metadata, dict):
            continue
        produced = set(_planner_unique_strings(metadata.get('output_fields', [])))
        if requested.issubset(produced):
            candidates.append(tool_name)
    return (candidates[0] if len(candidates) == 1 else None, candidates)

def detect_promising_request(state: Dict[str, Any]) -> bool:
    question_text = ' '.join([str(state.get('user_question', '')), str(state.get('question_analysis', {}).get('summary', ''))]).lower()
    indicators = {'most promising', 'best opportunities', 'best stocks', 'best shares', 'best', 'worst', 'least promising', 'strongest', 'weakest'}
    return any((indicator in question_text for indicator in indicators))

def build_promising_selection_steps(state: Dict[str, Any], tool_registry: Dict[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Creates the steps required for a multi-factor ranking.
    """
    steps = []
    priority = 1
    for component in PROMISING_COMPOSITE_CRITERIA['preferred_components']:
        tool_name = component['tool']
        if tool_name not in tool_registry:
            continue
        steps.append({'step_id': f'PROMISING_{priority}', 'sub_question_id': 'PROMISING_SELECTION', 'action_type': 'execute_tool', 'objective': f"Calculate the {component['concept']} component of the ranking.", 'selected_tool': tool_name, 'required_outputs': list(tool_registry[tool_name].get('output_fields', [])), 'reused_outputs': [], 'tool_parameters': {'metrics': list(component.get('metrics', [])), 'ranking_direction': component.get('direction'), 'top_n': PROMISING_COMPOSITE_CRITERIA['default_selection_size'], 'default_horizon': component.get('default_horizon')}, 'referenced_tickers': [], 'financial_concepts': [component['concept']], 'time_periods': normalize_time_periods(state.get('extracted_entities', {}).get('time_periods', [])) or [component.get('default_horizon')], 'depends_on': [], 'priority': priority, 'status': 'planned'})
        priority += 1
    if steps:
        steps.append({'step_id': f'PROMISING_{priority}', 'sub_question_id': 'PROMISING_SELECTION', 'action_type': 'synthesis_only', 'objective': 'Build the composite ranking and select the most promising stocks.', 'selected_tool': None, 'required_outputs': [], 'reused_outputs': [], 'tool_parameters': {'ranking_criterion': PROMISING_COMPOSITE_CRITERIA['criterion_name'], 'consensus_method': PROMISING_COMPOSITE_CRITERIA['consensus_method'], 'confutation_method': PROMISING_COMPOSITE_CRITERIA['confutation_method'], 'top_n': PROMISING_COMPOSITE_CRITERIA['default_selection_size']}, 'referenced_tickers': [], 'financial_concepts': ['return', 'momentum', 'risk', 'capm'], 'time_periods': normalize_time_periods(state.get('extracted_entities', {}).get('time_periods', [])), 'depends_on': [step['step_id'] for step in steps], 'priority': priority, 'status': 'planned'})
    return steps
QUESTION_PLANNING_OUTPUT_SCHEMA = {'planning_summary': {'objective': '', 'planning_status': 'ready | clarification_required | unsupported | no_action', 'reuse_strategy': '', 'execution_strategy': '', 'limitations': [], 'requires_clarification': False, 'clarification_question': None}, 'execution_plan': [{'step_id': 'STEP_1', 'sub_question_id': 'SQ1', 'component_id': 'COMP_1', 'metric': 'annualized_volatility', 'component_match_status': 'REUSE | EXECUTE | UNAVAILABLE', 'matched_result_id': None, 'matched_source_tool': None, 'matched_source_turn': None, 'action_type': 'reuse_output | execute_tool | synthesis_only | clarification | unsupported', 'objective': '', 'selected_tool': None, 'required_outputs': [], 'reused_outputs': [], 'tool_parameters': {}, 'referenced_tickers': [], 'financial_concepts': [], 'time_periods': [], 'depends_on': [], 'priority': 1, 'status': 'planned'}], 'agent_assignments': [], 'selected_tools': [], 'tool_parameters': {}, 'task_dependencies': []}
QUESTION_PLANNING_SYSTEM_INSTRUCTION = '\n\nMANDATORY DOCUMENTARY RULE:\nfor each component assigned to press_release_fy2025, the metric received\nfrom BOX 41 is a canonical key from the BOX 36 catalog. Do not rename it,\ntranslate it, or replace it. Preserve the same metric in the plan and in\ntool_parameters together with component_id, ticker/tickers, and time_period/time_periods.\n\nYou are Agent 12, the Planner Agent of an agentic system for\nanalyzing Dow Jones Industrial Average stocks.\n\nYou must transform Agent 11\'s analysis into a JSON plan.\n\nRULES\n\n1. Select exclusively tools present in the catalog.\n\n2. Do not perform calculations and do not produce the final answer.\n\n3. Reuse an output only if ticker, period, parameters, and\n   validation are compatible. Python will perform the final check\n   through the result signature.\n\n4. Always preserve the requested periods in the time_periods field,\n   except for pearson_correlation, which always uses the full available\n   history irrespective of any requested or inherited period.\n\n5. Use only one primary tool per step. If a component contains\n   multiple tickers with the same metric and the same period, keep all\n   tickers in the same step through referenced_tickers/execution_scope\n   and do not create a separate step for each ticker, EXCEPT for\n   press_release_fy2025: that tool accepts exactly one ticker per\n   execution step. Preserve the original ticker-level requirement atoms\n   and create one ordinary plan step per ticker, with its own step_id,\n   component_id, canonical metric, time period and required outputs.\n   Do not invent press-release result IDs or evidence IDs: these are\n   produced by the existing execution and evidence-normalization flow.\n\n6. Preserve the dependencies expressed by the sub-questions.\n\n7. For earnings, guidance, KPIs, and FY2025 results use\n   press_release_fy2025.\n\n8. For return, volatility, Sharpe, and Return-to-Risk use\n   financial_metrics.\n\n9. For correlations use pearson_correlation and always request\n   all_correlation_pairs. Add high_correlation_pairs only when a\n   threshold-specific output is required. Pearson\'s effective period\n   is always full_available_dataset, regardless of the question.\n\n\n11. For Momentum and Momentum ranking use momentum.\n\n12. For beta use capm_beta, for alpha use capm_alpha, and for CAPM expected return use capm_expected_return.\n\n13. An evidence_based_assessment must first retrieve the\n    evidence and conclude with synthesis_only.\n\n14. An unsupported_prediction must not activate tools.\n\n17. Do not involve press releases or other documentation in a\n    generic quantitative ranking. Use press_release_fy2025 only\n    for explicit documentary KPIs or for a prospective assessment\n    against corporate guidance and expectations.\n\n18. Request clarification only when information is missing\n    and cannot be derived either from the context or from the tools.\n\n    If retrieval_context.resolved_slots.ticker.source is\n    "current_question_global_universe", every relevant step must\n    preserve the entire set of tickers specified in ticker.value,\n    without restricting it to tickers from the previous question.\n\n19. Return exclusively JSON with:\n    planning_summary, execution_plan, agent_assignments,\n    selected_tools, tool_parameters, and task_dependencies.\n\n- In follow-ups, ticker, ranking, period, metric, and other constraints\n  validly inherited from the current flow must be treated as constraints\n  of the current plan.\n- If part of the request is already available and compatible in the current\n  flow, reuse it; plan a new calculation only for the new or missing\n  information component.\n- Before planning any execute_tool, compare each information component\n  identified by Agent 11 with available_results.\n- Treat already available results as building blocks in the toolbox:\n  if tool, time horizon, and result selection match, use reuse_output.\n  Do not recalculate the building block merely because it is being compared\n  with a new result.\n- The tickers contained in an already calculated ranking are not the primary\n  key for recognizing that ranking: the tool, its time horizon, and the requested\n  selection (all, top N, bottom N, or winner) are required.\n- If the request contains expressions such as "over the same period",\n  first resolve the time horizon against the metric, instrument,\n  ranking, or other references present in the current question.\n  Only if the horizon remains genuinely unresolved, retrieve it backward\n  from the current flow, starting from the relevant previous turn and\n  proceeding toward older ones.\n\n- For the momentum tool, treat the time horizon as the\n  formation_period_months parameter and preserve it also in time_periods.\n- Determine formation_period_months with this priority:\n  explicit period in the current question; if absent, a period semantically\n  derivable from a metric, instrument, ranking, or other reference\n  present in the current question; only if still absent, the relevant period\n  retrieved backward from the current flow, from the previous turn toward\n  older ones; only if all previous levels are absent,\n  use the default declared in the tool registry.\n- Do not create separate tools or routing for different Momentum horizons.\n'

def build_question_planning_prompt(state: Dict[str, Any], tool_catalog: List[Dict[str, Any]]) -> str:
    prompt_payload = {'task': 'Build the plan without executing the tools.', 'question_analysis': state.get('question_analysis', {}), 'question_intent': state.get('question_intent', ''), 'sub_questions': state.get('sub_questions', []), 'extracted_entities': state.get('extracted_entities', {}), 'retrieval_context': state.get('retrieval_context', {}), 'tool_catalog': tool_catalog, 'required_output_schema': QUESTION_PLANNING_OUTPUT_SCHEMA}
    return json.dumps(prompt_payload, ensure_ascii=False, indent=2, default=str)

def has_dependency_cycle(execution_plan: Sequence[Dict[str, Any]]) -> bool:
    graph = {step['step_id']: list(step.get('depends_on', [])) for step in execution_plan}
    visiting = set()
    visited = set()

    def visit(node: str) -> bool:
        if node in visiting:
            return True
        if node in visited:
            return False
        visiting.add(node)
        for dependency in graph.get(node, []):
            if dependency in graph and visit(dependency):
                return True
        visiting.remove(node)
        visited.add(node)
        return False
    return any((visit(node) for node in graph))

def validate_execution_graph(execution_plan: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
    step_ids = {step['step_id'] for step in execution_plan}
    missing_dependencies = []
    self_dependencies = []
    duplicate_dependencies = []
    for step in execution_plan:
        dependencies = step.get('depends_on', [])
        if len(dependencies) != len(set(dependencies)):
            duplicate_dependencies.append(step['step_id'])
        for dependency in dependencies:
            if dependency == step['step_id']:
                self_dependencies.append(step['step_id'])
            if dependency not in step_ids:
                missing_dependencies.append({'step_id': step['step_id'], 'missing_dependency': dependency})
    cycle_detected = has_dependency_cycle(execution_plan)
    return {'valid': not (missing_dependencies or self_dependencies or duplicate_dependencies or cycle_detected), 'missing_dependencies': missing_dependencies, 'self_dependencies': self_dependencies, 'duplicate_dependencies': duplicate_dependencies, 'cycle_detected': cycle_detected}

def validate_question_planning_output(raw_output: Dict[str, Any], state: Dict[str, Any], tool_registry: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    if not isinstance(raw_output, dict):
        raise TypeError('Agent 12 output must be a dictionary.')
    required_fields = {'planning_summary', 'execution_plan', 'agent_assignments', 'selected_tools', 'tool_parameters', 'task_dependencies'}
    missing_fields = required_fields - set(raw_output)
    if missing_fields:
        raise ValueError('Missing fields: ' + ', '.join(sorted(missing_fields)))
    raw_summary = raw_output.get('planning_summary', {})
    if not isinstance(raw_summary, dict):
        raw_summary = {}
    allowed_statuses = {'ready', 'clarification_required', 'unsupported', 'no_action'}
    planning_status = str(raw_summary.get('planning_status', 'ready')).strip()
    if planning_status not in allowed_statuses:
        planning_status = 'ready'
    planning_summary = {'objective': str(raw_summary.get('objective', '')).strip(), 'planning_status': planning_status, 'reuse_strategy': str(raw_summary.get('reuse_strategy', '')).strip(), 'execution_strategy': str(raw_summary.get('execution_strategy', '')).strip(), 'limitations': _planner_unique_strings(raw_summary.get('limitations', [])), 'requires_clarification': bool(raw_summary.get('requires_clarification', planning_status == 'clarification_required')), 'clarification_question': None if raw_summary.get('clarification_question') in {None, '', 'null'} else str(raw_summary.get('clarification_question')).strip()}
    raw_sub_questions = [item for item in _planner_ensure_list(state.get('sub_questions', [])) if isinstance(item, dict)]
    sub_question_map = {str(item.get('sub_question_id', '')).upper(): item for item in raw_sub_questions}
    sq_to_step = {}
    raw_steps = [step for step in _planner_ensure_list(raw_output.get('execution_plan', [])) if isinstance(step, dict)]
    for position, raw_step in enumerate(raw_steps, start=1):
        sub_question_id = str(raw_step.get('sub_question_id', '')).strip().upper()
        step_id = str(raw_step.get('step_id', f'STEP_{position}')).strip().upper()
        if sub_question_id:
            sq_to_step.setdefault(sub_question_id, step_id)
    required_components = [component for component in _planner_ensure_list(state.get('required_components', [])) if isinstance(component, dict)]
    existing_component_ids = {str(step.get('component_id', '')).strip().upper() for step in raw_steps if isinstance(step, dict)}
    for component in required_components:
        component_metric = str(component.get('metric', '') or '').strip().lower()
        component_id = str(component.get('component_id', '') or '').strip().upper()
        if component_metric != 'capm_beta' or not component_id or component_id in existing_component_ids:
            continue
        component_tickers = _planner_unique_strings(component.get('referenced_tickers', []) or ([component.get('ticker')] if component.get('ticker') else []), uppercase=True)
        component_periods = normalize_time_periods(component.get('time_periods', []) or ([component.get('time_period')] if component.get('time_period') else []))
        raw_steps.append({'step_id': f'STEP_{len(raw_steps) + 1}', 'sub_question_id': '', 'component_id': component_id, 'metric': 'capm_beta', 'component_match_status': 'EXECUTE', 'matched_result_id': None, 'matched_source_tool': None, 'matched_source_turn': None, 'action_type': 'execute_tool', 'objective': 'Calculate or reuse the requested CAPM Beta for the missing component.', 'selected_tool': 'capm_beta', 'required_outputs': list(tool_registry.get('capm_beta', {}).get('output_fields', [])), 'reused_outputs': [], 'tool_parameters': {}, 'referenced_tickers': component_tickers, 'financial_concepts': ['capm'], 'time_periods': component_periods, 'depends_on': [], 'priority': len(raw_steps) + 1, 'status': 'planned'})
        existing_component_ids.add(component_id)
    for component in required_components:
        component_id = str(component.get('component_id') or '').strip().upper()
        if not component_id or component_id in existing_component_ids:
            continue
        metric = str(component.get('metric') or '').strip()
        tool_name = str(component.get('selected_tool') or component.get('tool') or '').strip()
        if not tool_name:
            tool_name = metric if metric in tool_registry else ''
        if not tool_name or tool_name not in tool_registry:
            continue
        tickers = _planner_unique_strings(component.get('referenced_tickers') or ([component.get('ticker')] if component.get('ticker') else []), uppercase=True)
        periods = normalize_time_periods(component.get('time_periods') or ([component.get('time_period')] if component.get('time_period') else []))
        if not tickers:
            continue
        for ticker_group in [[ticker] for ticker in tickers] if tool_name == 'press_release_fy2025' else [tickers]:
            raw_steps.append({'step_id': f'STEP_{len(raw_steps) + 1}', 'sub_question_id': str(component.get('sub_question_id') or ''), 'component_id': component_id, 'metric': metric, 'component_match_status': 'EXECUTE', 'matched_result_id': None, 'action_type': 'execute_tool', 'objective': 'Retrieve the explicitly requested missing component.', 'selected_tool': tool_name, 'required_outputs': list(tool_registry[tool_name].get('output_fields', [])), 'reused_outputs': [], 'tool_parameters': {'metric': metric} if tool_name == 'press_release_fy2025' else {}, 'referenced_tickers': ticker_group, 'financial_concepts': [], 'time_periods': periods, 'depends_on': [], 'priority': len(raw_steps) + 1, 'status': 'planned'})
        existing_component_ids.add(component_id)
    normalized_plan = []
    used_step_ids = set()
    routing_corrections = []
    rejected_parameters = []
    reuse_decisions = []
    allowed_actions = {'reuse_output', 'execute_tool', 'synthesis_only', 'clarification', 'unsupported'}
    for position, raw_step in enumerate(raw_steps, start=1):
        step_id = str(raw_step.get('step_id', f'STEP_{position}')).strip().upper()
        if not step_id or step_id in used_step_ids:
            step_id = f'STEP_{position}'
        used_step_ids.add(step_id)
        sub_question_id = str(raw_step.get('sub_question_id', '')).strip().upper()
        sub_question = sub_question_map.get(sub_question_id, {})
        action_type = str(raw_step.get('action_type', 'synthesis_only')).strip()
        if action_type not in allowed_actions:
            action_type = 'synthesis_only'
        concepts = _planner_unique_strings(raw_step.get('financial_concepts', sub_question.get('financial_concepts', [])))
        routing_metric = str(raw_step.get('metric', sub_question.get('metric', ''))).strip() or None
        metric_tool_map = {'capm_beta': 'capm_beta', 'capm_alpha': 'capm_alpha', 'capm_expected_return': 'capm_expected_return'}
        proposed_tool = metric_tool_map.get(routing_metric, raw_step.get('selected_tool'))
        proposed_tool = None if proposed_tool in {None, '', 'null'} else str(proposed_tool).strip()
        matched_result_id = raw_step.get('matched_result_id')
        persistent_result_store = state.get('tool_results_by_key', {})
        matched_persistent_entry = persistent_result_store.get(matched_result_id) if matched_result_id and isinstance(persistent_result_store, dict) else None
        if action_type == 'synthesis_only' and isinstance(matched_persistent_entry, dict):
            matched_tool_name = matched_persistent_entry.get('tool_name')
            if matched_tool_name and matched_tool_name in tool_registry:
                action_type = 'reuse_output'
                proposed_tool = matched_tool_name
        if action_type in {'execute_tool', 'reuse_output'}:
            selected_tool, routing_correction = resolve_tool_routing(proposed_tool=proposed_tool, concepts=concepts, tool_registry=tool_registry)
            if routing_correction:
                routing_correction['step_id'] = step_id
                routing_corrections.append(routing_correction)
            if not selected_tool:
                action_type = 'synthesis_only'
        else:
            selected_tool = None
        referenced_tickers = _planner_unique_strings(raw_step.get('referenced_tickers', sub_question.get('referenced_tickers', state.get('extracted_entities', {}).get('tickers', []))), uppercase=True)
        retrieval_context = state.get('retrieval_context', {})
        if isinstance(retrieval_context, dict):
            resolved_slots = retrieval_context.get('resolved_slots', {})
        else:
            resolved_slots = {}
        if isinstance(resolved_slots, dict):
            resolved_ticker_slot = resolved_slots.get('ticker', {}) or {}
        else:
            resolved_ticker_slot = {}
        if resolved_ticker_slot.get('source') == 'current_question_global_universe':
            referenced_tickers = _planner_unique_strings(resolved_ticker_slot.get('value', []), uppercase=True)
        raw_step_time_periods = normalize_time_periods(raw_step.get('time_periods', []))
        sub_question_time_periods = normalize_time_periods(sub_question.get('time_periods', []))
        global_time_periods_for_step = normalize_time_periods(state.get('extracted_entities', {}).get('time_periods', []))
        if raw_step_time_periods:
            time_periods = raw_step_time_periods
        elif sub_question_time_periods:
            time_periods = sub_question_time_periods
        elif len(global_time_periods_for_step) <= 1:
            time_periods = global_time_periods_for_step
        else:
            time_periods = []
        proposed_parameters = raw_step.get('tool_parameters', {})
        is_correlation_step = selected_tool == 'pearson_correlation' or 'correlation' in (sub_question.get('financial_concepts', []) or [])
        step_extracted_entities = copy.deepcopy(state.get('extracted_entities', {}))
        global_time_periods = normalize_time_periods(step_extracted_entities.get('time_periods', []))
        if time_periods:
            step_extracted_entities.pop('start_date', None)
            step_extracted_entities.pop('end_date', None)
            step_extracted_entities.pop('time_period', None)
            step_extracted_entities.pop('rolling_period', None)
            step_extracted_entities['time_periods'] = copy.deepcopy(time_periods)
        exact_start_date, exact_end_date = extract_exact_date_range(time_periods=time_periods, extracted_entities=step_extracted_entities, state=state)
        period_type = state.get('extracted_entities', {}).get('period_type')
        resolved_time_slot = resolved_slots.get('time_period', {}) if isinstance(resolved_slots, dict) else {}
        resolved_time_value = resolved_time_slot.get('value') if isinstance(resolved_time_slot, dict) else None
        correlation_full_dataset = bool(is_correlation_step)
        if correlation_full_dataset:
            time_periods = []
            exact_start_date = None
            exact_end_date = None
            period_type = 'full_available_dataset'
        if selected_tool == 'financial_metrics' and str(period_type or '').strip().lower() == 'rolling' and (not (exact_start_date and exact_end_date)):
            raise ValueError('Rolling period identified for financial_metrics, but it cannot be materialized into start_date/end_date.')
        if selected_tool:
            validated_parameters, rejected_keys = validate_tool_parameters(tool_name=selected_tool, proposed_parameters=proposed_parameters, tool_registry=tool_registry)
            if rejected_keys:
                rejected_parameters.append({'step_id': step_id, 'tool_name': selected_tool, 'rejected_keys': rejected_keys})
            if selected_tool == 'pearson_correlation':
                for _pearson_time_key in ('time_periods', 'start_date', 'end_date'):
                    validated_parameters.pop(_pearson_time_key, None)
                validated_parameters['period_type'] = 'full_available_dataset'
            if referenced_tickers:
                validated_parameters['tickers'] = referenced_tickers
            if time_periods:
                validated_parameters.pop('start_date', None)
                validated_parameters.pop('end_date', None)
                validated_parameters['time_periods'] = time_periods
            if exact_start_date and exact_end_date:
                validated_parameters['start_date'] = exact_start_date
                validated_parameters['end_date'] = exact_end_date
            if period_type:
                validated_parameters['period_type'] = period_type
            requested_signature = build_requested_result_signature(tool_name=selected_tool, tickers=referenced_tickers, time_periods=time_periods, parameters=validated_parameters)
            availability = inspect_tool_output_availability(state=state, tool_name=selected_tool, tool_registry=tool_registry, requested_signature=requested_signature)
            if availability['reusable']:
                action_type = 'reuse_output'
                reused_outputs = availability['available_outputs']
            else:
                action_type = 'execute_tool'
                reused_outputs = []
            reuse_decisions.append({'step_id': step_id, 'tool_name': selected_tool, 'reusable': availability['reusable'], 'reasons': availability['incompatibility_reasons']})
            required_outputs = _planner_unique_strings(raw_step.get('required_outputs', tool_registry[selected_tool].get('output_fields', [])))
            if selected_tool == 'pearson_correlation':
                if len(referenced_tickers) == 2:
                    required_outputs = ['all_correlation_pairs']
                else:
                    correlation_text = ' '.join([str(sub_question.get('sub_question', '')), str(sub_question.get('objective', '')), str(state.get('user_question', ''))]).lower()
                    if '75%' in correlation_text or '0.75' in correlation_text or 'above' in correlation_text or ('over' in correlation_text) or ('highest' in correlation_text) or ('highest' in correlation_text) or ('most correlated' in correlation_text) or ('most correlated' in correlation_text) or ('ranking' in correlation_text):
                        required_outputs = ['all_correlation_pairs', 'high_correlation_pairs']
                    else:
                        required_outputs = ['all_correlation_pairs']
            registered_outputs = set(_planner_unique_strings(tool_registry.get(selected_tool, {}).get('output_fields', [])))
            requested_outputs_set = set(required_outputs)
            if requested_outputs_set and (not requested_outputs_set.issubset(registered_outputs)):
                output_compatible_tool, output_tool_candidates = resolve_tool_from_required_outputs(required_outputs=required_outputs, tool_registry=tool_registry)
                if output_compatible_tool and output_compatible_tool != selected_tool:
                    previous_selected_tool = selected_tool
                    selected_tool = output_compatible_tool
                    routing_corrections.append({'step_id': step_id, 'proposed_tool': previous_selected_tool, 'selected_tool': selected_tool, 'reason': 'Routing corrected because required_outputs is not compatible with the outputs of the selected tool and a single registered tool produces all requested outputs.', 'required_outputs': list(required_outputs)})
                    validated_parameters, rejected_after_output_routing = validate_tool_parameters(tool_name=selected_tool, proposed_parameters=proposed_parameters, tool_registry=tool_registry)
                    if referenced_tickers:
                        validated_parameters['tickers'] = referenced_tickers
                    if time_periods:
                        validated_parameters['time_periods'] = time_periods
                    if exact_start_date and exact_end_date:
                        validated_parameters['start_date'] = exact_start_date
                        validated_parameters['end_date'] = exact_end_date
                    if period_type:
                        validated_parameters['period_type'] = period_type
                    if rejected_after_output_routing:
                        rejected_parameters.append({'step_id': step_id, 'tool_name': selected_tool, 'rejected_keys': rejected_after_output_routing})
                    requested_signature = build_requested_result_signature(tool_name=selected_tool, tickers=referenced_tickers, time_periods=time_periods, parameters=validated_parameters)
                    availability = inspect_tool_output_availability(state=state, tool_name=selected_tool, tool_registry=tool_registry, requested_signature=requested_signature)
                    if availability['reusable']:
                        action_type = 'reuse_output'
                        reused_outputs = availability['available_outputs']
                    else:
                        action_type = 'execute_tool'
                        reused_outputs = []
                    reuse_decisions.append({'step_id': step_id, 'tool_name': selected_tool, 'reusable': availability['reusable'], 'reasons': availability['incompatibility_reasons']})
                elif not output_compatible_tool:
                    action_type = 'synthesis_only'
                    routing_corrections.append({'step_id': step_id, 'proposed_tool': selected_tool, 'selected_tool': None, 'reason': 'required_outputs is not compatible with the selected tool and no unique producer was identified in TOOL_REGISTRY.', 'required_outputs': list(required_outputs), 'candidate_tools': list(output_tool_candidates)})
                    selected_tool = None
                    validated_parameters = {}
                    reused_outputs = []
        else:
            validated_parameters = proposed_parameters if isinstance(proposed_parameters, dict) else {}
            reused_outputs = []
            required_outputs = _planner_unique_strings(raw_step.get('required_outputs', []))
        raw_dependencies = _planner_unique_strings(raw_step.get('depends_on', sub_question.get('depends_on', [])), uppercase=True)
        converted_dependencies = []
        for dependency in raw_dependencies:
            converted_dependency = sq_to_step.get(dependency, dependency)
            if converted_dependency not in converted_dependencies:
                converted_dependencies.append(converted_dependency)
        priority = raw_step.get('priority', sub_question.get('priority', position))
        try:
            priority = int(priority)
        except (TypeError, ValueError):
            priority = position
        component_id = str(raw_step.get('component_id', sub_question.get('component_id', f'COMP_{position}'))).strip().upper()
        metric = str(raw_step.get('metric', sub_question.get('metric', ''))).strip() or None
        if selected_tool == 'press_release_fy2025':
            if str(metric or '').strip().upper() == 'GENERAL_FUNDAMENTAL':
                continue
            if metric:
                validated_parameters['metric'] = metric
            if component_id:
                validated_parameters['component_id'] = component_id
            if referenced_tickers:
                validated_parameters['tickers'] = list(referenced_tickers)
            if time_periods:
                validated_parameters['time_periods'] = list(time_periods)
        component_match_status = 'REUSE' if action_type == 'reuse_output' else 'EXECUTE' if action_type == 'execute_tool' else 'UNAVAILABLE'
        normalized_plan.append({'step_id': step_id, 'sub_question_id': sub_question_id, 'component_id': component_id, 'metric': metric, 'component_signature': {'tickers': list(referenced_tickers), 'time_periods': list(time_periods), 'metric': metric}, 'component_match_status': component_match_status, 'matched_result_id': raw_step.get('matched_result_id'), 'matched_source_tool': raw_step.get('matched_source_tool'), 'matched_source_turn': raw_step.get('matched_source_turn'), 'action_type': action_type, 'objective': str(raw_step.get('objective', sub_question.get('objective', ''))).strip(), 'selected_tool': selected_tool, 'required_outputs': required_outputs, 'reused_outputs': reused_outputs, 'tool_parameters': validated_parameters, 'execution_scope': {'tickers': referenced_tickers, 'time_periods': time_periods, 'start_date': exact_start_date, 'end_date': exact_end_date, 'period_type': period_type, 'evidence_rows': None}, 'referenced_tickers': referenced_tickers, 'financial_concepts': concepts, 'time_periods': time_periods, 'depends_on': converted_dependencies, 'priority': max(1, priority), 'execution_owner': DETERMINISTIC_EXECUTOR_NODE_NAME, 'status': 'planned'})
    import re
    _press_existing_ids = {str(step.get('step_id', '')).upper() for step in normalized_plan}
    _press_next_id = max([int(match.group(1)) for step_id in _press_existing_ids if (match := re.fullmatch('STEP_(\\d+)', step_id))] or [0]) + 1
    _press_normalized_steps = []
    for _press_step in normalized_plan:
        _press_tickers = list(dict.fromkeys((str(ticker).strip().upper() for ticker in _press_step.get('referenced_tickers') or [] if str(ticker).strip())))
        if _press_step.get('selected_tool') != 'press_release_fy2025' or _press_step.get('action_type') != 'execute_tool' or len(_press_tickers) <= 1:
            _press_normalized_steps.append(_press_step)
            continue
        for _press_index, _press_ticker in enumerate(_press_tickers):
            _press_atomic_step = copy.deepcopy(_press_step)
            if _press_index:
                while f'STEP_{_press_next_id}' in _press_existing_ids:
                    _press_next_id += 1
                _press_atomic_step['step_id'] = f'STEP_{_press_next_id}'
                _press_existing_ids.add(_press_atomic_step['step_id'])
                _press_next_id += 1
            _press_atomic_step['referenced_tickers'] = [_press_ticker]
            _press_atomic_step['execution_scope']['tickers'] = [_press_ticker]
            _press_atomic_step['component_signature']['tickers'] = [_press_ticker]
            _press_atomic_step['tool_parameters']['tickers'] = [_press_ticker]
            _press_normalized_steps.append(_press_atomic_step)
    normalized_plan = _press_normalized_steps
    for step in normalized_plan:
        if step.get('selected_tool') != 'pearson_correlation':
            continue
        step['time_periods'] = []
        scope = step.setdefault('execution_scope', {})
        scope['time_periods'] = []
        scope['start_date'] = None
        scope['end_date'] = None
        scope['period_type'] = 'full_available_dataset'
        params = step.setdefault('tool_parameters', {})
        for key in ('time_periods', 'start_date', 'end_date'):
            params.pop(key, None)
        params['period_type'] = 'full_available_dataset'
        outputs = list(step.get('required_outputs') or [])
        if 'all_correlation_pairs' not in outputs:
            outputs.insert(0, 'all_correlation_pairs')
        step['required_outputs'] = outputs
    pearson_execution_steps = {}
    for step in normalized_plan:
        if step.get('selected_tool') != 'pearson_correlation' or step.get('action_type') not in {'execute_tool', 'reuse_output'}:
            continue
        pearson_parameters = step.get('tool_parameters', {}) or {}
        pearson_scope = step.get('execution_scope', {}) or {}
        pearson_signature = (tuple(step.get('referenced_tickers', []) or []), json.dumps(step.get('time_periods', []) or [], ensure_ascii=False, sort_keys=True, default=str), pearson_scope.get('start_date'), pearson_scope.get('end_date'), pearson_scope.get('period_type'), pearson_parameters.get('correlation_threshold'), tuple(sorted(step.get('required_outputs', []) or [])))
        primary_step_id = pearson_execution_steps.get(pearson_signature)
        if primary_step_id is None:
            pearson_execution_steps[pearson_signature] = step['step_id']
            continue
        dependencies = list(step.get('depends_on', []) or [])
        if primary_step_id not in dependencies:
            dependencies.append(primary_step_id)
        step['action_type'] = 'synthesis_only'
        step['selected_tool'] = None
        step['component_match_status'] = 'UNAVAILABLE'
        step['required_outputs'] = []
        step['reused_outputs'] = []
        step['tool_parameters'] = {}
        step['depends_on'] = dependencies
    for step in normalized_plan:
        step.setdefault('referenced_tickers', [])
        step.setdefault('time_periods', [])
        step.setdefault('execution_scope', {'tickers': list(step.get('referenced_tickers', [])), 'time_periods': list(step.get('time_periods', []))})
        step.setdefault('execution_owner', DETERMINISTIC_EXECUTOR_NODE_NAME)
        step.setdefault('status', 'planned')
    normalized_plan = sorted(normalized_plan, key=lambda item: (item['priority'], item['step_id']))
    graph_validation = validate_execution_graph(normalized_plan)
    if not graph_validation['valid']:
        planning_summary['planning_status'] = 'clarification_required'
        planning_summary['requires_clarification'] = True
        planning_summary['clarification_question'] = 'The plan contains invalid dependencies and must be regenerated.'
    selected_tools = _planner_unique_strings([step['selected_tool'] for step in normalized_plan if step['selected_tool']])
    consolidated_parameters = {}
    for step in normalized_plan:
        if not step['selected_tool']:
            continue
        consolidated_parameters.setdefault(step['selected_tool'], [])
        consolidated_parameters[step['selected_tool']].append({'step_id': step['step_id'], 'parameters': copy.deepcopy(step['tool_parameters']), 'execution_scope': copy.deepcopy(step['execution_scope'])})
    task_dependencies = [{'from_step': dependency, 'to_step': step['step_id']} for step in normalized_plan for dependency in step['depends_on']]
    agent_assignments = [{'step_id': step['step_id'], 'sub_question_id': step['sub_question_id'], 'planning_agent': QUESTION_PLANNING_AGENT_NAME, 'execution_node': DETERMINISTIC_EXECUTOR_NODE_NAME, 'assigned_tool': step['selected_tool']} for step in normalized_plan]
    return {'planning_summary': planning_summary, 'execution_plan': normalized_plan, 'agent_assignments': agent_assignments, 'selected_tools': selected_tools, 'selected_agents': [QUESTION_PLANNING_AGENT_NAME], 'tool_parameters': consolidated_parameters, 'task_dependencies': task_dependencies, 'planning_validation_report': {'graph_validation': graph_validation, 'routing_corrections': routing_corrections, 'rejected_parameters': rejected_parameters, 'reuse_decisions': reuse_decisions, 'time_scope_preserved': all(('time_periods' in step for step in normalized_plan)), 'promising_composite_used': False}}

def build_fallback_execution_plan(state: Dict[str, Any], tool_registry: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    question_analysis = state.get('question_analysis', {})
    question_intent = str(state.get('question_intent', ''))
    if question_intent == 'unsupported_prediction' or not question_analysis.get('is_supported', True):
        return {'planning_summary': {'objective': 'Handle the unsupported request.', 'planning_status': 'unsupported', 'reuse_strategy': '', 'execution_strategy': 'No tool is executed.', 'limitations': ['The request requires an unsupported prediction.'], 'requires_clarification': False, 'clarification_question': None}, 'execution_plan': [{'step_id': 'STEP_1', 'sub_question_id': '', 'action_type': 'unsupported', 'objective': 'State the system limitation.', 'selected_tool': None, 'required_outputs': [], 'reused_outputs': [], 'tool_parameters': {}, 'execution_scope': {'tickers': [], 'time_periods': []}, 'referenced_tickers': [], 'financial_concepts': [], 'time_periods': [], 'depends_on': [], 'priority': 1, 'execution_owner': DETERMINISTIC_EXECUTOR_NODE_NAME, 'status': 'planned'}], 'agent_assignments': [], 'selected_tools': [], 'selected_agents': [QUESTION_PLANNING_AGENT_NAME], 'tool_parameters': {}, 'task_dependencies': [], 'planning_validation_report': {'graph_validation': {'valid': True, 'missing_dependencies': [], 'self_dependencies': [], 'duplicate_dependencies': [], 'cycle_detected': False}, 'routing_corrections': [], 'rejected_parameters': [], 'reuse_decisions': [], 'time_scope_preserved': True, 'promising_composite_used': False}}
    raw_steps = []
    for position, sub_question in enumerate(_planner_ensure_list(state.get('sub_questions', [])), start=1):
        if not isinstance(sub_question, dict):
            continue
        concepts = _planner_unique_strings(sub_question.get('financial_concepts', []))
        compatible_tools = get_allowed_tools_for_concepts(concepts=concepts, tool_registry=tool_registry)
        selected_tool = compatible_tools[0] if len(compatible_tools) == 1 else None
        raw_steps.append({'step_id': f'STEP_{position}', 'sub_question_id': sub_question.get('sub_question_id', f'SQ{position}'), 'action_type': 'execute_tool' if selected_tool else 'synthesis_only', 'objective': sub_question.get('objective', sub_question.get('sub_question', '')), 'selected_tool': selected_tool, 'required_outputs': [], 'reused_outputs': [], 'tool_parameters': {}, 'referenced_tickers': sub_question.get('referenced_tickers', []), 'financial_concepts': concepts, 'time_periods': state.get('extracted_entities', {}).get('time_periods', []), 'depends_on': sub_question.get('depends_on', []), 'priority': sub_question.get('priority', position)})
    fallback_raw = {'planning_summary': {'objective': 'Execute Agent 11 sub-questions.', 'planning_status': 'ready' if raw_steps else 'no_action', 'reuse_strategy': 'Reuse only compatible and certified results.', 'execution_strategy': 'Execute only the necessary tools.', 'limitations': ['Plan generated through deterministic fallback.'], 'requires_clarification': False, 'clarification_question': None}, 'execution_plan': raw_steps, 'agent_assignments': [], 'selected_tools': [], 'tool_parameters': {}, 'task_dependencies': []}
    return validate_question_planning_output(raw_output=fallback_raw, state=state, tool_registry=tool_registry)
CONSENSUS_TOP_POSITIONS = 3
CONSENSUS_MIN_CONFIRMATIONS = 3
CONSENSUS_MAX_RESULTS = None
CONSENSUS_INCLUDE_TIES = True

def attach_result_identity_to_plan(validated_plan: Dict[str, Any], state: Dict[str, Any]) -> Dict[str, Any]:
    """Propagates tool + period + selection as the operational result identity."""
    plan = copy.deepcopy(validated_plan)
    default_selection = state.get('extracted_entities', {}).get('result_selection', {})
    for step in plan.get('execution_plan', []):
        if not isinstance(step, dict):
            continue
        tool_name = step.get('selected_tool')
        if not tool_name:
            continue
        parameters = step.setdefault('tool_parameters', {})
        selection = step.get('result_selection')
        if isinstance(default_selection, dict) and default_selection.get('type') == 'winner':
            selection = copy.deepcopy(default_selection)
        if not isinstance(selection, dict) or not selection:
            if parameters.get('top_n') is not None:
                selection = {'type': 'top_n', 'size': int(parameters['top_n'])}
            elif isinstance(default_selection, dict) and default_selection:
                selection = copy.deepcopy(default_selection)
            else:
                selection = {'type': 'all', 'size': None}
        step['result_selection'] = selection
        time_periods = list(step.get('time_periods', []) or [])
        if tool_name == 'momentum' and parameters.get('formation_period_months') is not None:
            time_periods = [f"{int(parameters['formation_period_months'])}M"]
            step['time_periods'] = time_periods
        step['result_identity'] = {'tool': tool_name, 'time_period': time_periods[0] if time_periods else 'default', 'selection': selection}
    return plan

def agent_12_question_planning(state: Dict[str, Any]) -> Dict[str, Any]:
    start_time = time.perf_counter()
    tool_registry = state.get('tool_registry', TOOL_REGISTRY if 'TOOL_REGISTRY' in globals() else {})
    if not isinstance(tool_registry, dict) or not tool_registry:
        raise ValueError('TOOL_REGISTRY is not available.')
    tool_catalog = build_planning_tool_catalog(state=state, tool_registry=tool_registry)
    user_prompt = build_question_planning_prompt(state=state, tool_catalog=tool_catalog)
    _dd_check = state.get('dual_domain_check') or {}
    if _dd_check.get('active'):
        user_prompt += '\n\n' + dual_domain_internal_report(_dd_check)
    planning_error = None
    planning_source = 'llm'
    try:
        raw_output = call_llm_json(system_instruction=QUESTION_PLANNING_SYSTEM_INSTRUCTION, user_content=user_prompt, model=QUESTION_PLANNING_MODEL, temperature=0.0)
        validated_plan = validate_question_planning_output(raw_output=raw_output, state=state, tool_registry=tool_registry)
    except Exception as error:
        planning_error = str(error)
        planning_source = 'deterministic_fallback'
        validated_plan = build_fallback_execution_plan(state=state, tool_registry=tool_registry)
    validated_plan = attach_result_identity_to_plan(validated_plan=validated_plan, state=state)
    elapsed_time = time.perf_counter() - start_time
    planning_status = validated_plan['planning_summary']['planning_status']
    next_node = 'tool_execution' if planning_status == 'ready' else 'answer_synthesis'
    return {**validated_plan, 'planning_status': planning_status, 'planning_source': planning_source, 'planning_error': planning_error, 'planning_execution_time_seconds': round(elapsed_time, 6), 'planning_model': QUESTION_PLANNING_MODEL, 'current_question_node': 'question_planning', 'question_workflow_status': 'planned' if planning_status == 'ready' else planning_status, 'next_node': next_node}
question_planning_node = agent_12_question_planning
if 'AGENT_REGISTRY' in globals() and 'build_registry_entry' in globals():
    if 'agent_11_question_analysis' in globals():
        AGENT_REGISTRY['question_analysis_agent'] = build_registry_entry(name='question_analysis_agent', function=agent_11_question_analysis, component_type='llm_agent', description='Semantically understands the question and decomposes it into sub-questions.', required_state_fields=['user_question', 'retrieval_context'], output_fields=['question_analysis', 'question_intent', 'sub_questions', 'extracted_entities'], uses_llm=True)
    AGENT_REGISTRY['question_planning_agent'] = build_registry_entry(name='question_planning_agent', function=agent_12_question_planning, component_type='llm_agent', description='Builds and validates the execution plan.', required_state_fields=['question_analysis', 'sub_questions', 'tool_registry'], output_fields=['execution_plan', 'agent_assignments', 'selected_tools', 'tool_parameters', 'task_dependencies', 'planning_summary', 'planning_validation_report'], uses_llm=True)
    final_state['agent_registry'] = AGENT_REGISTRY
final_state.setdefault('execution_plan', [])
final_state.setdefault('execution_plan_version', 2)
final_state.setdefault('planning_summary', {})
final_state.setdefault('selected_agents', [])
final_state.setdefault('selected_tools', [])
final_state.setdefault('agent_assignments', [])
final_state.setdefault('tool_parameters', {})
final_state.setdefault('task_dependencies', [])
final_state.setdefault('planning_validation_report', {})
final_state.setdefault('tool_result_signatures', {})
final_state.setdefault('planning_status', 'not_started')
_original_attach_result_identity_to_plan_box42 = attach_result_identity_to_plan

def attach_result_identity_to_plan(validated_plan: Dict[str, Any], state: Dict[str, Any]) -> Dict[str, Any]:
    plan = _original_attach_result_identity_to_plan_box42(validated_plan, state)
    components = {c.get('component_id'): c for c in state.get('required_components') or [] if isinstance(c, dict)}
    default_sel = (state.get('extracted_entities', {}) or {}).get('result_selection') or {'type': 'all', 'size': None}
    for step in plan.get('execution_plan', []):
        if not isinstance(step, dict):
            continue
        comp = components.get(step.get('component_id'), {})
        metric = canonical_metric_name(step.get('metric') or comp.get('metric'))
        periods = step.get('time_periods') or comp.get('time_periods') or []
        tickers = step.get('referenced_tickers') or comp.get('referenced_tickers') or []
        tool = step.get('selected_tool') or ''
        period = canonical_time_period(periods[0]) if periods else ''
        atomic_id = comp.get('atomic_id') or build_atomic_id(tool, tickers, metric, period)
        atomic_id = build_atomic_id(tool, tickers, metric, period)
        step['atomic_id'] = atomic_id
        step['metric'] = metric
        step['time_periods'] = [period] if period else []
        sig = build_canonical_result_signature(tool, tickers, step['time_periods'], metric, step.get('result_selection') or default_sel, step.get('tool_parameters') or {})
        step['requested_result_signature'] = sig
        step['requested_signature_id'] = canonical_result_signature_id(sig)
        step['result_identity'] = {'atomic_id': atomic_id, 'tool_name': tool, 'tickers': sig['tickers'], 'metric': metric, 'time_period': period, 'selection': sig['result_selection']}
    return plan
_original_attach_result_identity_to_plan_requirement_map = attach_result_identity_to_plan

def attach_result_identity_to_plan(validated_plan: Dict[str, Any], state: Dict[str, Any]) -> Dict[str, Any]:
    plan = _original_attach_result_identity_to_plan_requirement_map(validated_plan, state)
    atoms = [a for a in state.get('requirement_atoms') or [] if isinstance(a, dict)]
    for step in plan.get('execution_plan', []):
        if not isinstance(step, dict):
            continue
        metric = canonical_metric_name(step.get('metric'))
        periods = {canonical_time_period(p) for p in step.get('time_periods') or [] if canonical_time_period(p)}
        tickers = {str(t).strip().upper() for t in step.get('referenced_tickers') or [] if str(t).strip()}
        component_id = step.get('component_id')
        matched = []
        for atom in atoms:
            if component_id and atom.get('component_id') and (atom.get('component_id') != component_id):
                continue
            if metric and canonical_metric_name(atom.get('metric')) != metric:
                continue
            ap = canonical_time_period(atom.get('time_period'))
            if periods and ap not in periods:
                continue
            at = str(atom.get('ticker') or '').strip().upper()
            if tickers and at and (at not in tickers):
                continue
            matched.append(atom['requirement_id'])
        step['requirement_ids'] = sorted(set(matched))
        step['satisfies_requirement_ids'] = list(step['requirement_ids'])
        sig = step.get('requested_result_signature') or build_canonical_result_signature(step.get('selected_tool'), step.get('referenced_tickers') or [], step.get('time_periods') or [], metric, step.get('result_selection'), step.get('tool_parameters') or {})
        step['requested_result_signature'] = sig
        step['requested_signature_id'] = canonical_result_signature_id(sig)
        step['execution_signature_id'] = step['requested_signature_id']
    return plan
_original_attach_result_identity_to_plan_period_coverage = attach_result_identity_to_plan

def attach_result_identity_to_plan(validated_plan: Dict[str, Any], state: Dict[str, Any]) -> Dict[str, Any]:
    plan = _original_attach_result_identity_to_plan_period_coverage(validated_plan, state)
    required_ids = {a.get('requirement_id') for a in state.get('requirement_atoms') or [] if isinstance(a, dict) and a.get('requirement_id')}
    represented_ids = set()
    for step in plan.get('execution_plan', []) or []:
        if isinstance(step, dict):
            represented_ids.update(step.get('requirement_ids') or step.get('satisfies_requirement_ids') or [])
    plan['requirement_plan_coverage'] = {'required_requirement_ids': sorted(required_ids), 'represented_requirement_ids': sorted(represented_ids), 'missing_requirement_ids': sorted(required_ids - represented_ids), 'passed': required_ids.issubset(represented_ids)}
    return plan
_original_attach_result_identity_to_plan_condition_filters = attach_result_identity_to_plan

def _box42_resolve_threshold_logic(state: Dict[str, Any]) -> str:
    entities = state.get('extracted_entities', {}) or {}
    explicit = str(entities.get('threshold_logic') or entities.get('condition_logic') or '').strip().upper()
    if explicit in {'AND', 'OR'}:
        return explicit
    question = str(state.get('user_question', '') or '').lower()
    if re.search('\\b(?:oppure|or)\\b', question):
        return 'OR'
    return 'AND'

def attach_result_identity_to_plan(validated_plan: Dict[str, Any], state: Dict[str, Any]) -> Dict[str, Any]:
    plan = _original_attach_result_identity_to_plan_condition_filters(validated_plan, state)
    entities = state.get('extracted_entities', {}) or {}
    thresholds = copy.deepcopy(entities.get('thresholds', []) or [])
    threshold_logic = _box42_resolve_threshold_logic(state)
    plan['thresholds'] = thresholds
    plan['threshold_logic'] = threshold_logic
    for step in plan.get('execution_plan', []) or []:
        if not isinstance(step, dict):
            continue
        step['thresholds'] = copy.deepcopy(thresholds)
        step['threshold_logic'] = threshold_logic
    return plan
_original_attach_result_identity_to_plan_period_binding = attach_result_identity_to_plan

def _box42_threshold_metric_family(value: Any) -> str:
    text = str(value or '').lower()
    text = re.sub('[^a-z0-9àèéìòù]+', '_', text).strip('_')
    if 'momentum' in text:
        return 'momentum'
    if 'sharpe' in text:
        return 'sharpe'
    if 'volatil' in text or text in {'risk', 'annualized_risk'}:
        return 'volatility'
    if 'beta' in text:
        return 'beta'
    if 'alpha' in text:
        return 'alpha'
    if 'return' in text or 'rendimento' in text or 'performance' in text:
        return 'return'
    return text

def _box42_threshold_metric(raw: Any) -> str:
    if isinstance(raw, dict):
        value = raw.get('metric') or raw.get('financial_metric') or raw.get('field') or raw.get('indicator') or raw.get('name') or ' '.join((str(v) for v in raw.values() if v is not None))
    else:
        value = raw
    return _box42_threshold_metric_family(value)

def _box42_step_supports_metric(step: Dict[str, Any], metric: str) -> bool:
    selected_tool = str(step.get('selected_tool') or '').strip().lower()
    if metric == 'momentum':
        return selected_tool == 'momentum'
    if metric in {'volatility', 'sharpe', 'return'}:
        return selected_tool == 'financial_metrics'
    if metric in {'beta', 'alpha'}:
        return 'capm' in selected_tool or selected_tool in {'beta', 'alpha'}
    return False

def _box42_step_period_identity(step: Dict[str, Any]) -> Dict[str, Any]:
    parameters = step.get('tool_parameters', {}) or {}
    scope = step.get('execution_scope', {}) or {}
    periods = list(scope.get('time_periods') or step.get('time_periods') or [])
    if step.get('selected_tool') == 'momentum' and parameters.get('formation_period_months') is not None:
        period_label = f"{int(parameters['formation_period_months'])}M"
    elif periods:
        period_label = str(periods[0])
    elif parameters.get('start_date') and parameters.get('end_date'):
        period_label = f"{parameters['start_date']}_{parameters['end_date']}"
    elif scope.get('start_date') and scope.get('end_date'):
        period_label = f"{scope['start_date']}_{scope['end_date']}"
    else:
        period_label = 'default'
    return {'period_label': period_label, 'time_periods': periods, 'start_date': scope.get('start_date') or parameters.get('start_date'), 'end_date': scope.get('end_date') or parameters.get('end_date')}

def attach_result_identity_to_plan(validated_plan: Dict[str, Any], state: Dict[str, Any]) -> Dict[str, Any]:
    plan = _original_attach_result_identity_to_plan_period_binding(validated_plan, state)
    thresholds = copy.deepcopy(plan.get('thresholds', []) or [])
    execution_plan = plan.get('execution_plan', []) or []
    bound_thresholds = []
    for raw_threshold in thresholds:
        metric = _box42_threshold_metric(raw_threshold)
        compatible_steps = [step for step in execution_plan if isinstance(step, dict) and _box42_step_supports_metric(step, metric)]
        bound = copy.deepcopy(raw_threshold)
        if not isinstance(bound, dict):
            bound = {'condition': copy.deepcopy(raw_threshold)}
        if len(compatible_steps) == 1:
            source_step = compatible_steps[0]
            bound['source_step_id'] = source_step.get('step_id')
            bound['source_tool'] = source_step.get('selected_tool')
            bound['source_period'] = _box42_step_period_identity(source_step)
        bound_thresholds.append(bound)
    plan['thresholds'] = bound_thresholds
    for step in execution_plan:
        if isinstance(step, dict):
            step['thresholds'] = copy.deepcopy(bound_thresholds)
    return plan
_reuse_contract_original_attach_result_identity_to_plan = attach_result_identity_to_plan

def attach_result_identity_to_plan(*args, **kwargs):
    plan = _reuse_contract_original_attach_result_identity_to_plan(*args, **kwargs)

    def normalize_step(step):
        if not isinstance(step, dict):
            return
        action = str(step.get('action_type') or '').lower()
        expected = {'reuse_output': 'REUSE', 'execute_tool': 'EXECUTE'}.get(action)
        if expected:
            step['component_match_status'] = expected
        elif action in {'unsupported', 'clarification'}:
            step['component_match_status'] = 'UNAVAILABLE'
    if isinstance(plan, list):
        for step in plan:
            normalize_step(step)
    elif isinstance(plan, dict):
        for step in plan.get('execution_plan') or plan.get('steps') or []:
            normalize_step(step)
    return plan
TOOL_EXECUTOR_NODE_NAME = 'deterministic_tool_executor_node'
MAX_TOOL_EXECUTION_SECONDS = 300
STOP_ON_FIRST_ERROR = False

def _executor_ensure_list(value: Any) -> List[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, (tuple, set)):
        return list(value)
    return [value]

def _executor_unique_strings(values: Any, uppercase: bool=False) -> List[str]:
    output = []
    seen = set()
    for value in _executor_ensure_list(values):
        if value is None:
            continue
        text = str(value).strip()
        if not text:
            continue
        if uppercase:
            text = text.upper()
        key = text.lower()
        if key in seen:
            continue
        seen.add(key)
        output.append(text)
    return output

def _executor_is_empty(value: Any) -> bool:
    if value is None:
        return True
    if isinstance(value, (str, bytes, list, tuple, set, dict)):
        return len(value) == 0
    if hasattr(value, 'empty'):
        try:
            return bool(value.empty)
        except Exception:
            return False
    return False

def safe_copy_state(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Deep-copies the state whenever possible.
    DataFrames and Series are copied explicitly.
    """
    copied_state = {}
    for key, value in state.items():
        if isinstance(value, pd.DataFrame):
            copied_state[key] = value.copy(deep=True)
        elif isinstance(value, pd.Series):
            copied_state[key] = value.copy(deep=True)
        else:
            try:
                copied_state[key] = copy.deepcopy(value)
            except Exception:
                copied_state[key] = value
    return copied_state

def topological_execution_order(execution_plan: Sequence[Dict[str, Any]]) -> List[str]:
    """
    Topological ordering with priority as the secondary criterion.
    """
    step_map = {step['step_id']: step for step in execution_plan}
    graph = {step_id: [] for step_id in step_map}
    indegree = {step_id: 0 for step_id in step_map}
    for step in execution_plan:
        current_step = step['step_id']
        for dependency in step.get('depends_on', []):
            if dependency not in graph:
                raise ValueError(f'Nonexistent dependency: {dependency}.')
            graph[dependency].append(current_step)
            indegree[current_step] += 1
    ready = [step_id for step_id, degree in indegree.items() if degree == 0]
    ordered_steps = []
    while ready:
        ready.sort(key=lambda step_id: (int(step_map[step_id].get('priority', 999999)), step_id))
        current = ready.pop(0)
        ordered_steps.append(current)
        for successor in graph[current]:
            indegree[successor] -= 1
            if indegree[successor] == 0:
                ready.append(successor)
    if len(ordered_steps) != len(step_map):
        raise ValueError('The plan contains a dependency cycle.')
    return ordered_steps
PROJECT_OUTPUT_NOMENCLATURE = {'financial_metrics': {'producer_box': 30, 'producer_function': 'financial_metrics_tool', 'object_type': 'DataFrame', 'ticker_location': 'index', 'time_location': 'index', 'index_type': 'string', 'index_rule': '{Ticker}_{Year} OR {Ticker}_{StartDate}_{EndDate}', 'index_separator': '_', 'ticker_rule': 'The part to the left of the last underscore is the ticker.', 'time_rule': 'The part to the right of the last underscore is the four-digit calendar year.', 'example': 'AAPL_2025', 'meaning': 'Return and risk metrics for ticker AAPL calculated over the trading sessions belonging to calendar year 2025.'}, 'all_correlation_pairs': {'producer_box': 31, 'producer_function': 'pearson_correlation_tool', 'object_type': 'DataFrame', 'ticker_location': 'columns', 'ticker_columns': ['Ticker 1', 'Ticker 2'], 'time_location': None, 'example': 'Ticker 1=AAPL, Ticker 2=MSFT, Correlation=...', 'meaning': 'Each row represents a unique ticker pair.'}, 'high_correlation_pairs': {'producer_box': 31, 'producer_function': 'pearson_correlation_tool', 'object_type': 'DataFrame', 'ticker_location': 'columns', 'ticker_columns': ['Ticker 1', 'Ticker 2'], 'time_location': None, 'example': 'Ticker 1=AAPL, Ticker 2=MSFT, Correlation=...', 'meaning': 'Each row represents a unique ticker pair.'}, 'momentum_results': {'producer_box': 33, 'producer_function': 'momentum_tool', 'object_type': 'DataFrame', 'ticker_location': 'column', 'ticker_column': 'Ticker', 'time_location': None, 'time_semantics': 'Momentum is a metric calculated using the requested formation period; the period is not encoded in the ticker name.', 'example': 'Ticker=AAPL', 'meaning': 'One row per ticker with Rank, Momentum, and average Dollar Volume.'}, 'capm_results': {'producer_box': 34, 'producer_function': 'capm_tool', 'object_type': 'DataFrame', 'ticker_location': 'column', 'ticker_column': 'Ticker', 'benchmark_column': 'Benchmark', 'time_location': 'metadata', 'time_metadata_field': 'capm_metadata', 'time_metadata_keys': ['start_date', 'end_date', 'time_periods', 'period_type'], 'parameter_metadata_keys': ['benchmark_ticker', 'risk_free_rate', 'trading_days'], 'benchmark_semantics': 'Benchmark identifies the market benchmark used in the CAPM; it does not identify the stock ticker of the row.', 'example': 'Ticker=AAPL, Benchmark=^DJI', 'meaning': 'One row per ticker with Beta, Alpha, R-squared, observed return, CAPM return, and the difference between observed return and CAPM return, calculated over the requested period.'}, 'capm_beta_results': {'producer_box': 34, 'producer_function': 'capm_beta_tool', 'object_type': 'DataFrame', 'ticker_location': 'column', 'ticker_column': 'Ticker', 'benchmark_column': 'Benchmark', 'time_location': 'metadata', 'time_metadata_field': 'capm_beta_results_metadata', 'time_metadata_keys': ['start_date', 'end_date', 'time_periods', 'period_type'], 'parameter_metadata_keys': ['benchmark_ticker', 'risk_free_rate', 'trading_days'], 'meaning': 'One row per ticker with CAPM Beta.'}, 'capm_alpha_results': {'producer_box': 34, 'producer_function': 'capm_alpha_tool', 'object_type': 'DataFrame', 'ticker_location': 'column', 'ticker_column': 'Ticker', 'benchmark_column': 'Benchmark', 'time_location': 'metadata', 'time_metadata_field': 'capm_alpha_results_metadata', 'time_metadata_keys': ['start_date', 'end_date', 'time_periods', 'period_type'], 'parameter_metadata_keys': ['benchmark_ticker', 'risk_free_rate', 'trading_days'], 'meaning': 'One row per ticker with CAPM Alpha.'}, 'capm_expected_return_results': {'producer_box': 34, 'producer_function': 'capm_expected_return_tool', 'object_type': 'DataFrame', 'ticker_location': 'column', 'ticker_column': 'Ticker', 'benchmark_column': 'Benchmark', 'time_location': 'metadata', 'time_metadata_field': 'capm_expected_return_results_metadata', 'time_metadata_keys': ['start_date', 'end_date', 'time_periods', 'period_type'], 'parameter_metadata_keys': ['benchmark_ticker', 'risk_free_rate', 'trading_days'], 'meaning': 'One row per ticker with annual CAPM expected return.'}, 'press_release_archive': {'producer_box': 35, 'producer_function': 'build_press_release_archive', 'object_type': 'dict', 'ticker_location': 'dict_key', 'time_location': 'document_content', 'key_rule': 'Ticker', 'example': "{'AAPL': {...}, 'MSFT': {...}}", 'meaning': "The dictionary keys are actual tickers; each value contains the company's FY2025 Press Release."}}
PROJECT_SCOPE_NOMENCLATURE = {'DJI_UNIVERSE': {'type': 'universe', 'meaning': 'entire Dow Jones ticker universe', 'resolution': "state['tickers']"}, 'DJIA_UNIVERSE': {'type': 'universe', 'meaning': 'entire Dow Jones ticker universe', 'resolution': "state['tickers']"}, 'DOW_JONES_UNIVERSE': {'type': 'universe', 'meaning': 'entire Dow Jones ticker universe', 'resolution': "state['tickers']"}, 'DOW_JONES': {'type': 'universe', 'meaning': 'entire Dow Jones ticker universe', 'resolution': "state['tickers']"}, 'DOW30': {'type': 'universe', 'meaning': 'entire Dow Jones ticker universe', 'resolution': "state['tickers']"}, 'DOW_30': {'type': 'universe', 'meaning': 'entire Dow Jones ticker universe', 'resolution': "state['tickers']"}, 'ALL_DOW_JONES': {'type': 'universe', 'meaning': 'entire Dow Jones ticker universe', 'resolution': "state['tickers']"}, 'ALL_DJIA': {'type': 'universe', 'meaning': 'entire Dow Jones ticker universe', 'resolution': "state['tickers']"}}

def get_project_ticker_universe(state: Dict[str, Any]) -> List[str]:
    """
    Retrieves the actual ticker list defined by the project.
    """
    ticker_values = state.get('tickers', [])
    if not ticker_values:
        ticker_values = state.get('selected_tickers', [])
    if not ticker_values:
        ticker_values = globals().get('tickers', [])
    return _executor_unique_strings(ticker_values, uppercase=True)

def resolve_project_scope_tickers(state: Dict[str, Any], values: Any) -> List[str]:
    """
    Resolves only the tokens defined by the project.
    """
    requested = _executor_unique_strings(values, uppercase=True)
    if not requested:
        return []
    if any((value in PROJECT_SCOPE_NOMENCLATURE and PROJECT_SCOPE_NOMENCLATURE[value]['type'] == 'universe' for value in requested)):
        return get_project_ticker_universe(state)
    known_tickers = set(get_project_ticker_universe(state))
    return requested

def decode_financial_metrics_index(index_value: Any) -> Dict[str, Any]:
    """
    Decodes the only two valid forms produced by BOX 30:

      TICKER_YYYY
      TICKER_YYYY-MM-DD_YYYY-MM-DD

    It does not derive a year from the dates of a rolling interval.
    """
    text = str(index_value).strip()
    interval_match = re.fullmatch('(.+?)_(\\d{4}-\\d{2}-\\d{2})_(\\d{4}-\\d{2}-\\d{2})', text)
    if interval_match:
        return {'ticker': interval_match.group(1).strip().upper(), 'period_type': 'exact_date_range', 'calendar_year': None, 'year': None, 'start_date': interval_match.group(2), 'end_date': interval_match.group(3)}
    year_match = re.fullmatch('(.+?)_((?:19|20)\\d{2})', text)
    if year_match:
        year = int(year_match.group(2))
        return {'ticker': year_match.group(1).strip().upper(), 'period_type': 'calendar_year', 'calendar_year': year, 'year': year, 'start_date': None, 'end_date': None}
    return {'ticker': None, 'period_type': None, 'calendar_year': None, 'year': None, 'start_date': None, 'end_date': None}

def extract_output_scope_values(output_name: str, value: Any) -> Dict[str, Any]:
    """
    Reads tickers and years by applying EXCLUSIVELY the rule
    declared for the specific output.
    """
    tickers = set()
    years = set()
    schema = PROJECT_OUTPUT_NOMENCLATURE.get(output_name, {})
    if output_name == 'financial_metrics':
        if isinstance(value, pd.DataFrame):
            for index_value in value.index:
                decoded = decode_financial_metrics_index(index_value)
                if decoded['ticker']:
                    tickers.add(decoded['ticker'])
                if decoded['year'] is not None:
                    years.add(decoded['year'])
    elif output_name == 'all_correlation_pairs':
        if isinstance(value, pd.DataFrame):
            for column_name in ['Ticker 1', 'Ticker 2']:
                if column_name in value.columns:
                    tickers |= set(value[column_name].dropna().astype(str).str.strip().str.upper())
    elif output_name == 'high_correlation_pairs':
        if isinstance(value, pd.DataFrame):
            for column_name in ['Ticker 1', 'Ticker 2']:
                if column_name in value.columns:
                    tickers |= set(value[column_name].dropna().astype(str).str.strip().str.upper())
    elif output_name == 'momentum_results':
        if isinstance(value, pd.DataFrame) and 'Ticker' in value.columns:
            tickers |= set(value['Ticker'].dropna().astype(str).str.strip().str.upper())
    elif output_name in {'capm_results', 'capm_beta_results', 'capm_alpha_results', 'capm_expected_return_results'}:
        if isinstance(value, pd.DataFrame) and 'Ticker' in value.columns:
            tickers |= set(value['Ticker'].dropna().astype(str).str.strip().str.upper())
    elif output_name == 'press_release_archive':
        if isinstance(value, dict):
            tickers |= {str(key).strip().upper() for key in value.keys()}
    return {'schema': schema, 'tickers': tickers, 'years': years}

def filter_known_output_by_scope(output_name: str, result: Any, execution_scope: Dict[str, Any], state: Dict[str, Any]) -> Any:
    """
    Filters registered outputs using a single temporal semantic.
    Exact intervals are NEVER converted back into years.
    """
    requested_tickers = resolve_project_scope_tickers(state=state, values=execution_scope.get('tickers', []))
    ticker_set = set(requested_tickers)
    time_scope = _resolve_execution_time_scope(execution_scope)
    if output_name == 'financial_metrics' and isinstance(result, pd.DataFrame):
        selected_index = []
        for index_value in result.index:
            decoded = decode_financial_metrics_index(index_value)
            ticker_ok = not ticker_set or decoded.get('ticker') in ticker_set
            if time_scope['mode'] == 'exact_date_range':
                time_ok = decoded.get('period_type') == 'exact_date_range' and decoded.get('start_date') == time_scope['start_date'] and (decoded.get('end_date') == time_scope['end_date'])
            elif time_scope['mode'] == 'calendar_years':
                time_ok = decoded.get('period_type') == 'calendar_year' and decoded.get('calendar_year') in set(time_scope['calendar_years'])
            else:
                time_ok = True
            if ticker_ok and time_ok:
                selected_index.append(index_value)
        return result.loc[selected_index].copy()
    if output_name == 'all_correlation_pairs' and isinstance(result, pd.DataFrame):
        filtered = result.copy()
        if ticker_set and {'Ticker 1', 'Ticker 2'}.issubset(filtered.columns):
            mask = filtered['Ticker 1'].astype(str).str.upper().isin(ticker_set) & filtered['Ticker 2'].astype(str).str.upper().isin(ticker_set)
            filtered = filtered.loc[mask]
        return filtered.copy()
    if output_name == 'high_correlation_pairs' and isinstance(result, pd.DataFrame):
        filtered = result.copy()
        if ticker_set and {'Ticker 1', 'Ticker 2'}.issubset(filtered.columns):
            mask = filtered['Ticker 1'].astype(str).str.upper().isin(ticker_set) & filtered['Ticker 2'].astype(str).str.upper().isin(ticker_set)
            filtered = filtered.loc[mask]
        return filtered.copy()
    if output_name in {'momentum_results', 'capm_results'} and isinstance(result, pd.DataFrame):
        filtered = result.copy()
        if ticker_set and 'Ticker' in filtered.columns:
            filtered = filtered.loc[filtered['Ticker'].astype(str).str.upper().isin(ticker_set)]
        return filtered.copy()
    if output_name == 'press_release_archive' and isinstance(result, dict):
        if not ticker_set:
            return copy.deepcopy(result)
        return {key: copy.deepcopy(value) for key, value in result.items() if str(key).strip().upper() in ticker_set}
    return copy.deepcopy(result)

def _extract_years_from_periods(time_periods: Sequence[Any]) -> List[int]:
    """
    Extracts ONLY explicit calendar years.

    Important:
    '2025-08-12/2026-08-12' is an exact interval and returns [].
    It must never become {2025, 2026}.
    """
    years = set()
    for period in _executor_ensure_list(time_periods):
        text = str(period).strip()
        if re.fullmatch('\\d{4}-\\d{2}-\\d{2}\\s*/\\s*\\d{4}-\\d{2}-\\d{2}', text):
            continue
        single_year = re.fullmatch('(?:19|20)\\d{2}', text)
        if single_year:
            years.add(int(text))
            continue
        range_match = re.fullmatch('((?:19|20)\\d{2})\\s*[-/]\\s*((?:19|20)\\d{2})', text)
        if range_match:
            start_year = int(range_match.group(1))
            end_year = int(range_match.group(2))
            if start_year > end_year:
                start_year, end_year = (end_year, start_year)
            years.update(range(start_year, end_year + 1))
    return sorted(years)

def _resolve_execution_time_scope(execution_scope: Dict[str, Any]) -> Dict[str, Any]:
    """
    Produces a single temporal representation usable by BOX 42.
    An exact interval takes absolute precedence over calendar years.
    """
    scope = execution_scope if isinstance(execution_scope, dict) else {}
    start_date = scope.get('start_date')
    end_date = scope.get('end_date')
    period_type = scope.get('period_type')
    if start_date and end_date:
        return {'mode': 'exact_date_range', 'start_date': pd.Timestamp(start_date).strftime('%Y-%m-%d'), 'end_date': pd.Timestamp(end_date).strftime('%Y-%m-%d'), 'calendar_years': [], 'period_type': period_type or 'exact_date_range'}
    for period in _executor_ensure_list(scope.get('time_periods', [])):
        match = re.fullmatch('\\s*(\\d{4}-\\d{2}-\\d{2})\\s*/\\s*(\\d{4}-\\d{2}-\\d{2})\\s*', str(period))
        if match:
            return {'mode': 'exact_date_range', 'start_date': match.group(1), 'end_date': match.group(2), 'calendar_years': [], 'period_type': period_type or 'exact_date_range'}
    years = _extract_years_from_periods(scope.get('time_periods', []))
    return {'mode': 'calendar_years' if years else 'none', 'start_date': None, 'end_date': None, 'calendar_years': years, 'period_type': period_type}

def filter_result_by_scope(result: Any, execution_scope: Dict[str, Any], output_name: Optional[str]=None, state: Optional[Dict[str, Any]]=None) -> Any:
    state = state if isinstance(state, dict) else {}
    if output_name is not None and output_name in PROJECT_OUTPUT_NOMENCLATURE:
        return filter_known_output_by_scope(output_name=output_name, result=result, execution_scope=execution_scope, state=state)
    tickers = _executor_unique_strings(execution_scope.get('tickers', []), uppercase=True)
    time_scope = _resolve_execution_time_scope(execution_scope)
    if isinstance(result, pd.Series):
        filtered = result.copy()
        if tickers:
            idx = filtered.index.astype(str).str.upper()
            mask = idx.isin(tickers)
            if mask.any():
                filtered = filtered.loc[mask]
        return filtered
    if isinstance(result, pd.DataFrame):
        filtered = result.copy()
        if tickers and 'Ticker' in filtered.columns:
            filtered = filtered.loc[filtered['Ticker'].astype(str).str.upper().isin(tickers)]
        elif tickers:
            idx = filtered.index.astype(str).str.upper()
            mask = idx.isin(tickers)
            if mask.any():
                filtered = filtered.loc[mask]
        date_values = None
        date_source = None
        if isinstance(filtered.index, pd.DatetimeIndex):
            date_values = pd.to_datetime(filtered.index, errors='coerce')
            date_source = 'index'
        elif 'Date' in filtered.columns:
            date_values = pd.to_datetime(filtered['Date'], errors='coerce')
            date_source = 'column'
        if time_scope['mode'] == 'exact_date_range' and date_values is not None:
            start = pd.Timestamp(time_scope['start_date'])
            end = pd.Timestamp(time_scope['end_date'])
            mask = (date_values >= start) & (date_values <= end)
            filtered = filtered.loc[mask]
        elif time_scope['mode'] == 'calendar_years':
            years = time_scope['calendar_years']
            if date_values is not None:
                if date_source == 'index':
                    filtered = filtered.loc[date_values.year.isin(years)]
                else:
                    filtered = filtered.loc[date_values.dt.year.isin(years)]
            elif 'Year' in filtered.columns:
                parsed_years = pd.to_numeric(filtered['Year'], errors='coerce')
                filtered = filtered.loc[parsed_years.isin(years)]
        return filtered
    if isinstance(result, dict):
        return {key: filter_result_by_scope(result=value, execution_scope=execution_scope, output_name=None, state=state) for key, value in result.items()}
    return copy.deepcopy(result)

def build_component_signature(step: Dict[str, Any]) -> Dict[str, Any]:
    """Identifies the individual calculation identity: ticker + period + metric."""
    scope = step.get('execution_scope', {}) or {}
    return {'component_id': step.get('component_id'), 'tickers': sorted(_executor_unique_strings(scope.get('tickers', step.get('referenced_tickers', [])), uppercase=True)), 'time_periods': sorted((str(value) for value in _executor_ensure_list(scope.get('time_periods', step.get('time_periods', []))))), 'metric': step.get('metric')}

def build_execution_signature(step: Dict[str, Any]) -> Dict[str, Any]:
    selected_tool = step.get('selected_tool')
    scope = step.get('execution_scope', {})
    parameters = step.get('tool_parameters', {})
    return {'tool_name': selected_tool, 'tickers': sorted(_executor_unique_strings(scope.get('tickers', step.get('referenced_tickers', [])), uppercase=True)), 'time_periods': sorted([str(value) for value in _executor_ensure_list(scope.get('time_periods', step.get('time_periods', [])))]), 'result_selection': copy.deepcopy(step.get('result_selection', {'type': 'all', 'size': None})), 'parameters': {key: value for key, value in sorted(parameters.items()) if key not in {'tickers', 'time_periods'}}}

def build_result_signature_id(signature: Dict[str, Any]) -> str:
    """
    Generates a stable identifier for tool, ticker,
    period, and parameters.
    """
    canonical = json.dumps(signature, ensure_ascii=False, sort_keys=True, default=str)
    digest = hashlib.sha256(canonical.encode('utf-8')).hexdigest()[:16]
    return f"{signature.get('tool_name', 'tool')}__{digest}"

def check_reuse_compatibility(state: Dict[str, Any], step: Dict[str, Any]) -> Tuple[bool, List[str]]:
    requested_signature = build_execution_signature(step)
    signatures = state.get('tool_result_signatures', {})
    reasons = []
    if not isinstance(signatures, dict):
        return (False, ['Composite tool + period + selection signature not available: the result cannot be reused.'])
    requested_instrument_signature = build_reuse_instrument_signature(requested_signature)
    requested_tickers = set(requested_signature.get('tickers', []))
    compatible_signature = None
    best_coverage = -1
    for stored_signature in signatures.values():
        if not isinstance(stored_signature, dict):
            continue
        if build_reuse_instrument_signature(stored_signature) != requested_instrument_signature:
            continue
        stored_tickers = set(stored_signature.get('tickers', []))
        coverage = len(requested_tickers & stored_tickers)
        if requested_tickers and coverage == 0:
            continue
        if coverage > best_coverage:
            compatible_signature = stored_signature
            best_coverage = coverage
    if not compatible_signature:
        reasons.append('Composite tool + period + selection signature not available: the result cannot be reused.')
        return (False, reasons)
    if compatible_signature.get('validation_status') not in {'PASSED', 'CERTIFIED'}:
        reasons.append('Result not validated or certified.')
    return (not reasons, reasons)
ORCHESTRATION_ONLY_PARAMETERS = {'tickers', 'time_periods', 'years', 'start_date', 'end_date', 'top_n', 'ranking_criterion'}

def prepare_tool_call(tool_function: Callable, state: Dict[str, Any], parameters: Dict[str, Any]) -> Tuple[List[Any], Dict[str, Any], List[str]]:
    signature = inspect.signature(tool_function)
    function_parameters = signature.parameters
    accepts_var_kwargs = any((parameter.kind == inspect.Parameter.VAR_KEYWORD for parameter in function_parameters.values()))
    args = []
    kwargs = {}
    ignored_parameters = []
    state_parameter_names = {'state', 'final_state', 'market_data_state'}
    for name, parameter in function_parameters.items():
        source_value_available = False
        source_value = None
        if name in state_parameter_names:
            source_value = state
            source_value_available = True
        elif name in parameters:
            source_value = parameters[name]
            source_value_available = True
        if not source_value_available:
            continue
        if parameter.kind == inspect.Parameter.POSITIONAL_ONLY:
            args.append(source_value)
        else:
            kwargs[name] = source_value
    for key, value in parameters.items():
        if key in kwargs:
            continue
        if key in ORCHESTRATION_ONLY_PARAMETERS:
            ignored_parameters.append(key)
            continue
        if accepts_var_kwargs:
            kwargs[key] = value
        elif key not in function_parameters:
            ignored_parameters.append(key)
    missing_required = []
    positional_only_names = [name for name, parameter in function_parameters.items() if parameter.kind == inspect.Parameter.POSITIONAL_ONLY]
    supplied_positional_names = set(positional_only_names[:len(args)])
    for name, parameter in function_parameters.items():
        if parameter.kind in {inspect.Parameter.VAR_POSITIONAL, inspect.Parameter.VAR_KEYWORD}:
            continue
        supplied = name in kwargs or name in supplied_positional_names
        if parameter.default is inspect.Parameter.empty and (not supplied):
            missing_required.append(name)
    if missing_required:
        raise TypeError('Missing required parameters for the tool: ' + ', '.join(missing_required))
    return (args, kwargs, ignored_parameters)

def normalize_tool_return(tool_name: str, raw_result: Any, expected_outputs: Sequence[str]) -> Dict[str, Any]:
    """
    Converts the tool output into a stable dictionary.
    """
    expected_outputs = list(expected_outputs)
    if tool_name == 'press_release_fy2025' and isinstance(raw_result, dict):
        compact_outputs = {output_name: raw_result[output_name] for output_name in expected_outputs if output_name in raw_result}
        if compact_outputs:
            return compact_outputs
    if isinstance(raw_result, dict):
        if any((output_name in raw_result for output_name in expected_outputs)):
            return raw_result
        if len(expected_outputs) == 1:
            return {expected_outputs[0]: raw_result}
        return {'result': raw_result}
    if isinstance(raw_result, tuple):
        if expected_outputs and len(raw_result) == len(expected_outputs):
            return {output_name: value for output_name, value in zip(expected_outputs, raw_result)}
        return {'result': list(raw_result)}
    if len(expected_outputs) == 1:
        return {expected_outputs[0]: raw_result}
    return {'result': raw_result}

def validate_tool_outputs(outputs: Dict[str, Any], expected_outputs: Sequence[str], execution_scope: Dict[str, Any], state: Optional[Dict[str, Any]]=None) -> Dict[str, Any]:
    issues = []
    state = state if isinstance(state, dict) else {}
    if not isinstance(outputs, dict) or not outputs:
        return {'valid': False, 'issues': ['Output is missing or not structured.']}
    if expected_outputs:
        missing_expected = [name for name in expected_outputs if name not in outputs]
        if len(expected_outputs) == 1 and 'result' in outputs:
            missing_expected = []
        if missing_expected:
            issues.append('Missing declared outputs: ' + ', '.join(missing_expected))
    requested_tickers = set(resolve_project_scope_tickers(state=state, values=execution_scope.get('tickers', [])))
    validation_time_scope = _resolve_execution_time_scope(execution_scope)
    requested_years = set(validation_time_scope['calendar_years'] if validation_time_scope['mode'] == 'calendar_years' else [])
    outputs_to_validate = {output_name: outputs[output_name] for output_name in expected_outputs if output_name in outputs} if expected_outputs else outputs
    for output_name, value in outputs_to_validate.items():
        if output_name == 'high_correlation_pairs' and isinstance(value, pd.DataFrame) and value.empty and isinstance(outputs.get('all_correlation_pairs'), pd.DataFrame) and (not outputs['all_correlation_pairs'].empty):
            continue
        if _executor_is_empty(value):
            issues.append(f'Empty output: {output_name}.')
            continue
        if isinstance(value, pd.DataFrame):
            numeric_values = value.select_dtypes(include='number')
            if not numeric_values.empty:
                if numeric_values.isna().all().all():
                    issues.append(f'Only NaN values in {output_name}.')
                finite_mask = numeric_values.map(lambda item: True if pd.isna(item) else math.isfinite(float(item)))
                if not finite_mask.all().all():
                    issues.append(f'Infinite values in {output_name}.')
        if output_name in PROJECT_OUTPUT_NOMENCLATURE:
            extracted = extract_output_scope_values(output_name=output_name, value=value)
            found_tickers = extracted['tickers']
            found_years = extracted['years']
            if output_name == 'financial_metrics' and validation_time_scope['mode'] == 'exact_date_range' and isinstance(value, pd.DataFrame):
                exact_match_found = any((decode_financial_metrics_index(index_value).get('start_date') == validation_time_scope['start_date'] and decode_financial_metrics_index(index_value).get('end_date') == validation_time_scope['end_date'] for index_value in value.index))
                if not exact_match_found:
                    issues.append(f"Requested exact time interval not found in {output_name}: {validation_time_scope['start_date']}/{validation_time_scope['end_date']}.")
            if requested_tickers and output_name not in {'high_correlation_pairs'}:
                missing_tickers = requested_tickers - found_tickers
                if missing_tickers:
                    issues.append(f'Requested tickers not found in {output_name}: ' + ', '.join(sorted(missing_tickers)) + '.')
            time_location = PROJECT_OUTPUT_NOMENCLATURE[output_name].get('time_location')
            if requested_years and time_location in {'index', 'multiindex_level'}:
                missing_years = requested_years - found_years
                if missing_years:
                    issues.append(f'Requested period not found in {output_name}: ' + ', '.join((str(year) for year in sorted(missing_years))) + '.')
    return {'valid': not issues, 'issues': issues}

def _tool_process_target(queue: Any, tool_function: Callable, args: List[Any], kwargs: Dict[str, Any]) -> None:
    try:
        queue.put({'ok': True, 'result': tool_function(*args, **kwargs)})
    except Exception as error:
        queue.put({'ok': False, 'error': str(error)})

def run_tool_with_timeout(tool_function: Callable, args: List[Any], kwargs: Dict[str, Any], timeout_seconds: int) -> Any:
    context = mp.get_context('fork' if 'fork' in mp.get_all_start_methods() else 'spawn')
    queue = context.Queue()
    process = context.Process(target=_tool_process_target, args=(queue, tool_function, args, kwargs))
    process.start()
    process.join(timeout_seconds)
    if process.is_alive():
        process.terminate()
        process.join()
        raise TimeoutError(f'Real timeout after {timeout_seconds} seconds.')
    if queue.empty():
        raise RuntimeError('The tool process did not return any result.')
    payload = queue.get()
    if not payload.get('ok'):
        raise RuntimeError(payload.get('error', 'Unknown tool error.'))
    return payload.get('result')

def _result_identity_token(value: Any) -> str:
    text = str(value if value is not None else 'default').strip()
    text = re.sub('[^A-Za-z0-9]+', '_', text).strip('_')
    return text or 'default'

def build_result_storage_key(step: Dict[str, Any]) -> str:
    """Builds <tool>_<period>_<selection>_result."""
    tool_name = _result_identity_token(step.get('selected_tool', 'tool'))
    parameters = step.get('tool_parameters', {}) or {}
    periods = list(step.get('time_periods', []) or [])
    if step.get('selected_tool') == 'momentum' and parameters.get('formation_period_months') is not None:
        period = f"{int(parameters['formation_period_months'])}M"
    elif periods:
        period = periods[0]
    elif parameters.get('start_date') and parameters.get('end_date'):
        period = f"{parameters['start_date']}_{parameters['end_date']}"
    else:
        period = 'default'
    selection = step.get('result_selection', {}) or {}
    selection_type = str(selection.get('type', 'all')).lower()
    selection_size = selection.get('size')
    if selection_type in {'top_n', 'top'} and selection_size is not None:
        selection_token = f'top{int(selection_size)}'
    elif selection_type in {'bottom_n', 'bottom'} and selection_size is not None:
        selection_token = f'bottom{int(selection_size)}'
    elif selection_type == 'winner':
        selection_token = 'top1'
    elif parameters.get('top_n') is not None:
        selection_token = f"top{int(parameters['top_n'])}"
    else:
        selection_token = 'all'
    return f'{tool_name}_{_result_identity_token(period)}_{_result_identity_token(selection_token)}_result'

def find_reusable_result_entry(state: Dict[str, Any], requested_signature: Dict[str, Any]) -> Tuple[Optional[str], Optional[Dict[str, Any]]]:
    store = state.get('tool_results_by_key', {})
    if not isinstance(store, dict):
        return (None, None)
    requested_instrument_signature = build_reuse_instrument_signature(requested_signature)
    requested_tickers = set(requested_signature.get('tickers', []))
    best_match = None
    best_coverage = -1
    for result_key, entry in reversed(list(store.items())):
        if not isinstance(entry, dict):
            continue
        stored_signature = entry.get('result_signature', {})
        if build_reuse_instrument_signature(stored_signature) != requested_instrument_signature:
            continue
        stored_tickers = set(stored_signature.get('tickers', []))
        coverage = len(requested_tickers & stored_tickers)
        if requested_tickers and coverage == 0:
            continue
        if coverage > best_coverage:
            best_match = (result_key, entry)
            best_coverage = coverage
    if best_match is not None:
        return best_match
    return (None, None)

def merge_partial_reuse_outputs(reused_value: Any, new_value: Any) -> Any:
    """
    Merges the reused portion with the newly calculated portion.
    """
    if reused_value is None:
        return copy.deepcopy(new_value)
    if new_value is None:
        return copy.deepcopy(reused_value)
    if isinstance(reused_value, pd.DataFrame) and isinstance(new_value, pd.DataFrame):
        return new_value.combine_first(reused_value)
    if isinstance(reused_value, pd.Series) and isinstance(new_value, pd.Series):
        return new_value.combine_first(reused_value)
    if isinstance(reused_value, dict) and isinstance(new_value, dict):
        merged = copy.deepcopy(reused_value)
        for key, value in new_value.items():
            if key in merged:
                merged[key] = merge_partial_reuse_outputs(merged[key], value)
            else:
                merged[key] = copy.deepcopy(value)
        return merged
    if isinstance(reused_value, list) and isinstance(new_value, list):
        merged = copy.deepcopy(reused_value)
        for value in new_value:
            if value not in merged:
                merged.append(copy.deepcopy(value))
        return merged
    return copy.deepcopy(new_value)

def execute_plan_step(state: Dict[str, Any], step: Dict[str, Any], tool_registry: Dict[str, Dict[str, Any]], completed_statuses: Dict[str, str]) -> Dict[str, Any]:
    step_id = step['step_id']
    action_type = step.get('action_type', 'synthesis_only')
    selected_tool = step.get('selected_tool')
    dependencies = step.get('depends_on', [])
    failed_dependencies = [dependency for dependency in dependencies if completed_statuses.get(dependency) not in {'COMPLETED', 'REUSED', 'SKIPPED_SYNTHESIS'}]
    if failed_dependencies:
        return {'step_id': step_id, 'status': 'BLOCKED', 'action_type': action_type, 'selected_tool': selected_tool, 'source': None, 'outputs': {}, 'output_fields': [], 'execution_time_seconds': 0.0, 'error': 'Uncompleted dependencies: ' + ', '.join(failed_dependencies), 'ignored_parameters': [], 'result_signature': None}
    tool_backed_requirement = bool(step.get('requirement_ids') or step.get('satisfies_requirement_ids')) and bool(selected_tool and selected_tool in tool_registry)
    if tool_backed_requirement:
        action_type = 'reuse_output'
    if action_type == 'synthesis_only':
        return {'step_id': step_id, 'status': 'SKIPPED_SYNTHESIS', 'action_type': action_type, 'selected_tool': None, 'source': 'plan', 'outputs': {}, 'output_fields': [], 'execution_time_seconds': 0.0, 'error': None, 'ignored_parameters': [], 'result_signature': None}
    if action_type in {'clarification', 'unsupported'}:
        return {'step_id': step_id, 'status': 'SKIPPED', 'action_type': action_type, 'selected_tool': None, 'source': 'plan', 'outputs': {}, 'output_fields': [], 'execution_time_seconds': 0.0, 'error': None, 'ignored_parameters': [], 'result_signature': None}
    if not selected_tool or selected_tool not in tool_registry:
        return {'step_id': step_id, 'status': 'FAILED', 'action_type': action_type, 'selected_tool': selected_tool, 'source': None, 'outputs': {}, 'output_fields': [], 'execution_time_seconds': 0.0, 'error': 'Tool is missing or not registered.', 'ignored_parameters': [], 'result_signature': None}
    metadata = tool_registry[selected_tool]
    expected_outputs = list(step.get('required_outputs', []) or metadata.get('output_fields', []))
    execution_scope = copy.deepcopy(step.get('execution_scope', {'tickers': step.get('referenced_tickers', []), 'time_periods': step.get('time_periods', [])}))
    step_tool_parameters = copy.deepcopy(step.get('tool_parameters', {}))
    if step_tool_parameters.get('start_date'):
        execution_scope['start_date'] = step_tool_parameters.get('start_date')
    if step_tool_parameters.get('end_date'):
        execution_scope['end_date'] = step_tool_parameters.get('end_date')
    if step_tool_parameters.get('period_type'):
        execution_scope['period_type'] = step_tool_parameters.get('period_type')
    if selected_tool == 'financial_metrics' and str(execution_scope.get('period_type', '')).strip().lower() == 'rolling':
        scope_start_date = execution_scope.get('start_date')
        scope_end_date = execution_scope.get('end_date')
        if not (scope_start_date and scope_end_date):
            raise ValueError('financial_metrics requires start_date/end_date for a rolling period.')
        step_tool_parameters['start_date'] = scope_start_date
        step_tool_parameters['end_date'] = scope_end_date
        step_tool_parameters['period_type'] = 'rolling'
    resolved_ticker_slot = state.get('retrieval_context', {}).get('resolved_slots', {}).get('ticker', {}) or {}
    if resolved_ticker_slot.get('source') == 'current_question_global_universe':
        execution_scope['tickers'] = resolved_ticker_slot.get('value', [])
    execution_scope['tickers'] = resolve_project_scope_tickers(state=state, values=execution_scope.get('tickers', []))
    normalized_step = copy.deepcopy(step)
    normalized_step['execution_scope'] = execution_scope
    normalized_step['tool_parameters'] = step_tool_parameters
    normalized_step['referenced_tickers'] = execution_scope['tickers']
    result_signature = build_execution_signature(normalized_step)
    component_signature = build_component_signature(normalized_step)
    partial_reuse_outputs = {}
    partial_reuse_key = None
    partial_reuse_missing_tickers = []
    if action_type == 'reuse_output':
        matched_result_id = normalized_step.get('matched_result_id')
        result_store = state.get('tool_results_by_key', {})
        matched_entry_compatible = False
        if matched_result_id and isinstance(result_store, dict) and (matched_result_id in result_store):
            matched_entry = result_store[matched_result_id]
            if isinstance(matched_entry, dict):
                matched_signature = matched_entry.get('result_signature', {})
                requested_instrument_signature = build_reuse_instrument_signature(result_signature)
                matched_instrument_signature = build_reuse_instrument_signature(matched_signature) if isinstance(matched_signature, dict) else {}
                requested_tickers = set(result_signature.get('tickers', []))
                matched_tickers = set(matched_signature.get('tickers', []) if isinstance(matched_signature, dict) else [])
                matched_entry_compatible = matched_instrument_signature == requested_instrument_signature and (not requested_tickers or bool(requested_tickers & matched_tickers))
        if matched_entry_compatible:
            reusable_key = matched_result_id
            reusable_entry = result_store[matched_result_id]
        else:
            reusable_key, reusable_entry = find_reusable_result_entry(state=state, requested_signature=result_signature)
        if not reusable_entry:
            action_type = 'execute_tool'
            normalized_step['action_type'] = action_type
        else:
            stored_signature = reusable_entry.get('result_signature', {})
            requested_tickers = set(result_signature.get('tickers', []))
            stored_tickers = set(stored_signature.get('tickers', []))
            partial_reuse_missing_tickers = sorted(requested_tickers - stored_tickers)
            reused_outputs = {output_name: filter_result_by_scope(result=copy.deepcopy(output_value), execution_scope=execution_scope, output_name=output_name, state=state) for output_name, output_value in copy.deepcopy(reusable_entry.get('outputs', {})).items()}
            if not partial_reuse_missing_tickers:
                return {'step_id': step_id, 'status': 'REUSED', 'action_type': action_type, 'selected_tool': selected_tool, 'source': 'tool_results_by_key', 'outputs': reused_outputs, 'output_fields': list(reused_outputs), 'execution_time_seconds': 0.0, 'error': None, 'ignored_parameters': [], 'result_signature': result_signature, 'component_signature': component_signature, 'component_id': normalized_step.get('component_id'), 'metric': normalized_step.get('metric'), 'result_key': reusable_key}
            partial_reuse_outputs = reused_outputs
            partial_reuse_key = reusable_key
            execution_scope['tickers'] = partial_reuse_missing_tickers
            normalized_step['execution_scope'] = execution_scope
            normalized_step['referenced_tickers'] = partial_reuse_missing_tickers
    tool_function = metadata.get('function')
    if not callable(tool_function):
        return {'step_id': step_id, 'status': 'FAILED', 'action_type': action_type, 'selected_tool': selected_tool, 'source': None, 'outputs': {}, 'output_fields': [], 'execution_time_seconds': 0.0, 'error': 'The registered function is not callable.', 'ignored_parameters': [], 'result_signature': result_signature}
    start_time = time.perf_counter()
    try:
        if selected_tool == 'press_release_fy2025':
            press_release_state_keys = ['press_release_validation', 'press_release_keywords', 'press_release_semantic_kpi_families', 'press_release_information_catalog', 'press_release_section_catalog', 'press_release_search_catalog', 'press_release_catalog_index', 'press_release_tool_contract']
            isolated_state = {key: copy.deepcopy(state[key]) for key in press_release_state_keys if key in state}
            if 'press_release_archive' in state:
                isolated_state['press_release_archive'] = state['press_release_archive']
        else:
            isolated_state = safe_copy_state(state)
        effective_tool_parameters = copy.deepcopy(normalized_step.get('tool_parameters', {}))
        if partial_reuse_missing_tickers:
            effective_tool_parameters['tickers'] = list(partial_reuse_missing_tickers)
        if selected_tool == 'pearson_correlation':
            for key in ('start_date', 'end_date', 'time_periods', 'period_type'):
                effective_tool_parameters.pop(key, None)
        if selected_tool == 'press_release_fy2025':
            if step.get('metric') is not None:
                effective_tool_parameters['metric'] = step.get('metric')
            if step.get('component_id') is not None:
                effective_tool_parameters['component_id'] = step.get('component_id')
            scope_tickers = _executor_unique_strings(execution_scope.get('effective_tickers', step.get('referenced_tickers', [])), uppercase=True)
            scope_periods = execution_scope.get('effective_time_periods', step.get('time_periods', []))
            if len(scope_tickers) != 1:
                raise ValueError('press_release_fy2025 requires exactly one ticker per step; received: ' + ', '.join(scope_tickers))
            effective_tool_parameters.pop('tickers', None)
            effective_tool_parameters['ticker'] = scope_tickers[0]
            if scope_periods:
                effective_tool_parameters['time_periods'] = list(scope_periods)
        args, kwargs, ignored_parameters = prepare_tool_call(tool_function=tool_function, state=isolated_state, parameters=effective_tool_parameters)
        raw_result = run_tool_with_timeout(tool_function=tool_function, args=args, kwargs=kwargs, timeout_seconds=MAX_TOOL_EXECUTION_SECONDS)
        elapsed_time = time.perf_counter() - start_time
        normalized_outputs = normalize_tool_return(tool_name=selected_tool, raw_result=raw_result, expected_outputs=expected_outputs)
        normalized_outputs = {output_name: filter_result_by_scope(result=output_value, execution_scope=execution_scope, output_name=output_name, state=state) for output_name, output_value in normalized_outputs.items()}
        if partial_reuse_outputs:
            normalized_outputs = {output_name: merge_partial_reuse_outputs(partial_reuse_outputs.get(output_name), normalized_outputs.get(output_name)) for output_name in set(partial_reuse_outputs) | set(normalized_outputs)}
            execution_scope['tickers'] = result_signature.get('tickers', [])
        if selected_tool == 'press_release_fy2025':
            press_output = normalized_outputs.get('press_release_result')
            if isinstance(press_output, dict):
                requested_category = str(effective_tool_parameters.get('metric') or step.get('metric') or '').upper()
                records = press_output.get('evidence') or []
                verified_records = [item for item in records if isinstance(item, dict) and str(item.get('evidence_text') or '').strip() and (str(item.get('matched_metric') or '').upper() == requested_category)]
                press_output['requested_metric'] = requested_category
                press_output['verified_metric'] = requested_category if verified_records else None
                press_output['content_relevance_status'] = 'VERIFIED' if verified_records else 'MISSING'
        output_validation = validate_tool_outputs(outputs=normalized_outputs, expected_outputs=expected_outputs, execution_scope=execution_scope, state=state)
        if not output_validation['valid']:
            raise ValueError('Invalid output: ' + '; '.join(output_validation['issues']))
        if partial_reuse_outputs:
            normalized_step['execution_scope'] = {**normalized_step.get('execution_scope', {}), 'tickers': result_signature.get('tickers', [])}
            normalized_step['referenced_tickers'] = result_signature.get('tickers', [])
        return {'step_id': step_id, 'status': 'COMPLETED', 'action_type': action_type, 'selected_tool': selected_tool, 'source': 'partial_reuse+tool_execution' if partial_reuse_outputs else 'tool_execution', 'outputs': normalized_outputs, 'output_fields': list(normalized_outputs), 'execution_time_seconds': round(elapsed_time, 6), 'error': None, 'ignored_parameters': ignored_parameters, 'result_signature': result_signature, 'result_key': build_result_storage_key(normalized_step), 'output_validation': output_validation}
    except Exception as error:
        elapsed_time = time.perf_counter() - start_time
        return {'step_id': step_id, 'status': 'FAILED', 'action_type': action_type, 'selected_tool': selected_tool, 'source': 'tool_execution', 'outputs': {}, 'output_fields': [], 'execution_time_seconds': round(elapsed_time, 6), 'error': str(error), 'ignored_parameters': [], 'result_signature': result_signature}

def consolidate_step_result(state: Dict[str, Any], step_result: Dict[str, Any]) -> None:
    if step_result['status'] not in {'COMPLETED', 'REUSED'}:
        return
    step_id = step_result['step_id']
    outputs = copy.deepcopy(step_result['outputs'])
    state.setdefault('tool_results_by_step', {})
    state['tool_results_by_step'][step_id] = outputs
    state.setdefault('tool_result_keys_by_step', {})
    state.setdefault('tool_results_by_key', {})
    state.setdefault('tool_output_history', {})
    result_key = step_result.get('result_key')
    if step_result['status'] == 'COMPLETED':
        base_key = result_key or f"{step_result.get('selected_tool', 'tool')}_default_all_result"
        result_key = base_key
        counter = 2
        while result_key in state['tool_results_by_key']:
            result_key = f'{base_key}__{counter}'
            counter += 1
        state['tool_results_by_key'][result_key] = {'result_key': result_key, 'tool_name': step_result.get('selected_tool'), 'result_signature': copy.deepcopy(step_result.get('result_signature') or {}), 'outputs': outputs, 'source': step_result.get('source'), 'step_id': step_id, 'updated_at': pd.Timestamp.utcnow().isoformat()}
    state['tool_result_keys_by_step'][step_id] = result_key
    for output_name, output_value in outputs.items():
        state.setdefault(output_name, output_value)
        state['tool_output_history'].setdefault(output_name, [])
        state['tool_output_history'][output_name].append({'step_id': step_id, 'selected_tool': step_result.get('selected_tool'), 'source': step_result.get('source'), 'result_key': result_key, 'value': output_value})
    tool_name = step_result.get('selected_tool')
    if tool_name:
        state.setdefault('tool_result_signatures', {})
        signature = copy.deepcopy(step_result.get('result_signature') or {})
        signature_id = build_result_signature_id(signature)
        signature['result_signature_id'] = signature_id
        signature['result_key'] = result_key
        signature['validation_status'] = 'CERTIFIED' if step_result['status'] == 'REUSED' else 'PENDING_VALIDATION'
        signature['source'] = step_result.get('source')
        signature['step_id'] = step_id
        signature['updated_at'] = pd.Timestamp.utcnow().isoformat()
        state['tool_result_signatures'][signature_id] = signature

def _validate_momentum_execution_context(*, selected_tool: str, tool_parameters: Dict[str, Any], tool_output: Dict[str, Any]) -> None:
    if selected_tool != 'momentum':
        return
    requested_months = tool_parameters.get('formation_period_months')
    context = tool_output.get('momentum_context', {})
    if not isinstance(context, dict):
        raise ValueError('The momentum tool did not return momentum_context.')
    executed_months = context.get('formation_period_months')
    if requested_months is not None and executed_months is not None and (int(requested_months) != int(executed_months)):
        raise ValueError('The executed Momentum period does not match the requested formation_period_months.')

def deterministic_tool_executor_node(state: Dict[str, Any]) -> Dict[str, Any]:
    state['tool_results_by_step'] = {}
    state['tool_result_keys_by_step'] = {}
    start_time = time.perf_counter()
    execution_plan = state.get('execution_plan', [])
    tool_registry = state.get('tool_registry', TOOL_REGISTRY if 'TOOL_REGISTRY' in globals() else {})
    if not isinstance(execution_plan, list):
        raise TypeError('execution_plan must be a list.')
    if not isinstance(tool_registry, dict) or not tool_registry:
        raise ValueError('TOOL_REGISTRY is not available.')
    execution_order = topological_execution_order(execution_plan) if execution_plan else []
    step_map = {step['step_id']: step for step in execution_plan}
    tool_results = {}
    tool_execution_status = {}
    tool_execution_times = {}
    tool_execution_errors = {}
    effective_execution_scopes = {}
    execution_trace = []
    for step_id in execution_order:
        step = step_map[step_id]
        step_result = execute_plan_step(state=state, step=step, tool_registry=tool_registry, completed_statuses=tool_execution_status)
        if step.get('action_type') == 'execute_tool' and step_result.get('status') == 'FAILED' and (step.get('selected_tool') in tool_registry):
            retry_step = copy.deepcopy(step)
            retry_step_result = execute_plan_step(state=state, step=retry_step, tool_registry=tool_registry, completed_statuses=tool_execution_status)
            if retry_step_result.get('status') != 'FAILED':
                step_result = retry_step_result
        tool_results[step_id] = step_result['outputs']
        tool_execution_status[step_id] = step_result['status']
        tool_execution_times[step_id] = step_result['execution_time_seconds']
        tool_execution_errors[step_id] = step_result['error']
        planned_scope = copy.deepcopy(step.get('execution_scope', {}) or {})
        effective_scope = {'effective_tickers': list(planned_scope.get('tickers', step.get('referenced_tickers', [])) or []), 'effective_start_date': planned_scope.get('start_date'), 'effective_end_date': planned_scope.get('end_date'), 'effective_time_periods': list(planned_scope.get('time_periods', step.get('time_periods', [])) or []), 'effective_time_scope': planned_scope.get('period_type')}
        if step.get('selected_tool') == 'pearson_correlation' and (not effective_scope['effective_time_periods']) and (not effective_scope['effective_start_date']) and (not effective_scope['effective_end_date']):
            effective_scope['effective_time_scope'] = 'full_available_dataset'
        financial_output = (step_result.get('outputs', {}) or {}).get('financial_metrics')
        if isinstance(financial_output, pd.DataFrame) and (not financial_output.empty):
            decoded_rows = [decode_financial_metrics_index(index_value) for index_value in financial_output.index]
            decoded_tickers = sorted({str(item.get('ticker', '')).upper() for item in decoded_rows if item.get('ticker')})
            decoded_starts = sorted({str(item.get('start_date')) for item in decoded_rows if item.get('start_date')})
            decoded_ends = sorted({str(item.get('end_date')) for item in decoded_rows if item.get('end_date')})
            if decoded_tickers:
                effective_scope['effective_tickers'] = decoded_tickers
            if len(decoded_starts) == 1:
                effective_scope['effective_start_date'] = decoded_starts[0]
            if len(decoded_ends) == 1:
                effective_scope['effective_end_date'] = decoded_ends[0]
        effective_execution_scopes[step_id] = effective_scope
        execution_trace.append({'step_id': step_id, 'action_type': step_result['action_type'], 'selected_tool': step_result['selected_tool'], 'source': step_result['source'], 'status': step_result['status'], 'execution_time_seconds': step_result['execution_time_seconds'], 'output_fields': step_result['output_fields'], 'ignored_parameters': step_result['ignored_parameters'], 'error': step_result['error'], 'output_validation': step_result.get('output_validation'), 'effective_execution_scope': effective_scope})
        consolidate_step_result(state=state, step_result=step_result)
        if STOP_ON_FIRST_ERROR and step_result['status'] == 'FAILED':
            break
    total_time = time.perf_counter() - start_time
    completed_steps = sum((status in {'COMPLETED', 'REUSED', 'SKIPPED_SYNTHESIS', 'SKIPPED'} for status in tool_execution_status.values()))
    failed_steps = sum((status == 'FAILED' for status in tool_execution_status.values()))
    blocked_steps = sum((status == 'BLOCKED' for status in tool_execution_status.values()))
    overall_status = 'COMPLETED' if execution_plan and failed_steps == 0 and (blocked_steps == 0) else 'PARTIAL' if completed_steps > 0 else 'FAILED'
    execution_summary = {'overall_status': overall_status, 'planned_steps': len(execution_plan), 'executed_steps': len(execution_trace), 'completed_steps': completed_steps, 'failed_steps': failed_steps, 'blocked_steps': blocked_steps, 'reused_steps': sum((status == 'REUSED' for status in tool_execution_status.values())), 'tool_calls': sum((status == 'COMPLETED' for status in tool_execution_status.values())), 'total_execution_time_seconds': round(total_time, 6)}
    return {'tool_results': tool_results, 'tool_execution_status': tool_execution_status, 'tool_execution_times': tool_execution_times, 'tool_execution_errors': tool_execution_errors, 'effective_execution_scopes': effective_execution_scopes, 'tool_result_signatures': state.get('tool_result_signatures', {}), 'execution_trace': execution_trace, 'execution_summary': execution_summary, 'current_question_node': 'tool_execution', 'question_workflow_status': 'tools_executed' if overall_status in {'COMPLETED', 'PARTIAL'} else 'tool_execution_failed', 'next_node': 'evidence_normalization'}
tool_executor_node = deterministic_tool_executor_node
if 'AGENT_REGISTRY' in globals() and 'build_registry_entry' in globals():
    AGENT_REGISTRY[TOOL_EXECUTOR_NODE_NAME] = build_registry_entry(name=TOOL_EXECUTOR_NODE_NAME, function=deterministic_tool_executor_node, component_type='deterministic_node', description='Deterministically executes the plan, reuses compatible outputs, and records results, errors, and execution times.', required_state_fields=['execution_plan', 'tool_registry'], output_fields=['tool_results', 'tool_execution_status', 'tool_execution_times', 'tool_execution_errors', 'tool_result_signatures', 'execution_trace', 'execution_summary'], uses_llm=False)
    final_state['agent_registry'] = AGENT_REGISTRY
final_state.setdefault('tool_results', {})
final_state.setdefault('tool_execution_status', {})
final_state.setdefault('tool_execution_times', {})
final_state.setdefault('tool_execution_errors', {})
final_state.setdefault('execution_trace', [])
final_state.setdefault('execution_summary', {})
final_state.setdefault('tool_results_by_step', {})
final_state.setdefault('tool_output_history', {})

def _safe_nested_get(source: Dict[str, Any], *keys: str, default: Any=None) -> Any:
    current = source
    for key in keys:
        if not isinstance(current, dict):
            return default
        current = current.get(key)
        if current is None:
            return default
    return current
_original_build_execution_signature_box43 = build_execution_signature

def build_execution_signature(step: Dict[str, Any]) -> Dict[str, Any]:
    base = _original_build_execution_signature_box43(step)
    periods = step.get('time_periods') or base.get('time_periods') or []
    tickers = step.get('referenced_tickers') or base.get('tickers') or []
    metric = step.get('metric') or base.get('metric') or ''
    params = step.get('tool_parameters') or base.get('parameters') or {}
    selection = step.get('result_selection') or base.get('result_selection') or {'type': 'all', 'size': None}
    sig = build_canonical_result_signature(step.get('selected_tool') or base.get('tool_name'), tickers, periods, metric, selection, params)
    sig['atomic_id'] = step.get('atomic_id') or build_atomic_id(sig['tool_name'], sig['tickers'], metric, (sig['time_periods'] or [''])[0])
    return sig

def build_result_signature_id(signature: Dict[str, Any]) -> str:
    return canonical_result_signature_id(signature)

def find_reusable_result_entry(state: Dict[str, Any], requested_signature: Dict[str, Any]):
    store = state.get('tool_results_by_key', {}) or {}
    for result_key, entry in reversed(list(store.items())):
        if not isinstance(entry, dict):
            continue
        stored = entry.get('result_signature') or {}
        if not isinstance(stored, dict):
            continue
        stored_metric = stored.get('metric') or entry.get('metric') or ''
        candidate = build_canonical_result_signature(stored.get('tool_name', entry.get('tool_name')), stored.get('tickers', entry.get('tickers', [])), stored.get('time_periods', entry.get('time_periods', [])), stored_metric, stored.get('result_selection', entry.get('result_selection')), stored.get('parameters', {}), stored.get('effective_start_date'), stored.get('effective_end_date'))
        if canonical_result_signatures_match(requested_signature, candidate):
            status = str(entry.get('validation_status') or stored.get('validation_status') or '').upper()
            if status and status not in {'PASSED', 'CERTIFIED', 'COMPLETED'}:
                continue
            return (result_key, entry)
    return (None, None)

def find_reusable_result_entry(state: Dict[str, Any], requested_signature: Dict[str, Any]):
    """Choose a validated result covering ALL requested tickers; never accept a partial subset."""
    store = state.get('tool_results_by_key', {}) or {}
    candidates = []
    for key, entry in store.items():
        if not isinstance(entry, dict):
            continue
        stored = entry.get('result_signature') or {}
        if not isinstance(stored, dict) or not stored:
            continue
        signature = build_canonical_result_signature(stored.get('tool_name', entry.get('tool_name')), stored.get('tickers', entry.get('tickers', [])), stored.get('time_periods', entry.get('time_periods', [])), stored.get('metric', entry.get('metric', '')), stored.get('result_selection', entry.get('result_selection')), stored.get('parameters', {}), stored.get('effective_start_date'), stored.get('effective_end_date'))
        if not reusable_signature_covers_request(requested_signature, signature):
            continue
        validation = str(entry.get('validation_status') or stored.get('validation_status') or '').upper()
        if validation and validation not in {'PASSED', 'CERTIFIED', 'COMPLETED'}:
            continue
        if not any((entry.get(k) is not None for k in ('outputs', 'result', 'data', 'tool_result'))):
            continue
        requested_count = len(requested_signature.get('tickers') or [])
        surplus = len(signature.get('tickers') or []) - requested_count
        candidates.append((max(surplus, 0), key, entry))
    if not candidates:
        return (None, None)
    candidates.sort(key=lambda x: x[0])
    return (candidates[0][1], candidates[0][2])
_original_build_execution_signature_requirement_safe = build_execution_signature

def build_execution_signature(step: Dict[str, Any]) -> Dict[str, Any]:
    sig = _original_build_execution_signature_requirement_safe(step)
    if isinstance(sig, dict):
        sig.pop('atomic_id', None)
        sig.pop('requirement_id', None)
        sig.pop('requirement_ids', None)
        sig.pop('satisfies_requirement_ids', None)
    return sig
_original_consolidate_step_result_requirement_map = consolidate_step_result

def consolidate_step_result(state: Dict[str, Any], step_result: Dict[str, Any]) -> None:
    _original_consolidate_step_result_requirement_map(state, step_result)
    step_id = step_result.get('step_id')
    if not step_id:
        return
    step = next((s for s in state.get('execution_plan') or [] if isinstance(s, dict) and s.get('step_id') == step_id), {})
    requirement_ids = list(step.get('requirement_ids') or step.get('satisfies_requirement_ids') or [])
    result_key = (state.get('tool_result_keys_by_step') or {}).get(step_id)
    if result_key and isinstance((state.get('tool_results_by_key') or {}).get(result_key), dict):
        entry = state['tool_results_by_key'][result_key]
        entry['satisfies_requirement_ids'] = requirement_ids
        entry['execution_signature_id'] = canonical_result_signature_id(entry.get('result_signature') or {})
import unicodedata

def _box43_condition_token(value: Any) -> str:
    text = unicodedata.normalize('NFKD', str(value or ''))
    text = ''.join((ch for ch in text if not unicodedata.combining(ch)))
    return re.sub('[^a-z0-9]+', '_', text.lower()).strip('_')

def _box43_metric_family(value: Any) -> str:
    token = _box43_condition_token(value)
    if 'momentum' in token:
        return 'momentum'
    if 'sharpe' in token:
        return 'sharpe'
    if 'volatil' in token or token in {'risk', 'annualized_risk'}:
        return 'volatility'
    if 'beta' in token:
        return 'beta'
    if 'alpha' in token:
        return 'alpha'
    if 'return' in token or 'rendimento' in token or 'performance' in token:
        return 'return'
    return token

def _box43_parse_numeric(value: Any) -> Optional[float]:
    if isinstance(value, (int, float, np.integer, np.floating)) and (not pd.isna(value)):
        return float(value)
    text = str(value or '').strip().replace(',', '.')
    match = re.search('[-+]?\\d+(?:\\.\\d+)?', text)
    if not match:
        return None
    number = float(match.group(0))
    if '%' in text:
        number /= 100.0
    return number

def _box43_normalize_threshold(raw: Any) -> Optional[Dict[str, Any]]:
    if isinstance(raw, dict):
        metric = raw.get('metric') or raw.get('financial_metric') or raw.get('field') or raw.get('indicator') or raw.get('name')
        operator = str(raw.get('operator') or raw.get('op') or raw.get('comparator') or '').strip()
        reference = str(raw.get('reference') or raw.get('reference_type') or raw.get('benchmark') or '').strip().lower()
        value = raw.get('value', raw.get('threshold'))
        text = ' '.join((str(v) for v in raw.values() if v is not None))
    else:
        metric = None
        operator = ''
        reference = ''
        value = None
        text = str(raw or '')
    normalized_text = _box43_condition_token(text)
    if not metric:
        metric = _box43_metric_family(text)
    metric = _box43_metric_family(metric)
    if operator not in {'>', '>=', '<', '<=', '==', '!='}:
        if re.search('\\b(?:below|inferior|sotto|lower|less)\\w*\\b', text, re.I):
            operator = '<'
        elif re.search('\\b(?:above|superior|sopra|higher|greater)\\w*\\b', text, re.I):
            operator = '>'
        elif re.search('\\b(?:positive|positivo|positiva|positivi|positive)\\b', text, re.I):
            operator = '>'
            value = 0 if value is None else value
        elif re.search('\\b(?:negative|negativo|negativa|negativi|negative)\\b', text, re.I):
            operator = '<'
            value = 0 if value is None else value
        else:
            symbol = re.search('(>=|<=|!=|==|>|<)', text)
            operator = symbol.group(1) if symbol else ''
    if reference in {'mean', 'average', 'media', 'cross_section_mean', 'cross_sectional_mean'} or 'average' in normalized_text or 'media' in normalized_text:
        reference = 'mean'
    numeric_value = _box43_parse_numeric(value)
    if numeric_value is None and reference != 'mean':
        symbol_match = re.search('(?:>=|<=|!=|==|>|<)\\s*([-+]?\\d+(?:[\\.,]\\d+)?%?)', text)
        if symbol_match:
            numeric_value = _box43_parse_numeric(symbol_match.group(1))
        elif re.search('\\b(?:positive|positivo|positiva|positivi|negative|negativo|negativa|negativi)\\b', text, re.I):
            numeric_value = 0.0
    if not metric or not operator or (reference != 'mean' and numeric_value is None):
        return None
    return {'metric': metric, 'operator': operator, 'reference': reference or 'value', 'value': numeric_value, 'raw': copy.deepcopy(raw)}

def _box43_ticker_from_index(index_value: Any) -> Optional[str]:
    if 'decode_financial_metrics_index' in globals():
        try:
            decoded = decode_financial_metrics_index(index_value)
            ticker = str(decoded.get('ticker') or '').strip().upper()
            if ticker:
                return ticker
        except Exception:
            pass
    text = str(index_value or '').strip()
    if not text:
        return None
    return text.split('_')[0].upper()

def _box43_collect_metric_values(tool_results: Dict[str, Any]) -> Dict[str, Dict[str, float]]:
    metric_values: Dict[str, Dict[str, float]] = {}

    def register(metric_name: Any, ticker: Any, value: Any) -> None:
        family = _box43_metric_family(metric_name)
        ticker_text = str(ticker or '').strip().upper()
        if not family or not ticker_text:
            return
        try:
            numeric = float(value)
        except Exception:
            return
        if pd.isna(numeric):
            return
        metric_values.setdefault(family, {})[ticker_text] = numeric
    for outputs in (tool_results or {}).values():
        if not isinstance(outputs, dict):
            continue
        for output_name, obj in outputs.items():
            if not isinstance(obj, pd.DataFrame) or obj.empty:
                continue
            ticker_column = next((c for c in obj.columns if _box43_condition_token(c) == 'ticker'), None)
            for idx, row in obj.iterrows():
                ticker = row.get(ticker_column) if ticker_column is not None else _box43_ticker_from_index(idx)
                if not ticker:
                    continue
                for column in obj.columns:
                    if column == ticker_column:
                        continue
                    register(column, ticker, row.get(column))
    return metric_values

def _box43_compare(value: float, operator: str, threshold: float) -> bool:
    if operator == '>':
        return value > threshold
    if operator == '>=':
        return value >= threshold
    if operator == '<':
        return value < threshold
    if operator == '<=':
        return value <= threshold
    if operator == '==':
        return value == threshold
    if operator == '!=':
        return value != threshold
    return False

def _box43_apply_condition_filter(*, state: Dict[str, Any], execution_result: Dict[str, Any], execution_plan: List[Dict[str, Any]]) -> Dict[str, Any]:
    entities = state.get('extracted_entities', {}) or {}
    thresholds = copy.deepcopy(entities.get('thresholds', []) or [])
    for step in execution_plan or []:
        if isinstance(step, dict) and step.get('thresholds'):
            thresholds = copy.deepcopy(step.get('thresholds') or [])
            break
    selection = entities.get('result_selection', {}) or {}
    selection_type = str(selection.get('type', 'all') or 'all').strip().lower()
    if selection_type not in {'', 'all', 'none'} or not thresholds:
        return {'applied': False, 'reason': 'ranking_selection_or_no_thresholds', 'thresholds': thresholds, 'logic': 'AND', 'filtered_tickers': []}
    normalized_conditions = [condition for condition in (_box43_normalize_threshold(item) for item in thresholds) if condition is not None]
    if not normalized_conditions:
        return {'applied': False, 'reason': 'no_parseable_thresholds', 'thresholds': thresholds, 'logic': 'AND', 'filtered_tickers': []}
    logic = 'AND'
    for step in execution_plan or []:
        if isinstance(step, dict) and str(step.get('threshold_logic', '')).upper() in {'AND', 'OR'}:
            logic = str(step['threshold_logic']).upper()
            break
    metric_values = _box43_collect_metric_values(execution_result.get('tool_results', {}) or {})
    condition_results = []
    candidate_sets = []
    for condition in normalized_conditions:
        values = metric_values.get(condition['metric'], {}) or {}
        if not values:
            condition_results.append({**condition, 'status': 'metric_not_available', 'matched_tickers': []})
            candidate_sets.append(set())
            continue
        if condition['reference'] == 'mean':
            threshold_value = float(np.mean(list(values.values())))
        else:
            threshold_value = float(condition['value'])
        matched = {ticker for ticker, metric_value in values.items() if _box43_compare(metric_value, condition['operator'], threshold_value)}
        candidate_sets.append(matched)
        condition_results.append({**condition, 'status': 'evaluated', 'resolved_threshold': threshold_value, 'matched_tickers': sorted(matched)})
    if not candidate_sets or any((item.get('status') != 'evaluated' for item in condition_results)):
        return {'applied': False, 'reason': 'one_or_more_condition_metrics_unavailable', 'thresholds': thresholds, 'normalized_conditions': condition_results, 'logic': logic, 'filtered_tickers': []}
    selected = set.union(*candidate_sets) if logic == 'OR' else set.intersection(*candidate_sets)
    return {'applied': True, 'reason': 'deterministic_multi_condition_filter', 'thresholds': thresholds, 'normalized_conditions': condition_results, 'logic': logic, 'filtered_tickers': sorted(selected)}
_original_deterministic_tool_executor_node_condition_filter = deterministic_tool_executor_node

def deterministic_tool_executor_node(state: Dict[str, Any]) -> Dict[str, Any]:
    result = _original_deterministic_tool_executor_node_condition_filter(state)
    execution_plan = state.get('execution_plan', []) or []
    condition_filter_result = _box43_apply_condition_filter(state=state, execution_result=result, execution_plan=execution_plan)
    for step in execution_plan:
        if isinstance(step, dict):
            step['condition_filter_result'] = copy.deepcopy(condition_filter_result)
    result['condition_filter_result'] = condition_filter_result
    result['filtered_tickers'] = list(condition_filter_result.get('filtered_tickers', []))
    result['execution_plan'] = execution_plan
    return result
tool_executor_node = deterministic_tool_executor_node
if 'AGENT_REGISTRY' in globals() and TOOL_EXECUTOR_NODE_NAME in AGENT_REGISTRY:
    try:
        AGENT_REGISTRY[TOOL_EXECUTOR_NODE_NAME]['function'] = deterministic_tool_executor_node
    except Exception:
        pass

def _box43_collect_metric_values_from_step(tool_results: Dict[str, Any], *, metric: str, source_step_id: Optional[str]=None) -> Dict[str, float]:
    values: Dict[str, float] = {}
    if source_step_id:
        selected_outputs = {source_step_id: (tool_results or {}).get(source_step_id, {})}
    else:
        selected_outputs = tool_results or {}
    for step_id, outputs in selected_outputs.items():
        if not isinstance(outputs, dict):
            continue
        for output_name, obj in outputs.items():
            if not isinstance(obj, pd.DataFrame) or obj.empty:
                continue
            ticker_column = next((c for c in obj.columns if _box43_condition_token(c) == 'ticker'), None)
            for idx, row in obj.iterrows():
                ticker = row.get(ticker_column) if ticker_column is not None else _box43_ticker_from_index(idx)
                ticker_text = str(ticker or '').strip().upper()
                if not ticker_text:
                    continue
                for column in obj.columns:
                    if column == ticker_column:
                        continue
                    if _box43_metric_family(column) != metric:
                        continue
                    try:
                        numeric = float(row.get(column))
                    except Exception:
                        continue
                    if pd.isna(numeric):
                        continue
                    values[ticker_text] = numeric
    return values

def _box43_apply_condition_filter(*, state: Dict[str, Any], execution_result: Dict[str, Any], execution_plan: List[Dict[str, Any]]) -> Dict[str, Any]:
    entities = state.get('extracted_entities', {}) or {}
    thresholds = copy.deepcopy(entities.get('thresholds', []) or [])
    for step in execution_plan or []:
        if isinstance(step, dict) and step.get('thresholds'):
            thresholds = copy.deepcopy(step.get('thresholds') or [])
            break
    selection = entities.get('result_selection', {}) or {}
    selection_type = str(selection.get('type', 'all') or 'all').strip().lower()
    if selection_type not in {'', 'all', 'none'} or not thresholds:
        return {'applied': False, 'reason': 'ranking_selection_or_no_thresholds', 'thresholds': thresholds, 'logic': 'AND', 'filtered_tickers': []}
    normalized_conditions = []
    for item in thresholds:
        condition = _box43_normalize_threshold(item)
        if condition is None:
            continue
        if isinstance(item, dict):
            condition['source_step_id'] = item.get('source_step_id')
            condition['source_tool'] = item.get('source_tool')
            condition['source_period'] = copy.deepcopy(item.get('source_period'))
        normalized_conditions.append(condition)
    if not normalized_conditions:
        return {'applied': False, 'reason': 'no_parseable_thresholds', 'thresholds': thresholds, 'logic': 'AND', 'filtered_tickers': []}
    logic = 'AND'
    for step in execution_plan or []:
        if isinstance(step, dict) and str(step.get('threshold_logic', '')).upper() in {'AND', 'OR'}:
            logic = str(step['threshold_logic']).upper()
            break
    tool_results = execution_result.get('tool_results', {}) or {}
    condition_results = []
    candidate_sets = []
    for condition in normalized_conditions:
        source_step_id = condition.get('source_step_id')
        values = _box43_collect_metric_values_from_step(tool_results, metric=condition['metric'], source_step_id=source_step_id)
        if not values:
            condition_results.append({**condition, 'status': 'metric_not_available_in_bound_step', 'matched_tickers': []})
            candidate_sets.append(set())
            continue
        if condition['reference'] == 'mean':
            threshold_value = float(np.mean(list(values.values())))
        else:
            threshold_value = float(condition['value'])
        matched = {ticker for ticker, metric_value in values.items() if _box43_compare(metric_value, condition['operator'], threshold_value)}
        candidate_sets.append(matched)
        condition_results.append({**condition, 'status': 'evaluated', 'resolved_threshold': threshold_value, 'matched_tickers': sorted(matched)})
    if not candidate_sets or any((item.get('status') != 'evaluated' for item in condition_results)):
        return {'applied': False, 'reason': 'one_or_more_condition_metrics_unavailable', 'thresholds': thresholds, 'normalized_conditions': condition_results, 'logic': logic, 'filtered_tickers': []}
    selected = set.union(*candidate_sets) if logic == 'OR' else set.intersection(*candidate_sets)
    return {'applied': True, 'reason': 'deterministic_multi_condition_filter_period_result_aware', 'thresholds': thresholds, 'normalized_conditions': condition_results, 'logic': logic, 'filtered_tickers': sorted(selected)}
from datetime import datetime, date
EVIDENCE_NORMALIZER_NODE_NAME = 'evidence_normalizer'
SUCCESSFUL_TOOL_STATUSES = {'COMPLETED', 'REUSED'}
NON_EXECUTION_ACTIONS = {'synthesis_only', 'clarification', 'unsupported'}
MAX_SELECTED_EVIDENCE = None
MAX_EVIDENCE_ROWS = globals().get('MAX_OUTPUT_ROWS', None)
MAX_EVIDENCE_COLUMNS = globals().get('MAX_OUTPUT_COLUMNS', None)
MAX_EVIDENCE_TEXT_LENGTH = globals().get('MAX_TEXT_LENGTH', None)
MAX_EVIDENCE_VALUE_CHARACTERS = None
MAX_EVIDENCE_PACKAGE_CHARACTERS = globals().get('MAX_JSON_CHARACTERS', None)

def _build_current_flow_context_evidence(state: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Transforms the validated context retrieved from the current flow into
    reusable evidence, preserving its provenance.
    """
    context_evidence = []
    retrieved_current_flow = state.get('retrieved_current_flow', [])
    for index, item in enumerate(_evidence_ensure_list(retrieved_current_flow)):
        if not isinstance(item, dict):
            continue
        selected_tickers = copy.deepcopy(item.get('selected_tickers', []))
        time_periods = copy.deepcopy(item.get('time_periods', []))
        if not time_periods:
            execution_plan = item.get('execution_plan', [])
            for step in _evidence_ensure_list(execution_plan):
                if not isinstance(step, dict):
                    continue
                execution_scope = step.get('execution_scope', {})
                if isinstance(execution_scope, dict):
                    step_periods = execution_scope.get('time_periods', [])
                    for period in _evidence_ensure_list(step_periods):
                        if period and period not in time_periods:
                            time_periods.append(period)
        previous_answer = item.get('answer', '')
        context_evidence.append({'evidence_id': f'CURRENT_FLOW::{index + 1}', 'source': 'retrieved_current_flow', 'provenance': 'current_flow', 'component_id': item.get('component_id'), 'metric': item.get('metric'), 'component_signature': copy.deepcopy(item.get('component_signature', {})), 'value': {'selected_tickers': selected_tickers, 'time_periods': time_periods, 'answer': previous_answer}})
    return context_evidence

def _evidence_ensure_list(value: Any) -> List[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, (tuple, set)):
        return list(value)
    return [value]

def _evidence_unique_strings(values: Sequence[Any], uppercase: bool=False) -> List[str]:
    unique_values = []
    seen = set()
    for value in _evidence_ensure_list(values):
        text = str(value).strip()
        if not text:
            continue
        if uppercase:
            text = text.upper()
        if text in seen:
            continue
        seen.add(text)
        unique_values.append(text)
    return unique_values

def _evidence_is_empty(value: Any) -> bool:
    if value is None:
        return True
    if isinstance(value, pd.DataFrame):
        return value.empty
    if isinstance(value, pd.Series):
        return value.empty
    if isinstance(value, (dict, list, tuple, set, str)):
        return len(value) == 0
    return False

def _evidence_json_length(value: Any) -> int:
    try:
        normalized = normalize_for_json(value, max_rows=MAX_EVIDENCE_ROWS, max_columns=MAX_EVIDENCE_COLUMNS, max_text_length=MAX_EVIDENCE_TEXT_LENGTH) if 'normalize_for_json' in globals() else value
        return len(json.dumps(normalized, ensure_ascii=False, default=str))
    except Exception:
        return len(str(value))

def _normalize_evidence_value(value: Any) -> Tuple[Any, bool, int]:
    if 'normalize_for_json' not in globals():
        raise RuntimeError('normalize_for_json is not available. Run BOX 39 first.')
    normalized_value = normalize_for_json(value, max_rows=MAX_EVIDENCE_ROWS, max_columns=MAX_EVIDENCE_COLUMNS, max_text_length=MAX_EVIDENCE_TEXT_LENGTH)
    serialized_value = json.dumps(normalized_value, ensure_ascii=False, default=str)
    original_character_count = len(serialized_value)
    if MAX_EVIDENCE_VALUE_CHARACTERS is None or original_character_count <= MAX_EVIDENCE_VALUE_CHARACTERS:
        return (normalized_value, False, original_character_count)
    compact_preview = {'object_type': type(value).__name__, 'preview': serialized_value[:MAX_EVIDENCE_VALUE_CHARACTERS], 'truncated': True, 'original_character_count': original_character_count}
    return (compact_preview, True, original_character_count)

def _get_expected_outputs(step: Dict[str, Any], tool_registry: Dict[str, Any]) -> List[str]:
    expected_outputs = step.get('required_outputs') or step.get('reused_outputs') or []
    if expected_outputs:
        return _evidence_unique_strings(expected_outputs)
    selected_tool = step.get('selected_tool')
    if selected_tool and selected_tool in tool_registry:
        return _evidence_unique_strings(tool_registry[selected_tool].get('output_fields', []))
    return []

def _build_missing_information(step: Dict[str, Any], reason: str, missing_outputs: Sequence[str]=(), execution_status: str='', error: Any=None) -> Dict[str, Any]:
    return {'step_id': step.get('step_id'), 'sub_question_id': step.get('sub_question_id'), 'objective': step.get('objective', ''), 'selected_tool': step.get('selected_tool'), 'action_type': step.get('action_type'), 'execution_status': execution_status, 'missing_outputs': list(missing_outputs), 'reason': reason, 'error': str(error) if error else None}

def _trim_evidence_package(selected_evidence: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], int, int]:
    selected = copy.deepcopy(selected_evidence)
    removed_for_size = 0
    final_size = _evidence_json_length(selected)
    return (selected, removed_for_size, final_size)

def _extract_certified_momentum_time_period(tool_result: Any) -> List[str]:
    if not isinstance(tool_result, dict):
        return []
    context = tool_result.get('momentum_context', {})
    if not isinstance(context, dict):
        return []
    time_horizon = str(context.get('time_horizon', '')).strip()
    if not time_horizon:
        return []
    return [time_horizon]

def evidence_normalizer_node(state: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(state, dict):
        raise TypeError('state must be a dictionary.')
    execution_plan = state.get('execution_plan', [])
    tool_results = state.get('tool_results', {})
    tool_execution_status = state.get('tool_execution_status', {})
    tool_execution_errors = state.get('tool_execution_errors', {})
    tool_registry = state.get('tool_registry', globals().get('TOOL_REGISTRY', {}))
    if not isinstance(execution_plan, list):
        raise TypeError('execution_plan must be a list.')
    if not isinstance(tool_results, dict):
        raise TypeError('tool_results must be a dictionary.')
    if not isinstance(tool_execution_status, dict):
        raise TypeError('tool_execution_status must be a dictionary.')
    normalized_tool_results = {}
    candidate_evidence = []
    missing_information = []
    seen_evidence = set()
    for plan_position, step in enumerate(execution_plan, start=1):
        if not isinstance(step, dict):
            continue
        step_id = str(step.get('step_id', f'STEP_{plan_position}'))
        action_type = str(step.get('action_type', ''))
        execution_status = str(tool_execution_status.get(step_id, ''))
        selected_tool = step.get('selected_tool')
        atomic_capm_metric = {'capm_beta': 'capm_beta', 'capm_alpha': 'capm_alpha', 'capm_expected_return': 'capm_expected_return'}.get(str(selected_tool or ''))
        if atomic_capm_metric and (not step.get('metric')):
            step = copy.deepcopy(step)
            step['metric'] = atomic_capm_metric
        expected_outputs = _get_expected_outputs(step=step, tool_registry=tool_registry)
        if action_type == 'synthesis_only':
            continue
        if action_type in {'clarification', 'unsupported'}:
            missing_information.append(_build_missing_information(step=step, reason='The step does not produce evidence because it requires clarification or concerns an unsupported request.', execution_status=execution_status))
            continue
        if execution_status not in SUCCESSFUL_TOOL_STATUSES:
            missing_information.append(_build_missing_information(step=step, reason='The step did not produce a usable result.', missing_outputs=expected_outputs, execution_status=execution_status, error=tool_execution_errors.get(step_id)))
            continue
        step_outputs = tool_results.get(step_id, {})
        if not step_outputs:
            tool_results_by_key = state.get('tool_results_by_key', {})
            if isinstance(tool_results_by_key, dict):
                requested_tool = str(step.get('selected_tool', '')).strip().lower()
                requested_metric = str(step.get('metric', '')).strip().lower()
                requested_periods = {str(value).strip().upper() for value in step.get('time_periods', []) or [] if str(value).strip()}
                requested_tickers = {str(value).strip().upper() for value in step.get('referenced_tickers', []) or [] if str(value).strip()}
                for stored_entry in reversed(list(tool_results_by_key.values())):
                    if not isinstance(stored_entry, dict):
                        continue
                    stored_signature = stored_entry.get('result_signature', {}) or {}
                    stored_outputs = stored_entry.get('outputs', {}) or {}
                    stored_tool = str(stored_entry.get('tool_name', stored_signature.get('tool_name', ''))).strip().lower()
                    stored_periods = {str(value).strip().upper() for value in stored_signature.get('time_periods', []) or [] if str(value).strip()}
                    stored_tickers = {str(value).strip().upper() for value in stored_signature.get('tickers', []) or [] if str(value).strip()}
                    metadata_metrics = {str(value.get('metric', '')).strip().lower() for value in stored_outputs.values() if isinstance(value, dict) and value.get('metric')}
                    stored_metric = str(stored_signature.get('metric', '')).strip().lower()
                    tool_matches = not requested_tool or stored_tool == requested_tool
                    metric_matches = not requested_metric or stored_metric == requested_metric or requested_metric in metadata_metrics or (requested_metric in stored_tool)
                    period_matches = not requested_periods or requested_periods.issubset(stored_periods)
                    ticker_matches = not requested_tickers or requested_tickers.issubset(stored_tickers)
                    if tool_matches and metric_matches and period_matches and ticker_matches and isinstance(stored_outputs, dict) and stored_outputs:
                        step_outputs = stored_outputs
                        break
        if not isinstance(step_outputs, dict):
            step_outputs = {'result': step_outputs}
        planned_period_type = str((step.get('execution_scope', {}) or {}).get('period_type', (step.get('tool_parameters', {}) or {}).get('period_type', ''))).strip().lower()
        if selected_tool == 'financial_metrics' and planned_period_type == 'rolling':
            financial_metrics_report = step_outputs.get('financial_metrics_report', {})
            output_period_mode = str(financial_metrics_report.get('period_mode', '')).strip().lower() if isinstance(financial_metrics_report, dict) else ''
            if output_period_mode != 'exact_interval':
                missing_information.append(_build_missing_information(step=step, reason="financial_metrics output is temporally incompatible: the plan requires a rolling period but the tool did not certify period_mode='exact_interval'.", missing_outputs=_get_expected_outputs(step=step, tool_registry=tool_registry), execution_status=execution_status))
                continue
        available_output_names = list(step_outputs.keys())
        outputs_to_consider = expected_outputs if expected_outputs else available_output_names
        missing_outputs = [output_name for output_name in outputs_to_consider if output_name not in step_outputs or _evidence_is_empty(step_outputs.get(output_name))]
        if missing_outputs:
            missing_information.append(_build_missing_information(step=step, reason='One or more outputs required by the plan are not available.', missing_outputs=missing_outputs, execution_status=execution_status))
        normalized_step_outputs = {}
        for output_name in outputs_to_consider:
            if output_name not in step_outputs:
                continue
            if selected_tool == 'press_release_fy2025' and output_name == 'press_release_query':
                normalized_step_outputs[output_name] = normalize_for_json(step_outputs[output_name])
                continue
            raw_value = step_outputs[output_name]
            if _evidence_is_empty(raw_value):
                continue
            if selected_tool == 'press_release_fy2025' and output_name == 'press_release_result' and isinstance(raw_value, dict):
                normalized_step_outputs[output_name] = normalize_for_json(raw_value)
                press_release_evidence = raw_value.get('evidence', [])
                if not isinstance(press_release_evidence, list):
                    press_release_evidence = []
                effective_scope = state.get('effective_execution_scopes', {}).get(step_id, {}) or {}
                for evidence_index, evidence_item in enumerate(press_release_evidence, start=1):
                    if not isinstance(evidence_item, dict):
                        continue
                    evidence_text = str(evidence_item.get('evidence_text', '')).strip()
                    if not evidence_text:
                        continue
                    evidence_key = (step_id, f'{output_name}::{evidence_index}')
                    if evidence_key in seen_evidence:
                        continue
                    seen_evidence.add(evidence_key)
                    candidate_evidence.append({'evidence_id': f'{step_id}::{output_name}::{evidence_index}', 'plan_position': plan_position, 'step_id': step_id, 'sub_question_id': step.get('sub_question_id'), 'objective': step.get('objective', ''), 'selected_tool': selected_tool, 'action_type': action_type, 'source': 'final_state' if execution_status == 'REUSED' else 'tool_execution', 'execution_status': execution_status, 'output_name': output_name, 'result_key': state.get('tool_result_keys_by_step', {}).get(step_id), 'result_selection': step.get('result_selection', {}), 'evidence_role': 'tool_result', 'financial_concepts': _evidence_unique_strings(step.get('financial_concepts', [])), 'referenced_tickers': _evidence_unique_strings(step.get('referenced_tickers', []), uppercase=True), 'time_periods': _evidence_unique_strings(step.get('time_periods', [])), 'component_id': raw_value.get('component_id') or step.get('component_id'), 'metric': raw_value.get('metric') or step.get('metric'), 'retrieval_status': raw_value.get('retrieval_status'), 'requested_metric': evidence_item.get('requested_metric') or raw_value.get('requested_metric') or raw_value.get('metric'), 'section_title': evidence_item.get('section_title'), 'matched_metric': evidence_item.get('matched_metric') or raw_value.get('matched_metrics'), 'effective_tickers': _evidence_unique_strings(effective_scope.get('effective_tickers', step.get('referenced_tickers', [])), uppercase=True), 'effective_start_date': effective_scope.get('effective_start_date'), 'effective_end_date': effective_scope.get('effective_end_date'), 'effective_time_periods': _evidence_unique_strings(effective_scope.get('effective_time_periods', step.get('time_periods', []))), 'effective_time_scope': effective_scope.get('effective_time_scope'), 'value': {'section': evidence_item.get('section'), 'evidence_text': evidence_text}, 'display_value': {'section': evidence_item.get('section'), 'evidence_text': evidence_text}, 'value_truncated': False, 'original_character_count': len(evidence_text)})
                continue
            normalized_value, value_truncated, original_character_count = _normalize_evidence_value(raw_value)
            normalized_step_outputs[output_name] = normalized_value
            evidence_key = (step_id, str(output_name))
            if evidence_key in seen_evidence:
                continue
            seen_evidence.add(evidence_key)
            effective_scope = state.get('effective_execution_scopes', {}).get(step_id, {}) or {}
            if selected_tool == 'pearson_correlation':
                effective_scope = dict(effective_scope)
                effective_scope['effective_time_periods'] = []
                effective_scope['effective_start_date'] = None
                effective_scope['effective_end_date'] = None
                effective_scope['effective_time_scope'] = 'full_available_dataset'
            candidate_evidence.append({'evidence_id': f'{step_id}::{output_name}', 'plan_position': plan_position, 'step_id': step_id, 'sub_question_id': step.get('sub_question_id'), 'objective': step.get('objective', ''), 'selected_tool': selected_tool, 'action_type': action_type, 'source': 'final_state' if execution_status == 'REUSED' else 'tool_execution', 'execution_status': execution_status, 'output_name': output_name, 'result_key': state.get('tool_result_keys_by_step', {}).get(step_id), 'result_selection': step.get('result_selection', {}), 'evidence_role': 'tool_result', 'financial_concepts': _evidence_unique_strings(step.get('financial_concepts', [])), 'referenced_tickers': _evidence_unique_strings(step.get('referenced_tickers', []), uppercase=True), 'time_periods': _evidence_unique_strings(step.get('time_periods', [])), 'component_id': raw_value.get('component_id') if isinstance(raw_value, dict) and raw_value.get('component_id') else step.get('component_id'), 'metric': step.get('metric'), 'retrieval_status': raw_value.get('retrieval_status') if isinstance(raw_value, dict) else None, 'requested_metric': raw_value.get('requested_metric') if isinstance(raw_value, dict) else None, 'matched_metric': raw_value.get('matched_metric', raw_value.get('matched_metrics')) if isinstance(raw_value, dict) else None, 'effective_tickers': _evidence_unique_strings(effective_scope.get('effective_tickers', step.get('referenced_tickers', [])), uppercase=True), 'effective_start_date': effective_scope.get('effective_start_date'), 'effective_end_date': effective_scope.get('effective_end_date'), 'effective_time_periods': _evidence_unique_strings(effective_scope.get('effective_time_periods', step.get('time_periods', []))), 'effective_time_scope': effective_scope.get('effective_time_scope'), 'value': normalized_value, 'display_value': format_financial_response_structure(normalized_value) if 'format_financial_response_structure' in globals() else normalized_value, 'value_truncated': value_truncated, 'original_character_count': original_character_count})
        if normalized_step_outputs:
            normalized_tool_results[step_id] = {'selected_tool': selected_tool, 'execution_status': execution_status, 'outputs': normalized_step_outputs}
    candidate_evidence = sorted(candidate_evidence, key=lambda item: (item.get('plan_position', 10 ** 9), str(item.get('output_name', ''))))
    required_component_ids = {str(step.get('component_id')) for step in execution_plan if isinstance(step, dict) and step.get('component_id')}
    reuse_component_ids = {str(step.get('component_id')) for step in execution_plan if isinstance(step, dict) and step.get('action_type') == 'reuse_output' and step.get('component_id')}
    current_flow_context_evidence = _build_current_flow_context_evidence(state) if reuse_component_ids else []
    current_flow_context_evidence = [item for item in current_flow_context_evidence if str(item.get('component_id')) in reuse_component_ids]
    candidate_evidence.extend(current_flow_context_evidence)
    selected_evidence, removed_for_size, evidence_package_characters = _trim_evidence_package(candidate_evidence)
    if removed_for_size > 0:
        missing_information.append({'step_id': None, 'sub_question_id': None, 'objective': 'Evidence size check', 'selected_tool': None, 'action_type': 'evidence_compaction', 'execution_status': 'COMPACTED', 'missing_outputs': [], 'reason': f'{removed_for_size} evidence items were excluded from the package sent to the model in order to comply with the size limit.', 'error': None})
    selected_evidence_ids = {item['evidence_id'] for item in selected_evidence}
    selected_evidence = [item for item in candidate_evidence if item['evidence_id'] in selected_evidence_ids]
    normalization_summary = {'planned_steps': len(execution_plan), 'successful_execution_steps': sum((str(status) in SUCCESSFUL_TOOL_STATUSES for status in tool_execution_status.values())), 'normalized_steps': len(normalized_tool_results), 'candidate_evidence': len(candidate_evidence), 'selected_evidence': len(selected_evidence), 'required_component_ids': sorted(required_component_ids), 'covered_component_ids': sorted({str(item.get('component_id')) for item in selected_evidence if isinstance(item, dict) and item.get('component_id')}), 'missing_information': len(missing_information), 'removed_for_size': removed_for_size, 'evidence_package_characters': evidence_package_characters, 'within_size_limit': True if MAX_EVIDENCE_PACKAGE_CHARACTERS is None else evidence_package_characters <= MAX_EVIDENCE_PACKAGE_CHARACTERS}
    return {'normalized_tool_results': normalized_tool_results, 'selected_evidence': selected_evidence, 'missing_information': missing_information, 'evidence_normalization_summary': normalization_summary, 'current_question_node': 'evidence_normalization', 'question_workflow_status': 'evidence_normalized', 'next_node': 'answer_synthesis'}
evidence_normalizer = evidence_normalizer_node
if 'AGENT_REGISTRY' in globals() and 'build_registry_entry' in globals():
    AGENT_REGISTRY[EVIDENCE_NORMALIZER_NODE_NAME] = build_registry_entry(name=EVIDENCE_NORMALIZER_NODE_NAME, function=evidence_normalizer_node, component_type='deterministic_node', description='Normalizes tool outputs, selects usable evidence and records missing information.', required_state_fields=['tool_results', 'user_question', 'execution_plan'], output_fields=['normalized_tool_results', 'selected_evidence', 'missing_information', 'evidence_normalization_summary'], uses_llm=False)
    final_state['agent_registry'] = AGENT_REGISTRY
final_state.setdefault('normalized_tool_results', {})
final_state.setdefault('selected_evidence', [])
final_state.setdefault('missing_information', [])
final_state.setdefault('evidence_normalization_summary', {})
_original_evidence_normalizer_node_box44 = evidence_normalizer_node

def evidence_normalizer_node(state: Dict[str, Any]) -> Dict[str, Any]:
    result = _original_evidence_normalizer_node_box44(state)
    plan = {s.get('step_id'): s for s in state.get('execution_plan') or [] if isinstance(s, dict)}
    for item in result.get('selected_evidence', []) or []:
        if not isinstance(item, dict):
            continue
        step = plan.get(item.get('step_id'), {})
        item['atomic_id'] = step.get('atomic_id') or item.get('atomic_id')
        item['metric'] = canonical_metric_name(step.get('metric') or item.get('metric'))
        item['time_periods'] = [canonical_time_period(x) for x in step.get('time_periods') or item.get('time_periods') or [] if canonical_time_period(x)]
    return result

def _req_norm_key(value: Any) -> str:
    return re.sub('[^a-z0-9]+', '', str(value or '').strip().lower())

def _requirement_metric_aliases(metric: Any) -> set:
    m = canonical_metric_name(metric)
    aliases = {'sharpe_ratio': {'sharpe', 'sharperatio', 'sharpe_ratio'}, 'annualized_return': {'annualizedreturn', 'annualisedreturn', 'return', 'annualreturn', 'annualized_return'}, 'annualized_volatility': {'annualizedvolatility', 'annualisedvolatility', 'volatility', 'annualvolatility', 'annualized_volatility'}, 'capm_beta': {'capmbeta', 'beta', 'capm_beta'}, 'momentum': {'momentum', 'momentumreturn', 'momentum_return'}}
    return {_req_norm_key(x) for x in aliases.get(m, {m})}

def _extract_requirement_scalar(value: Any, ticker: Any, metric: Any, period: Any) -> Any:
    ticker_key = str(ticker or '').strip().upper()
    aliases = _requirement_metric_aliases(metric)
    if isinstance(value, pd.DataFrame):
        df = value.copy()
        candidate = df
        ticker_cols = [c for c in df.columns if _req_norm_key(c) in {'ticker', 'symbol', 'stock'}]
        if ticker_key:
            if ticker_cols:
                mask = df[ticker_cols[0]].astype(str).str.upper().eq(ticker_key)
                candidate = df.loc[mask]
            elif ticker_key in {str(i).strip().upper() for i in df.index}:
                candidate = df.loc[[i for i in df.index if str(i).strip().upper() == ticker_key]]
        for col in candidate.columns:
            if _req_norm_key(col) in aliases and len(candidate):
                v = candidate.iloc[0][col]
                if pd.notna(v):
                    return v.item() if hasattr(v, 'item') else v
        return None
    if isinstance(value, pd.Series):
        for k, v in value.items():
            if _req_norm_key(k) in aliases and (not _evidence_is_empty(v)):
                return v.item() if hasattr(v, 'item') else v
        return None
    if isinstance(value, dict):
        if ticker_key:
            for k, v in value.items():
                if str(k).strip().upper() == ticker_key:
                    found = _extract_requirement_scalar(v, ticker, metric, period)
                    if found is not None:
                        return found
        for k, v in value.items():
            if _req_norm_key(k) in aliases and (not isinstance(v, (dict, list, tuple, pd.DataFrame, pd.Series))):
                return v
        for v in value.values():
            found = _extract_requirement_scalar(v, ticker, metric, period)
            if found is not None:
                return found
        return None
    if isinstance(value, (list, tuple)):
        for item in value:
            found = _extract_requirement_scalar(item, ticker, metric, period)
            if found is not None:
                return found
        return None
    if isinstance(value, (int, float, np.number)) and (not isinstance(value, bool)):
        return value.item() if hasattr(value, 'item') else value
    if isinstance(value, str):
        lines = value.splitlines()
        relevant = [line for line in lines if not ticker_key or ticker_key in line.upper()]
        for line in relevant + lines:
            nk = _req_norm_key(line)
            if any((alias in nk for alias in aliases)):
                nums = re.findall('[-+]?\\d+(?:\\.\\d+)?%?', line)
                if nums:
                    return nums[-1]
    return None
_original_evidence_normalizer_node_requirement_split = evidence_normalizer_node

def evidence_normalizer_node(state: Dict[str, Any]) -> Dict[str, Any]:
    result = _original_evidence_normalizer_node_requirement_split(state)
    merged_state = dict(state)
    merged_state.update(result or {})
    raw_evidence = [e for e in merged_state.get('selected_evidence') or [] if isinstance(e, dict)]
    evidence_by_step = {}
    for ev in raw_evidence:
        evidence_by_step.setdefault(ev.get('step_id'), []).append(ev)
    atoms_by_id = {a.get('requirement_id'): a for a in state.get('requirement_atoms') or [] if isinstance(a, dict) and a.get('requirement_id')}
    requirement_evidence = []
    missing = list(merged_state.get('missing_information') or [])
    for step in state.get('execution_plan') or []:
        if not isinstance(step, dict):
            continue
        rids = list(step.get('requirement_ids') or step.get('satisfies_requirement_ids') or [])
        if not rids:
            continue
        step_evidence = evidence_by_step.get(step.get('step_id'), [])
        for rid in rids:
            atom = atoms_by_id.get(rid)
            if not atom:
                continue
            scalar = None
            source_ev = None
            for ev in step_evidence:
                scalar = _extract_requirement_scalar(ev.get('value'), atom.get('ticker'), atom.get('metric'), atom.get('time_period'))
                if scalar is not None:
                    source_ev = ev
                    break
            if scalar is None:
                missing.append({'step_id': step.get('step_id'), 'requirement_id': rid, 'ticker': atom.get('ticker'), 'metric': atom.get('metric'), 'time_period': atom.get('time_period'), 'reason': 'No scalar value could be isolated for the required ticker × metric × period atom.'})
                continue
            base = copy.deepcopy(source_ev or {})
            base.update({'evidence_id': f'REQ_EVIDENCE::{rid}', 'requirement_id': rid, 'atomic_id': rid, 'ticker': atom.get('ticker'), 'referenced_tickers': [atom.get('ticker')] if atom.get('ticker') else [], 'metric': atom.get('metric'), 'time_period': atom.get('time_period'), 'time_periods': [atom.get('time_period')] if atom.get('time_period') else [], 'value': scalar, 'source_evidence_id': (source_ev or {}).get('evidence_id')})
            requirement_evidence.append(base)
    if requirement_evidence:
        combined = list(raw_evidence)
        known_ids = {e.get('evidence_id') for e in combined if isinstance(e, dict)}
        for ev in requirement_evidence:
            if ev.get('evidence_id') not in known_ids:
                combined.append(ev)
                known_ids.add(ev.get('evidence_id'))
        result['selected_evidence'] = combined
        result['requirement_evidence'] = requirement_evidence
    result['missing_information'] = missing
    result['evidence_requirement_ids'] = [e['requirement_id'] for e in requirement_evidence]
    return result
evidence_normalization_node = evidence_normalizer_node
_original_extract_requirement_scalar_period_matrix = _extract_requirement_scalar

def _extract_requirement_scalar(value: Any, ticker: Any, metric: Any, period: Any) -> Any:
    ticker_key = str(ticker or '').strip().upper()

    def _record_ticker(record):
        if not isinstance(record, dict):
            return None
        for key, val in record.items():
            if _req_norm_key(key) in {'ticker', 'symbol', 'stock'}:
                return str(val or '').strip().upper()
        return None
    if isinstance(value, dict) and isinstance(value.get('records'), list):
        records = value.get('records') or []
        if ticker_key:
            tagged = [r for r in records if _record_ticker(r)]
            if tagged:
                records = [r for r in tagged if _record_ticker(r) == ticker_key]
                if not records:
                    return None
        for record in records:
            found = _original_extract_requirement_scalar_period_matrix(record, ticker, metric, period)
            if found is not None:
                return found
        return None
    if isinstance(value, (list, tuple)) and ticker_key:
        tagged = [item for item in value if isinstance(item, dict) and _record_ticker(item)]
        if tagged:
            matching = [item for item in tagged if _record_ticker(item) == ticker_key]
            if not matching:
                return None
            for item in matching:
                found = _original_extract_requirement_scalar_period_matrix(item, ticker, metric, period)
                if found is not None:
                    return found
            return None
    return _original_extract_requirement_scalar_period_matrix(value, ticker, metric, period)
_original_evidence_normalizer_node_condition_contract = evidence_normalizer_node

def _box44_condition_filter_from_state(state: Dict[str, Any], result: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    candidates = [(result or {}).get('condition_filter_result'), state.get('condition_filter_result')]
    for step in state.get('execution_plan') or []:
        if isinstance(step, dict):
            candidates.append(step.get('condition_filter_result'))
    for candidate in candidates:
        if isinstance(candidate, dict) and candidate.get('applied'):
            return copy.deepcopy(candidate)
    return None

def evidence_normalizer_node(state: Dict[str, Any]) -> Dict[str, Any]:
    result = _original_evidence_normalizer_node_condition_contract(state)
    condition_filter_result = _box44_condition_filter_from_state(state, result)
    if not condition_filter_result:
        return result
    filtered_tickers = [str(t).strip().upper() for t in condition_filter_result.get('filtered_tickers') or [] if str(t).strip()]
    condition_filter_result['filtered_tickers'] = filtered_tickers
    result['condition_filter_result'] = condition_filter_result
    result['filtered_tickers'] = filtered_tickers
    selected_evidence = list(result.get('selected_evidence') or [])
    selected_evidence = [e for e in selected_evidence if not (isinstance(e, dict) and e.get('evidence_type') == 'deterministic_condition_filter')]
    selected_evidence.append({'evidence_id': 'DETERMINISTIC_CONDITION_FILTER', 'evidence_type': 'deterministic_condition_filter', 'source': 'BOX_43_DETERMINISTIC_EXECUTOR', 'authoritative': True, 'condition_filter_result': copy.deepcopy(condition_filter_result), 'filtered_tickers': filtered_tickers, 'logic': condition_filter_result.get('logic') or condition_filter_result.get('threshold_logic'), 'conditions': copy.deepcopy(condition_filter_result.get('conditions') or []), 'instruction': 'Deterministic selection result. Downstream LLM agents must preserve this selection and must not recalculate, add, remove, rank or replace tickers unless a separate deterministic ranking/Top-N result in the execution plan explicitly requires it.'})
    result['selected_evidence'] = selected_evidence
    return result
evidence_normalization_node = evidence_normalizer_node
_reuse_integrity_original_evidence_normalizer_node = evidence_normalizer_node

def evidence_normalizer_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """Recover a missing status from a verified output, never from status alone."""
    working = dict(state)
    statuses = dict(state.get('tool_execution_status') or {})
    results = state.get('tool_results') or {}
    by_step = state.get('tool_results_by_step') or {}
    keys = state.get('tool_result_keys_by_step') or {}
    store = state.get('tool_results_by_key') or {}
    repairs = []
    for step in state.get('execution_plan') or []:
        if not isinstance(step, dict):
            continue
        sid = step.get('step_id')
        if not sid or str(statuses.get(sid) or '').upper() in SUCCESSFUL_TOOL_STATUSES:
            continue
        action = str(step.get('action_type') or '').lower()
        if action not in {'reuse_output', 'execute_tool'}:
            continue
        output = results.get(sid) or by_step.get(sid)
        result_key = keys.get(sid)
        stored = store.get(result_key) if isinstance(result_key, str) else None
        if not output or not isinstance(stored, dict):
            continue
        validation = str(stored.get('validation_status') or '').upper()
        if validation and validation not in {'PASSED', 'CERTIFIED', 'COMPLETED'}:
            continue
        signature = stored.get('result_signature') or {}
        requested = step.get('result_signature') or step.get('requested_result_signature')
        if requested and (not reusable_signature_covers_request(requested, signature)):
            continue
        if not signature:
            continue
        statuses[sid] = 'REUSED' if action == 'reuse_output' else 'COMPLETED'
        repairs.append({'step_id': sid, 'reconciled_status': statuses[sid], 'result_key': result_key})
    working['tool_execution_status'] = statuses
    normalized = _reuse_integrity_original_evidence_normalizer_node(working)
    normalized['reuse_status_reconciliation'] = repairs
    return normalized
evidence_normalization_node = evidence_normalizer_node

_box44_original_normalizer_document_status = evidence_normalizer_node
def evidence_normalizer_node(state: Dict[str, Any]) -> Dict[str, Any]:
    result = _box44_original_normalizer_document_status(state)
    check_state = dict(state)
    check_state.update(result or {})
    result['document_retrieval_check'] = dual_domain_post_validation_check(check_state)
    for evidence in result.get('selected_evidence') or []:
        if not isinstance(evidence, dict):
            continue
        evidence_id = str(evidence.get('evidence_id') or '')
        if evidence.get('selected_tool') == 'press_release_fy2025' and '::press_release_result::' in evidence_id:
            evidence.setdefault('parent_evidence_id', evidence_id.rsplit('::', 1)[0])
    return result
evidence_normalization_node = evidence_normalizer_node
import json
import re
from collections import Counter
BOX45_APPROVED_EXAMPLES = json.loads('[{"id": 1, "context": "", "question": "What has IBM\'s volatility been over the last 3 years?", "approved_answer": "IBM\'s annualized volatility over the last 3 years has been 36.06%."}, {"id": 2, "context": "The previous question concerned IBM\'s annualized volatility.", "question": "And what about over the last 2 months?", "approved_answer": "Over the last 2 months (2026-07-16 to 2026-09-16), IBM\'s annualized volatility was 33.99%."}, {"id": 3, "context": "The previous answer established the period from 2026-07-16 to 2026-09-16 and IBM\'s annualized volatility of 33.99%.", "question": "Over the same period, what was IBM\'s return and what was its Return-to-Risk Ratio?", "approved_answer": "Over the 2-month period from 2026-07-16 to 2026-09-16, IBM\'s annualized return was 13.25%,\\nand its Return-to-Risk Ratio (raw) was 0.39."}, {"id": 4, "context": "", "question": "Compare Apple and Microsoft over the last 12 months in terms of return, volatility, and\\nSharpe Ratio, and tell me which one has the better risk-return profile.", "approved_answer": "Over the last 12 months (2025-09-16 to 2026-09-16):\\n\\nApple (AAPL):\\n- Annual Return: 40.95%\\n- Annualized Volatility: 25.03%\\n- Sharpe Ratio: 1.25\\n\\nMicrosoft (MSFT):\\n- Annual Return: -4.08%\\n- Annualized Volatility: 32.12%\\n- Sharpe Ratio: -0.22\\n\\nComparing the two, Apple (AAPL) has a better risk-return profile with a higher annual\\nreturn, lower annualized volatility, and a significantly higher Sharpe Ratio compared to\\nMicrosoft (MSFT)."}, {"id": 5, "context": "", "question": "Which Dow Jones stock has had the highest annualized volatility over the last 6 months?", "approved_answer": "Over the last 6 months (2026-03-16 to 2026-09-16), IBM had the highest annualized\\nvolatility among Dow Jones stocks, at 60.81%."}, {"id": 6, "context": "", "question": "Which pairs of Dow Jones stocks have a correlation above 75%? Among them, which pair\\nhas the highest correlation?", "approved_answer": "The Dow Jones stocks with a correlation above 75% are GS and JPM. This pair also has the\\nhighest correlation, at 0.8020."}, {"id": 7, "context": "", "question": "What is the correlation between IBM and Microsoft over the last 3 months? Is it above\\n75%?", "approved_answer": "The Pearson correlation between IBM and Microsoft over the last 3 months (2026-06-16 to\\n2026-09-16) is 0.1892. This is below 75%."}, {"id": 10, "context": "", "question": "Which are the 5 Dow Jones stocks with the highest 12-month momentum? For each one,\\nindicate its momentum, Dollar Volume, and position in the ranking.", "approved_answer": "The 5 Dow Jones stocks with the highest 12-month momentum are:\\n\\n1. MRK: Momentum of 77.73%, Average Dollar Volume of $ 1,630,428,392.\\n2. CAT: Momentum of 65.52%, Average Dollar Volume of $ 1,908,149,996.\\n3. CSCO: Momentum of 60.73%, Average Dollar Volume of $ 1,531,182,485.\\n4. JNJ: Momentum of 47.40%, Average Dollar Volume of $ 1,639,496,158.\\n5. CVX: Momentum of 41.59%, Average Dollar Volume of $ 1,647,708,499.\\n\\nMomentum is calculated over a time horizon of 12 months."}, {"id": 11, "context": "The previous answer identified the five Dow Jones stocks with the highest 12-month momentum, in descending order: MRK (77.73%), CAT (65.52%), CSCO (60.73%), JNJ (47.40%), and CVX (41.59%).", "question": "Among the 5 stocks with the highest momentum, which one also has the highest Sharpe\\nRatio over the same period?", "approved_answer": "Among the top 5 stocks with the highest momentum over the last 12 months, Johnson &\\nJohnson (JNJ) has the highest Sharpe Ratio of 2.11. The Sharpe Ratios for the other top\\nmomentum stocks over the same period are: Merck & Co. (MRK) at 1.95, Caterpillar (CAT) at\\n1.43, Cisco Systems (CSCO) at 1.36, and Chevron (CVX) at 1.29."}, {"id": 12, "context": "The previous answer established the 12-month momentum ranking: MRK first (77.73%), CAT second (65.52%), CSCO third (60.73%), JNJ fourth (47.40%), and CVX fifth (41.59%). The complete 12-month ranking, where available in prior tool results, is relevant to comparing changes in rank.", "question": "Which are the 5 Dow Jones stocks with the highest 3-month momentum? Compare the\\nranking with the 12-month momentum ranking and indicate which stocks have improved their\\nposition the most.", "approved_answer": "The 5 Dow Jones stocks with the highest 3-month momentum are:\\n\\n1.  CRM with 59.93%\\n2.  MSFT with 31.69%\\n3.  CVX with 28.73%\\n4.  VZ with 19.53%\\n5.  TRV with 15.17%\\n\\nMomentum is calculated over a time horizon of 3 months.\\n\\nComparing the 3-month momentum ranking with the 12-month momentum ranking, the following\\nstocks show significant improvements in their position:\\n\\n- CRM: Improved from rank 18 (12-month momentum of 6.42%) to rank 1 (3-month\\nmomentum of 59.93%).\\n- MSFT: Improved from rank 22 (12-month momentum of -4.56%) to rank 2 (3-month\\nmomentum of 31.69%).\\n- VZ: Improved from rank 10 (12-month momentum of 20.95%) to rank 4 (3-month\\nmomentum of 19.53%).\\n\\nOther stocks in the top 5 for 3-month momentum, CVX and TRV, were already highly\\nranked in the 12-month momentum, at rank 5 and rank 6 respectively."}, {"id": 13, "context": "", "question": "Compare the 6-month and 12-month momentum of Apple, Nvidia, and Amazon, and tell me\\nfor which stocks the more recent momentum indicates an acceleration or slowdown relative\\nto the longer horizon.", "approved_answer": "Momentum is calculated over a time horizon of 6 months and 12 months.\\n\\nFor Apple (AAPL):\\n- 6-month momentum: 31.21%\\n- 12-month momentum: 31.03%\\n\\nFor Nvidia (NVDA):\\n- 6-month momentum: 22.93%\\n- 12-month momentum: 14.92%\\n\\nFor Amazon (AMZN):\\n- 6-month momentum: 18.10%\\n- 12-month momentum: 12.02%\\n\\nComparing the 6-month momentum to the 12-month momentum:\\n- Apple (AAPL) shows an acceleration, with its 6-month momentum (31.21%) being higher than\\nits 12-month momentum (31.03%).\\n- Nvidia (NVDA) shows an acceleration, with its 6-month momentum (22.93%) being higher\\nthan its 12-month momentum (14.92%).\\n- Amazon (AMZN) shows an acceleration, with its 6-month momentum (18.10%) being higher\\nthan its 12-month momentum (12.02%)."}, {"id": 14, "context": "", "question": "Calculate the CAPM for Visa and American Express over the last 3 years and compare\\ntheir Beta, Alpha, and expected return.", "approved_answer": "Over the last 3 years (2023-09-25 to 2026-09-25), the CAPM analysis for Visa (V) and\\nAmerican Express (AXP) shows the following:\\n\\nBeta:\\n- American Express (AXP): 1.4811\\n- Visa (V): 0.8617\\n\\nAlpha:\\n- American Express (AXP): 3.89%\\n- Visa (V): 3.91%\\n\\nExpected Return:\\n- American Express (AXP): 20.53%\\n- Visa (V): 13.20%\\n\\nComparing the two companies:\\n- American Express (AXP) has a higher Beta (1.4811) than Visa (V) (0.8617), indicating\\nthat AXP\'s stock price is more volatile relative to the Dow Jones Industrial Average (DJI)\\nbenchmark. Visa\'s Beta is less than 1, suggesting lower volatility compared to the\\nbenchmark.\\n- Visa (V) has a slightly higher Annual Alpha (3.91%) compared to American Express (AXP)\\n(3.89%), indicating that Visa has generated slightly more excess return relative to its\\nexpected return based on the CAPM model.\\n- American Express (AXP) has a significantly higher CAPM Expected Annual Return (20.53%)\\nthan Visa (V) (13.20%)."}, {"id": 15, "context": "", "question": "Between Visa and American Express, which one simultaneously has lower volatility, a\\nhigher Sharpe Ratio, and a lower Beta over the last 3 years?", "approved_answer": "Over the last 3 years (2023-09-16 to 2026-09-16):\\n\\nVisa (V) had an Annualized Volatility of 20.25%, a Sharpe Ratio of 0.60, and a Beta of\\n0.8663.\\n\\nAmerican Express (AXP) had an Annualized Volatility of 27.41%, a Sharpe Ratio of 0.72, and\\na Beta of 1.4834.\\n\\nComparing the two:\\n\\n- Lower Volatility: Visa (20.25%) had lower volatility than American Express\\n(27.41%).\\n- Higher Sharpe Ratio: American Express (0.72) had a higher Sharpe Ratio than Visa\\n(0.60).\\n- Lower Beta: Visa (0.8663) had a lower Beta than American Express (1.4834).\\n\\nTherefore, Visa simultaneously had lower volatility and a lower Beta, but American Express\\nhad a higher Sharpe Ratio. Neither company simultaneously met all three criteria."}, {"id": 16, "context": "", "question": "What financial and operating results did Boeing report for FY2025, and according to\\nthe release, what were the main drivers of those results?", "approved_answer": "For the full year 2025, Boeing reported revenue of $89.5 billion and 600 commercial\\ndeliveries, marking the highest annual totals since 2018. GAAP earnings per share were\\n$10.23, and core earnings per share (non-GAAP) were $9.92. The company\'s operating cash\\nflow was $1.3 billion, and free cash flow (non-GAAP) was $0.4 billion. The total company\\nbacklog reached a record $682 billion.\\n\\nThe main drivers of these results were:\\n- A $9.6 billion gain on sale from the Digital Aviation Solutions transaction, which\\nincreased earnings per share by $11.83.\\n- Higher commercial deliveries and working capital timing contributed to the operating\\ncash flow.\\n- Higher investments in Charleston and Saint Louis sites led to additions to property,\\nplant, and equipment.\\n- The acquisition of Spirit AeroSystems primarily caused the increase in debt to $54.1\\nbillion from $53.4 billion at the beginning of the quarter.\\n- The record backlog was primarily driven by 1,173 Commercial Airplanes net orders\\nduring the year, with all three segments achieving record levels."}, {"id": 17, "context": "", "question": "What did Boeing\'s management say about its guidance and objectives for 2026?\\nDistinguish the CEO\'s statements from the CFO\'s statements.", "approved_answer": "For 2026, Boeing\'s CEO stated that the company made significant progress on its recovery\\nin 2025 and has set the foundation to maintain momentum. Key objectives include completing\\nthe acquisition of Spirit AeroSystems, selling portions of the Digital Aviation Solutions\\nbusiness, promoting stable operations, completing development programs, rebuilding\\nstakeholder trust, and fully restoring Boeing. No statements from the CFO regarding 2026\\nguidance and objectives were found."}, {"id": 18, "context": "", "question": "Compare Salesforce\'s FY2025 results with Cisco\'s and tell me what differences emerge\\nfrom the information provided in their respective releases.", "approved_answer": "For FY2025, Salesforce reported a total revenue of $37.9 billion, marking a 9%\\nyear-over-year increase (both year-over-year and in constant currency). Its subscription\\nand support revenue reached $35.7 billion, up 10% year-over-year (and in constant\\ncurrency). Salesforce also highlighted $900 million in Data Cloud & AI annual recurring\\nrevenue, an increase of 120% year-over-year, and noted that Data Cloud surpassed 50\\ntrillion records, doubling year-over-year. Additionally, nearly half of the Fortune 100\\nare AI & Data Cloud customers.\\n\\nIn contrast, Cisco reported a FY2025 revenue of $56.7 billion, an increase of 5%\\nyear-over-year. Its GAAP Earnings per Share (EPS) was $2.61, up 3% year-over-year, while\\nNon-GAAP EPS was $3.81, up 2% year-over-year. Cisco\'s cash flow from operating activities\\nfor FY2025 was $14.2 billion, a 30% increase compared to $10.9 billion in fiscal 2024. The\\ncompany also reported that AI Infrastructure orders from webscale customers exceeded $800\\nmillion, bringing the FY2025 total to over $2 billion, more than double its original $1\\nbillion target."}, {"id": 19, "context": "", "question": "19. Compare Walmart\'s FY2025 financial results with the annualized return and annualized volatility of its stock from the beginning of calendar year 2026 to date. What observations can be made by considering the company\'s 2025 financial results, management\'s statements regarding the outlook for 2026, and the stock\'s observed market performance?", "approved_answer": "In fiscal year 2025 (FY2025), Walmart reported revenue of $681.0 billion, an increase of 5.1% (or 5.6%). Operating income increased by $2.3 billion, or 8.6%, and by 9.7% on an adjusted basis, outpacing sales growth. ROA stood at 7.9%, while ROI reached 15.5%, an improvement of 50 basis points. Global inventory increased by 2.8%, including a 3.0% increase at Walmart U.S., with inventory levels considered healthy. The company also increased its dividend by 13% to $0.94 per share, marking its largest increase in more than a decade.\\n\\nDoug McMillon, President and CEO of Walmart, stated that the team had closed the year with strong results, driven by low prices, an expanding assortment, and an e-commerce business offering faster delivery times. He emphasized that the company was gaining market share, maintaining healthy top-line growth, and managing inventory effectively. Looking ahead, the company\'s focus will be on growth, improving operating margins, and strengthening ROI, while investing to better serve customers and members.\\n\\nFrom the beginning of calendar year 2026 to date, Walmart (WMT) stock recorded an annualized return of 0.58% and annualized volatility of 27.38%.\\n\\nConcluding Observations\\n\\nWalmart closed FY2025 with positive financial results, supported by competitive pricing, an expanding product assortment, and e-commerce growth, alongside gains in market share. Management anticipates further growth, improvements in operating margins and ROI, supported in part by additional investments. In 2026, however, the stock has recorded an annualized return of 0.58% and annualized volatility of 27.38%, indicating significant price fluctuations alongside an overall return close to zero.\\n\\nAlthough the available information does not allow for a comprehensive assessment of the underlying dynamics, this market evidence suggests, as a preliminary interpretation, that the company\'s growth prospects may not yet be fully reflected in its stock performance."}, {"id": 20, "context": "", "question": "Among Nvidia, Amazon, and Home Depot, which one has the most favorable overall profile\\nconsidering momentum, Sharpe Ratio, CAPM, and management guidance for 2026? If some\\nelements are not directly comparable, state this explicitly.", "approved_answer": "Nvidia (NVDA) demonstrates the most favorable overall profile among the three companies\\nbased on the provided metrics.\\n\\nMomentum (over a 12-month rolling period):\\n- Nvidia (NVDA): 20.66%\\n- Amazon (AMZN): 13.58%\\n- Home Depot (HD): -25.85%\\n\\nSharpe Ratio (over a 12-month rolling period):\\n- Nvidia (NVDA): 0.54\\n- Amazon (AMZN): 0.27\\n- Home Depot (HD): -1.34\\n\\nCAPM Expected Annual Return (over a 12-month rolling period):\\n- Nvidia (NVDA): 12.20%\\n- Amazon (AMZN): 11.93%\\n- Home Depot (HD): 11.91%\\n\\nManagement Guidance for 2026:\\n- Nvidia (NVDA): Expects revenue of $43.0 billion (±2%), GAAP gross margins of 70.6%\\n(±50 basis points), non-GAAP gross margins of 71.0% (±50 basis points), GAAP operating\\nexpenses of approximately $5.2 billion, non-GAAP operating expenses of approximately $3.6\\nbillion, GAAP and non-GAAP other income of approximately $400 million (excluding certain\\nequity securities), and GAAP and non-GAAP tax rates of 17.0% (±1%, excluding discrete\\nitems).\\n- Amazon (AMZN): For the first quarter of 2026, net sales are expected to be between\\n$173.5 billion and $178.5 billion, representing 11% to 15% growth compared to Q1 2025\\n(including a favorable foreign exchange impact of approximately 180 basis points).\\nOperating income is expected to be between $16.5 billion and $21.5 billion, compared to\\n$18.4 billion in Q1 2025, and includes approximately $1 billion of higher year-over-year\\nAmazon Leo costs, as well as investments in quick commerce and international stores.\\n- Home Depot (HD): No management guidance for 2026 was found in the provided\\nevidence.\\n\\nBased on the quantitative metrics (Momentum, Sharpe Ratio, and CAPM Expected Annual\\nReturn) over a 12-month rolling period, Nvidia consistently shows the strongest\\nperformance. While management guidance for 2026 is available for Nvidia and Amazon, it is\\nnot directly comparable across all companies due to the absence of guidance for Home Depot\\nand the differing nature of the provided guidance details (e.g., full-year for NVDA vs. Q1\\nfor AMZN)."}, {"id": 21, "context": "", "question": "Which Dow Jones stocks have a Pearson correlation above 70% with JPMorgan? Compare their 12-month momentum.", "approved_answer": "The Dow Jones stocks with a Pearson correlation above 70% with JPMorgan, calculated over the entire available historical dataset, are:\\n\\n- GS with a correlation of 0.8017\\n- AXP with a correlation of 0.7022\\n\\nComparing their 12-month Momentum:\\n\\n- GS has a Momentum of 15.83%. - AXP has a Momentum of -15.57%."}, {"id": 22, "context": "", "question": "Compare Boeing and IBM using their FY2025 corporate disclosures and their 12-month stock performance. What does each source tell us, and which conclusions cannot be drawn from the available evidence?", "approved_answer": "For FY2025, Boeing reported revenue of $89.5 billion and 600 commercial deliveries, the\\nhighest annual totals since 2018. GAAP earnings per share were $10.23, and core earnings\\nper share (non-GAAP) were $9.92, primarily reflecting a $9.6 billion gain on sale from the\\nDigital Aviation Solutions transaction, which increased earnings per share by $11.83.\\nOperating cash flow was $1.3 billion, and free cash flow (non-GAAP) was $0.4 billion. The\\ntotal company backlog grew to a record $682 billion, primarily due to 1,173 Commercial\\nAirplanes net orders. Debt increased to $54.1 billion, mainly due to the acquisition of\\nSpirit AeroSystems.\\n\\nFor FY2025, IBM reported revenue of $67.5 billion, up 8% (6% at constant currency), with\\nSoftware revenue up 11% (9% at constant currency), Consulting revenue up 2% (flat at\\nconstant currency), and Infrastructure revenue up 12% (10% at constant currency). The GAAP\\nGross Profit Margin was 58.2%, and the Operating (Non-GAAP) Gross Profit Margin was 59.5%.\\nNet cash from operating activities was $13.2 billion, and free cash flow was $14.7\\nbillion. IBM\'s generative AI book of business reached over $12.5 billion. The company\\ndeclared a quarterly cash dividend of $1.68 per common share.\\n\\nOver the 12-month period from October 1, 2025, to October 1, 2026, Boeing (BA) had an\\nannual return of -10.91% with an annualized volatility of 34.24%. IBM had an annual return\\nof -17.96% with an annualized volatility of 50.82%.\\n\\nBased on the available evidence, although Boeing and IBM reported several positive developments in their FY2025 corporate disclosures, both recorded negative 12-month stock returns: −10.91% and −17.96%, respectively. Both stocks also exhibited substantial annualized volatility, particularly IBM (50.82% versus Boeing’s 34.24%), indicating significant price fluctuations during the period. This highlights a divergence between the positive elements reported in their corporate disclosures and their negative stock performance, with IBM experiencing both greater volatility and a larger decline. However, volatility alone does not explain the negative returns, and the available evidence does not establish their underlying causes."}, {"id": 23, "context": "", "question": "Compare Cisco and IBM using their FY2025 corporate disclosures and their 12-month stock performance. What does each source tell us, and which conclusions cannot be drawn from the available evidence?", "approved_answer": "For FY2025, Cisco reported revenue of $56.7 billion, up 5% year over year. AI infrastructure orders from webscale customers exceeded $800 million in the fourth quarter, bringing the FY2025 total to over $2 billion, more than double the original $1 billion target. GAAP earnings per share were $2.61 (up 3% year over year), and Non-GAAP earnings per share were $3.81 (up 2% year over year). Cash flow from operating activities was $14.2 billion, an increase of 30% compared with $10.9 billion in FY2024. Cisco\'s CFO, Mark Patterson, stated that fourth-quarter revenue, gross margin, and operating margin were at the high end of their guidance ranges, earnings per share exceeded guidance, and the company generated solid operating cash flow. He also emphasized Cisco\'s continued focus on strategic investments in innovation, profitable growth, and shareholder value.\\n\\nFor FY2026, Cisco projected revenue between $59.0 billion and $60.0 billion, GAAP earnings per share between $2.79 and $2.91, and Non-GAAP earnings per share between $4.00 and $4.06. Chuck Robbins, Cisco\'s Chair and CEO, highlighted that AI infrastructure orders had more than doubled the original target, pointing to significant growth opportunities. CFO Mark Patterson reiterated the company\'s focus on innovation investments, profitable growth, and shareholder value creation in 2026.\\n\\nFor FY2025, IBM reported revenue of $67.5 billion, up 8% (6% at constant currency), with Software revenue increasing 11% (9% at constant currency), Consulting revenue increasing 2% (flat at constant currency), and Infrastructure revenue increasing 12% (10% at constant currency). The GAAP gross profit margin was 58.2%, and the operating (Non-GAAP) gross profit margin was 59.5%. Net cash from operating activities was $13.2 billion, and free cash flow was $14.7 billion. IBM\'s generative AI book of business exceeded $12.5 billion. The company declared a quarterly cash dividend of $1.68 per common share. Arvind Krishna, IBM\'s Chairman and CEO, stated that the company achieved strong fourth-quarter revenue growth, with double-digit performance in Software and Infrastructure, while its generative AI business exceeded $12.5 billion. He also emphasized that IBM entered 2026 with momentum and from a position of strength, expecting constant-currency revenue growth above 5% and an approximately $1 billion year-over-year increase in free cash flow.\\n\\nFor FY2026, IBM projected constant-currency revenue growth exceeding 5% and an approximately $1 billion increase in free cash flow compared with the previous year. CEO Arvind Krishna expressed confidence in the company\'s 2026 outlook, highlighting growth in Software, Infrastructure, and generative AI-related activities. CFO James Kavanaugh emphasized the strength of IBM\'s portfolio, innovation, and operational efficiency as factors supporting the company\'s outlook.\\n\\nOver the last 12 months (from October 3, 2025, to October 3, 2026), Cisco (CSCO) recorded an annual return of 68.30% and annualized volatility of 34.75%. Over the same period, IBM recorded an annual return of −20.33% and annualized volatility of 50.91%.\\n\\nCisco\'s and IBM\'s FY2025 corporate disclosures highlight positive results for both companies, accompanied by favorable FY2026 guidance and growth expectations expressed by their management teams. However, their stock performance over the last 12 months reveals a sharp divergence: Cisco recorded a return of +68.30%, consistent with its positive outlook, while IBM posted a return of −20.33%, in clear contrast with the positive expectations expressed by its management for 2026, representing a difference of 88.63 percentage points. Annualized volatility also differed significantly: 34.75% for Cisco versus 50.91% for IBM, a gap of 16.16 percentage points. Overall, Cisco combined a positive corporate outlook with positive stock returns and lower volatility, whereas IBM experienced negative returns and greater price fluctuations despite favorable FY2025 results and management\'s positive growth expectations. The available evidence therefore highlights consistency between Cisco\'s corporate outlook and its stock performance, in contrast to the divergence observed for IBM, without establishing a causal relationship between corporate results, expectations, and stock returns, or demonstrating through stock prices alone whether the FY2026 financial targets were actually achieved."}, {"id": 24, "context": "", "question": "Compare the FY2025 financial results of Apple and Microsoft using their respective\\nofficial earnings releases. Examine revenue growth, profitability, business segment\\nperformance and the principal factors identified by management.", "approved_answer": "For fiscal year 2025, Apple reported record revenue of $416.2 billion, a 6% year-over-year\\nincrease, driven by robust iPhone and Services sales. Net income rose 19.5% to $112.0\\nbillion, with diluted EPS up 22% to $7.46. Operating income increased by 8% to $133.1\\nbillion. The overall gross margin improved to 46.9%, primarily due to higher-margin\\nServices, which saw its margin rise to 75.4%. Operating cash flow was $111.5 billion. Key\\ndrivers for Apple included a 4% increase in iPhone revenue to $209.6 billion, a 12% rise\\nin Mac sales to $33.7 billion, a 5% climb in iPad revenue to $28.0 billion, and a 14%\\nsurge in Services revenue to $109.2 billion. Geographically, net sales grew across the\\nAmericas (+7%), Europe (+10%), Japan (+15%), and Rest of Asia Pacific (+10%), while\\nGreater China declined by 4% due to competitive and macro headwinds.\\n\\nMicrosoft reported revenue of $281.7 billion for fiscal year 2025, an increase of 15%.\\nOperating income grew by 17% to $128.5 billion, and net income increased by 16% to $101.8\\nbillion. Diluted earnings per share were $13.64, up 16%. Microsoft Cloud revenue reached\\n$46.7 billion, up 27% year-over-year. Business segment performance highlights for\\nMicrosoft included a 16% increase in Productivity and Business Processes revenue to $33.1\\nbillion, driven by Microsoft 365 Commercial products and cloud services (up 16%) and\\nMicrosoft 365 Consumer products and cloud services (up 21%). LinkedIn revenue increased by\\n9%, and Dynamics products and cloud services revenue rose by 18%. Intelligent Cloud\\nrevenue was $29.9 billion, up 26%, with server products and cloud services revenue\\nincreasing by 27%, driven by Azure and other cloud services revenue growth of 39%. The\\nchief financial officer of Microsoft highlighted the strong quarter, with Microsoft Cloud\\nrevenue reaching $46.7 billion, up 27% year-over-year, as a key factor in their\\nperformance.\\n\\nComparative Analysis – Apple vs. Microsoft (FY2025)\\nMicrosoft significantly outperformed Apple in revenue growth (+15% vs. +6%) and operating income growth (+17% vs. +8%), demonstrating stronger business expansion. Apple maintained higher absolute revenue ($416.2B vs. $281.7B), net income ($112.0B vs. $101.8B), and operating profitability (32.0% vs. 45.6% for Microsoft, which therefore led on operating margin). Microsoft\'s growth was primarily driven by Azure, cloud services and enterprise demand, while Apple\'s performance relied on iPhone sales and its expanding, high-margin Services business. Overall, Microsoft demonstrated stronger growth and operating efficiency, whereas Apple generated greater absolute earnings and benefited from its diversified hardware-and-services ecosystem."}, {"id": 25, "context": "", "question": "Compare Amazon\'s FY2025 financial performance with its stock\'s annualized return and annualized volatility during calendar year 2026 to date. How do the financial results and management\'s statements about its 2026 outlook relate to observed market performance?", "approved_answer": "In fiscal year 2025, Amazon reported net sales of $716.9 billion, a 12% increase from $638.0 billion in 2024. Operating income rose to $80.0 billion from $68.6 billion in 2024, and net income increased to $77.7 billion, or $7.17 per diluted share, compared with $59.2 billion, or $5.53 per diluted share, in 2024. Operating cash flow increased by 20% to $139.5 billion for the trailing twelve months. However, free cash flow decreased to $11.2 billion for the trailing twelve months, primarily due to a $50.7 billion year-over-year increase in purchases of property and equipment.\\n\\nFor calendar year 2026 to date (January 1, 2026, to October 4, 2026), Amazon\'s annualized return was 8.97%, and its annualized volatility was 34.30%.\\n\\nRegarding management\'s statements about the 2026 outlook, Amazon\'s President and CEO, Andy Jassy, highlighted strong growth in AWS (24%), Advertising (22%), and triple-digit percentage growth in the chips business in 2025. He attributed this growth to rapid innovation and addressing customer problems. For 2026, he stated an expectation to invest approximately $200 billion in capital expenditures across Amazon, anticipating a strong long-term return on invested capital, driven by demand for existing offerings and opportunities in AI, chips, robotics, and low earth orbit satellites. The company\'s guidance for the first quarter of 2026 anticipates net sales between $173.5 billion and $178.5 billion, representing 11% to 15% growth compared to the first quarter of 2025. Operating income for the first quarter of 2026 is expected to be between $16.5 billion and $21.5 billion, which includes approximately $1 billion in higher year-over-year Amazon Leo costs, as well as investments in quick commerce and international stores.\\n\\nComparative Analysis – Financial Results, Stock Performance and 2026 Outlook\\n\\nAmazon\'s FY2025 financial results demonstrated solid fundamental growth, with revenue increasing by 12% and net income by approximately 31%. Building on this strong financial foundation, management announced plans to invest approximately $200 billion in 2026, targeting long-term growth and shareholder value creation. During 2026 to date, Amazon\'s stock delivered an annualized return of 8.97%, accompanied by relatively high annualized volatility of 34.30%, indicating positive but volatile market performance.\\n\\nAdditional financial and market data would be necessary to establish any causal relationship. Based solely on the available figures, the positive stock return appears consistent with favorable investor expectations, while its relatively modest magnitude and elevated volatility may suggest that the planned 2026 investments, underpinned by the company\'s positive financial fundamentals demonstrated in FY2025, may not yet have generated their potential contribution to stock returns."}, {"id": 26, "context": "", "question": "22. Compare Microsoft, Visa and Walmart using their 6-month and 12-month momentum, Sharpe Ratio, CAPM Beta and the most recent available management guidance for 2026. Identify the differences in their quantitative risk-return profiles and reported business outlooks. Clearly distinguish supported findings from missing or non-comparable information.", "approved_answer": "Here\'s a comparison of Microsoft (MSFT), Visa (V), and Walmart (WMT) based on their 6-month and 12-month momentum, Sharpe Ratio, CAPM Beta, and available management guidance for 2026:\\n\\nMomentum:\\n- 6-month Momentum (measured as of 2026-10-31):\\n  - Microsoft (MSFT): 27.43%\\n  - Visa (V): 9.77%\\n  - Walmart (WMT): -20.63%\\n- 12-month Momentum (measured as of 2026-10-31):\\n  - Visa (V): 6.69%\\n  - Walmart (WMT): 3.91%\\n  - Microsoft (MSFT): 0.77%\\n\\nSharpe Ratio (Risk-Free Rate: 0.03):\\n- 6-month Sharpe Ratio (from 2026-04-02 to 2026-10-02):\\n  - Microsoft (MSFT): 1.78 (Annual Return: 40.68%, Annualized Volatility: 36.36%)\\n  - Visa (V): 1.62 (Annual Return: 21.30%, Annualized Volatility: 21.88%)\\n  - Walmart (WMT): -1.33 (Annual Return: -16.06%, Annualized Volatility: 28.41%)\\n- 12-month Sharpe Ratio (from 2025-10-02 to 2026-10-02):\\n  - Visa (V): 0.07 (Annual Return: 4.52%, Annualized Volatility: 21.86%)\\n  - Walmart (WMT): 0.00 (Annual Return: 3.12%, Annualized Volatility: 26.43%)\\n  - Microsoft (MSFT): -0.08 (Annual Return: 0.40%, Annualized Volatility: 32.34%)\\n\\nCAPM Beta (over a 12-month period from 2025-10-02 to 2026-10-02, using ^DJI as benchmark and a risk-free rate of 0.03):\\n- Microsoft (MSFT): 0.7309\\n- Visa (V): 0.6339\\n- Walmart (WMT): 0.2798\\n\\nManagement Guidance for 2026:\\n- Microsoft (MSFT): Business highlights include a 16% increase in Productivity and Business Processes revenue (14% in constant currency), with Microsoft 365 Commercial products and cloud services revenue up 16% (15% in constant currency), Microsoft 365 Consumer products and cloud services revenue up 21%, LinkedIn revenue up 9% (8% in constant currency), and Dynamics products and cloud services revenue up 18% (17% in constant currency). Intelligent Cloud revenue increased 26% (25% in constant currency), with Server products and cloud services revenue up 27% driven by Azure and other cloud services revenue growth of 39%.\\n- Visa (V): No management guidance for 2026 was found in the provided evidence.\\n- Walmart (WMT): No management guidance for 2026 was found in the provided evidence.\\n\\nDifferences in Quantitative Risk-Return Profiles and Reported Business Outlooks:\\n\\nQuantitative Risk-Return Profiles:\\n- Momentum: Microsoft shows strong positive 6-month momentum, while Walmart has negative 6-month momentum. Over 12 months, Visa and Walmart have positive momentum, but Microsoft\'s 12-month momentum is significantly lower than its 6-month performance.\\n- Sharpe Ratio: For the 6-month period, Microsoft and Visa have positive Sharpe Ratios, indicating good risk-adjusted returns, with Microsoft having a higher ratio. Walmart has a negative Sharpe Ratio, suggesting its returns did not compensate for the risk taken. Over the 12-month period, all three companies have significantly lower Sharpe Ratios, with Microsoft\'s turning negative, indicating a less favorable risk-adjusted return profile compared to the 6-month period.\\n- CAPM Beta: Walmart has the lowest Beta (0.2798), suggesting it is less volatile than the market benchmark (^DJI). Visa has a moderate Beta (0.6339), and Microsoft has the highest Beta (0.7309) among the three, indicating it is more sensitive to market movements than Visa and Walmart.\\n\\nReported Business Outlooks:\\n- Microsoft provided detailed business highlights for its Productivity and Business Processes and Intelligent Cloud segments, showing strong growth across various products and services, including Microsoft 365, LinkedIn, Dynamics, and Azure.\\n- No management guidance for 2026 was found for Visa or Walmart, making a direct comparison of their reported business outlooks impossible with the available information.\\n\\nOverall Interpretation:\\n\\nThe 12-month metrics provide the broader view of performance, while the 6-month metrics help determine whether that picture has been confirmed or has changed more recently. This distinction is particularly evident for Microsoft: its 12-month momentum of 0.77% and Sharpe Ratio of -0.08 describe a weak profile over the broader horizon, while its 6-month momentum of 27.43% and Sharpe Ratio of 1.78 point to a marked recent improvement. Visa shows a more consistent pattern across the two horizons, with positive momentum over both 6 and 12 months and a higher Sharpe Ratio over the most recent 6-month period; Walmart shows the opposite dynamic, moving from positive 12-month momentum to a strongly negative 6-month reading, accompanied by a 6-month Sharpe Ratio of -1.33.\\n\\nWithin this framework, Microsoft combines the strongest recent momentum and risk-adjusted performance with the highest CAPM Beta among the three companies (0.7309), indicating greater market sensitivity than Visa (0.6339) and especially Walmart (0.2798). Microsoft\'s available 2026 management information, which highlights growth across its main business areas, can therefore be considered alongside this recent strengthening in its quantitative market profile. For Visa and Walmart, in the absence of comparable 2026 management guidance in the retrieved evidence, the same comparison between management indications and quantitative market metrics cannot be made."}, {"id": 27, "context": "", "question": "22. Compare Microsoft, Amazon and Apple using their 6-month and 12-month momentum, Sharpe Ratio, CAPM Beta and the most recent available management guidance for 2026. Identify the differences in their quantitative risk-return profiles and reported business outlooks. Clearly distinguish supported findings from missing or non-comparable information.", "approved_answer": "Here\'s a comparison of Microsoft (MSFT), Amazon (AMZN), and Apple (AAPL) based on their 6-month and 12-month momentum, Sharpe Ratio, CAPM Beta, and available management guidance for 2026:\\n\\nMomentum:\\n- 6-month Momentum (measured as of 2026-10-31):\\n  - Microsoft (MSFT): 27.43%\\n  - Apple (AAPL): 23.19%\\n  - Amazon (AMZN): -5.11%\\n- 12-month Momentum (measured as of 2026-10-31):\\n  - Apple (AAPL): 23.88%\\n  - Amazon (AMZN): 2.99%\\n  - Microsoft (MSFT): 0.77%\\n\\nSharpe Ratio (Risk-Free Rate: 0.03):\\n- 6-month Sharpe Ratio (from 2026-04-02 to 2026-10-02):\\n  - Apple (AAPL): 1.82 (Annual Return: 30.77%, Annualized Volatility: 27.56%)\\n  - Microsoft (MSFT): 1.78 (Annual Return: 40.68%, Annualized Volatility: 36.36%)\\n  - Amazon (AMZN): 0.91 (Annual Return: 19.45%, Annualized Volatility: 35.45%)\\n- 12-month Sharpe Ratio (from 2025-10-02 to 2026-10-02):\\n  - Apple (AAPL): 0.98 (Annual Return: 31.11%, Annualized Volatility: 24.73%)\\n  - Amazon (AMZN): 0.30 (Annual Return: 14.00%, Annualized Volatility: 33.81%)\\n  - Microsoft (MSFT): -0.08 (Annual Return: 0.40%, Annualized Volatility: 32.34%)\\n\\nCAPM Beta (over a 12-month period from 2025-10-02 to 2026-10-02, using ^DJI as benchmark and a risk-free rate of 0.03):\\n- Amazon (AMZN): 1.1151\\n- Apple (AAPL): 0.7366\\n- Microsoft (MSFT): 0.7309\\n\\nManagement Guidance for 2026:\\n- Microsoft (MSFT): Business highlights include a 16% increase in Productivity and Business Processes revenue (14% in constant currency), with Microsoft 365 Commercial products and cloud services revenue up 16% (15% in constant currency), Microsoft 365 Consumer products and cloud services revenue up 21%, LinkedIn revenue up 9% (8% in constant currency), and Dynamics products and cloud services revenue up 18% (17% in constant currency). Intelligent Cloud revenue increased 26% (25% in constant currency), with Server products and cloud services revenue up 27% driven by Azure and other cloud services revenue growth of 39%.\\n- Amazon (AMZN): For the first quarter of 2026, net sales are expected to be between $173.5 billion and $178.5 billion, representing 11% to 15% growth compared to Q1 2025 (including a favorable foreign exchange impact of approximately 180 basis points). Operating income is expected to be between $16.5 billion and $21.5 billion, compared to $18.4 billion in Q1 2025, and includes approximately $1 billion of higher year-over-year Amazon Leo costs, as well as investments in quick commerce and international stores.\\n- Apple (AAPL): Apple expects revenue growth from strong iPhone and Services demand and new product launches, despite not having issued specific fiscal 2026 guidance. The CEO noted a September quarter revenue record of $102.5 billion, driven by iPhone and Services performance, and highlighted a strong product lineup for the holiday season.\\n\\nDifferences in Quantitative Risk-Return Profiles and Reported Business Outlooks:\\n\\nQuantitative Risk-Return Profiles:\\n- Momentum: Microsoft and Apple show strong positive 6-month momentum, with Microsoft slightly higher. Amazon, however, has negative 6-month momentum. Over the 12-month period, Apple leads significantly, while Amazon has positive momentum and Microsoft\'s momentum is much lower.\\n- Sharpe Ratio: For the 6-month period, Apple and Microsoft have the highest Sharpe Ratios, indicating strong risk-adjusted returns, with Apple slightly outperforming Microsoft. Amazon also has a positive Sharpe Ratio. Over the 12-month period, Apple maintains a strong positive Sharpe Ratio, followed by Amazon. Microsoft\'s 12-month Sharpe Ratio is negative, suggesting its returns did not compensate for the risk taken over the longer period.\\n- CAPM Beta: Amazon has the highest Beta (1.1151), indicating it is more volatile and sensitive to market movements than Apple and Microsoft. Apple and Microsoft have similar Betas (0.7366 and 0.7309 respectively), suggesting they are less volatile than the market benchmark (^DJI) and Amazon.\\n\\nReported Business Outlooks:\\n- Microsoft provided detailed business highlights for its Productivity and Business Processes and Intelligent Cloud segments, showing strong growth across various products and services.\\n- Amazon provided specific first-quarter 2026 guidance for net sales and operating income, including anticipated growth rates and investment areas.\\n- Apple, while not providing specific fiscal 2026 guidance, indicated expected revenue growth driven by strong iPhone and Services demand and new product launches, and highlighted a strong product lineup.\\n\\nOverall Interpretation:\\n\\nIn the overall quantitative comparison, Apple presents the most favorable profile among the three companies. Its 12-month momentum is by far the highest (23.88%), while its 6-month momentum remains very strong (23.19%), indicating that the strength observed over the broader period is also confirmed by the more recent trend. Apple also records the highest Sharpe Ratio over both the 6-month (1.82) and 12-month (0.98) periods, giving it the strongest risk-adjusted performance among the three companies. Its 12-month CAPM Beta of 0.7366 indicates relatively limited market sensitivity, very close to Microsoft\'s 0.7309 and substantially below Amazon\'s 1.1151.\\n\\nMicrosoft shows the strongest improvement in recent momentum. Its momentum rises from just 0.77% over 12 months to 27.43% over 6 months, the highest recent momentum among the three companies. Its 6-month Sharpe Ratio is also strong at 1.78, only slightly below Apple\'s 1.82. However, Microsoft\'s 12-month Sharpe Ratio remains negative at -0.08, showing that the strong recent acceleration has not yet translated into an equally favorable risk-adjusted profile over the broader annual period. Amazon presents the weakest momentum profile, moving from positive 12-month momentum of 2.99% to negative 6-month momentum of -5.11%. Its Sharpe Ratios remain positive at both horizons (0.91 over 6 months and 0.30 over 12 months), but it also has the highest CAPM Beta (1.1151), indicating the greatest sensitivity to market movements among the three companies.\\n\\nDifferent leaders therefore emerge depending on the dimension considered: Apple has the strongest overall quantitative and risk-adjusted profile; Microsoft has the strongest recent momentum; and Microsoft has the lowest CAPM Beta, although only marginally below Apple. When momentum and Sharpe Ratio are considered together, Apple nevertheless emerges as the strongest overall quantitative performer, combining persistent momentum across both time horizons with the best risk-adjusted performance.\\n\\nManagement guidance represents a different type of information and is not directly comparable with these market metrics. Microsoft and Amazon provide predominantly quantitative indications, while the available information for Apple is more qualitative. Overall, the information retrieved points to a growth-oriented business environment for all three companies, although Amazon also identifies specific cost and investment pressures. The available management information does not indicate particular critical conditions related to debt or broader macroeconomic factors and is therefore consistent, in directional terms, with an overall positive growth outlook."}, {"id": 28, "context": "", "question": "22. Which Dow Jones stocks currently have positive 6-month momentum and an annualized return above the average over the same period?", "approved_answer": "The Dow Jones stocks that currently have positive 6-month momentum and an annualized return above the average over the same period are:\\n\\n- AAPL: Momentum of 24.28% and annualized return of 30.26%.\\n- AMGN: Momentum of 21.43% and annualized return of 20.19%.\\n- CRM: Momentum of 30.36% and annualized return of 30.81%.\\n- CSCO: Momentum of 30.38% and annualized return of 42.53%.\\n- CVX: Momentum of 11.63% and annualized return of 11.87%.\\n- DIS: Momentum of 4.94% and annualized return of 9.78%.\\n- JNJ: Momentum of 14.96% and annualized return of 9.51%.\\n- JPM: Momentum of 7.32% and annualized return of 9.15%.\\n- KO: Momentum of 13.19% and annualized return of 15.34%.\\n- MMM: Momentum of 10.22% and annualized return of 8.26%.\\n- MRK: Momentum of 35.11% and annualized return of 19.75%.\\n- MSFT: Momentum of 31.75% and annualized return of 43.52%.\\n- NVDA: Momentum of 15.15% and annualized return of 26.21%.\\n- TRV: Momentum of 21.77% and annualized return of 23.20%.\\n- UNH: Momentum of 3.60% and annualized return of 25.44%.\\n- V: Momentum of 17.32% and annualized return of 25.25%.\\n\\nThe average annualized return over the 6-month period is 7%.\\n\\nMomentum is calculated over a 6-month time horizon."}, {"id": 29, "context": "", "question": "Identify the 5 Dow Jones stocks with the lowest annualized volatility over the last year and compare their annualized returns over the same period.", "approved_answer": "Over the last year (from 2025-10-09 to 2026-10-09), the 5 Dow Jones stocks with the lowest annualized volatility are:\\n\\n1. KO (Coca-Cola Co): Annualized volatility of 18.71%, with an annualized return of 36.71%.\\n2. JNJ (Johnson & Johnson): Annualized volatility of 19.20%, with an annualized return of 40.93%.\\n3. MCD (McDonald’s Corp): Annualized volatility of 19.31%, with an annualized return of -18.04%.\\n4. PG (Procter & Gamble Co): Annualized volatility of 19.86%, with an annualized return of 3.31%.\\n5. TRV (The Travelers Companies Inc): Annualized volatility of 20.82%, with an annualized return of 32.40%.\\n\\nConclusion: JNJ has the highest annualized return (40.93%), followed by KO (36.71%) and TRV (32.40%). PG records a modest positive return (3.31%), while MCD posts a negative return (-18.04%). Lower volatility does not necessarily correspond to higher returns."}]')
_BOX45_STOPWORDS = {'the', 'and', 'for', 'with', 'what', 'which', 'that', 'this', 'over', 'last', 'from', 'their', 'tell', 'among', 'does', 'have', 'has', 'were', 'are', 'its', 'one', 'two', 'three', 'same', 'year', 'years', 'months', 'month', 'stocks', 'stock', 'company', 'companies', 'compare', 'comparison', 'period'}
_BOX45_STRUCTURAL_TERMS = {'volatility', 'return', 'risk', 'sharpe', 'ratio', 'correlation', 'momentum', 'ranking', 'rank', 'volume', 'capm', 'beta', 'alpha', 'expected', 'guidance', 'management', 'ceo', 'cfo', 'revenue', 'financial', 'operating', 'results', 'drivers', 'earnings', 'documentary', 'release', 'annual', 'cash', 'flow'}

def _box45_example_tokens(text):
    return [token for token in re.findall('[a-z]+[0-9]*', str(text).lower()) if token not in _BOX45_STOPWORDS and len(token) > 1]

def select_box45_reference_examples(user_question, execution_plan=None, count=2):
    """Select 2–3 structurally relevant historical Q/A examples."""
    plan_text = json.dumps(execution_plan or [], ensure_ascii=False, default=str)
    query_tokens = _box45_example_tokens(str(user_question) + ' ' + plan_text)
    query_counts = Counter(query_tokens)
    scored = []
    for example in BOX45_APPROVED_EXAMPLES:
        question_tokens = _box45_example_tokens(example['question'])
        example_counts = Counter(question_tokens)
        shared = set(query_counts) & set(example_counts)
        structural_score = sum((4 if term in _BOX45_STRUCTURAL_TERMS else 1 for term in shared))
        score = structural_score / max(1, len(set(question_tokens)) ** 0.5)
        scored.append((score, -example['id'], example))
    scored.sort(reverse=True, key=lambda item: (item[0], item[1]))
    chosen = [item[2] for item in scored[:max(2, min(3, int(count)))]]
    return [{'question': example['question'], **({'conversation_context': example['context']} if example['context'] else {}), 'approved_answer': example['approved_answer'], 'output_format_rule': 'Always answer in plain text. Do not use asterisks (*) for bold, italics, lists, or any other Markdown formatting, including concluding observations. Use paragraphs and simple hyphens for lists.'} for example in chosen]
ANSWER_SYNTHESIZER_AGENT_NAME = 'answer_synthesizer'
ANSWER_SYNTHESIZER_MODEL = MAIN_MODEL
MAX_SYNTHESIS_EVIDENCE = None
MAX_SYNTHESIS_MISSING_INFORMATION = None
MAX_SYNTHESIS_PLAN_STEPS = None
MAX_SYNTHESIS_PROMPT_CHARACTERS = float('inf')
ANSWER_SYNTHESIZER_SYSTEM_INSTRUCTION = '\nYou are the Answer Synthesizer of an agentic system for Dow Jones\nfinancial analysis.\n\nYou must answer the user\'s question using exclusively\nthe structured evidence provided to you.\n\nMandatory rules:\n\nPEARSON CORRELATION — CONDITIONAL METHODOLOGICAL DISCLOSURE:\nPearson correlation is ALWAYS calculated using the ENTIRE AVAILABLE HISTORICAL\nDATASET, regardless of any observation period requested by the user.\nONLY IF the user EXPLICITLY requests a specific observation period DIFFERENT\nFROM THE ENTIRE AVAILABLE HISTORY (for example, the last five months), you MUST\nstate in the answer that, by the project\'s methodological rule, Pearson\ncorrelation is calculated using the ENTIRE AVAILABLE HISTORICAL DATASET rather\nthan the requested period. Merely reporting the effective start and end dates\nis NOT sufficient in this case: explicitly explain the full-history rule.\nIf the user does NOT explicitly request a different observation period for\nPearson, do NOT add this methodological disclosure. Report the actual start\nand end dates when supported by the evidence. NEVER describe a full-history\nPearson coefficient as having been calculated over a shorter requested window.\nThe full-history scope is a DELIBERATE METHODOLOGICAL RULE of this project,\nNOT a fallback caused by missing, unavailable, insufficient, or inaccessible\ndata for the user-requested period. If a different period was explicitly\nrequested, you MUST explain that the full available history was used BECAUSE\nOF THIS METHODOLOGICAL RULE. You MUST NOT state or imply that data for the\nrequested period was unavailable unless separate, explicit evidence confirms\nan actual data-availability problem. The methodological full-history scope\nmust NEVER be classified as missing information.\nFor a highest-correlation request, use the top-ranked row of\nall_correlation_pairs, not the threshold-filtered table.\n\n1. Do not perform new calculations.\n2. Do not invent values, facts, sources, or conclusions not present\n   in the evidence.\n3. Do not use external knowledge to complete missing data.\n4. Clearly distinguish:\n   - results supported by the evidence;\n   - missing or unavailable information.\n5. If the question requires a comparison, explicitly state the criteria\n   actually used.\n   When the user asks to compare or contrast results, explicitly compare\n   the already calculated values and add a brief evidence-based\n   comparative conclusion; listing the numbers alone is not enough.\n   Do not recalculate metrics or change the selected securities.\n6. Always explicitly state in the answer the time horizon actually\n   used for each metric or quantitative analysis, whenever that\n   horizon is present in the user_question, the plan, the evidence,\n   or is validly inherited from the current flow.\n7. If the plan contains a deterministic ranking or consensus rule\n   or criterion, follow it and state it.\n8. Do not transform a descriptive analysis into a prediction.\n9. Do not state that a stock will rise or fall in the future if\n   the evidence does not contain a supported forecast.\n10. The answer must be concise, readable, and directly\n    connected to the question.\n10A. When evidence contains display_value, use exclusively that\n     representation of the value in the answer. Do not alter its\n     scale, unit, currency, sign, or number of decimal places, and do not\n     reconstruct the format from the raw numerical value.\n10B. Prices and monetary amounts in USD must preserve the "$" symbol\n     provided by display_value. Documentary evidence must preserve\n     the numerical precision and units reported by the source.\n11. Do not cite STEP_1, STEP_2, or other technical identifiers\n    in the answer intended for the user.\n12. Never disclose internal agent names, tool names, STEP identifiers, evidence IDs, or workflow details in the user-facing answer. Keep internal provenance only in the system state.\n    Report the financial metrics explicitly or implicitly requested by the question and its conversational context; do not add other metrics merely because they are available in evidence.\n13. For each documentary evidence item containing retrieval_status,\n    requested_metric, and matched_metric, you must interpret\n    these fields before formulating the answer:\n    - if retrieval_status is EXACT_MATCH, SYNONYM_MATCH, or\n      SEMANTIC_EQUIVALENT, you may use the evidence as the answer\n      to the requested metric or information;\n    - if retrieval_status is RELATED_IN_SAME_MACRO_AREA, DO NOT present\n      the retrieved information as equivalent to the requested metric.\n      Explicitly state that the requested metric or information\n      was not found directly and that related information\n      belonging to the same semantic macro-area is available instead;\n    - if retrieval_status is SECTION_FALLBACK, use the evidence\n      while specifying, when relevant, that it comes from an alternative\n      documentary section;\n    - if retrieval_status is NOT_FOUND, state that the requested\n      information is not available in the retrieved evidence.\n    Never transform a semantic relationship or membership in the\n    same macro-area into equivalence between two metrics.\n    Never attribute to requested_metric a value, explanation,\n    or evidence belonging exclusively to a different matched_metric.\n13A. RESPONSE RULE FOR CEO/CFO COMMENTARY.\n    When the question asks what the CEO and/or CFO stated about\n    guidance, outlook, strategy, objectives, milestones, or equivalent topics,\n    treat those topics as content of the role\'s commentary, not as\n    separate missing information. Use the available CEO_COMMENTARY\n    and/or CFO_COMMENTARY to answer. If the commentary of a requested role\n    is not available, state only that no statements from that role\n    were found on the requested topics. Do not transform the absence\n    of the CFO or CEO quote into the absence of guidance, strategy,\n    objectives, or milestones as such. If both requested commentaries\n    are absent, state the absence of both.\n\nReturn a JSON object with this structure:\n\n{\n    "draft_answer": "final answer in natural language",\n    "used_evidence_ids": [\n        "identifiers of only the evidence actually used"\n    ],\n    "reported_missing_information": [\n        "brief descriptions of the missing information actually\n         relevant to the answer"\n    ]\n}\n\n- Information explicitly present in the current question\n  constitutes valid context for the answer. Do not declare tickers,\n  time periods, thresholds, counts, or metrics missing\n  when such information is explicitly specified in the\n  user_question, even if it is not replicated in the\n  selected_evidence fields.\n- Use quantitative evidence to support calculated values;\n  use the current question for constraints and parameters explicitly\n  requested by the user.\n\n- Treat as valid answer context both information\n  explicitly present in the user_question and information validly\n  retrieved from a previous question in the current flow.\n- Do not declare tickers, time periods, metrics, thresholds,\n  counts, rankings, or other constraints missing when such information\n  is present in the user_question or in evidence with\n  provenance=current_flow.\n- Use quantitative evidence to support calculated values; use the\n  current question and current flow for constraints and references already\n  established in the conversation.\n\n- For every Momentum result, always state in natural language\n  the time horizon certified by the tool in the evidence.\n  Use a sentence such as:\n  "Momentum is calculated over a time horizon of X months."\n  where X is derived from the period certified by the tool.\n- Do not infer the period from the metric name: use the period\n  transmitted in the evidence.\n\nADDITIONAL TEMPORAL RULES\n\n- The current_date provided in the payload is the system\'s authoritative\n  temporal reference and must be used only as internal context.\n- Do not report current_date in the answer and do not introduce autonomous\n  assessments that a date is future, present, or past.\n- For forecasting requests or unsupported periods, use exclusively\n  selected_evidence, tool results, and the actual dataset coverage.\n  If the required data or calculations are unavailable, state\n  their unavailability without independently attributing it to the fact\n  that the date is in the future.\n'.strip()
ANSWER_SYNTHESIZER_SYSTEM_INSTRUCTION += '\n\nApproved historical reference examples, when supplied in reference_examples,\nillustrate answer structure, completeness, and appropriate use of conversation\ncontext only. They are not financial evidence. Never copy their historical\nnumbers, dates, findings, or conclusions into a new answer. The current\nselected_evidence is the sole source of factual financial claims. If an\nexample conflicts with current evidence or the current question, follow the\ncurrent evidence and question. The examples do not add new mandatory output\nsections or override any rule above.\n'

def _synthesis_ensure_list(value: Any) -> List[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, (tuple, set)):
        return list(value)
    return [value]

def _synthesis_unique_strings(values: Sequence[Any]) -> List[str]:
    output = []
    seen = set()
    for value in _synthesis_ensure_list(values):
        text = str(value).strip()
        if not text or text in seen:
            continue
        seen.add(text)
        output.append(text)
    return output

def _compact_execution_plan_for_synthesis(execution_plan: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    compact_plan = []
    for step in list(execution_plan):
        if not isinstance(step, dict):
            continue
        compact_plan.append({'step_id': step.get('step_id'), 'sub_question_id': step.get('sub_question_id'), 'objective': step.get('objective', ''), 'action_type': step.get('action_type'), 'selected_tool': step.get('selected_tool'), 'required_outputs': _synthesis_unique_strings(step.get('required_outputs', [])), 'financial_concepts': _synthesis_unique_strings(step.get('financial_concepts', [])), 'referenced_tickers': _synthesis_unique_strings(step.get('referenced_tickers', [])), 'time_periods': _synthesis_unique_strings(step.get('time_periods', [])), 'result_selection': step.get('result_selection', {}), 'result_identity': step.get('result_identity', {}), 'tool_parameters': step.get('tool_parameters', {}) if isinstance(step.get('tool_parameters', {}), dict) else {}})
    return compact_plan

def _compact_selected_evidence_for_synthesis(selected_evidence: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    compact_evidence = []
    for item in list(selected_evidence):
        if not isinstance(item, dict):
            continue
        compact_evidence.append({'evidence_id': item.get('evidence_id'), 'objective': item.get('objective', ''), 'selected_tool': item.get('selected_tool'), 'source': item.get('source'), 'output_name': item.get('output_name'), 'result_key': item.get('result_key'), 'result_selection': item.get('result_selection', {}), 'financial_concepts': item.get('financial_concepts', []), 'referenced_tickers': item.get('referenced_tickers', []), 'time_periods': item.get('time_periods', []), 'value': {'section_title': item.get('section_title') or (item.get('value', {}).get('section_title') if isinstance(item.get('value'), dict) else None), 'canonical_category': item.get('matched_metric') or item.get('requested_metric'), 'section': item.get('value', {}).get('section') if isinstance(item.get('value'), dict) else None, 'evidence_text': item.get('value', {}).get('evidence_text') if isinstance(item.get('value'), dict) else item.get('value')} if item.get('selected_tool') == 'press_release_fy2025' else item.get('display_value', item.get('value')), 'retrieval_status': item.get('retrieval_status'), 'requested_metric': item.get('requested_metric'), 'matched_metric': item.get('matched_metric')})
    return compact_evidence

def _compact_missing_information_for_synthesis(missing_information: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    compact_missing = []
    for item in list(missing_information):
        if not isinstance(item, dict):
            continue
        compact_missing.append({'objective': item.get('objective', ''), 'selected_tool': item.get('selected_tool'), 'execution_status': item.get('execution_status'), 'missing_outputs': item.get('missing_outputs', []), 'reason': item.get('reason')})
    return compact_missing

def _build_answer_sources(selected_evidence: Sequence[Dict[str, Any]], used_evidence_ids: Sequence[str]) -> List[Dict[str, Any]]:
    used_ids = set(_synthesis_unique_strings(used_evidence_ids))
    sources = []
    seen = set()
    for item in selected_evidence:
        if not isinstance(item, dict):
            continue
        evidence_id = str(item.get('evidence_id', '')).strip()
        if not evidence_id or evidence_id not in used_ids:
            continue
        source_key = (evidence_id, item.get('selected_tool'), item.get('output_name'))
        if source_key in seen:
            continue
        seen.add(source_key)
        sources.append({'evidence_id': evidence_id, 'selected_tool': item.get('selected_tool'), 'output_name': item.get('output_name'), 'source': item.get('source'), 'referenced_tickers': item.get('referenced_tickers', []), 'time_periods': item.get('time_periods', [])})
    return sources
FINAL_INTEGRATED_COMMENTARY_INSTRUCTIONS = '\n\nTOOL COVERAGE CONTRACT FOR COMPOSED QUESTIONS:\nUse the incoming selected_evidence and the requested tool/metric matrix as the\ncoverage checklist. Integrate every supported requested metric into the answer.\nFor a requested metric with no supporting selected evidence, explicitly disclose\nits absence; never fabricate figures or claim a source was retrieved without evidence.\nPreserve quantitative and documentary evidence and discuss their relationship.\n\nINTEGRATED COMMENTARY METHODOLOGY — WHEN RELEVANT\n\nUse this analytical methodology only for dimensions requested by the user.\nDo not introduce business, documentary, quantitative, or guidance dimensions\nthat the question does not request. A quantitative-only comparison remains\nquantitative-only. Apply the relevant assessment methods below when useful.\n\nThis commentary must follow the reasoning structure illustrated in\nBOX PRELIMINARY TO BOX 45 / BOX45_APPROVED_EXAMPLES.\n\nIt must not simply repeat the individual metrics, press-release\nsummaries, or management guidance already presented.\n\nEvaluate only the dimensions relevant to the question and compare\ntheir signals where a comparison is requested.\n\n1. BUSINESS AND PRESS-RELEASE ASSESSMENT\n\nEvaluate the business information contained in each retrieved\npress release as a whole.\n\nConsider, where supported by evidence:\n- Revenue and earnings developments.\n- Operating performance and core-business developments.\n- Business growth, contraction, or stability.\n- Margins, profitability, costs, and investments.\n- Debt, financial position, and other material constraints.\n- Favorable or unfavorable market and macroeconomic conditions.\n- Management-reported opportunities, challenges, and risks.\n\nClassify the overall business signal as:\n\nPOSITIVE:\nThe available business indicators are predominantly favorable\nand there are no material negative findings that overturn\nthe positive assessment.\n\nNEGATIVE:\nThe available business indicators are predominantly unfavorable.\n\nMIXED:\nMaterial positive and negative findings coexist.\n\nINSUFFICIENT EVIDENCE:\nThe retrieved information does not support a reliable assessment.\n\nExplain the specific evidence behind the classification.\nDo not infer the absence of debt, business risks, or other\nproblems merely because they are not mentioned in a document.\n\n2. QUANTITATIVE MARKET ASSESSMENT\n\nEvaluate the requested quantitative indicators together,\nnot as isolated numbers.\n\nConsider, where available:\n- Positive or negative stock returns and momentum.\n- Evolution across the requested observation periods.\n- Sharpe Ratio and risk-adjusted performance.\n- Annualized volatility and Return-to-Risk Ratio.\n- CAPM Beta and market sensitivity.\n- Differences between short-term and long-term signals.\n- Relative positioning against the other companies.\n\nClassify the overall quantitative signal as:\n\nPOSITIVE:\nThe available indicators consistently support favorable\nmarket performance and risk-adjusted results.\n\nNEGATIVE:\nThe available indicators consistently indicate unfavorable\nmarket performance or risk-return characteristics.\n\nMIXED:\nPositive and negative signals coexist, including differences\nbetween time horizons, returns, risk, or market sensitivity.\n\nINSUFFICIENT EVIDENCE:\nThe available metrics do not permit a reliable assessment.\n\nExplain which metrics support the classification and which\nmetrics diverge.\n\nDo not treat a low Beta as automatically positive, or a\npositive return as sufficient to establish an overall\npositive risk-adjusted profile.\n\n3. MANAGEMENT GUIDANCE AND OUTLOOK ASSESSMENT\n\nEvaluate management guidance and strategic expectations\nseparately from historical business results.\n\nIdentify:\n- Explicit numerical guidance, when available.\n- Qualitative management expectations.\n- Growth objectives and strategic priorities.\n- Planned investments, restructuring, and operational actions.\n- Risks, assumptions, and uncertainties attached to the outlook.\n\nClassify the guidance signal as:\n\nPOSITIVE:\nManagement communicates favorable expectations or growth\nobjectives supported by the retrieved evidence.\n\nNEGATIVE:\nManagement communicates unfavorable expectations.\n\nMIXED:\nPositive objectives coexist with material warnings,\nconstraints, or adverse expectations.\n\nINSUFFICIENT EVIDENCE:\nThe available documents do not support an outlook assessment.\n\nManagement\'s positive intentions must be identified as\nforward-looking statements, not established results.\n\nThe absence of explicit numerical FY2026 guidance does not\nmean that the press release is missing or that qualitative\nmanagement commentary is unavailable.\n\n4. FINAL DIFFERENTIAL ASSESSMENT\n\nWhen all three dimensions are requested, compare the three assessments for each company:\n\nA. Business and press-release signal.\nB. Quantitative market signal.\nC. Management guidance and outlook signal.\n\nDetermine whether the requested dimensions converge or diverge.\n\nOVERALL POSITIVE:\nThe available dimensions are consistently favorable.\n\nOVERALL NEGATIVE:\nThe available dimensions are consistently unfavorable.\n\nOVERALL MIXED:\nMaterial favorable and unfavorable signals coexist\nacross the three dimensions.\n\nINSUFFICIENT EVIDENCE:\nThe evidence is inadequate for an integrated conclusion.\n\nIf business fundamentals and management guidance are positive\nbut stock performance is weak, flat, or negative, explicitly\nexplain that the stock has not yet reflected the favorable\nbusiness developments or management expectations.\n\nUse appropriately qualified language, for example:\n\n"Despite favorable business developments and management\'s\npositive growth expectations, the stock\'s performance has\nnot yet reflected the same strength over the observed period."\n\nDo not assert that a stock is undervalued or has unexpressed\nupside potential without valuation evidence.\n\nIf stock performance is strong despite mixed or unfavorable\nbusiness developments, explicitly identify the divergence\nand explain what the available evidence does and does not\nestablish.\n\nIf the quantitative indicators themselves diverge across\nperiods, explain the difference between the short-term and\nlong-term signals.\n\n5. CROSS-COMPANY DIFFERENTIAL COMMENTARY\n\nWhen a cross-company comparison is requested, compare the companies together.\n\nIdentify:\n- Which company shows the strongest alignment between\n  business performance, quantitative indicators, and guidance.\n- Which company shows the most significant divergence.\n- Whether positive management expectations are already\n  reflected in stock performance.\n- Which differences arise from business fundamentals,\n  market behavior, or management expectations.\n- Which findings are supported and which remain uncertain\n  or non-comparable.\n\nWhere multiple dimensions are requested, establish an analytical\nrelationship between those requested dimensions.\n\nIt must explain WHY the companies differ, using the available\nevidence, rather than merely stating WHICH company ranks first.\n\n6. OUTPUT STRUCTURE WHEN INTEGRATED COMMENTARY IS RELEVANT\n\nUse the following elements only where relevant to the question:\n\n- An integrated assessment of the requested dimensions.\n- An explanation of converging or conflicting requested signals.\n- A concluding cross-company comparison when requested.\n\nWrite substantive analytical prose consistent with the\napproved examples in BOX45_APPROVED_EXAMPLES.\n\nDo not substitute:\n- A list of metrics.\n- Separate press-release summaries.\n- A ranking without interpretation.\n- A generic concluding sentence.\n- A missing-information disclaimer.\n\nPreserve all supported facts and distinguish evidence,\nmanagement expectations, and analytical interpretation.\n\nNever invent missing information.\n\nThe methodology governs how to interpret relevant evidence; it does\nnot mandate commentary or analytical dimensions not requested.\n'

def build_answer_synthesis_prompt(user_question: str, execution_plan: Sequence[Dict[str, Any]], selected_evidence: Sequence[Dict[str, Any]], missing_information: Sequence[Dict[str, Any]]) -> str:
    payload = {'current_date': datetime.now().date().isoformat(), 'user_question': str(user_question).strip(), 'execution_plan': _compact_execution_plan_for_synthesis(execution_plan), 'selected_evidence': _compact_selected_evidence_for_synthesis(selected_evidence), 'missing_information': _compact_missing_information_for_synthesis(missing_information)}
    if 'select_box45_reference_examples' in globals():
        payload['reference_examples'] = select_box45_reference_examples(user_question=user_question, execution_plan=execution_plan, count=2)
    serialized_payload = json.dumps(payload, ensure_ascii=False, default=str)
    return 'Build the answer to the question using exclusively the following JSON package:\n\n' + serialized_payload + '\n\n' + FINAL_INTEGRATED_COMMENTARY_INSTRUCTIONS

def validate_answer_synthesis_output(raw_output: Dict[str, Any], available_evidence_ids: Sequence[str]) -> Dict[str, Any]:
    if not isinstance(raw_output, dict):
        raise TypeError('The Answer Synthesizer output must be a dictionary.')
    draft_answer = str(raw_output.get('draft_answer', '')).strip()
    if not draft_answer:
        raise ValueError('draft_answer is empty.')
    available_ids = set(_synthesis_unique_strings(available_evidence_ids))
    requested_used_ids = _synthesis_unique_strings(raw_output.get('used_evidence_ids', []))
    resolved_used_ids = []
    for evidence_id in requested_used_ids:
        if evidence_id in available_ids:
            resolved_used_ids.append(evidence_id)
            continue
        if evidence_id.endswith('::press_release_result'):
            children = sorted((candidate for candidate in available_ids if candidate.startswith(evidence_id + '::') and candidate[len(evidence_id) + 2:].isdigit()))
            if children:
                resolved_used_ids.extend(children)
                continue
        resolved_used_ids.append(evidence_id)
    requested_used_ids = list(dict.fromkeys(resolved_used_ids))
    invalid_evidence_ids = [evidence_id for evidence_id in requested_used_ids if evidence_id not in available_ids]
    if invalid_evidence_ids:
        raise ValueError('The model declared unavailable evidence: ' + ', '.join(invalid_evidence_ids))
    reported_missing_information = _synthesis_unique_strings(raw_output.get('reported_missing_information', []))
    return {'draft_answer': draft_answer, 'used_evidence_ids': requested_used_ids, 'reported_missing_information': reported_missing_information}

def _box45_enforce_pearson_disclosure(answer: str, user_question: str, execution_plan: Sequence[Dict[str, Any]], missing_information: Sequence[Dict[str, Any]]) -> str:
    import re
    pearson_planned = any((isinstance(step, dict) and (step.get('selected_tool') == 'pearson_correlation' or step.get('tool_name') == 'pearson_correlation') for step in execution_plan))
    if not pearson_planned:
        return answer
    explicit_window = bool(re.search('\\b(?:over|during|within|in|for)\\s+(?:the\\s+)?(?:last|past|previous|preceding|most recent|first|next)\\s+\\d+\\s*(?:trading\\s+)?(?:days?|weeks?|months?|years?)\\b|\\b(?:from|between)\\s+\\d{4}[-/]\\d{1,2}|\\b(?:in|during|for)\\s+(?:calendar\\s+year\\s+)?(?:19|20)\\d{2}\\b', user_question, flags=re.IGNORECASE))
    actual_failure = any((isinstance(item, dict) and ('pearson' in str(item).lower() or 'correlation' in str(item).lower()) and any((term in str(item).lower() for term in ('source data unavailable', 'price history unavailable', 'missing observations', 'insufficient observations'))) for item in missing_information))
    corrected = str(answer).strip()
    if not actual_failure:
        corrected = re.sub('(?:,?\\s*\\b(?:as|because|since|due to the fact that)\\s+)(?:the\\s+)?(?:data|historical data|price data)\\s+(?:for\\s+[^.!?;]{0,100}?\\s+)?(?:was|were|is|are)\\s+(?:not\\s+available|unavailable|missing|insufficient)[^.!?;]*', '', corrected, flags=re.IGNORECASE)
        corrected = re.sub('\\s+([.,;:])', '\\1', corrected)
        corrected = re.sub('\\.{2,}', '.', corrected)
    if explicit_window:
        disclosure = "Under the project's methodological rule, Pearson correlation is calculated using the entire available historical dataset, regardless of the observation period requested."
        if not re.search('methodolog(?:ical|y).{0,160}(?:entire|full)|(?:entire|full).{0,160}methodolog(?:ical|y)', corrected, flags=re.IGNORECASE | re.DOTALL):
            corrected = corrected.rstrip() + ' ' + disclosure
    if not explicit_window:
        sentences = re.split('(?<=[.!?])\\s+', corrected)

        def _is_unsolicited_methodology(sentence: str) -> bool:
            low = sentence.lower()
            return bool(re.search('metodolog|methodolog|regola\\s+del\\s+progetto|project.s\\s+rule', low)) and bool(re.search('storico|historical|history|full\\s+(?:available\\s+)?dataset|entire\\s+available', low)) and bool(re.search('pearson|correlaz|correlation', low)) and (not bool(re.search('\\b(?:0[.,]\\d{2,}|\\d{2,}%)\\b', low)))
        corrected = ' '.join((sentence for sentence in sentences if not _is_unsolicited_methodology(sentence))).strip()
    return corrected.strip()

def agent_13_answer_synthesis(state: Dict[str, Any], llm_function: Optional[Callable[..., Dict[str, Any]]]=None) -> Dict[str, Any]:
    start_time = time.perf_counter()
    if not isinstance(state, dict):
        raise TypeError('state must be a dictionary.')
    user_question = str(state.get('user_question', '')).strip()
    execution_plan = state.get('execution_plan', [])
    selected_evidence = state.get('selected_evidence', [])
    missing_information = state.get('missing_information', [])
    if not user_question:
        raise ValueError('user_question is not available.')
    if not isinstance(execution_plan, list):
        raise TypeError('execution_plan must be a list.')
    if not isinstance(selected_evidence, list):
        raise TypeError('selected_evidence must be a list.')
    if not isinstance(missing_information, list):
        raise TypeError('missing_information must be a list.')
    if not selected_evidence and (not missing_information):
        raise ValueError('Neither evidence nor missing information is available for synthesis.')
    synthesis_prompt = build_answer_synthesis_prompt(user_question=user_question, execution_plan=execution_plan, selected_evidence=selected_evidence, missing_information=missing_information)
    if llm_function is None:
        if 'call_llm_json' not in globals():
            raise RuntimeError('call_llm_json is not available. Run BOX 6 first.')
        llm_function = call_llm_json
    raw_output = llm_function(system_instruction=ANSWER_SYNTHESIZER_SYSTEM_INSTRUCTION, user_content=synthesis_prompt, model=ANSWER_SYNTHESIZER_MODEL, temperature=0.0)
    available_evidence_ids = [item.get('evidence_id') for item in selected_evidence if isinstance(item, dict) and item.get('evidence_id')]
    validated_output = validate_answer_synthesis_output(raw_output=raw_output, available_evidence_ids=available_evidence_ids)
    validated_output['draft_answer'] = _box45_enforce_pearson_disclosure(answer=validated_output['draft_answer'], user_question=user_question, execution_plan=execution_plan, missing_information=missing_information)
    answer_sources = _build_answer_sources(selected_evidence=selected_evidence, used_evidence_ids=validated_output['used_evidence_ids'])
    execution_time = round(time.perf_counter() - start_time, 6)
    return {'draft_answer': validated_output['draft_answer'], 'answer_sources': answer_sources, 'answer_synthesis_status': 'completed', 'answer_synthesis_error': None, 'answer_synthesis_model': ANSWER_SYNTHESIZER_MODEL, 'answer_synthesis_execution_time_seconds': execution_time, 'answer_synthesis_used_evidence_ids': validated_output['used_evidence_ids'], 'answer_synthesis_reported_missing_information': validated_output['reported_missing_information'], 'current_question_node': 'answer_synthesis', 'question_workflow_status': 'draft_answer_generated', 'next_node': 'answer_validation'}
answer_synthesizer_agent = agent_13_answer_synthesis
if 'AGENT_REGISTRY' in globals() and 'build_registry_entry' in globals():
    AGENT_REGISTRY[ANSWER_SYNTHESIZER_AGENT_NAME] = build_registry_entry(name=ANSWER_SYNTHESIZER_AGENT_NAME, function=agent_13_answer_synthesis, component_type='llm_agent', description='Synthesizes the answer in natural language using exclusively the plan and the evidence selected by the workflow.', required_state_fields=['user_question', 'execution_plan', 'selected_evidence', 'missing_information'], output_fields=['draft_answer', 'answer_sources'], uses_llm=True)
    final_state['agent_registry'] = AGENT_REGISTRY
final_state.setdefault('draft_answer', '')
final_state.setdefault('answer_sources', [])
final_state.setdefault('answer_synthesis_status', '')
final_state.setdefault('answer_synthesis_error', None)
final_state.setdefault('answer_synthesis_model', '')
final_state.setdefault('answer_synthesis_execution_time_seconds', 0.0)
final_state.setdefault('answer_synthesis_used_evidence_ids', [])
final_state.setdefault('answer_synthesis_reported_missing_information', [])

def _box_45_fake_llm(system_instruction: str, user_content: str, model: str, temperature: float) -> Dict[str, Any]:
    return {'draft_answer': 'In the available comparison, MSFT shows lower annualized volatility than AAPL (0.19 versus 0.21), while AAPL shows higher Momentum (0.18 versus 0.14). The FY2025 guidance component is not available and is therefore not used to formulate conclusions.', 'used_evidence_ids': ['STEP_1::financial_metrics', 'STEP_2::momentum'], 'reported_missing_information': ['FY2025 guidance is not available.']}
import textwrap
_original_build_answer_synthesis_prompt_box45 = build_answer_synthesis_prompt

def build_answer_synthesis_prompt(user_question, execution_plan, selected_evidence, missing_information):
    prompt = _original_build_answer_synthesis_prompt_box45(user_question, execution_plan, selected_evidence, missing_information)
    atomic_manifest = []
    evidence_by_atom = {e.get('atomic_id'): e for e in selected_evidence or [] if isinstance(e, dict) and e.get('atomic_id')}
    for step in execution_plan or []:
        if not isinstance(step, dict) or not step.get('atomic_id'):
            continue
        aid = step['atomic_id']
        atomic_manifest.append({'atomic_id': aid, 'tool_name': step.get('selected_tool'), 'tickers': step.get('referenced_tickers', []), 'metric': step.get('metric'), 'time_periods': step.get('time_periods', []), 'evidence_available': aid in evidence_by_atom})
    return prompt + '\n\nDETERMINISTIC ATOMIC COVERAGE CONTRACT:\n' + json.dumps(atomic_manifest, ensure_ascii=False, default=str) + '\nEvery atomic component with evidence_available=true MUST be explicitly represented by its correct numerical value in the answer. Never substitute the same metric from another time period or ticker. Do not omit an available atomic component because the request contains many components.\n'
_original_agent_13_answer_synthesis_requirement_evidence = agent_13_answer_synthesis

def agent_13_answer_synthesis(state: Dict[str, Any]) -> Dict[str, Any]:
    synthesis_state = dict(state)
    requirement_evidence = state.get('requirement_evidence') or state.get('selected_evidence') or []
    synthesis_state['selected_evidence'] = requirement_evidence
    result = _original_agent_13_answer_synthesis_requirement_evidence(synthesis_state)
    result['answer_required_requirement_ids'] = list(state.get('required_requirement_ids') or [])
    return result
answer_synthesizer_agent = agent_13_answer_synthesis
if 'AGENT_REGISTRY' in globals() and ANSWER_SYNTHESIZER_AGENT_NAME in AGENT_REGISTRY:
    try:
        AGENT_REGISTRY[ANSWER_SYNTHESIZER_AGENT_NAME]['function'] = agent_13_answer_synthesis
    except Exception:
        pass
_original_agent_13_answer_synthesis_complete_requirement_matrix = agent_13_answer_synthesis

def agent_13_answer_synthesis(state: Dict[str, Any]) -> Dict[str, Any]:
    synthesis_state = dict(state)
    evidence = state.get('requirement_evidence') or state.get('selected_evidence') or []
    evidence_by_rid = {e.get('requirement_id'): e for e in evidence if isinstance(e, dict) and e.get('requirement_id')}
    requirement_plan = []
    for atom in state.get('requirement_atoms') or []:
        if not isinstance(atom, dict) or not atom.get('requirement_id'):
            continue
        rid = atom['requirement_id']
        source_ev = evidence_by_rid.get(rid) or {}
        requirement_plan.append({'step_id': f'REQ_STEP::{rid}', 'atomic_id': rid, 'requirement_ids': [rid], 'satisfies_requirement_ids': [rid], 'selected_tool': source_ev.get('tool_name') or source_ev.get('selected_tool'), 'referenced_tickers': [atom.get('ticker')] if atom.get('ticker') else [], 'metric': atom.get('metric'), 'time_periods': [atom.get('time_period')] if atom.get('time_period') else [], 'action_type': 'reuse_output' if rid in evidence_by_rid else 'execute_tool'})
    if requirement_plan:
        synthesis_state['execution_plan'] = requirement_plan
        synthesis_state['selected_evidence'] = evidence
    result = _original_agent_13_answer_synthesis_complete_requirement_matrix(synthesis_state)
    result['answer_required_requirement_ids'] = list(state.get('required_requirement_ids') or [])
    return result
answer_synthesizer_agent = agent_13_answer_synthesis
if 'AGENT_REGISTRY' in globals() and ANSWER_SYNTHESIZER_AGENT_NAME in AGENT_REGISTRY:
    try:
        AGENT_REGISTRY[ANSWER_SYNTHESIZER_AGENT_NAME]['function'] = agent_13_answer_synthesis
    except Exception:
        pass
_original_build_answer_synthesis_prompt_condition_filter = build_answer_synthesis_prompt

def build_answer_synthesis_prompt(user_question, execution_plan, selected_evidence, missing_information):
    prompt = _original_build_answer_synthesis_prompt_condition_filter(user_question, execution_plan, selected_evidence, missing_information)
    filter_result = None
    for step in execution_plan or []:
        if isinstance(step, dict) and isinstance(step.get('condition_filter_result'), dict):
            candidate = step.get('condition_filter_result')
            if candidate.get('applied'):
                filter_result = candidate
                break
    if not filter_result:
        return prompt
    deterministic_contract = {'logic': filter_result.get('logic', 'AND'), 'filtered_tickers': filter_result.get('filtered_tickers', []), 'conditions': filter_result.get('normalized_conditions', [])}
    return prompt + '\n\nDETERMINISTIC MULTI-CONDITION FILTER CONTRACT:\n' + json.dumps(deterministic_contract, ensure_ascii=False, default=str) + '\nThe filtered_tickers list was computed deterministically by BOX 43 from the already calculated metrics. It is authoritative. Do NOT independently select, add, remove, rank, or replace tickers. Use exactly and only filtered_tickers when answering which assets satisfy the requested conditions. Your task is limited to presenting and explaining the deterministic result using the available evidence.\n'

_box45_original_prompt_document_check = build_answer_synthesis_prompt
def build_answer_synthesis_prompt(user_question, execution_plan, selected_evidence, missing_information):
    prompt = _box45_original_prompt_document_check(user_question, execution_plan, selected_evidence, missing_information)
    documentary = [e for e in selected_evidence or [] if isinstance(e, dict) and e.get('selected_tool') == 'press_release_fy2025' and (e.get('output_name') == 'press_release_result') and isinstance(e.get('value'), dict) and str(e['value'].get('evidence_text') or '').strip()]
    exact_document_ids = [str(e.get('evidence_id')) for e in documentary if e.get('evidence_id')]
    if not documentary:
        return prompt
    prompt += '\n\nDOCUMENT EVIDENCE IDS: When populating used_evidence_ids, copy the full evidence_id verbatim, including numbered ::1, ::2 suffixes. Do not cite a parent STEP_N::press_release_result ID. Available documentary IDs: ' + json.dumps(exact_document_ids, ensure_ascii=False) + '\n'
    return prompt + '\n\nDOCUMENT AVAILABILITY CONTRACT: The selected_evidence includes successfully retrieved press releases (press_release_result). Never say that an available document was not retrieved. Use its actual content in the comparative management-outlook commentary. Absence of explicit numerical FY2026 guidance is distinct from absence of the press release; discuss qualitative outlook when supported. For any genuinely missing document, state the limitation without inventing facts. Do not claim that every requested metric is available merely because a press release exists.\n'

_box45_original_synthesis_document_check = agent_13_answer_synthesis
def agent_13_answer_synthesis(state: Dict[str, Any]) -> Dict[str, Any]:
    synthesis_state = dict(state)
    full = list(state.get('selected_evidence') or [])
    atoms = list(state.get('requirement_evidence') or [])
    known = {e.get('evidence_id') for e in full if isinstance(e, dict)}
    for ev in atoms:
        if isinstance(ev, dict) and ev.get('evidence_id') not in known:
            full.append(ev)
            known.add(ev.get('evidence_id'))
    synthesis_state['selected_evidence'] = full
    synthesis_state['document_retrieval_check'] = dual_domain_post_validation_check(synthesis_state)
    synthesis_state['requirement_evidence'] = full
    result = _box45_original_synthesis_document_check(synthesis_state)
    result['document_retrieval_check'] = synthesis_state['document_retrieval_check']
    return result
answer_synthesizer_agent = agent_13_answer_synthesis
if 'AGENT_REGISTRY' in globals() and ANSWER_SYNTHESIZER_AGENT_NAME in AGENT_REGISTRY:
    AGENT_REGISTRY[ANSWER_SYNTHESIZER_AGENT_NAME]['function'] = agent_13_answer_synthesis

_box45_prompt_before_document_classification = build_answer_synthesis_prompt
def build_answer_synthesis_prompt(user_question, execution_plan, selected_evidence, missing_information):
    prompt = _box45_prompt_before_document_classification(user_question, execution_plan, selected_evidence, missing_information)
    return prompt + '\n\nPRESS RELEASES ONLY (press_release_fy2025): The documentary category and its synonyms were already resolved by BOX 36. Treat matched_metric as the canonical category; do not re-test whether the supplied section qualifies as FY_RESULTS, GUIDANCE_OUTLOOK, CEO_COMMENTARY, CFO_COMMENTARY, HIGHLIGHTS, or another BOX 36 category. Summarize the actual supplied section content, retaining the original title and citing its evidence IDs. Missing individual figures are not missing sections. Do not apply this rule to quantitative tools.\n'
ANSWER_VALIDATOR_AGENT_NAME = 'answer_validator'
ANSWER_VALIDATOR_MODEL = MAIN_MODEL
MAX_VALIDATION_EVIDENCE = None
MAX_VALIDATION_MISSING_INFORMATION = None
MAX_VALIDATION_PROMPT_CHARACTERS = float('inf')
ANSWER_VALIDATOR_SYSTEM_INSTRUCTION = '\nYou are the Answer Validator of an agentic system for Dow Jones\nfinancial analysis.\n\nYou must critically check the answer produced by the main model\nby comparing it exclusively with:\n- the original question;\n- the selected evidence;\n- explicitly recorded missing information.\n\nMANDATORY RULES\n\n1. Do not add external knowledge.\n\n2. Do not perform new calculations.\n\n3. Do not autonomously determine whether a date is future, present,\n   or past, and do not use the current calendar as a validation\n   criterion. Evaluate the period exclusively against the\n   user_question and the evidence provided.\n\n4. Do not criticize, modify, or reinterpret the time horizon\n   requested by the user. Verify only that the period stated in the\n   answer matches the requested period and the one reported in the\n   available evidence.\n\n5. Verify that every significant quantitative or factual claim\n   is supported by the available evidence.\n\n6. Verify that the answer actually responds to the question.\n\n7. Verify that all relevant components of the question are\n   addressed or declared unavailable.\n\n8. Report omissions, contradictions, unsupported numbers,\n   excessive conclusions, and unjustified predictions.\n\n9. If a required component is absent from the evidence, the answer\n   is acceptable only if it clearly states the limitation.\n\n10. Do not penalize the answer for information that the system\n    correctly declares as missing.\n\n11. Set requires_revision = true if there is at least one\n    material issue requiring modification of the answer.\n    Do not invalidate or reject an otherwise supported answer solely because extra unrequested metrics or internal tool references appear; these should be omitted from user-facing wording without changing the substantive validation outcome.\n    Check that the answer follows the metrics explicitly or implicitly requested by the question, not every metric available in evidence.\n\n12. question_answer_alignment must measure correspondence between\n    the question and what the answer actually addresses.\n\n13. When the evidence contains display_value, verify that every\n    value reported in the answer exactly preserves its scale,\n    unit, currency, sign, and number of decimal places. Treat as\n    material any formatting change that alters the financial meaning\n    of the value.\n\n14. Verify in particular that prices and monetary amounts in USD\n    include the "$" symbol, that percentages and coefficients are not\n    confused with one another, and that documentary evidence preserves\n    the numerical precision expressed by the source.\n\n15. If the question compares a limited subset of Dow Jones stocks,\n    verify that the answer reports the value of the metric considered\n    for all stocks in the subset when those values are present in the\n    evidence, in addition to identifying the winner. This rule does NOT\n    apply when the comparison concerns the entire Dow Jones universe:\n    in that case it is not necessary to report the values of all\n    components.\n\n16. Treat as incorrect an answer that declares unavailable a\n    parameter explicitly present in the user_question, such as ticker,\n    time horizon, threshold, count, or requested metric.\n\n17. Treat as incorrect an answer that declares unavailable a parameter,\n    ticker, time period, metric, ranking, or other constraint when that\n    information is explicitly present in the user_question or is\n    supported by the selected factual evidence.\n\n18. The current flow serves as conversational context and does not\n    constitute factual evidence capable of contradicting or overriding\n    current results produced or reused by the plan steps.\n\n19. In follow-ups, verify that each reference has been resolved according\n    to this mandatory priority: first the information explicitly present\n    or semantically derivable from the current question; only for slots\n    that remain genuinely unresolved, the current flow searched backward\n    from the previous turn toward more distant ones. Treat as incorrect\n    an answer that gives precedence to a value inherited from the current\n    flow over a value determinable from the current question.\n\n20. Treat as incomplete an answer that does not explicitly state the\n    time horizon used for a metric or quantitative analysis when\n    that information is available in the user_question, the plan,\n    the evidence, or the current flow.\n\n21. For every Momentum result, verify that the answer explicitly states\n    in natural language the time horizon certified in the evidence.\n\n22. Verify that the stated period matches the period actually certified\n    in the evidence: effective_start_date, effective_end_date,\n    effective_time_periods, and effective_time_scope.\n\n23. For pearson_correlation without an explicit period,\n    effective_time_scope = "full_available_dataset" is valid: do not\n    artificially require a rolling period.\n\nPEARSON OVERRIDE (takes precedence over general missing-data and temporal rules):\nFor Pearson, the effective full-history period is intentional, never\nproof that the requested shorter-period data is unavailable. When the\nuser explicitly specifies a period, require an explicit explanation\nthat the project systematically calculates Pearson over the entire\navailable history. Reject any unsupported statement that the requested\nperiod\'s data was missing or unavailable. When no period is requested,\ndo not require the methodological disclosure. Do not reject the\nintentional Pearson period difference under temporal rule 24.\n\n24. If the requested period, operational period, effective period, and\n    communicated period do not match, set requires_revision = true.\n\nADDITIONAL TEMPORAL RULES\n\n- current_date and last_completed_market_session are authoritative\n  temporal references provided by the system.\n\n- Do not report current_date in the validation and do not autonomously\n  classify a date as future, present, or past.\n\n- Do not fail or require revision of an answer based on the model\'s\n  internal temporal knowledge.\n\n- Validate temporal coverage exclusively against user_question,\n  selected_evidence, tool results, and data/calculations actually\n  available in the dataset.\n\n- For forecasting requests without available data or calculations,\n  treat the limitation as missing information or insufficient dataset\n  coverage, not as an error caused by a future date.\n\nReturn exclusively a JSON object with this structure:\n\n{\n    "validation_result": {\n        "status": "PASSED or FAILED",\n        "supported_by_evidence": true,\n        "complete_given_available_evidence": true,\n        "missing_information_acknowledged": true,\n        "unsupported_claims": [],\n        "contradictions": [],\n        "omissions": [],\n        "validation_notes": []\n    },\n    "question_answer_alignment": {\n        "status": "ALIGNED or PARTIAL or MISALIGNED",\n        "score": 0.0,\n        "covered_components": [],\n        "uncovered_components": []\n    },\n    "requires_revision": false,\n    "revision_instructions": []\n}\n'.strip()

def _validation_ensure_list(value: Any) -> List[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, (tuple, set)):
        return list(value)
    return [value]

def _validation_unique_strings(values: Sequence[Any]) -> List[str]:
    output = []
    seen = set()
    for value in _validation_ensure_list(values):
        text = str(value).strip()
        if not text or text in seen:
            continue
        seen.add(text)
        output.append(text)
    return output

def _compact_validation_evidence(selected_evidence: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    compact_evidence = []
    for item in list(selected_evidence):
        if not isinstance(item, dict):
            continue
        if item.get('evidence_role') == 'context_only' or item.get('provenance') == 'current_flow':
            continue
        compact_evidence.append({'evidence_id': item.get('evidence_id'), 'objective': item.get('objective', ''), 'selected_tool': item.get('selected_tool'), 'output_name': item.get('output_name'), 'referenced_tickers': item.get('referenced_tickers', []), 'time_periods': item.get('time_periods', []), 'effective_tickers': item.get('effective_tickers', []), 'effective_start_date': item.get('effective_start_date'), 'effective_end_date': item.get('effective_end_date'), 'effective_time_periods': item.get('effective_time_periods', []), 'effective_time_scope': item.get('effective_time_scope'), 'value': item.get('value'), 'display_value': item.get('display_value', item.get('value'))})
    return compact_evidence

def _compact_validation_missing_information(missing_information: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    compact_missing = []
    for item in list(missing_information):
        if not isinstance(item, dict):
            continue
        compact_missing.append({'objective': item.get('objective', ''), 'selected_tool': item.get('selected_tool'), 'execution_status': item.get('execution_status'), 'missing_outputs': item.get('missing_outputs', []), 'reason': item.get('reason')})
    return compact_missing

def build_answer_validation_prompt(user_question: str, draft_answer: str, selected_evidence: Sequence[Dict[str, Any]], missing_information: Sequence[Dict[str, Any]]) -> str:
    payload = {'current_date': datetime.now().date().isoformat(), 'last_completed_market_session': str(DEFAULT_END_DATE), 'user_question': str(user_question).strip(), 'draft_answer': str(draft_answer).strip(), 'selected_evidence': _compact_validation_evidence(selected_evidence), 'missing_information': _compact_validation_missing_information(missing_information)}
    serialized_payload = json.dumps(payload, ensure_ascii=False, default=str)
    if len(serialized_payload) > MAX_VALIDATION_PROMPT_CHARACTERS:
        raise ValueError('The package intended for the Answer Validator exceeds the expected size limit.')
    return 'Critically validate the following answer using exclusively the provided JSON package:\n\n' + serialized_payload

def validate_answer_validator_output(raw_output: Dict[str, Any], draft_answer: str='', selected_evidence: Optional[Sequence[Dict[str, Any]]]=None, required_components: Optional[Sequence[Dict[str, Any]]]=None) -> Dict[str, Any]:
    if not isinstance(raw_output, dict):
        raise TypeError('The Answer Validator output must be a dictionary.')
    if selected_evidence is None:
        selected_evidence = []
    if required_components is None:
        required_components = []
    validation_result = raw_output.get('validation_result', {})
    question_answer_alignment = raw_output.get('question_answer_alignment', {})
    requires_revision = raw_output.get('requires_revision')
    revision_instructions = _validation_unique_strings(raw_output.get('revision_instructions', []))
    if not isinstance(validation_result, dict):
        raise TypeError('validation_result must be a dictionary.')
    if not isinstance(question_answer_alignment, dict):
        raise TypeError('question_answer_alignment must be a dictionary.')
    if not isinstance(requires_revision, bool):
        raise TypeError('requires_revision must be boolean.')
    validation_status = str(validation_result.get('status', '')).upper()
    alignment_status = str(question_answer_alignment.get('status', '')).upper()
    if validation_status not in {'PASSED', 'FAILED'}:
        raise ValueError('validation_result.status must be PASSED or FAILED.')
    if alignment_status not in {'ALIGNED', 'PARTIAL', 'MISALIGNED'}:
        raise ValueError('question_answer_alignment.status must be ALIGNED, PARTIAL, or MISALIGNED.')
    try:
        alignment_score = float(question_answer_alignment.get('score', 0.0))
    except (TypeError, ValueError) as error:
        raise TypeError('question_answer_alignment.score must be numeric.') from error
    if not 0.0 <= alignment_score <= 1.0:
        raise ValueError('question_answer_alignment.score must be between 0 and 1.')
    supported_by_evidence = bool(validation_result.get('supported_by_evidence', False))
    complete_given_available_evidence = bool(validation_result.get('complete_given_available_evidence', False))
    missing_information_acknowledged = bool(validation_result.get('missing_information_acknowledged', False))
    unsupported_claims = _validation_unique_strings(validation_result.get('unsupported_claims', []))
    contradictions = _validation_unique_strings(validation_result.get('contradictions', []))
    omissions = _validation_unique_strings(validation_result.get('omissions', []))
    validation_notes = _validation_unique_strings(validation_result.get('validation_notes', []))
    covered_components = _validation_unique_strings(question_answer_alignment.get('covered_components', []))
    uncovered_components = _validation_unique_strings(question_answer_alignment.get('uncovered_components', []))
    required_component_ids = {str(item.get('component_id')) for item in required_components if isinstance(item, dict) and item.get('component_id')}
    evidence_component_ids = {str(item.get('component_id')) for item in selected_evidence if isinstance(item, dict) and item.get('component_id')}
    uncovered_component_ids = sorted(required_component_ids - evidence_component_ids)
    deterministic_revision_instructions = []
    if uncovered_component_ids:
        deterministic_revision_instructions.append({'type': 'missing_atomic_components', 'component_ids': uncovered_component_ids, 'instruction': 'The answer cannot be considered complete until all available/unavailable components of the question have been explicitly reconciled.'})
    answer_text_upper = str(draft_answer).upper()
    for evidence in selected_evidence:
        if not isinstance(evidence, dict):
            continue
        referenced_tickers = _validation_unique_strings(evidence.get('effective_tickers', evidence.get('referenced_tickers', [])))
        normalized_tickers = [str(ticker).upper() for ticker in referenced_tickers if str(ticker).strip()]
        evidence_value = evidence.get('value')
        records = []
        if isinstance(evidence_value, dict):
            records = evidence_value.get('records', []) or []
        if 1 < len(normalized_tickers) < 30 and isinstance(records, list) and (len(records) == len(normalized_tickers)):
            missing_tickers = [ticker for ticker in normalized_tickers if ticker not in answer_text_upper]
            if missing_tickers:
                omissions.append('Subset values omitted for: ' + ', '.join(missing_tickers))
                deterministic_revision_instructions.append('Report the metric value for all components of the subset actually compared, in addition to the winner: ' + ', '.join(normalized_tickers) + '.')
        effective_scope = evidence.get('effective_time_scope')
        effective_start = evidence.get('effective_start_date')
        effective_end = evidence.get('effective_end_date')
        declared_periods = evidence.get('time_periods', []) or []
        if effective_scope == 'full_available_dataset':
            pass
        elif effective_start and effective_end and declared_periods:
            for declared_period in declared_periods:
                declared_text = str(declared_period)
                rolling_match = re.search("'value'\\s*:\\s*(\\d+).*?'unit'\\s*:\\s*'?(months|years|weeks|days)'?", declared_text, flags=re.IGNORECASE)
                if not rolling_match:
                    rolling_match = re.search('(?:last|past)\\s+(\\d+)\\s+(months|years|weeks|days)', declared_text, flags=re.IGNORECASE)
                if rolling_match:
                    amount = int(rolling_match.group(1))
                    unit = rolling_match.group(2).lower()
                    unit_map = {'months': 'months', 'years': 'years', 'weeks': 'weeks', 'days': 'days'}
                    unit = unit_map.get(unit, unit)
                    start_ts = pd.Timestamp(effective_start).normalize()
                    end_ts = pd.Timestamp(effective_end).normalize()
                    if unit == 'months':
                        expected_start = end_ts - pd.DateOffset(months=amount)
                    elif unit == 'years':
                        expected_start = end_ts - pd.DateOffset(years=amount)
                    elif unit == 'weeks':
                        expected_start = end_ts - pd.DateOffset(weeks=amount)
                    else:
                        expected_start = end_ts - pd.DateOffset(days=amount)
                    if abs((start_ts - expected_start).days) > 5:
                        contradictions.append(f'Temporal mismatch: the declared period ({declared_text}) does not match the period actually calculated ({effective_start}/{effective_end}).')
                        deterministic_revision_instructions.append('Do not communicate a period different from the one actually used by the tool; correct or block the answer until the requested period and the effective period match.')
                        break
    revision_instructions = _validation_unique_strings(list(revision_instructions) + deterministic_revision_instructions)
    material_issues_present = bool(unsupported_claims or contradictions or omissions or (validation_status == 'FAILED') or (alignment_status in {'PARTIAL', 'MISALIGNED'}))
    if material_issues_present:
        requires_revision = True
        if validation_status == 'PASSED':
            validation_status = 'FAILED'
        if not revision_instructions:
            revision_instructions = ['Revise the answer to correct the material issues detected by the validator.']
    else:
        requires_revision = False
    return {'validation_result': {'status': validation_status, 'supported_by_evidence': supported_by_evidence, 'complete_given_available_evidence': complete_given_available_evidence, 'missing_information_acknowledged': missing_information_acknowledged, 'unsupported_claims': unsupported_claims, 'contradictions': contradictions, 'omissions': omissions, 'validation_notes': validation_notes}, 'question_answer_alignment': {'status': alignment_status, 'score': alignment_score, 'covered_components': covered_components, 'uncovered_components': uncovered_components}, 'requires_revision': requires_revision, 'revision_instructions': revision_instructions}

def agent_14_answer_validation(state: Dict[str, Any], llm_function: Optional[Callable[..., Dict[str, Any]]]=None) -> Dict[str, Any]:
    start_time = time.perf_counter()
    if not isinstance(state, dict):
        raise TypeError('state must be a dictionary.')
    user_question = str(state.get('user_question', '')).strip()
    draft_answer = str(state.get('draft_answer', '')).strip()
    selected_evidence = state.get('selected_evidence', [])
    missing_information = state.get('missing_information', [])
    if not user_question:
        raise ValueError('user_question is not available.')
    if not draft_answer:
        raise ValueError('draft_answer is not available.')
    if not isinstance(selected_evidence, list):
        raise TypeError('selected_evidence must be a list.')
    if not isinstance(missing_information, list):
        raise TypeError('missing_information must be a list.')
    validation_prompt = build_answer_validation_prompt(user_question=user_question, draft_answer=draft_answer, selected_evidence=selected_evidence, missing_information=missing_information)
    if llm_function is None:
        if 'call_llm_json' not in globals():
            raise RuntimeError('call_llm_json is not available. Run BOX 6 first.')
        llm_function = call_llm_json
    raw_output = llm_function(system_instruction=ANSWER_VALIDATOR_SYSTEM_INSTRUCTION, user_content=validation_prompt, model=ANSWER_VALIDATOR_MODEL, temperature=0.0)
    validated_output = validate_answer_validator_output(raw_output, draft_answer=draft_answer, selected_evidence=selected_evidence, required_components=state.get('required_components', []) or [])
    pearson_planned = any((isinstance(step, dict) and (step.get('selected_tool') == 'pearson_correlation' or step.get('tool_name') == 'pearson_correlation') for step in state.get('execution_plan') or []))
    if pearson_planned:
        corrected_pearson = _box45_enforce_pearson_disclosure(draft_answer, user_question, state.get('execution_plan') or [], missing_information)
        if corrected_pearson != draft_answer.strip():
            validated_output['requires_revision'] = True
            validated_output['revision_instructions'] = list(validated_output.get('revision_instructions') or []) + ["For Pearson, remove any unsupported claim that the requested period's data is unavailable; if the question specifies a period, state that full history is used by project methodology. Preserve the supported Pearson coefficient and ticker pair."]
            validated_output['validation_result']['status'] = 'FAILED'
            validated_output['validation_result'].setdefault('validation_notes', []).append('Pearson methodological disclosure requires correction.')
    execution_statuses = state.get('tool_execution_status') or {}
    execution_results = state.get('tool_results') or {}
    failed_required_steps = []
    for planned_step in state.get('execution_plan') or []:
        if not isinstance(planned_step, dict):
            continue
        if planned_step.get('action_type') != 'execute_tool':
            continue
        planned_step_id = planned_step.get('step_id')
        step_status = execution_statuses.get(planned_step_id)
        step_outputs = execution_results.get(planned_step_id) or {}
        required_outputs = planned_step.get('required_outputs') or []
        missing_outputs = [output_name for output_name in required_outputs if not isinstance(step_outputs, dict) or output_name not in step_outputs or step_outputs[output_name] is None or (hasattr(step_outputs[output_name], 'empty') and step_outputs[output_name].empty)]
        if step_status != 'COMPLETED' or missing_outputs:
            failed_required_steps.append(f"{planned_step_id}: status={step_status or 'UNAVAILABLE'}; missing outputs={missing_outputs}")
    if failed_required_steps:
        validated_output['validation_result']['status'] = 'FAILED'
        validated_output['validation_result']['complete_given_available_evidence'] = False
        validated_output['validation_result'].setdefault('omissions', []).append('Required steps not completed or required outputs missing.')
        validated_output['validation_result'].setdefault('validation_notes', []).extend(failed_required_steps)
        validated_output['requires_revision'] = True
        validated_output['revision_instructions'] = list(validated_output.get('revision_instructions') or []) + ['Do not declare the answer complete: one or more required steps failed or did not return the required outputs. Report the execution problem without inventing results.']
    execution_time = round(time.perf_counter() - start_time, 6)
    return {'validation_result': validated_output['validation_result'], 'question_answer_alignment': validated_output['question_answer_alignment'], 'requires_revision': validated_output['requires_revision'], 'revision_instructions': validated_output['revision_instructions'], 'answer_validation_status': 'completed', 'answer_validation_error': None, 'answer_validation_model': ANSWER_VALIDATOR_MODEL, 'answer_validation_execution_time_seconds': execution_time, 'current_question_node': 'answer_validation', 'question_workflow_status': 'revision_required' if validated_output['requires_revision'] else 'answer_validated', 'next_node': 'answer_revision' if validated_output['requires_revision'] else 'end'}
answer_validator_agent = agent_14_answer_validation
if 'AGENT_REGISTRY' in globals() and 'build_registry_entry' in globals():
    AGENT_REGISTRY[ANSWER_VALIDATOR_AGENT_NAME] = build_registry_entry(name=ANSWER_VALIDATOR_AGENT_NAME, function=agent_14_answer_validation, component_type='llm_agent', description='Validates and refutes the draft_answer by comparing it with the question, available evidence, and missing information.', required_state_fields=['user_question', 'selected_evidence', 'missing_information', 'draft_answer'], output_fields=['validation_result', 'question_answer_alignment', 'requires_revision'], uses_llm=True)
    final_state['agent_registry'] = AGENT_REGISTRY
final_state.setdefault('validation_result', {})
final_state.setdefault('question_answer_alignment', {})
final_state.setdefault('requires_revision', False)
final_state.setdefault('revision_instructions', [])
final_state.setdefault('answer_validation_status', '')
final_state.setdefault('answer_validation_error', None)
final_state.setdefault('answer_validation_model', '')
final_state.setdefault('answer_validation_execution_time_seconds', 0.0)

def _box_46_fake_critic_pass(system_instruction: str, user_content: str, model: str, temperature: float) -> Dict[str, Any]:
    return {'validation_result': {'status': 'PASSED', 'supported_by_evidence': True, 'complete_given_available_evidence': True, 'missing_information_acknowledged': True, 'unsupported_claims': [], 'contradictions': [], 'omissions': [], 'validation_notes': ['The volatility and momentum values are consistent with the available evidence.', 'The missing FY2025 guidance is explicitly declared in the answer.']}, 'question_answer_alignment': {'status': 'ALIGNED', 'score': 1.0, 'covered_components': ['risk', 'momentum', 'FY2025 guidance as missing information'], 'uncovered_components': []}, 'requires_revision': False, 'revision_instructions': []}

def _box_46_fake_critic_fail(system_instruction: str, user_content: str, model: str, temperature: float) -> Dict[str, Any]:
    return {'validation_result': {'status': 'FAILED', 'supported_by_evidence': False, 'complete_given_available_evidence': False, 'missing_information_acknowledged': False, 'unsupported_claims': ['The answer claims favorable FY2025 guidance without available evidence.'], 'contradictions': [], 'omissions': ['It does not state that FY2025 guidance is absent.'], 'validation_notes': []}, 'question_answer_alignment': {'status': 'PARTIAL', 'score': 0.67, 'covered_components': ['risk', 'momentum'], 'uncovered_components': ['FY2025 guidance']}, 'requires_revision': True, 'revision_instructions': ['Remove the unsupported conclusion about FY2025 guidance and state that the information is not available.']}

def _atomic_numeric_tokens(value: Any) -> List[str]:
    tokens = []

    def walk(x):
        if isinstance(x, dict):
            for v in x.values():
                walk(v)
        elif isinstance(x, (list, tuple)):
            for v in x:
                walk(v)
        elif isinstance(x, (int, float)) and (not isinstance(x, bool)):
            tokens.extend([str(x), f'{x:.2f}', f'{x:.4f}'])
    walk(value)
    return sorted({t.rstrip('0').rstrip('.') if '.' in t else t for t in tokens if t})

def deterministic_atomic_answer_check(state: Dict[str, Any], draft_answer: str) -> Dict[str, Any]:
    plan = [s for s in state.get('execution_plan') or [] if isinstance(s, dict) and s.get('atomic_id')]
    evidence = [e for e in state.get('selected_evidence') or [] if isinstance(e, dict) and e.get('atomic_id')]
    evidence_by_atom = {e['atomic_id']: e for e in evidence}
    required = {s['atomic_id']: s for s in plan if s.get('action_type') in {'execute_tool', 'reuse_output'}}
    missing_evidence = sorted(set(required) - set(evidence_by_atom))
    missing_numeric = []
    text = str(draft_answer or '')
    for aid, step in required.items():
        ev = evidence_by_atom.get(aid)
        if not ev:
            continue
        tokens = _atomic_numeric_tokens(ev.get('value'))
        if tokens and (not any((t in text for t in tokens))):
            missing_numeric.append({'atomic_id': aid, 'tool_name': step.get('selected_tool'), 'tickers': step.get('referenced_tickers', []), 'metric': step.get('metric'), 'time_periods': step.get('time_periods', [])})
    return {'required_atomic_ids': sorted(required), 'evidence_atomic_ids': sorted(evidence_by_atom), 'missing_evidence_atomic_ids': missing_evidence, 'missing_numeric_atomic_components': missing_numeric, 'passed': not missing_evidence and (not missing_numeric)}
_original_agent_14_answer_validation_box46 = agent_14_answer_validation

def agent_14_answer_validation(state: Dict[str, Any]) -> Dict[str, Any]:
    result = _original_agent_14_answer_validation_box46(state)
    check = deterministic_atomic_answer_check(state, state.get('draft_answer', ''))
    result['atomic_validation'] = check
    if not check['passed']:
        result['validation_result']['status'] = 'FAILED'
        result['validation_result']['complete_given_available_evidence'] = False
        result['validation_result'].setdefault('validation_notes', []).append('Deterministic atomic coverage failed: every requested tool+ticker+metric+time atom must have matching evidence and its numerical result in the answer.')
        result['validation_result'].setdefault('omissions', []).extend([str(x) for x in check['missing_numeric_atomic_components']])
        result['requires_revision'] = True
        result['revision_instructions'] = list(result.get('revision_instructions') or []) + ['Restore every missing atomic numerical component using only the evidence with the same atomic_id. Never substitute another ticker, metric or time period.']
        result['question_workflow_status'] = 'revision_required'
        result['next_node'] = 'answer_revision'
    return result
answer_validator_agent = agent_14_answer_validation
if 'AGENT_REGISTRY' in globals() and ANSWER_VALIDATOR_AGENT_NAME in AGENT_REGISTRY:
    try:
        AGENT_REGISTRY[ANSWER_VALIDATOR_AGENT_NAME]['function'] = agent_14_answer_validation
    except Exception:
        pass

def deterministic_requirement_answer_check(state: Dict[str, Any], draft_answer: str) -> Dict[str, Any]:
    required_atoms = {a.get('requirement_id'): a for a in state.get('requirement_atoms') or [] if isinstance(a, dict) and a.get('requirement_id')}
    evidence = {e.get('requirement_id'): e for e in state.get('requirement_evidence') or state.get('selected_evidence') or [] if isinstance(e, dict) and e.get('requirement_id')}
    required_ids = set(required_atoms)
    evidence_ids = set(evidence)
    missing_evidence = sorted(required_ids - evidence_ids)
    unexpected_evidence = sorted(evidence_ids - required_ids)
    missing_values = []
    text = str(draft_answer or '')
    for rid in sorted(required_ids & evidence_ids):
        ev = evidence[rid]
        value = ev.get('value')
        tokens = _atomic_numeric_tokens(value)
        if tokens and (not any((token in text for token in tokens))):
            atom = required_atoms[rid]
            missing_values.append({'requirement_id': rid, 'ticker': atom.get('ticker'), 'metric': atom.get('metric'), 'time_period': atom.get('time_period'), 'expected_value': value})
    return {'required_requirement_ids': sorted(required_ids), 'evidence_requirement_ids': sorted(evidence_ids), 'missing_evidence_requirement_ids': missing_evidence, 'unexpected_evidence_requirement_ids': unexpected_evidence, 'missing_answer_values': missing_values, 'required_count': len(required_ids), 'evidence_count': len(evidence_ids), 'passed': not missing_evidence and (not unexpected_evidence) and (not missing_values)}
_original_agent_14_answer_validation_requirement_check = agent_14_answer_validation

def agent_14_answer_validation(state: Dict[str, Any]) -> Dict[str, Any]:
    result = _original_agent_14_answer_validation_requirement_check(state)
    check = deterministic_requirement_answer_check(state, state.get('draft_answer', ''))
    result['requirement_validation'] = check
    if not check['passed']:
        vr = result.setdefault('validation_result', {})
        vr['status'] = 'FAILED'
        vr['complete_given_available_evidence'] = False
        vr.setdefault('validation_notes', []).append('Deterministic requirement coverage failed: every requested ticker × metric × period requirement must have its own evidence and numerical value in the answer.')
        vr.setdefault('omissions', []).extend([str(x) for x in check['missing_answer_values']])
        result['requires_revision'] = True
        result['revision_instructions'] = list(result.get('revision_instructions') or []) + ['Restore every missing requirement value using only evidence with the same requirement_id; never substitute another ticker, metric, or time period.']
        result['question_workflow_status'] = 'revision_required'
        result['next_node'] = 'answer_revision'
    return result
answer_validator_agent = agent_14_answer_validation
if 'AGENT_REGISTRY' in globals() and ANSWER_VALIDATOR_AGENT_NAME in AGENT_REGISTRY:
    try:
        AGENT_REGISTRY[ANSWER_VALIDATOR_AGENT_NAME]['function'] = agent_14_answer_validation
    except Exception:
        pass
_original_deterministic_requirement_answer_check_identity = deterministic_requirement_answer_check

def deterministic_requirement_answer_check(state: Dict[str, Any], draft_answer: str) -> Dict[str, Any]:
    check = _original_deterministic_requirement_answer_check_identity(state, draft_answer)
    atoms = {a.get('requirement_id'): a for a in state.get('requirement_atoms') or [] if isinstance(a, dict) and a.get('requirement_id')}
    evidence = {e.get('requirement_id'): e for e in state.get('requirement_evidence') or state.get('selected_evidence') or [] if isinstance(e, dict) and e.get('requirement_id')}
    mismatches = []
    for rid in sorted(set(atoms) & set(evidence)):
        atom = atoms[rid]
        ev = evidence[rid]
        expected = {'ticker': str(atom.get('ticker') or '').strip().upper(), 'metric': canonical_metric_name(atom.get('metric')), 'time_period': canonical_time_period(atom.get('time_period'))}
        observed = {'ticker': str(ev.get('ticker') or '').strip().upper(), 'metric': canonical_metric_name(ev.get('metric')), 'time_period': canonical_time_period(ev.get('time_period'))}
        if expected != observed:
            mismatches.append({'requirement_id': rid, 'expected': expected, 'observed': observed})
    check['identity_mismatches'] = mismatches
    check['passed'] = bool(check.get('passed')) and (not mismatches)
    return check
ANSWER_VALIDATOR_SYSTEM_INSTRUCTION = ANSWER_VALIDATOR_SYSTEM_INSTRUCTION + '\n\nDETERMINISTIC SELECTION CONSTRAINT\nIf selected_evidence contains an item with evidence_type = "deterministic_condition_filter" and authoritative = true:\n- filtered_tickers is the authoritative result of the deterministic selection already performed by the Executor;\n- DO NOT recalculate filters, thresholds, intersections, rankings, Top-N/Bottom-N, or ticker membership in the result;\n- DO NOT add, remove, replace, or reselect tickers based on a new interpretation of the quantitative evidence;\n- Instead, validate that draft_answer preserves the deterministic selection and that values, coverage, and explanations are supported by the evidence;\n- Any subsequent ranking/Top-N is valid only if it has already been produced deterministically by the workflow and is present in the evidence/plan, not if reconstructed by the Validator.\n\nMANDATORY JSON OUTPUT STRUCTURAL CONSTRAINT\nThe key structure must match the required schema EXACTLY.\n- requires_revision MUST be a TOP-LEVEL property of the JSON object and MUST be a JSON boolean true/false;\n- revision_instructions MUST be a TOP-LEVEL property of the JSON object;\n- DO NOT place requires_revision or revision_instructions inside validation_result, question_answer_alignment, or any other nested object;\n- DO NOT move, rename, or nest the required keys.\n'
_original_validate_answer_validator_output_schema_contract = validate_answer_validator_output

def validate_answer_validator_output(raw_output: Dict[str, Any], draft_answer: str='', selected_evidence: Optional[Sequence[Dict[str, Any]]]=None, required_components: Optional[Sequence[Dict[str, Any]]]=None) -> Dict[str, Any]:
    if not isinstance(raw_output, dict):
        return _original_validate_answer_validator_output_schema_contract(raw_output, draft_answer, selected_evidence, required_components)
    normalized_output = copy.deepcopy(raw_output)
    schema_violations = []
    if 'requires_revision' not in normalized_output:
        nested = normalized_output.get('validation_result')
        nested_value = nested.get('requires_revision') if isinstance(nested, dict) else None
        if isinstance(nested_value, bool):
            schema_violations.append('requires_revision was returned inside validation_result instead of as a top-level key.')
            normalized_output['requires_revision'] = nested_value
        else:
            validation_status = str((nested or {}).get('status', '')).upper() if isinstance(nested, dict) else ''
            alignment = normalized_output.get('question_answer_alignment')
            alignment_status = str((alignment or {}).get('status', '')).upper() if isinstance(alignment, dict) else ''
            recovered = validation_status == 'FAILED' or alignment_status in {'PARTIAL', 'MISALIGNED'}
            schema_violations.append('requires_revision top-level missing; value recovered deterministically from validation/alignment status.')
            normalized_output['requires_revision'] = bool(recovered)
    if 'revision_instructions' not in normalized_output:
        nested = normalized_output.get('validation_result')
        nested_value = nested.get('revision_instructions') if isinstance(nested, dict) else None
        if isinstance(nested_value, list):
            schema_violations.append('revision_instructions was returned inside validation_result instead of as a top-level key.')
            normalized_output['revision_instructions'] = nested_value
        else:
            normalized_output['revision_instructions'] = []
            schema_violations.append('revision_instructions top-level missing; recovered as an empty list.')
    validated = _original_validate_answer_validator_output_schema_contract(normalized_output, draft_answer, selected_evidence, required_components)
    if schema_violations:
        validated['validator_schema_violation'] = True
        validated['validator_schema_violations'] = schema_violations
    else:
        validated['validator_schema_violation'] = False
        validated['validator_schema_violations'] = []
    return validated

def audit_reuse_evidence_coverage(state):
    """Report valid stored reuse outputs that were omitted from selected evidence."""
    statuses = state.get('tool_execution_status') or {}
    selected = state.get('selected_evidence') or []
    selected_text = str(selected)
    issues = []
    for step in state.get('execution_plan') or []:
        if not isinstance(step, dict):
            continue
        sid = step.get('step_id')
        if step.get('action_type') != 'reuse_output':
            continue
        status = str(statuses.get(sid) or '').upper()
        if status not in {'REUSED', 'COMPLETED'}:
            issues.append({'step_id': sid, 'error': 'REUSE_STATUS_MISSING', 'status': status or None})
        elif sid and str(sid) not in selected_text:
            issues.append({'step_id': sid, 'error': 'REUSED_EVIDENCE_NOT_LINKED'})
    return issues

_box46_original_validator_document_check = agent_14_answer_validation
def agent_14_answer_validation(state: Dict[str, Any]) -> Dict[str, Any]:
    result = _box46_original_validator_document_check(state)
    check = dual_domain_post_validation_check(state)
    result['document_retrieval_check'] = check
    validation = result.setdefault('validation_result', {})
    validation['document_retrieved'] = check['document_retrieved']
    validation['all_documents_retrieved'] = check['all_documents_retrieved']
    validation['tool_evidence_retrieved'] = check.get('tool_evidence_retrieved', [])
    validation['all_requested_tools_retrieved'] = check.get('all_requested_tools_retrieved')
    if (state.get('dual_domain_check') or {}).get('active'):
        missing_rows = [r for r in check.get('tool_evidence_retrieved', []) if r.get('retrieved') == 0]
        validation['missing_requested_tool_evidence'] = missing_rows
        if missing_rows:
            validation.setdefault('validation_notes', []).append('Explicitly disclose missing selected evidence for: ' + ', '.join((str(r.get('tool')) + '/' + str(r.get('metric')) for r in missing_rows)))
        validation['tool_coverage_review_required'] = bool(missing_rows)
    if check['active'] and check['all_documents_retrieved'] == 0:
        validation['complete_given_available_evidence'] = False
        validation.setdefault('validation_notes', []).append('One or more requested press releases were not retrieved; disclose the missing source and do not fabricate its content.')
    return result
answer_validator_agent = agent_14_answer_validation
if 'AGENT_REGISTRY' in globals() and ANSWER_VALIDATOR_AGENT_NAME in AGENT_REGISTRY:
    AGENT_REGISTRY[ANSWER_VALIDATOR_AGENT_NAME]['function'] = agent_14_answer_validation
ANSWER_REVISION_NODE_NAME = 'controlled_answer_revision'
ANSWER_REVISION_MODEL = MAIN_MODEL
DEFAULT_MAXIMUM_REVISIONS = 2
MAX_REVISION_EVIDENCE = None
MAX_REVISION_MISSING_INFORMATION = None
MAX_REVISION_PROMPT_CHARACTERS = float('inf')
ANSWER_REVISION_SYSTEM_INSTRUCTION = '\nYou are the controlled answer reviewer of an agentic system\nfor Dow Jones financial analysis.\n\nYou receive:\n- the original question;\n- the previous answer;\n- the outcome of the Answer Validator;\n- the revision instructions;\n- the selected evidence;\n- the missing information.\n\nYou must correct exclusively the problems identified by the\nvalidation.\n\nMANDATORY RULES\n\n1. Do not perform new calculations.\n\n2. Do not add external knowledge.\n\n3. Do not invent values, facts, sources, or conclusions.\n\n4. Use exclusively the evidence provided.\n\n5. If information is missing, state that it is missing.\n\n6. Remove or correct all claims identified as unsupported.\n\n7. Resolve the omissions identified by the Answer Validator when the\n   available evidence allows it.\n\n8. Do not modify correct parts of the answer unnecessarily.\n\n9. When the revision_instructions identify missing component_id values,\n   correct the answer using exclusively the already certified evidence\n   associated with those components. Do not recalculate, do not perform\n   additional retrieval, and do not replace a component with a different metric.\n\n10. Do not transform descriptive analyses into predictions.\n\n11. The new answer must remain concise and directly\n    connected to the question.\n\n12. Never expose technical step identifiers, internal agent or tool names, evidence IDs, or workflow details in the user-facing answer.\n    Present only the financial metrics explicitly or implicitly requested by the question and context. Omit unrelated metrics merely available in evidence. This is a presentation correction, not a reason to invalidate an otherwise supported answer; preserve all requested results and comparisons.\n\n13. If the question compares a limited subset of Dow Jones stocks\n    and the previous answer reports only the winning result, integrate\n    the answer with the values of the same metric for all other stocks\n    in the subset actually compared, provided they are present in the\n    evidence. DO NOT apply this expansion when the comparison concerns\n    the entire Dow Jones universe: in that case it is not necessary to\n    report the values of all stocks.\n\n14. If the draft declares missing a parameter explicitly present\n    in the user_question, remove the disclaimer and use the parameter\n    provided by the user.\n\n15. If the draft declares missing information explicitly present\n    in the user_question or validly retrieved from the current flow,\n    remove the incorrect disclaimer and use the available reference.\n\n16. In follow-ups, keep ticker, time period, metric,\n    ranking, and other constraints consistent by applying this mandatory\n    priority: first the information explicitly present or semantically\n    derivable from the current question; only for slots that remain genuinely\n    unresolved, retrieve the current flow backward from the previous turn\n    toward more distant ones. Never replace a value determinable from the\n    current question with an inherited value.\n\n17. If the answer omits a time horizon certified in the\n    evidence, integrate the answer using exclusively\n    effective_start_date, effective_end_date, effective_time_periods,\n    and effective_time_scope. Do not communicate a period merely because\n    it appears in the question or plan if it does not match the one\n    actually used by the tool.\n\nPEARSON OVERRIDE (takes precedence over generic missing-data rules):\nFull-history Pearson is deliberate project methodology, not missing\nshorter-period data. If the question explicitly specifies a period,\nexplain this methodological rule. Remove unsupported claims that the\nrequested period\'s data was unavailable. If no period was requested,\ndo not add the methodological explanation. Preserve the supported\ncorrelation coefficients and ticker pairs.\n\n18. For pearson_correlation without an explicit period, when\n    effective_time_scope = "full_available_dataset", state that the\n    correlation is calculated over the entire available dataset without\n    inventing a rolling period.\n\n19. If a Momentum answer omits the time horizon, add it\n    using exclusively the period certified in the evidence.\n\n20. Use a sentence such as:\n    "Momentum is calculated over a time horizon of X months."\n\n21. Do not infer or invent the period from the metric name.\n\nADDITIONAL TEMPORAL RULES\n\n- current_date and last_completed_market_session are authoritative\n  temporal references provided by the system and must be used\n  only as internal context.\n\n- Do not report current_date in the revised answer and do not introduce\n  autonomous judgments that a date is future, present, or past.\n\n- Correct any temporal issues exclusively on the basis of\n  selected_evidence, tool results, and actual dataset coverage.\n\n- For forecasting requests without available data or calculations,\n  state the unavailability or insufficient dataset coverage,\n  without autonomously attributing it to the date being in the future.\n\nReturn exclusively a JSON object with this structure:\n\n{\n    "revised_answer": "new complete version of the answer",\n    "revision_actions": [\n        "brief description of the corrections made"\n    ]\n}\n'.strip()

def _revision_ensure_list(value: Any) -> List[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, (tuple, set)):
        return list(value)
    return [value]

def _revision_unique_strings(values: Sequence[Any]) -> List[str]:
    output = []
    seen = set()
    for value in _revision_ensure_list(values):
        text = str(value).strip()
        if not text or text in seen:
            continue
        seen.add(text)
        output.append(text)
    return output

def _revision_append_version(versions: Sequence[Any], answer: str) -> List[str]:
    clean_versions = _revision_unique_strings(versions)
    clean_answer = str(answer).strip()
    if clean_answer and (not clean_versions or clean_versions[-1] != clean_answer):
        clean_versions.append(clean_answer)
    return clean_versions

def _compact_revision_evidence(selected_evidence: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    compact_evidence = []
    for item in list(selected_evidence):
        if not isinstance(item, dict):
            continue
        compact_evidence.append({'evidence_id': item.get('evidence_id'), 'selected_tool': item.get('selected_tool'), 'output_name': item.get('output_name'), 'referenced_tickers': item.get('referenced_tickers', []), 'time_periods': item.get('time_periods', []), 'effective_tickers': item.get('effective_tickers', []), 'effective_start_date': item.get('effective_start_date'), 'effective_end_date': item.get('effective_end_date'), 'effective_time_periods': item.get('effective_time_periods', []), 'effective_time_scope': item.get('effective_time_scope'), 'value': item.get('value')})
    return compact_evidence

def _compact_revision_missing_information(missing_information: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    compact_missing = []
    for item in list(missing_information):
        if not isinstance(item, dict):
            continue
        compact_missing.append({'objective': item.get('objective', ''), 'selected_tool': item.get('selected_tool'), 'execution_status': item.get('execution_status'), 'missing_outputs': item.get('missing_outputs', []), 'reason': item.get('reason')})
    return compact_missing

def build_answer_revision_prompt(user_question: str, draft_answer: str, validation_result: Dict[str, Any], question_answer_alignment: Dict[str, Any], revision_instructions: Sequence[str], selected_evidence: Sequence[Dict[str, Any]], missing_information: Sequence[Dict[str, Any]], revision_count: int, maximum_revisions: int) -> str:
    payload = {'current_date': datetime.now().date().isoformat(), 'last_completed_market_session': str(DEFAULT_END_DATE), 'user_question': str(user_question).strip(), 'draft_answer': str(draft_answer).strip(), 'validation_result': validation_result if isinstance(validation_result, dict) else {}, 'question_answer_alignment': question_answer_alignment if isinstance(question_answer_alignment, dict) else {}, 'revision_instructions': _revision_unique_strings(revision_instructions), 'selected_evidence': _compact_revision_evidence(selected_evidence), 'missing_information': _compact_revision_missing_information(missing_information), 'revision_count': int(revision_count), 'maximum_revisions': int(maximum_revisions)}
    serialized_payload = json.dumps(payload, ensure_ascii=False, default=str)
    if len(serialized_payload) > MAX_REVISION_PROMPT_CHARACTERS:
        raise ValueError('The package intended for revision exceeds the expected size limit.')
    return 'Revise the answer by correcting exclusively the problems identified in the following JSON package:\n\n' + serialized_payload

def validate_answer_revision_output(raw_output: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(raw_output, dict):
        raise TypeError('The revision output must be a dictionary.')
    revised_answer = str(raw_output.get('revised_answer', '')).strip()
    if not revised_answer:
        raise ValueError('revised_answer is empty.')
    revision_actions = _revision_unique_strings(raw_output.get('revision_actions', []))
    return {'revised_answer': revised_answer, 'revision_actions': revision_actions}

def controlled_answer_revision_node(state: Dict[str, Any], llm_function: Optional[Callable[..., Dict[str, Any]]]=None) -> Dict[str, Any]:
    start_time = time.perf_counter()
    if not isinstance(state, dict):
        raise TypeError('state must be a dictionary.')
    user_question = str(state.get('user_question', '')).strip()
    draft_answer = str(state.get('draft_answer', '')).strip()
    validation_result = state.get('validation_result', {})
    question_answer_alignment = state.get('question_answer_alignment', {})
    requires_revision = bool(state.get('requires_revision', False))
    revision_instructions = state.get('revision_instructions', [])
    selected_evidence = state.get('selected_evidence', [])
    missing_information = state.get('missing_information', [])
    answer_versions = state.get('answer_versions', [])
    revision_count = int(state.get('revision_count', 0))
    maximum_revisions = int(state.get('maximum_revisions', DEFAULT_MAXIMUM_REVISIONS))
    if not user_question:
        raise ValueError('user_question is not available.')
    if not draft_answer:
        raise ValueError('draft_answer is not available.')
    if revision_count < 0:
        raise ValueError('revision_count cannot be negative.')
    if maximum_revisions < 0:
        raise ValueError('maximum_revisions cannot be negative.')
    answer_versions = _revision_append_version(versions=answer_versions, answer=draft_answer)
    draft_answer = _box45_enforce_pearson_disclosure(draft_answer, user_question, state.get('execution_plan') or [], missing_information)
    if not requires_revision:
        execution_time = round(time.perf_counter() - start_time, 6)
        return {'draft_answer': draft_answer, 'answer_versions': answer_versions, 'final_answer': draft_answer, 'revision_count': revision_count, 'maximum_revisions': maximum_revisions, 'requires_revision': False, 'revision_actions': [], 'revision_status': 'validated_without_revision', 'revision_limit_reached': False, 'revision_execution_time_seconds': execution_time, 'current_question_node': 'answer_revision', 'question_workflow_status': 'answer_validated', 'next_node': 'end'}
    if revision_count >= maximum_revisions:
        execution_time = round(time.perf_counter() - start_time, 6)
        return {'draft_answer': draft_answer, 'answer_versions': answer_versions, 'final_answer': draft_answer, 'revision_count': revision_count, 'maximum_revisions': maximum_revisions, 'requires_revision': True, 'revision_actions': [], 'revision_status': 'revision_limit_reached', 'revision_limit_reached': True, 'revision_execution_time_seconds': execution_time, 'current_question_node': 'answer_revision', 'question_workflow_status': 'revision_limit_reached', 'next_node': 'end'}
    revision_prompt = build_answer_revision_prompt(user_question=user_question, draft_answer=draft_answer, validation_result=validation_result, question_answer_alignment=question_answer_alignment, revision_instructions=revision_instructions, selected_evidence=selected_evidence, missing_information=missing_information, revision_count=revision_count, maximum_revisions=maximum_revisions)
    if llm_function is None:
        if 'call_llm_json' not in globals():
            raise RuntimeError('call_llm_json is not available. Run BOX 6 first.')
        llm_function = call_llm_json
    raw_output = llm_function(system_instruction=ANSWER_REVISION_SYSTEM_INSTRUCTION, user_content=revision_prompt, model=ANSWER_REVISION_MODEL, temperature=0.0)
    validated_revision = validate_answer_revision_output(raw_output)
    revised_answer = validated_revision['revised_answer']
    revised_answer = _box45_enforce_pearson_disclosure(revised_answer, user_question, state.get('execution_plan') or [], missing_information)
    revised_answer_versions = _revision_append_version(versions=answer_versions, answer=revised_answer)
    updated_revision_count = revision_count + 1
    execution_time = round(time.perf_counter() - start_time, 6)
    return {'draft_answer': revised_answer, 'answer_versions': revised_answer_versions, 'final_answer': '', 'revision_count': updated_revision_count, 'maximum_revisions': maximum_revisions, 'requires_revision': False, 'revision_actions': validated_revision['revision_actions'], 'revision_status': 'revised_pending_validation', 'revision_limit_reached': False, 'revision_execution_time_seconds': execution_time, 'current_question_node': 'answer_revision', 'question_workflow_status': 'revision_completed', 'next_node': 'answer_validation'}
answer_revision_node = controlled_answer_revision_node
if 'AGENT_REGISTRY' in globals() and 'build_registry_entry' in globals():
    AGENT_REGISTRY[ANSWER_REVISION_NODE_NAME] = build_registry_entry(name=ANSWER_REVISION_NODE_NAME, function=controlled_answer_revision_node, component_type='controlled_llm_node', description='Manages controlled answer revision, applies the corrections required by the Answer Validator, and prevents cycles beyond the defined limit.', required_state_fields=['validation_result', 'draft_answer', 'revision_count'], output_fields=['draft_answer', 'answer_versions', 'final_answer', 'revision_count', 'requires_revision', 'revision_status'], uses_llm=True)
    final_state['agent_registry'] = AGENT_REGISTRY
final_state.setdefault('answer_versions', [])
final_state.setdefault('final_answer', '')
final_state.setdefault('revision_count', 0)
final_state.setdefault('maximum_revisions', DEFAULT_MAXIMUM_REVISIONS)
final_state.setdefault('revision_actions', [])
final_state.setdefault('revision_status', '')
final_state.setdefault('revision_limit_reached', False)
final_state.setdefault('revision_execution_time_seconds', 0.0)

# Removed unused incomplete fake revision test helper (undefined _box_47_valid_draft).
ANSWER_REVISION_SYSTEM_INSTRUCTION = ANSWER_REVISION_SYSTEM_INSTRUCTION + '\n\nDETERMINISTIC SELECTION CONSTRAINT\nIf selected_evidence contains an item with evidence_type = "deterministic_condition_filter" and authoritative = true:\n- filtered_tickers is the authoritative result of the deterministic selection already performed by the workflow;\n- DO NOT recalculate filters, thresholds, intersections, rankings, Top-N/Bottom-N, or ticker membership;\n- DO NOT add, remove, replace, or reselect tickers during revision;\n- correct only form, coverage, values, or explanations required by validation, using the certified evidence;\n- ignore any revision_instructions asking to modify the authoritative selection based on a new calculation or comparison performed by the LLM;\n- any subsequent ranking/Top-N may be applied only if it has already been produced deterministically by the workflow and transmitted in the evidence/plan.\n'
ANSWER_REVISION_SYSTEM_INSTRUCTION += '\nFor composed questions, honor the tool_evidence_retrieved and\nmissing_requested_tool_evidence checks provided by the validator.\nIntegrate every requested metric supported by selected_evidence into the revised\nanswer, and explicitly distinguish missing selected evidence. Do not invent\nmetrics, documents, or sources. Do not rerun retrieval tools.\n'
QUESTION_GRAPH_NODE_NAMES = {'retrieval': 'retrieval', 'analysis': 'question_analysis', 'planning': 'question_planning', 'execution': 'tool_execution', 'normalization': 'evidence_normalization', 'synthesis': 'answer_synthesis', 'validation': 'answer_validation', 'revision': 'answer_revision'}
QUESTION_GRAPH_REQUIRED_COMPONENTS = {'retrieval_node': globals().get('retrieval_node'), 'agent_11_question_analysis': globals().get('agent_11_question_analysis'), 'agent_12_question_planning': globals().get('agent_12_question_planning'), 'deterministic_tool_executor_node': globals().get('deterministic_tool_executor_node'), 'evidence_normalizer_node': globals().get('evidence_normalizer_node'), 'agent_13_answer_synthesis': globals().get('agent_13_answer_synthesis'), 'agent_14_answer_validation': globals().get('agent_14_answer_validation'), 'controlled_answer_revision_node': globals().get('controlled_answer_revision_node')}

def route_after_validation(state: Dict[str, Any]) -> str:
    if not isinstance(state, dict):
        raise TypeError('state must be a dictionary.')
    requires_revision = bool(state.get('requires_revision', False))
    if requires_revision:
        return 'revision'
    return 'end'

def route_after_revision(state: Dict[str, Any]) -> str:
    if not isinstance(state, dict):
        raise TypeError('state must be a dictionary.')
    next_node = str(state.get('next_node', '')).strip()
    if next_node == 'answer_validation':
        return 'validation'
    if next_node == 'end':
        return 'end'
    if bool(state.get('revision_limit_reached', False)):
        return 'end'
    raise ValueError(f"Unrecognized routing after revision: {next_node or 'missing value'}")

def build_question_graph(*, retrieval_function: Optional[Callable[[Dict[str, Any]], Dict[str, Any]]]=None, analysis_function: Optional[Callable[[Dict[str, Any]], Dict[str, Any]]]=None, planning_function: Optional[Callable[[Dict[str, Any]], Dict[str, Any]]]=None, execution_function: Optional[Callable[[Dict[str, Any]], Dict[str, Any]]]=None, normalization_function: Optional[Callable[[Dict[str, Any]], Dict[str, Any]]]=None, synthesis_function: Optional[Callable[[Dict[str, Any]], Dict[str, Any]]]=None, validation_function: Optional[Callable[[Dict[str, Any]], Dict[str, Any]]]=None, revision_function: Optional[Callable[[Dict[str, Any]], Dict[str, Any]]]=None):
    resolved_components = {'retrieval': retrieval_function or QUESTION_GRAPH_REQUIRED_COMPONENTS['retrieval_node'], 'analysis': analysis_function or QUESTION_GRAPH_REQUIRED_COMPONENTS['agent_11_question_analysis'], 'planning': planning_function or QUESTION_GRAPH_REQUIRED_COMPONENTS['agent_12_question_planning'], 'execution': execution_function or QUESTION_GRAPH_REQUIRED_COMPONENTS['deterministic_tool_executor_node'], 'normalization': normalization_function or QUESTION_GRAPH_REQUIRED_COMPONENTS['evidence_normalizer_node'], 'synthesis': synthesis_function or QUESTION_GRAPH_REQUIRED_COMPONENTS['agent_13_answer_synthesis'], 'validation': validation_function or QUESTION_GRAPH_REQUIRED_COMPONENTS['agent_14_answer_validation'], 'revision': revision_function or QUESTION_GRAPH_REQUIRED_COMPONENTS['controlled_answer_revision_node']}
    missing_components = [name for name, function in resolved_components.items() if not callable(function)]
    if missing_components:
        raise RuntimeError('Unable to build question_graph. Missing or non-callable components: ' + ', '.join(missing_components))
    graph_builder = StateGraph(MarketDataState)
    graph_builder.add_node(QUESTION_GRAPH_NODE_NAMES['retrieval'], resolved_components['retrieval'])
    graph_builder.add_node(QUESTION_GRAPH_NODE_NAMES['analysis'], resolved_components['analysis'])
    graph_builder.add_node(QUESTION_GRAPH_NODE_NAMES['planning'], resolved_components['planning'])
    graph_builder.add_node(QUESTION_GRAPH_NODE_NAMES['execution'], resolved_components['execution'])
    graph_builder.add_node(QUESTION_GRAPH_NODE_NAMES['normalization'], resolved_components['normalization'])
    graph_builder.add_node(QUESTION_GRAPH_NODE_NAMES['synthesis'], resolved_components['synthesis'])
    graph_builder.add_node(QUESTION_GRAPH_NODE_NAMES['validation'], resolved_components['validation'])
    graph_builder.add_node(QUESTION_GRAPH_NODE_NAMES['revision'], resolved_components['revision'])
    graph_builder.add_edge(START, QUESTION_GRAPH_NODE_NAMES['retrieval'])
    graph_builder.add_edge(QUESTION_GRAPH_NODE_NAMES['retrieval'], QUESTION_GRAPH_NODE_NAMES['analysis'])
    graph_builder.add_edge(QUESTION_GRAPH_NODE_NAMES['analysis'], QUESTION_GRAPH_NODE_NAMES['planning'])
    graph_builder.add_edge(QUESTION_GRAPH_NODE_NAMES['planning'], QUESTION_GRAPH_NODE_NAMES['execution'])
    graph_builder.add_edge(QUESTION_GRAPH_NODE_NAMES['execution'], QUESTION_GRAPH_NODE_NAMES['normalization'])
    graph_builder.add_edge(QUESTION_GRAPH_NODE_NAMES['normalization'], QUESTION_GRAPH_NODE_NAMES['synthesis'])
    graph_builder.add_edge(QUESTION_GRAPH_NODE_NAMES['synthesis'], QUESTION_GRAPH_NODE_NAMES['validation'])
    graph_builder.add_conditional_edges(QUESTION_GRAPH_NODE_NAMES['validation'], route_after_validation, {'revision': QUESTION_GRAPH_NODE_NAMES['revision'], 'end': END})
    graph_builder.add_conditional_edges(QUESTION_GRAPH_NODE_NAMES['revision'], route_after_revision, {'validation': QUESTION_GRAPH_NODE_NAMES['validation'], 'end': END})
    return graph_builder.compile()
question_graph = build_question_graph()
final_state['question_graph_ready'] = True
final_state['question_graph_node_names'] = list(QUESTION_GRAPH_NODE_NAMES.values())

def _box_48_append_trace(state: Dict[str, Any], node_name: str) -> Dict[str, Any]:
    agent_results = copy.deepcopy(state.get('agent_results', {}))
    if not isinstance(agent_results, dict):
        agent_results = {}
    trace = list(agent_results.get('box_48_trace', []))
    trace.append(node_name)
    agent_results['box_48_trace'] = trace
    return {'agent_results': agent_results}

def _box_48_stub_retrieval(state: Dict[str, Any]) -> Dict[str, Any]:
    return _box_48_append_trace(state, 'retrieval')

def _box_48_stub_analysis(state: Dict[str, Any]) -> Dict[str, Any]:
    result = _box_48_append_trace(state, 'question_analysis')
    result['question_analysis'] = {'status': 'ready'}
    return result

def _box_48_stub_planning(state: Dict[str, Any]) -> Dict[str, Any]:
    result = _box_48_append_trace(state, 'question_planning')
    result['execution_plan'] = [{'step_id': 'STEP_1', 'action_type': 'reuse_output'}]
    return result

def _box_48_stub_execution(state: Dict[str, Any]) -> Dict[str, Any]:
    result = _box_48_append_trace(state, 'tool_execution')
    result['tool_results'] = {'STEP_1': {'test_output': {'value': 1}}}
    return result

def _box_48_stub_normalization(state: Dict[str, Any]) -> Dict[str, Any]:
    result = _box_48_append_trace(state, 'evidence_normalization')
    result['selected_evidence'] = [{'evidence_id': 'STEP_1::test_output', 'value': {'value': 1}}]
    result['missing_information'] = []
    return result

def _box_48_stub_synthesis(state: Dict[str, Any]) -> Dict[str, Any]:
    result = _box_48_append_trace(state, 'answer_synthesis')
    result['draft_answer'] = 'Synthesized answer.'
    return result

def _box_48_stub_validation_valid(state: Dict[str, Any]) -> Dict[str, Any]:
    result = _box_48_append_trace(state, 'answer_validation')
    result['validation_result'] = {'status': 'PASSED'}
    result['question_answer_alignment'] = {'status': 'ALIGNED', 'score': 1.0}
    result['requires_revision'] = False
    result['next_node'] = 'end'
    return result

def _box_48_stub_validation_revision(state: Dict[str, Any]) -> Dict[str, Any]:
    result = _box_48_append_trace(state, 'answer_validation')
    revision_count = int(state.get('revision_count', 0))
    if revision_count == 0:
        result['validation_result'] = {'status': 'FAILED'}
        result['question_answer_alignment'] = {'status': 'PARTIAL', 'score': 0.5}
        result['requires_revision'] = True
        result['next_node'] = 'answer_revision'
    else:
        result['validation_result'] = {'status': 'PASSED'}
        result['question_answer_alignment'] = {'status': 'ALIGNED', 'score': 1.0}
        result['requires_revision'] = False
        result['next_node'] = 'end'
    return result

def _box_48_stub_revision(state: Dict[str, Any]) -> Dict[str, Any]:
    result = _box_48_append_trace(state, 'answer_revision')
    updated_revision_count = int(state.get('revision_count', 0)) + 1
    result['revision_count'] = updated_revision_count
    result['draft_answer'] = 'Revised answer.'
    result['requires_revision'] = False
    result['revision_limit_reached'] = False
    result['next_node'] = 'answer_validation'
    return result
QUESTION_INTERFACE_NAME = 'ask_agentic_system'
QUESTION_RUNTIME_DEFAULTS = {'user_question': '', 'question_id': '', 'question_analysis': {}, 'question_intent': '', 'extracted_entities': {}, 'detected_ambiguities': [], 'interpretation_confidence': 0.0, 'sub_questions': [], 'required_components': [], 'matched_components': [], 'components_to_execute': [], 'component_evidence': [], 'task_dependencies': [], 'execution_plan': [], 'execution_plan_version': 0, 'planning_summary': {}, 'selected_agents': [], 'selected_tools': [], 'agent_assignments': [], 'tool_parameters': {}, 'tool_execution_status': {}, 'tool_results': {}, 'agent_results': {}, 'selected_evidence': [], 'missing_information': [], 'normalized_tool_results': {}, 'draft_answer': '', 'answer_versions': [], 'final_answer': '', 'answer_sources': [], 'validation_result': {}, 'question_answer_alignment': {}, 'unsupported_claims': [], 'missing_answer_components': [], 'numerical_inconsistencies': [], 'requires_revision': False, 'revision_count': 0, 'revision_actions': [], 'revision_status': '', 'revision_limit_reached': False, 'current_question_node': '', 'question_workflow_status': 'initialized', 'next_node': '', 'stop_workflow': False, 'agentic_errors': []}

def prepare_question_state(base_state: Dict[str, Any], question: str) -> Dict[str, Any]:
    if not isinstance(base_state, dict):
        raise TypeError('base_state must be a dictionary.')
    clean_question = str(question).strip()
    if not clean_question:
        raise ValueError('The question cannot be empty.')
    question_state = copy.deepcopy(base_state)
    preserved_conversation_history = copy.deepcopy(question_state.get('current_conversation_history', []))
    preserved_conversation_id = str(question_state.get('conversation_id', '')).strip()
    for field_name, default_value in QUESTION_RUNTIME_DEFAULTS.items():
        question_state[field_name] = copy.deepcopy(default_value)
    question_state['user_question'] = clean_question
    question_state['question_id'] = str(uuid.uuid4())
    question_state['conversation_id'] = preserved_conversation_id or str(uuid.uuid4())
    question_state['current_conversation_history'] = preserved_conversation_history
    question_state['conversation_turn'] = len(preserved_conversation_history) + 1
    question_state['primary_llm_name'] = globals().get('MODEL_NAME', question_state.get('primary_llm_name', ''))
    question_state['critic_llm_name'] = globals().get('CRITIC_MODEL', question_state.get('critic_llm_name', ''))
    question_state['maximum_revisions'] = int(question_state.get('maximum_revisions', 2) or 2)
    return question_state

def finalize_question_answer(question_state: Dict[str, Any]) -> Dict[str, Any]:
    finalized_state = copy.deepcopy(question_state)
    final_answer = str(finalized_state.get('final_answer', '')).strip()
    draft_answer = str(finalized_state.get('draft_answer', '')).strip()
    validation_status = str(finalized_state.get('validation_result', {}).get('status', '')).upper()
    requires_revision = bool(finalized_state.get('requires_revision', False))
    revision_limit_reached = bool(finalized_state.get('revision_limit_reached', False))
    if not final_answer and draft_answer and (validation_status == 'PASSED') and (not requires_revision):
        final_answer = draft_answer
        finalized_state['final_answer'] = final_answer
    if final_answer:
        if revision_limit_reached:
            finalized_state['question_workflow_status'] = 'completed_with_revision_limit'
        else:
            finalized_state['question_workflow_status'] = 'completed'
    return finalized_state

def preserve_reuse_store(previous_state, next_state):
    """Keep certified reusable calculations when a graph returns only a partial update."""
    if not isinstance(next_state, dict):
        return next_state
    for name in ('tool_results_by_key', 'tool_output_history'):
        old = previous_state.get(name) or {}
        new = next_state.get(name) or {}
        if isinstance(old, dict) and isinstance(new, dict):
            next_state[name] = {**copy.deepcopy(old), **new}
    return next_state

def register_question_turn(question_state: Dict[str, Any]) -> Dict[str, Any]:
    updated_state = copy.deepcopy(question_state)
    if 'create_conversation_turn' not in globals() or 'append_conversation_turn' not in globals():
        return updated_state
    answer_for_history = str(updated_state.get('final_answer', '') or updated_state.get('draft_answer', '')).strip()
    selected_tickers = updated_state.get('extracted_entities', {}).get('tickers', [])
    turn = create_conversation_turn(state=updated_state, question=updated_state.get('user_question', ''), answer=answer_for_history, execution_plan=updated_state.get('execution_plan', []), selected_tools=updated_state.get('selected_tools', []), selected_tickers=selected_tickers)
    append_conversation_turn(state=updated_state, turn=turn)
    updated_state['conversation_turn'] = len(updated_state.get('current_conversation_history', []))
    return updated_state

def ask_agentic_system(question: str, *, graph=None, base_state: Optional[Dict[str, Any]]=None, update_global_state: bool=True, register_history: bool=True) -> Dict[str, Any]:
    start_time = time.perf_counter()
    resolved_graph = graph if graph is not None else globals().get('question_graph')
    if resolved_graph is None:
        raise RuntimeError('question_graph is not available. Run BOX 48 first.')
    if not hasattr(resolved_graph, 'invoke'):
        raise TypeError('The graph must expose the invoke() method.')
    resolved_base_state = base_state if base_state is not None else globals().get('final_state')
    if not isinstance(resolved_base_state, dict):
        raise TypeError('final_state is not available or is invalid.')
    question_state = prepare_question_state(base_state=resolved_base_state, question=question)
    question_state['question_workflow_status'] = 'running'
    try:
        graph_result = resolved_graph.invoke(question_state)
        if not isinstance(graph_result, dict):
            raise TypeError('question_graph must return a state as a dictionary.')
        question_final_state = finalize_question_answer(graph_result)
        if register_history:
            question_final_state = register_question_turn(question_final_state)
        final_answer = str(question_final_state.get('final_answer', '')).strip()
        if not final_answer:
            if bool(question_final_state.get('revision_limit_reached', False)):
                final_answer = str(question_final_state.get('draft_answer', '')).strip()
                question_final_state['final_answer'] = final_answer
            else:
                raise RuntimeError('The workflow terminated without producing a usable final_answer.')
        total_execution_time = round(time.perf_counter() - start_time, 6)
        question_final_state['total_execution_time_seconds'] = total_execution_time
        question_final_state['question_interface_status'] = 'completed'
        if update_global_state:
            global final_state
            persistent_history = copy.deepcopy(question_final_state.get('current_conversation_history', []))
            persistent_conversation_id = question_final_state.get('conversation_id', '')
            final_state.update(question_final_state)
            final_state['current_conversation_history'] = persistent_history
            final_state['conversation_id'] = persistent_conversation_id
        return {'question_final_state': question_final_state, 'final_answer': final_answer}
    except Exception as error:
        failed_state = copy.deepcopy(question_state)
        failed_state['question_workflow_status'] = 'failed'
        failed_state['question_interface_status'] = 'failed'
        failed_state['agentic_errors'] = list(failed_state.get('agentic_errors', [])) + [{'node': QUESTION_INTERFACE_NAME, 'error': str(error), 'timestamp': datetime.now().isoformat(timespec='seconds')}]
        raise
ask_question = ask_agentic_system
final_state['question_graph_ready'] = 'question_graph' in globals() and question_graph is not None
_reuse_integrity_original_ask_agentic_system = ask_agentic_system

def ask_agentic_system(question, *, graph=None, base_state=None, update_global_state=True, register_history=True):
    previous = base_state if base_state is not None else globals().get('final_state', {})
    result = _reuse_integrity_original_ask_agentic_system(question, graph=graph, base_state=base_state, update_global_state=update_global_state, register_history=register_history)
    if isinstance(previous, dict) and isinstance(result, dict):
        preserve_reuse_store(previous, result)
        if update_global_state and isinstance(globals().get('final_state'), dict):
            preserve_reuse_store(previous, globals()['final_state'])
    return result

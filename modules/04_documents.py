# ========= ORIGINAL NOTEBOOK CELL 47 =========
# ============================================================
# BOX 36 — FUNDAMENTAL AGENTIC TOOL 1:
# INTEGRATION AND QUERYING OF FY2025 PRESS RELEASES
# ============================================================
# The tool integrates an unstructured documentary source into the agentic architecture
# that complements data acquired via APIs and the
# market time series already available in final_state.
#
# The objective is to transform corporate Press Releases into a
# structured, validated, and queryable information base capable of relating
# financial results, operating drivers,
# guidance, strategies, milestones, and management commentary to the
# quantitative evidence available in the project.
#
# The tool's semantic richness is built through a declarative catalog
# that associates the queryable information with:
# - canonical metrics and KPI families;
# - synonyms and equivalent formulations in English;
# - terms actually used in corporate documents;
# - information macro-areas and sector terminology;
# - preferred document sections.
#
# The search therefore does not depend on the literal presence of a single
# word or solely on the title/section of the release. The request is
# mapped to the relevant information metric and the evidence is
# located through a progressive strategy:
#
#     exact match -> synonyms -> document terms ->
#     semantic similarity -> retrieval by information macro-area
#
# Macro-area retrieval ("fallback") makes it possible to identify information
# that is semantically relevant even when the requested metric is not
# expressed with the same KPI or terminology, taking into account
# differences across sectors and the different ways in which
# companies present results, drivers, guidance, and indicators.
#
# The semantic fallback uses TF-IDF and cosine similarity when there
# is no direct lexical match. The system also preserves
# the distinction between the requested metric and the metric actually found,
# making it explicit whether the evidence is exact, equivalent, or
# only related within the same information area.
#
# If no relevant evidence is identified, the tool explicitly returns
# "Information not available", avoiding the transformation of
# a weak semantic relationship into an apparently certain answer.
#
# ALIGNMENT WITH THE QUESTION WORKFLOW ARCHITECTURE
# ------------------------------------------------------------
# As with the other tools in the system, each requested item of information
# is identified through the dimensions required to define
# the analysis to be performed precisely:
#
#     TOOL + UNIVERSE + TIME PERIOD + METRIC
#
# where:
# - TOOL identifies the analysis or calculation method to use,
#   for example CAPM, Momentum, or corporate press-release analysis;
# - UNIVERSE identifies the securities to which the analysis is applied, for example
#   a single ticker, a group of companies, or the entire universe considered;
# - TIME PERIOD defines the interval to which the analysis refers;
# - METRIC identifies the specific result or information
#   requested, for example return, Beta, winning ticker, or Top 5.
#
# This structure allows the agentic workflow to interpret the
# user's question, precisely identify what is requested
# and retrieve or produce the relevant evidence.
#
# For the document component, identification of the requested information
# is integrated with the semantic catalog, which makes it possible to
# recognize synonyms, equivalent formulations, corporate terminology
# and sector terminology, as well as information attributable to the same macro-area.
#
# Retrieval nevertheless keeps the actually requested information distinct
# from semantically related information, preserving
# the correspondence between the user's question and the evidence used.
#
# BOX 36:
# - acquires and validates the FY2025 Press Releases of the available companies;
# - preserves the original texts in final_state;
# - builds and maintains the unified document catalog/index;
# - preserves KPI families, synonyms, document_terms, keywords, and macro-areas;
# - interprets different formulations of the same information;
# - performs retrieval of the individual calculated component;
# - records evidence, section, period, match type, and URL;
# - stores archive, query, and results in final_state.
#
# The decomposition of a question composed of multiple components remains
# the responsibility of the subsequent workflow: this box receives and resolves
# one component at a time, retaining the full semantic depth
# required to retrieve documentary evidence.
#
# The final mini-tool makes it possible to directly verify the search
# method with questions, for example, about earnings, revenue, result
# drivers, guidance, strategy, and other content contained in the releases.
# ============================================================


try:
    import ipywidgets as widgets
    from IPython.display import display, clear_output
    IPYWIDGETS_AVAILABLE = True
except ImportError:
    IPYWIDGETS_AVAILABLE = False

REQUEST_TIMEOUT_SECONDS = 30
REQUEST_PAUSE_SECONDS = 0.10
MAX_RETRIES = 3
MAX_ANSWER_EVIDENCE = 8

SOURCE_BULLET_KEYWORDS = ['eps',
 'adjusted eps',
 'operating income margin',
 'adjusted net sales',
 'total sales',
 'adjusted sales',
 'dividends',
 'cash',
 'adjusted free cash flow',
 'net sales',
 'operating income',
 'net income',
 'operating cash flow',
 'free cash flow',
 'revenues',
 'consolidated provisions for credit losses',
 'net write-off rate',
 'tax rate',
 'total revenues',
 'product sales',
 'earnings per share',
 'revenue',
 'overall gross margin',
 'r&d spending',
 'share repurchase',
 'gross margin',
 'operating margin',
 'net income margin',
 'net orders',
 'debt',
 'sales',
 'operating profit margin',
 'adjusted operating profit margin',
 'profit per share',
 'adjusted profit per share',
 'cash for repurchases',
 'cash to shareholders',
 'share repurchases',
 'net revenues',
 'cash flow',
 'segment operating income',
 'diluted earnings per common share',
 'return on average common shareholders’ equity',
 'net earnings',
 'net earnings per share',
 'adjusted diluted earnings per share',
 'reported sales',
 'adjusted segment margin expansion',
 'gross profit margin',
 'net cash from operating activities',
 'adjusted operational',
 'roe',
 'rotce',
 'reported revenue',
 'expense',
 'credit costs',
 'average loans',
 'global comparable sales',
 'consolidated revenues',
 'systemwide sales',
 'consolidated operating income',
 'diluted earnings per share',
 'worldwide sales',
 'gaap eps',
 'direct revenues',
 'wholesale revenues',
 'selling and administrative expense',
 'operating overhead expense',
 'gaap earnings per diluted share',
 'organic sales',
 'core net earnings per share',
 'consolidated net sales',
 'adjusted diluted net income per share',
 'generating net operating cash',
 'capital returned to shareholders',
 'growth',
 'core income',
 'underlying underwriting gain',
 'net realized investment losses',
 'combined ratio',
 'underlying combined ratio',
 'net investment income',
 'net favorable',
 'net written premiums',
 'adjusted earnings per share',
 'earnings from operations',
 'net margin',
 'cash flows from operations',
 'total operating revenue',
 'cash flow from operating activities',
 'consolidated net income',
 'capital expenditures',
 'payment volume',
 'service revenue',
 'operating expenses',
 'non-operating income',
 'roa',
 'global inventory']

SEMANTIC_KPI_FAMILIES = {
 'REVENUE_SALES': {
     'label': 'Revenue and sales',
     'macro_area': 'REVENUE_AND_SALES_VOLUME',
     'sector': 'cross-sector',
     'query': ['revenue', 'revenues', 'sales', 'turnover', 'top line'],
     'document_terms': ['adjusted net sales',
                        'total sales',
                        'adjusted sales',
                        'net sales',
                        'revenues',
                        'total revenues',
                        'product sales',
                        'revenue',
                        'sales',
                        'reported sales',
                        'reported revenue',
                        'global comparable sales',
                        'consolidated revenues',
                        'systemwide sales',
                        'worldwide sales',
                        'direct revenues',
                        'wholesale revenues',
                        'organic sales',
                        'consolidated net sales',
                        'net revenues',
                        'total operating revenue',
                        'service revenue']
 },
 'NET_INCOME': {
     'label': 'Net income',
     'macro_area': 'CORPORATE_PROFITABILITY',
     'sector': 'cross-sector',
     'query': ['net income', 'net earnings', 'net profit', 'bottom line'],
     'document_terms': ['net income', 'net earnings', 'consolidated net income', 'core income']
 },
 'OPERATING_INCOME': {
     'label': 'Operating income',
     'macro_area': 'CORPORATE_PROFITABILITY',
     'sector': 'cross-sector',
     'query': ['operating income', 'operating profit', 'operating earnings', 'ebit'],
     'document_terms': ['operating income',
                        'segment operating income',
                        'consolidated operating income',
                        'earnings from operations',
                        'non-operating income']
 },
 'EARNINGS_PER_SHARE': {
     'label': 'Earnings per share',
     'macro_area': 'PER_SHARE_AND_SHAREHOLDER_METRICS',
     'sector': 'cross-sector',
     'query': ['eps',
               'earnings per share',
               'profit per share',
               'diluted earnings per share'],
     'document_terms': ['eps',
                        'adjusted eps',
                        'earnings per share',
                        'profit per share',
                        'adjusted profit per share',
                        'diluted earnings per common share',
                        'net earnings per share',
                        'adjusted diluted earnings per share',
                        'diluted earnings per share',
                        'gaap eps',
                        'gaap earnings per diluted share',
                        'core net earnings per share',
                        'adjusted diluted net income per share',
                        'adjusted earnings per share']
 },
 'GROSS_MARGIN': {
     'label': 'Gross margin',
     'macro_area': 'MARGINS',
     'sector': 'cross-sector',
     'query': ['gross margin', 'gross profit margin'],
     'document_terms': ['overall gross margin', 'gross margin', 'gross profit margin']
 },
 'OPERATING_MARGIN': {
     'label': 'Operating margin',
     'macro_area': 'MARGINS',
     'sector': 'cross-sector',
     'query': ['operating margin', 'operating profit margin', 'operating income margin'],
     'document_terms': ['operating income margin',
                        'operating margin',
                        'operating profit margin',
                        'adjusted operating profit margin',
                        'adjusted segment margin expansion']
 },
 'NET_MARGIN': {
     'label': 'Net margin',
     'macro_area': 'MARGINS',
     'sector': 'cross-sector',
     'query': ['net margin', 'net income margin'],
     'document_terms': ['net income margin', 'net margin']
 },
 'CASH_POSITION': {
     'label': 'Cash and liquidity',
     'macro_area': 'LIQUIDITY_AND_CASH_FLOWS',
     'sector': 'cross-sector',
     'query': ['cash', 'cash position', 'liquidity'],
     'document_terms': ['cash']
 },
 'OPERATING_CASH_FLOW': {
     'label': 'Operating cash flow',
     'macro_area': 'LIQUIDITY_AND_CASH_FLOWS',
     'sector': 'cross-sector',
     'query': ['operating cash flow',
               'cash flow from operations',
               'cash flow from operating activities'],
     'document_terms': ['operating cash flow',
                        'net cash from operating activities',
                        'generating net operating cash',
                        'cash flows from operations',
                        'cash flow from operating activities']
 },
 'FREE_CASH_FLOW': {
     'label': 'Free cash flow',
     'macro_area': 'LIQUIDITY_AND_CASH_FLOWS',
     'sector': 'cross-sector',
     'query': ['free cash flow', 'adjusted free cash flow', 'fcf'],
     'document_terms': ['adjusted free cash flow', 'free cash flow']
 },
 'CASH_FLOW_GENERIC': {
     'label': 'Cash flow',
     'macro_area': 'LIQUIDITY_AND_CASH_FLOWS',
     'sector': 'cross-sector',
     'query': ['cash flow'],
     'document_terms': ['cash flow']
 },
 'DIVIDENDS': {
     'label': 'Dividends',
     'macro_area': 'PER_SHARE_AND_SHAREHOLDER_METRICS',
     'sector': 'cross-sector',
     'query': ['dividend', 'dividends'],
     'document_terms': ['dividends']
 },
 'SHARE_REPURCHASES': {
     'label': 'Share repurchases',
     'macro_area': 'PER_SHARE_AND_SHAREHOLDER_METRICS',
     'sector': 'cross-sector',
     'query': ['share repurchase', 'share repurchases', 'stock buyback'],
     'document_terms': ['share repurchase', 'share repurchases', 'cash for repurchases']
 },
 'CAPITAL_RETURN': {
     'label': 'Capital returned to shareholders',
     'macro_area': 'PER_SHARE_AND_SHAREHOLDER_METRICS',
     'sector': 'cross-sector',
     'query': ['capital returned to shareholders',
               'cash to shareholders',
               'shareholder distributions'],
     'document_terms': ['cash to shareholders', 'capital returned to shareholders']
 },
 'DEBT': {
     'label': 'Debt and leverage',
     'macro_area': 'CAPITAL_STRUCTURE',
     'sector': 'cross-sector',
     'query': ['debt', 'borrowings', 'leverage'],
     'document_terms': ['debt']
 },
 'EXPENSES': {
     'label': 'Expenses and operating costs',
     'macro_area': 'COSTS_AND_INVESTMENTS',
     'sector': 'cross-sector',
     'query': ['expense', 'expenses', 'operating expenses', 'overhead'],
     'document_terms': ['expense',
                        'selling and administrative expense',
                        'operating overhead expense',
                        'operating expenses']
 },
 'CAPITAL_EXPENDITURES': {
     'label': 'Capital expenditures',
     'macro_area': 'COSTS_AND_INVESTMENTS',
     'sector': 'cross-sector',
     'query': ['capital expenditures', 'capital expenditure', 'capex'],
     'document_terms': ['capital expenditures']
 },
 'R_AND_D_SPENDING': {
     'label': 'Research and development spending',
     'macro_area': 'COSTS_AND_INVESTMENTS',
     'sector': 'technology-pharma-industrial',
     'query': ['r&d spending', 'research and development spending'],
     'document_terms': ['r&d spending']
 },
 'GROWTH': {
     'label': 'Growth',
     'macro_area': 'GROWTH_AND_DEVELOPMENT',
     'sector': 'cross-sector',
     'query': ['growth', 'increase', 'expansion'],
     'document_terms': ['growth']
 },
 'TAX_RATE': {
     'label': 'Tax rate',
     'macro_area': 'TAXATION',
     'sector': 'cross-sector',
     'query': ['tax rate', 'effective tax rate'],
     'document_terms': ['tax rate']
 },
 'ROE': {
     'label': 'Return on equity',
     'macro_area': 'RETURNS_ON_CAPITAL',
     'sector': 'banking-financial',
     'query': ['roe', 'return on equity', 'return on average common shareholders equity'],
     'document_terms': ['return on average common shareholders’ equity', 'roe']
 },
 'ROTCE': {
     'label': 'Return on tangible common equity',
     'macro_area': 'RETURNS_ON_CAPITAL',
     'sector': 'banking-financial',
     'query': ['rotce', 'return on tangible common equity'],
     'document_terms': ['rotce']
 },
 'ROA': {
     'label': 'Return on assets',
     'macro_area': 'RETURNS_ON_CAPITAL',
     'sector': 'banking-financial',
     'query': ['roa', 'return on assets'],
     'document_terms': ['roa']
 },
 'CREDIT_LOSS_PROVISIONS': {
     'label': 'Credit-loss provisions and credit costs',
     'macro_area': 'CREDIT_RISK',
     'sector': 'banking-financial',
     'query': ['credit losses', 'provisions for credit losses', 'credit costs'],
     'document_terms': ['consolidated provisions for credit losses', 'credit costs']
 },
 'NET_WRITE_OFF_RATE': {
     'label': 'Net write-off rate',
     'macro_area': 'CREDIT_RISK',
     'sector': 'banking-financial',
     'query': ['net write-off rate', 'net charge-off rate', 'write-off rate'],
     'document_terms': ['net write-off rate']
 },
 'AVERAGE_LOANS': {
     'label': 'Average loans',
     'macro_area': 'BANKING_VOLUMES',
     'sector': 'banking-financial',
     'query': ['average loans', 'average lending'],
     'document_terms': ['average loans']
 },
 'NET_ORDERS': {
     'label': 'Net orders',
     'macro_area': 'SECTOR_OPERATING_VOLUMES',
     'sector': 'industrial-aerospace-logistics',
     'query': ['orders', 'net orders', 'new orders'],
     'document_terms': ['net orders']
 },
 'GLOBAL_INVENTORY': {
     'label': 'Global inventory',
     'macro_area': 'SECTOR_OPERATING_VOLUMES',
     'sector': 'retail-consumer',
     'query': ['inventory', 'inventories', 'global inventory'],
     'document_terms': ['global inventory']
 },
 'PAYMENT_VOLUME': {
     'label': 'Payment volume',
     'macro_area': 'SECTOR_OPERATING_VOLUMES',
     'sector': 'payments-fintech',
     'query': ['payment volume', 'payments volume'],
     'document_terms': ['payment volume']
 },
 'NET_WRITTEN_PREMIUMS': {
     'label': 'Net written premiums',
     'macro_area': 'INSURANCE_KPIS',
     'sector': 'insurance',
     'query': ['insurance premiums', 'written premiums', 'net written premiums'],
     'document_terms': ['net written premiums']
 },
 'COMBINED_RATIO': {
     'label': 'Combined ratio',
     'macro_area': 'INSURANCE_KPIS',
     'sector': 'insurance',
     'query': ['combined ratio', 'underlying combined ratio'],
     'document_terms': ['combined ratio', 'underlying combined ratio']
 },
 'UNDERWRITING_RESULT': {
     'label': 'Underwriting result',
     'macro_area': 'INSURANCE_KPIS',
     'sector': 'insurance',
     'query': ['underwriting gain', 'underwriting result'],
     'document_terms': ['underlying underwriting gain', 'net favorable']
 },
 'NET_INVESTMENT_INCOME': {
     'label': 'Net investment income',
     'macro_area': 'INSURANCE_AND_INVESTMENT_KPIS',
     'sector': 'insurance-financial',
     'query': ['investment income', 'net investment income'],
     'document_terms': ['net investment income']
 },
 'REALIZED_INVESTMENT_LOSSES': {
     'label': 'Realized investment losses',
     'macro_area': 'INSURANCE_AND_INVESTMENT_KPIS',
     'sector': 'insurance-financial',
     'query': ['realized investment losses', 'net realized investment losses'],
     'document_terms': ['net realized investment losses']
 },
 'ADJUSTED_OPERATIONAL': {
     'label': 'Adjusted operational performance',
     'macro_area': 'ADJUSTED_OPERATING_KPIS',
     'sector': 'pharma-healthcare',
     'query': ['adjusted operational', 'adjusted operational performance'],
     'document_terms': ['adjusted operational']
 }
}

MACRO_AREA_RELATED_KPIS = {
 'REVENUE_AND_SALES_VOLUME': ['REVENUE_SALES'],
 'CORPORATE_PROFITABILITY': ['NET_INCOME', 'OPERATING_INCOME'],
 'MARGINS': ['GROSS_MARGIN', 'OPERATING_MARGIN', 'NET_MARGIN'],
 'LIQUIDITY_AND_CASH_FLOWS': ['CASH_POSITION',
                              'OPERATING_CASH_FLOW',
                              'FREE_CASH_FLOW',
                              'CASH_FLOW_GENERIC'],
 'PER_SHARE_AND_SHAREHOLDER_METRICS': ['EARNINGS_PER_SHARE',
                                       'DIVIDENDS',
                                       'SHARE_REPURCHASES',
                                       'CAPITAL_RETURN'],
 'CAPITAL_STRUCTURE': ['DEBT'],
 'COSTS_AND_INVESTMENTS': ['EXPENSES', 'CAPITAL_EXPENDITURES', 'R_AND_D_SPENDING'],
 'GROWTH_AND_DEVELOPMENT': ['GROWTH'],
 'TAXATION': ['TAX_RATE'],
 'RETURNS_ON_CAPITAL': ['ROE', 'ROTCE', 'ROA'],
 'CREDIT_RISK': ['CREDIT_LOSS_PROVISIONS', 'NET_WRITE_OFF_RATE'],
 'BANKING_VOLUMES': ['AVERAGE_LOANS'],
 'SECTOR_OPERATING_VOLUMES': ['NET_ORDERS', 'GLOBAL_INVENTORY', 'PAYMENT_VOLUME'],
 'INSURANCE_KPIS': ['NET_WRITTEN_PREMIUMS', 'COMBINED_RATIO', 'UNDERWRITING_RESULT'],
 'INSURANCE_AND_INVESTMENT_KPIS': ['NET_INVESTMENT_INCOME', 'REALIZED_INVESTMENT_LOSSES'],
 'ADJUSTED_OPERATING_KPIS': ['ADJUSTED_OPERATIONAL']
}

BULLET_KEYWORDS = list(dict.fromkeys(
    term
    for family in SEMANTIC_KPI_FAMILIES.values()
    for term in family['document_terms']
))



TITLE1 = ["full-year", "full year", "fiscal", "results", "fy"]
TITLE2 = ["highlights", "company updates", "key points", "business highlights"]
TITLE3 = ["guidance", "outlook", "milestones", "dividend", "expectations"]

CEO_KEYS = ["chairman", "ceo", "chief executive officer"]
CFO_KEYS = ["cfo", "chief financial officer"]

PRESS_RELEASE_URLS = {
    "MMM": "https://raw.githubusercontent.com/Valeria-Raele/agentic-financial-intelligence/refs/heads/main/data/financial_documents/3M%20fy%202025%20PR.txt",
    "AMZN": "https://raw.githubusercontent.com/Valeria-Raele/agentic-financial-intelligence/refs/heads/main/data/financial_documents/AMZN%20fy%202025%20PR.txt",
    "AXP": "https://raw.githubusercontent.com/Valeria-Raele/agentic-financial-intelligence/refs/heads/main/data/financial_documents/American%20Express%20fy%202025%20PR.txt",
    "AMGN": "https://raw.githubusercontent.com/Valeria-Raele/agentic-financial-intelligence/refs/heads/main/data/financial_documents/Amgen%20fy%202025%20PR.txt",
    "AAPL": "https://raw.githubusercontent.com/Valeria-Raele/agentic-financial-intelligence/refs/heads/main/data/financial_documents/Apple%20fy%202025%20PR.txt",
    "BA": "https://raw.githubusercontent.com/Valeria-Raele/agentic-financial-intelligence/refs/heads/main/data/financial_documents/Boeing%20fy%202025%20PR.txt",
    "CAT": "https://raw.githubusercontent.com/Valeria-Raele/agentic-financial-intelligence/refs/heads/main/data/financial_documents/Caterpillar%20fy%202025%20PR.txt",
    "CVX": "https://raw.githubusercontent.com/Valeria-Raele/agentic-financial-intelligence/refs/heads/main/data/financial_documents/Chevron%20fy%202025%20PR.txt",
    "CSCO": "https://raw.githubusercontent.com/Valeria-Raele/agentic-financial-intelligence/refs/heads/main/data/financial_documents/Cisco%20fy%202025%20PR.txt",
    "KO": "https://raw.githubusercontent.com/Valeria-Raele/agentic-financial-intelligence/refs/heads/main/data/financial_documents/Coca%20Cola%20fy%202025%20PR.txt",
    "DIS": "https://raw.githubusercontent.com/Valeria-Raele/agentic-financial-intelligence/refs/heads/main/data/financial_documents/Disney%20fy%202025%20PR.txt",
    "GS": "https://raw.githubusercontent.com/Valeria-Raele/agentic-financial-intelligence/refs/heads/main/data/financial_documents/GS%20fy%202025%20PR.txt",
    "HD": "https://raw.githubusercontent.com/Valeria-Raele/agentic-financial-intelligence/refs/heads/main/data/financial_documents/Home%20Depot%20fy%202025%20PR.txt",
    "HON": "https://raw.githubusercontent.com/Valeria-Raele/agentic-financial-intelligence/refs/heads/main/data/financial_documents/Honeywell%20fy%202025%20PR.txt",
    "IBM": "https://raw.githubusercontent.com/Valeria-Raele/agentic-financial-intelligence/refs/heads/main/data/financial_documents/IBM%20fy%202025%20PR.txt",
    "JNJ": "https://raw.githubusercontent.com/Valeria-Raele/agentic-financial-intelligence/refs/heads/main/data/financial_documents/J%26J%20fy%202025%20PR.txt",
    "JPM": "https://raw.githubusercontent.com/Valeria-Raele/agentic-financial-intelligence/refs/heads/main/data/financial_documents/JPM%20fy%202025%20PR.txt",
    "MCD": "https://raw.githubusercontent.com/Valeria-Raele/agentic-financial-intelligence/refs/heads/main/data/financial_documents/MCD%20fy%202025%20PR.txt",
    "MRK": "https://raw.githubusercontent.com/Valeria-Raele/agentic-financial-intelligence/refs/heads/main/data/financial_documents/Merck%20fy%202025%20PR.txt",
    "MSFT": "https://raw.githubusercontent.com/Valeria-Raele/agentic-financial-intelligence/refs/heads/main/data/financial_documents/Microsoft%20fy%202025%20PR.txt",
    "NKE": "https://raw.githubusercontent.com/Valeria-Raele/agentic-financial-intelligence/refs/heads/main/data/financial_documents/Nike%20fy%202025%20PR.txt",
    "NVDA": "https://raw.githubusercontent.com/Valeria-Raele/agentic-financial-intelligence/refs/heads/main/data/financial_documents/Nvidia%20fy%202025%20PR.txt",
    "PG": "https://raw.githubusercontent.com/Valeria-Raele/agentic-financial-intelligence/refs/heads/main/data/financial_documents/PG%20fy%202025%20PR.txt",
    "CRM": "https://raw.githubusercontent.com/Valeria-Raele/agentic-financial-intelligence/refs/heads/main/data/financial_documents/Salesforce%20fy%202025%20PR.txt",
    "SHW": "https://raw.githubusercontent.com/Valeria-Raele/agentic-financial-intelligence/refs/heads/main/data/financial_documents/SW%20fy%202025%20PR.txt",
    "TRV": "https://raw.githubusercontent.com/Valeria-Raele/agentic-financial-intelligence/refs/heads/main/data/financial_documents/Travelers%20fy%202025%20PR.txt",
    "UNH": "https://raw.githubusercontent.com/Valeria-Raele/agentic-financial-intelligence/refs/heads/main/data/financial_documents/UHG%20fy%202025%20PR.txt",
    "VZ": "https://raw.githubusercontent.com/Valeria-Raele/agentic-financial-intelligence/refs/heads/main/data/financial_documents/Verizon%20fy%202025%20PR.txt",
    "V": "https://raw.githubusercontent.com/Valeria-Raele/agentic-financial-intelligence/refs/heads/main/data/financial_documents/Visa%20fy%202025%20PR.txt",
    "WMT": "https://raw.githubusercontent.com/Valeria-Raele/agentic-financial-intelligence/refs/heads/main/data/financial_documents/Walmart%20fy%202025%20PR.txt"
}

COMPANY_NAMES = {
    "MMM": "3M", "AMZN": "Amazon", "AXP": "American Express",
    "AMGN": "Amgen", "AAPL": "Apple", "BA": "Boeing",
    "CAT": "Caterpillar", "CVX": "Chevron", "CSCO": "Cisco",
    "KO": "Coca-Cola", "DIS": "Disney", "GS": "Goldman Sachs",
    "HD": "Home Depot", "HON": "Honeywell", "IBM": "IBM",
    "JNJ": "Johnson & Johnson", "JPM": "JPMorgan Chase",
    "MCD": "McDonald's", "MRK": "Merck", "MSFT": "Microsoft",
    "NKE": "Nike", "NVDA": "NVIDIA", "PG": "Procter & Gamble",
    "CRM": "Salesforce", "SHW": "Sherwin-Williams",
    "TRV": "Travelers", "UNH": "UnitedHealth Group",
    "VZ": "Verizon", "V": "Visa", "WMT": "Walmart"
}

# ============================================================
# SYNONYMS FOR QUESTION INTERPRETATION
# ============================================================

FY2025_KEYS = [
    "2025", "fy2025", "fy 2025", "latest fiscal year",
    "latest financial year", "latest fiscal period", "fiscal year"
]
FY2026_KEYS = [
    "2026", "fy2026", "fy 2026", "next year", "following year",
    "next financial year", "future", "outlook"
]
REASON_KEYS = [
    "why", "reason", "reasons", "cause", "causes", "drivers",
    "what drove", "what caused", "highlights", "insights"
]
STRATEGY_KEYS = [
    "strategy", "guidance", "outlook", "expectations", "forecasts",
    "milestone", "milestones", "objectives", "prospects"
]
CEO_QUERY_KEYS = ["ceo", "chief executive", "chief executive officer", "chairman"]
CFO_QUERY_KEYS = ["cfo", "finance director", "chief financial officer"]

# ============================================================
# GUIDE TO THE MACHINE CATALOG AND SEMANTIC SEARCH
# ============================================================
#
# PURPOSE
# ------------------------------------------------------------
# This block constitutes the machine index of the information content
# available in the press releases.
#
# Its purpose is NOT to isolate the individual calculation contained in the user's question:
# this responsibility belongs to BOX 41.
#
# BOX 41 constructs the requested components according to the identity:
#
#     TICKER + TIME_PERIOD + METRIC
#
# BOX 36 receives a single calculation component and uses
# this catalog to determine:
#
#     - what the requested metric means;
#     - which equivalent formulations it may take;
#     - which synonyms to recognize;
#     - which terms may actually appear in the documents;
#     - which KPI family it belongs to;
#     - which macro-area it belongs to;
#     - which release sections should be searched first;
#     - which sections to use for semantic retrieval of search terms
#       not found, when sectors or companies use KPIs
#       that differ for information attributable to the same area
#       (e.g., Sales → Revenue);
#     - how to extend the search semantically when
#       the exact term is not present.
#
# ============================================================
# TWO COMPLEMENTARY SEARCH LEVELS
# ============================================================
#
# The catalog makes it possible to search for information both at a
# GENERAL level and at the highest available level of GRANULARITY.
#
# 1. GENERAL DOCUMENT INFORMATION
#
#    Document keys make it possible to retrieve information
#    that may span multiple KPIs and that in press releases
#    are normally expressed in narrative form.
#
# 2. SPECIFIC KPIs
#
#    The families contained in SEMANTIC_KPI_FAMILIES instead enable
#    granular search for individual information items.
#
#    Each KPI preserves its own semantic richness:
#
#       label
#       macro_area
#       sector
#       query
#       document_terms
#
#    In this way, different terminology used by
#    different companies, sectors, and releases can be
#    mapped to the same canonical information.
#
#
# ============================================================
# RETRIEVAL STRATEGY
# ============================================================
#
# The search proceeds from the most precise level to the more
# semantic level, avoiding confusion between a simple conceptual
# relationship and an actual metric identity.
#
# The logical sequence is:
#
#     1. EXPLICIT_METRIC
#     2. EXACT_ALIAS
#     3. EXACT_KPI_OR_SYNONYM
#     4. DOCUMENT_TERM
#     5. SEMANTIC_SIMILARITY
#     6. MACRO_AREA_FALLBACK
#     7. SECTION_FALLBACK
#
# This simultaneously enables:
#
#     - maximum precision when the information is explicit;
#     - recognition of synonyms;
#     - recognition of different sector terminology;
#     - semantic retrieval when the formulation changes;
#     - retrieval of related information when the requested metric
#       is not directly available.
#
#
# ============================================================
# DISTINCTION BETWEEN MATCHES AND RELATED INFORMATION
# ============================================================
#
# Semantic search must NOT automatically transform
# a similarity into equivalence.
#
# For this reason, the result preserves:
#
#     requested_metric
#     matched_metric
#
# and explicitly classifies the retrieval:
#
# +----------------------------+-----------------------------------------------+
# | RETRIEVAL_STATUS           | MEANING                                       |
# +----------------------------+-----------------------------------------------+
# | EXACT_MATCH                | Metric found directly.                        |
# | SYNONYM_MATCH              | Found through an equivalent synonym/alias.    |
# | SEMANTIC_EQUIVALENT        | Different formulation but the same information|
# | RELATED_IN_SAME_MACRO_AREA | Related information in the same area.         |
# | SECTION_FALLBACK           | Found outside the primary section.            |
# | NOT_FOUND                  | Sufficient evidence not available.            |
# +----------------------------+-----------------------------------------------+
#
# Particularly:
#
#     requested_metric != matched_metric
#
# must not be hidden.
#
# If only related information is found, it
# must be returned as such and NOT presented as if it
# matched the originally requested metric.
#
#
# ============================================================
# RELATIONSHIP WITH SUBSEQUENT BOXES
# ============================================================
#
# BOX 36:
#
#     - builds and preserves the document archive;
#     - catalogs all queryable information;
#     - preserves synonyms and sector terminology;
#     - identifies where to search for each information item;
#     - performs semantic retrieval of the individual component;
#     - returns evidence and match quality/type.
#
# BOX 36 does NOT:
#
#     - independently decompose a compound question;
#     - decide which calculation components are needed for the answer;
#     - replace the question-decomposition logic of BOX 41.
#
# BOX 41 remains solely responsible for constructing the
# components:
#
#     TICKER + TIME_PERIOD + METRIC
#
# Subsequent BOXES can therefore treat a documentary component
# in the same conceptual way as components
# coming from quantitative tools.
#
#
# ============================================================
# GENERAL CATALOG PRINCIPLE
# ============================================================
#
# +-------------------------------+--------------------------------------------+
# | CATALOG QUESTION              | KEYS USED                                  |
# +-------------------------------+--------------------------------------------+
# | WHAT EXISTS                   | information types + KPI families           |
# | HOW IT MAY BE CALLED          | aliases + synonyms + queries + terms |
# | WHERE TO SEARCH               | preferred_sections + fallback_sections     |
# | HOW IT WAS FOUND              | retrieval_status + match_type              |
# | WHAT WAS FOUND                | requested_metric + matched_metric          |
# | WHAT THE EVIDENCE IS          | evidence + source_url                      |
# +-------------------------------+--------------------------------------------+
#
# In this way, the system simultaneously preserves
# granularity, semantic coverage, match transparency, and
# compatibility with the project's architecture for decomposing and managing
# calculation components.
#
# ============================================================
# EXPLICIT MAP OF QUERYABLE DIMENSIONS
# ============================================================
#
# The identity of the individual calculation used by the architecture is
# composed by three main dimensions:
#
# +------------------+-----------------------------------------------+
# | DIMENSION        | FUNCTION                                      |
# +------------------+-----------------------------------------------+
# | TICKER           | Identifies company / instrument.              |
# | TIME_PERIOD      | Identifies the information period.            |
# | METRIC           | Identifies the requested information.         |
# +------------------+-----------------------------------------------+
#
# ============================================================
# DIMENSION 1 — TICKER / INSTRUMENT
# ============================================================
#
# Document universe available in BOX 36:
#
# +------+------------------------+------+--------------------------+
# | TICK | COMPANY                | TICK | COMPANY                  |
# +------+------------------------+------+--------------------------+
# | MMM  | 3M                     | AMZN | Amazon                   |
# | AXP  | American Express       | AMGN | Amgen                    |
# | AAPL | Apple                  | BA   | Boeing                   |
# | CAT  | Caterpillar            | CVX  | Chevron                  |
# | CSCO | Cisco                  | KO   | Coca-Cola                |
# | DIS  | Disney                 | GS   | Goldman Sachs            |
# | HD   | Home Depot             | HON  | Honeywell                |
# | IBM  | IBM                    | JNJ  | Johnson & Johnson        |
# | JPM  | JPMorgan Chase         | MCD  | McDonald's               |
# | MRK  | Merck                  | MSFT | Microsoft                |
# | NKE  | Nike                   | NVDA | NVIDIA                   |
# | PG   | Procter & Gamble       | CRM  | Salesforce               |
# | SHW  | Sherwin-Williams       | TRV  | Travelers                |
# | UNH  | UnitedHealth Group     | VZ   | Verizon                  |
# | V    | Visa                   | WMT  | Walmart                  |
# +------+------------------------+------+--------------------------+
#
#
# ============================================================
# DIMENSION 2 — TIME_PERIOD
# ============================================================
#
# The canonical period is also recognized through
# different linguistic formulations.
#
# +-----------------+------------------------------------------------------+
# | PERIOD          | RECOGNIZED KEYS / FORMULATIONS                       |
# +-----------------+------------------------------------------------------+
# | FY2025          | 2025; fy2025; fy 2025; latest fiscal year;           |
# |                 | latest financial year;                               |
# |                 | fiscal year                                          |
# +-----------------+------------------------------------------------------+
# | FY2026 / FUTURE | 2026; fy2026; fy 2026; next year;                    |
# |                 | following year; next fiscal year; future;            |
# |                 | outlook                                              |
# +-----------------+------------------------------------------------------+
#
#
# ============================================================
# DIMENSION 3 — METRIC / INFORMATION
# ============================================================
#
# METRIC can take two complementary levels:
#
# +----------------------+-----------------------------------------------+
# | LEVEL                | PURPOSE                                       |
# +----------------------+-----------------------------------------------+
# | DOCUMENT_INFORMATION | General/narrative document information        |
# | KPI                  | Granular financial information                |
# +----------------------+-----------------------------------------------+
#
#
# ============================================================
# A — DOCUMENT_INFORMATION
# ============================================================
#
# +----------------------+-----------------------------------------------+
# | METRIC               | INFORMATION SOUGHT                            |
# +----------------------+-----------------------------------------------+
# | FY_RESULTS           | Financial results / FY results                |
# | RESULT_DRIVERS       | Drivers, causes, and determinants of results  |
# | BUSINESS_HIGHLIGHTS  | Highlights and operating updates              |
# | GUIDANCE_OUTLOOK     | Guidance, outlook, and future expectations    |
# | STRATEGY_MILESTONES  | Strategy, objectives, and milestones          |
# | CEO_COMMENTARY       | Quote CEO / Chairman                          |
# | CFO_COMMENTARY       | Quote CFO                                     |
# | DIVIDEND_POLICY      | Dividends and remuneration policy             |
# | GENERAL_FUNDAMENTAL  | General fundamental information               |
# +----------------------+-----------------------------------------------+
#
# Each DOCUMENT_INFORMATION entry in the catalog contains:
#
# +----------------------+-----------------------------------------------+
# | PROPERTY             | FUNCTION                                      |
# +----------------------+-----------------------------------------------+
# | label                | Canonical label                       |
# | aliases              | English synonyms and formulations             |
# | document_cues        | Expressions searchable in the document text   |
# | preferred_sections   | Primary search sections                       |
# | fallback_sections    | Alternative sections                          |
# | temporal_scope       | Temporal compatibility                        |
# +----------------------+-----------------------------------------------+
#
#
# ============================================================
# B — SPECIFIC KPIs
# ============================================================
#
# The 35 available KPI families are:
#
# +-----------------------------+-----------------------------------------+
# | KPI                         | MACRO-AREA                              |
# +-----------------------------+-----------------------------------------+
# | REVENUE_SALES               | REVENUE_AND_BUSINESS_VOLUME             |
# | NET_INCOME                  | CORPORATE_PROFITABILITY                 |
# | OPERATING_INCOME            | CORPORATE_PROFITABILITY                 |
# | EARNINGS_PER_SHARE          | PER_SHARE_AND_SHAREHOLDER_METRICS       |
# | GROSS_MARGIN                | MARGINS                                 |
# | OPERATING_MARGIN            | MARGINS                                 |
# | NET_MARGIN                  | MARGINS                                 |
# | CASH_POSITION               | LIQUIDITY_AND_CASH_FLOWS                |
# | OPERATING_CASH_FLOW         | LIQUIDITY_AND_CASH_FLOWS                |
# | FREE_CASH_FLOW              | LIQUIDITY_AND_CASH_FLOWS                |
# | CASH_FLOW_GENERIC           | LIQUIDITY_AND_CASH_FLOWS                |
# | DIVIDENDS                   | PER_SHARE_AND_SHAREHOLDER_METRICS       |
# | SHARE_REPURCHASES           | PER_SHARE_AND_SHAREHOLDER_METRICS       |
# | CAPITAL_RETURN              | PER_SHARE_AND_SHAREHOLDER_METRICS       |
# | DEBT                        | FINANCIAL_STRUCTURE                     |
# | EXPENSES                    | COSTS_AND_INVESTMENTS                   |
# | CAPITAL_EXPENDITURES        | COSTS_AND_INVESTMENTS                   |
# | R_AND_D_SPENDING            | COSTS_AND_INVESTMENTS                   |
# | GROWTH                      | GROWTH_AND_DEVELOPMENT                  |
# | TAX_RATE                    | TAXATION                                |
# | ROE                         | RETURNS_ON_CAPITAL                      |
# | ROTCE                       | RETURNS_ON_CAPITAL                      |
# | ROA                         | RETURNS_ON_CAPITAL                      |
# | CREDIT_LOSS_PROVISIONS      | CREDIT_RISK                             |
# | NET_WRITE_OFF_RATE          | CREDIT_RISK                             |
# | AVERAGE_LOANS               | BANKING_VOLUMES                         |
# | NET_ORDERS                  | SECTOR_OPERATING_VOLUMES                |
# | GLOBAL_INVENTORY            | SECTOR_OPERATING_VOLUMES                |
# | PAYMENT_VOLUME              | SECTOR_OPERATING_VOLUMES                |
# | NET_WRITTEN_PREMIUMS        | INSURANCE_KPIS                          |
# | COMBINED_RATIO              | INSURANCE_KPIS                          |
# | UNDERWRITING_RESULT         | INSURANCE_KPIS                          |
# | NET_INVESTMENT_INCOME       | INSURANCE_AND_INVESTMENT_KPIS           |
# | REALIZED_INVESTMENT_LOSSES  | INSURANCE_AND_INVESTMENT_KPIS           |
# | ADJUSTED_OPERATIONAL        | ADJUSTED_OPERATING_KPIS                 |
# +-----------------------------+-----------------------------------------+
#
# Each KPI also retains the following properties in SEMANTIC_KPI_FAMILIES:
#
# +------------------+--------------------------------------------------+
# | PROPERTY         | FUNCTION                                         |
# +------------------+--------------------------------------------------+
# | label            | Canonical name                                   |
# | macro_area       | Higher-level semantic family                     |
# | sector           | Sector(s) in which the KPI is typically used     |
# | query            | English formulations and synonyms                |
# | document_terms   | Terminology actually used in the documents       |
# +------------------+--------------------------------------------------+
#
#
# ============================================================
# SEMANTIC MACRO-AREAS
# ============================================================
#
# Macro-areas make it possible to broaden the search without
# incorrectly claiming that a related metric is identical to
# the requested one, while ensuring information consistency
# across financial documents that use different KPIs but
# belong to the same information area.
#
# +---------------------------------------+--------------------------------+
# | MACRO-AREA                            | INCLUDED KPIs                  |
# +---------------------------------------+--------------------------------+
# | REVENUE_AND_BUSINESS_VOLUME           | REVENUE_SALES                  |
# | CORPORATE_PROFITABILITY               | NET_INCOME, OPERATING_INCOME   |
# | MARGINS                               | GROSS_MARGIN, OPERATING_MARGIN,|
# |                                       | NET_MARGIN                     |
# | LIQUIDITY_AND_CASH_FLOWS              | CASH_POSITION,                 |
# |                                       | OPERATING_CASH_FLOW,           |
# |                                       | FREE_CASH_FLOW,                |
# |                                       | CASH_FLOW_GENERIC              |
# | PER_SHARE_AND_SHAREHOLDER_METRICS     | EARNINGS_PER_SHARE, DIVIDENDS, |
# |                                       | SHARE_REPURCHASES,             |
# |                                       | CAPITAL_RETURN                 |
# | FINANCIAL_STRUCTURE                   | DEBT                           |
# | COSTS_AND_INVESTMENTS                 | EXPENSES, CAPITAL_EXPENDITURES,|
# |                                       | R_AND_D_SPENDING               |
# | GROWTH_AND_DEVELOPMENT                | GROWTH                         |
# | TAXATION                              | TAX_RATE                       |
# | RETURNS_ON_CAPITAL                    | ROE, ROTCE, ROA                |
# | CREDIT_RISK                           | CREDIT_LOSS_PROVISIONS,        |
# |                                       | NET_WRITE_OFF_RATE             |
# | BANKING_VOLUMES                       | AVERAGE_LOANS                  |
# | SECTOR_OPERATING_VOLUMES              | NET_ORDERS, GLOBAL_INVENTORY,  |
# |                                       | PAYMENT_VOLUME                 |
# | INSURANCE_KPIS                        | NET_WRITTEN_PREMIUMS,          |
# |                                       | COMBINED_RATIO,                |
# |                                       | UNDERWRITING_RESULT            |
# | INSURANCE_AND_INVESTMENT_KPIS         | NET_INVESTMENT_INCOME,         |
# |                                       | REALIZED_INVESTMENT_LOSSES     |
# | ADJUSTED_OPERATING_KPIS               | ADJUSTED_OPERATIONAL           |
# +---------------------------------------+--------------------------------+
#
#
# ============================================================
# DOCUMENT POSITIONS / LOCATION
# ============================================================
#
# LOCATION does NOT constitute a fourth calculation dimension.
# It is used exclusively to guide internal retrieval.
#
# +---------+------------------------------------------------------------+
# | SECTION | PRIMARY CONTENT                                            |
# +---------+------------------------------------------------------------+
# | TITLE1  | Full-year / fiscal / results / FY                          |
# | TITLE2  | Highlights / company updates / business highlights         |
# | TITLE3  | Guidance / outlook / milestones / dividend / expectations  |
# | CEO     | CEO / Chairman / Chief Executive Officer statements        |
# | CFO     | CFO / Chief Financial Officer statements                   |
# | OTHER   | Content not classified in the previous sections            |
# +---------+------------------------------------------------------------+
#
#
# ============================================================
# COMPLETE STRUCTURE OF THE MACHINE INDEX
# ============================================================
#
# The entire catalog can therefore be understood conceptually as:
#
# +----------------------+-----------------------------------------------+
# | LEVEL                | CONTENT                                       |
# +----------------------+-----------------------------------------------+
# | TICKER               | Company / instrument                          |
# | TIME_PERIOD          | Canonical time period                         |
# | METRIC               | Requested information                         |
# | METRIC_CLASS         | DOCUMENT_INFORMATION or KPI                   |
# | ALIASES              | Synonyms and equivalent formulations          |
# | QUERY                | English semantic formulations                 |
# | DOCUMENT_TERMS       | Actual terminology used in the releases       |
# | MACRO_AREA           | Higher-level semantic family                  |
# | SECTOR               | Sector context                                |
# | PREFERRED_SECTIONS   | Primary retrieval positions                   |
# | FALLBACK_SECTIONS    | Alternative positions                         |
# | RETRIEVAL_STATUS     | Match quality/type                            |
# | REQUESTED_METRIC     | Originally requested information              |
# | MATCHED_METRIC       | Information actually retrieved                |
# | EVIDENCE             | Documentary evidence                          |
# | SOURCE_URL           | Original source                               |
# +----------------------+-----------------------------------------------+
#
#
# ============================================================
# FINAL CONTRACT WITH THE CALCULATION ARCHITECTURE
# ============================================================
#
# +-------------------------+--------------------------------------------+
# | RESPONSIBILITY          | BOX                                        |
# +-------------------------+--------------------------------------------+
# | Catalog what exists     | BOX 36                                     |
# | Know where to search    | BOX 36                                     |
# | Handle synonyms         | BOX 36                                     |
# | Handle semantics        | BOX 36                                     |
# | Handle macro-areas      | BOX 36                                     |
# | Certify the match       | BOX 36                                     |
# | Calculation construction| BOX 41                                     |
# | Build T+T+M             | BOX 41                                     |
# | Decide REUSE/EXECUTE    | Subsequent orchestration BOXES             |
# +-------------------------+--------------------------------------------+
#
# ============================================================

# ============================================================
# UNIFIED CATALOG OF DOCUMENT INFORMATION
# ============================================================
# This catalog is the declarative guide used by the tool to translate
# a linguistic formulation into a queryable metric.
# Each entry declares aliases, preferred/fallback sections, document
# cues, typical period, and logical metric class.
#
# Specific KPIs are NOT recopied or reduced: they are incorporated
# dynamically from SEMANTIC_KPI_FAMILIES, fully preserving
# label, sector, macro-area, query, and document_terms.

PRESS_RELEASE_SECTION_CATALOG: Dict[str, Dict[str, Any]] = {
    "TITLE1": {
        "label": "FY2025 Results",
        "role": "results_and_financial_performance",
        "title_markers": TITLE1.copy(),
        "default_time_period": "FY2025"
    },
    "TITLE2": {
        "label": "FY2025 Drivers, Highlights and Updates",
        "role": "drivers_and_business_highlights",
        "title_markers": TITLE2.copy(),
        "default_time_period": "FY2025"
    },
    "TITLE3": {
        "label": "Strategy, Outlook and Guidance",
        "role": "forward_looking_strategy_and_guidance",
        "title_markers": TITLE3.copy(),
        "default_time_period": "FY2026 / guidance"
    },
    "CEO": {
        "label": "CEO Commentary",
        "role": "management_commentary",
        "title_markers": CEO_KEYS.copy(),
        "default_time_period": "FY2025"
    },
    "CFO": {
        "label": "CFO Commentary",
        "role": "management_commentary",
        "title_markers": CFO_KEYS.copy(),
        "default_time_period": "FY2025"
    },
    "OTHER": {
        "label": "Other Press Release Content",
        "role": "unclassified_document_content",
        "title_markers": [],
        "default_time_period": "FY2025"
    }
}

PRESS_RELEASE_INFORMATION_CATALOG: Dict[str, Dict[str, Any]] = {
    "FY_RESULTS": {
        "label": "Full-year financial results",
        "metric_class": "DOCUMENT_INFORMATION",
        "aliases_en": [
            "results", "financial results", "financial performance",
            "full year results", "full-year results", "fiscal year results",
            "annual results", "reported results", "full year financial performance",
            "full-year financial performance", "earnings results", "full year earnings",
            "full-year earnings", "fiscal year results", "performance full year"
        ],
        "preferred_sections": ["TITLE1"],
        "fallback_sections": ["TITLE2"],
        "document_cues": [
            "results", "full-year", "full year", "fiscal", "revenue",
            "sales", "net income", "earnings", "eps", "operating income",
            "cash flow", "free cash flow", "margin"
        ],
        "temporal_scope": ["FY2025"]
    },
    "RESULT_DRIVERS": {
        "label": "Drivers of results",
        "metric_class": "DOCUMENT_INFORMATION",
        "aliases_en": [
            "drivers", "results drivers", "drivers of results", "what drove",
            "what caused", "driven by", "factors affecting results",
            "factors impacting results", "reasons", "causes", "due to",
            "reflecting", "discussion of results", "results discussion",
            "segment commentary"
        ],
        "preferred_sections": ["TITLE2"],
        "fallback_sections": ["TITLE1", "TITLE3"],
        "document_cues": [
            "driven by", "primarily due to", "due to", "reflecting",
            "benefited from", "offset by", "higher", "lower", "increase",
            "decrease", "volume", "price", "mix", "cost", "productivity",
            "charges", "impairment", "demand", "deliveries", "growth"
        ],
        "temporal_scope": ["FY2025"]
    },
    "BUSINESS_HIGHLIGHTS": {
        "label": "Business highlights",
        "metric_class": "DOCUMENT_INFORMATION",
        "aliases_en": [
            "highlights", "business highlights", "company updates",
            "company highlights", "key points", "key developments",
            "major developments", "segment results", "segment commentary",
            "business updates", "discussion of results"
        ],
        "preferred_sections": ["TITLE2"],
        "fallback_sections": ["TITLE1", "TITLE3"],
        "document_cues": TITLE2.copy(),
        "temporal_scope": ["FY2025"]
    },
    "GUIDANCE_OUTLOOK": {
        "label": "Guidance and outlook",
        "metric_class": "DOCUMENT_INFORMATION",
        "aliases_en": [
            "guidance", "outlook", "expectations", "forecast", "forecasts",
            "forward outlook", "future expectations", "financial outlook",
            "full year guidance", "full-year guidance", "fiscal year guidance",
            "full year expectations", "full-year expectations"
        ],
        "preferred_sections": ["TITLE3"],
        "fallback_sections": ["TITLE2"],
        "document_cues": [
            "guidance", "outlook", "expectations", "expects", "expected",
            "forecast", "target", "targets", "2026"
        ],
        "temporal_scope": ["FY2026 / guidance"]
    },
    "STRATEGY_MILESTONES": {
        "label": "Strategy, targets and milestones",
        "metric_class": "DOCUMENT_INFORMATION",
        "aliases_en": [
            "strategy", "strategies", "strategic priorities",
            "strategic initiatives", "targets", "objectives",
            "milestone", "milestones", "strategic plan",
            "business projects", "business projects and milestones"
        ],
        "preferred_sections": ["TITLE3"],
        "fallback_sections": ["TITLE2"],
        "document_cues": [
            "strategy", "strategic", "milestone", "milestones", "target",
            "priority", "priorities", "initiative", "initiatives",
            "project", "projects"
        ],
        "temporal_scope": ["FY2025", "FY2026 / guidance"]
    },
    "DIVIDEND_POLICY": {
        "label": "Dividends and distribution policy",
        "metric_class": "DOCUMENT_INFORMATION",
        "aliases_en": [
            "dividend", "dividends", "dividend policy",
            "shareholder distribution", "shareholder distributions",
            "dividend increase", "planned dividend increase",
            "capital returned to shareholders", "cash to shareholders"
        ],
        "preferred_sections": ["TITLE3", "TITLE1"],
        "fallback_sections": ["TITLE2"],
        "document_cues": [
            "dividend", "dividends", "declared", "shareholders",
            "dividend increase", "capital returned", "cash to shareholders"
        ],
        "temporal_scope": ["FY2025", "FY2026 / guidance"]
    },
    "CEO_COMMENTARY": {
        "label": "CEO commentary",
        "metric_class": "MANAGEMENT_COMMENTARY",
        "aliases_en": CEO_QUERY_KEYS + [
            "ceo commentary", "ceo remarks", "ceo statement",
            "chief executive commentary", "chief executive remarks",
            "chief executive statement", "chairman and ceo",
            "chair and ceo", "president and ceo",
            "chairman and chief executive officer",
            "president and chief executive officer",
            "according to the ceo"
        ],
        "preferred_sections": ["CEO"],
        "fallback_sections": ["TITLE1", "TITLE2", "TITLE3"],
        "document_cues": CEO_KEYS.copy(),
        "temporal_scope": ["FY2025", "FY2026 / guidance"]
    },
    "CFO_COMMENTARY": {
        "label": "CFO commentary",
        "metric_class": "MANAGEMENT_COMMENTARY",
        "aliases_en": CFO_QUERY_KEYS + [
            "cfo commentary", "cfo remarks", "cfo statement",
            "chief financial officer commentary",
            "chief financial officer remarks",
            "chief financial officer statement",
            "according to the cfo"
        ],
        "preferred_sections": ["CFO"],
        "fallback_sections": ["TITLE1", "TITLE2", "TITLE3"],
        "document_cues": CFO_KEYS.copy(),
        "temporal_scope": ["FY2025", "FY2026 / guidance"]
    },
}


def build_press_release_search_catalog() -> Dict[str, Dict[str, Any]]:
    """Builds the complete registry of all queryable keys."""
    catalog: Dict[str, Dict[str, Any]] = {}

    for metric_name, spec in PRESS_RELEASE_INFORMATION_CATALOG.items():
        catalog[metric_name] = {
            "metric": metric_name,
            **spec,
            "macro_area": None,
            "sector": "cross-sector",
            "query_terms": list(dict.fromkeys(
                spec.get("aliases_en", [])
                + spec.get("document_cues", [])
            ))
        }

    for metric_name, family in SEMANTIC_KPI_FAMILIES.items():
        catalog[metric_name] = {
            "metric": metric_name,
            "label": family.get("label", metric_name),
            "metric_class": "KPI",
            "macro_area": family.get("macro_area"),
            "sector": family.get("sector"),
            "aliases": family.get("query", []).copy(),
            "document_cues": family.get("document_terms", []).copy(),
            "query_terms": list(dict.fromkeys(
                family.get("query", [])
                + family.get("document_terms", [])
            )),
            "preferred_sections": ["TITLE1", "TITLE2"],
            "fallback_sections": ["TITLE3"],
            "temporal_scope": ["FY2025"]
        }

    return catalog

PRESS_RELEASE_SEARCH_CATALOG = build_press_release_search_catalog()


def build_press_release_catalog_index() -> Dict[str, Any]:
    """
    Complete machine-readable structure of the Press Release tool.

    BOX 36 does NOT build the plan of the question's calculation components: this
    responsibility belongs to BOX 41. BOX 36 instead exposes all the
    information that can be requested and can retrieve ONE component
    at a time according to the project's common identity:

        ticker + time_period + metric

    Sections, synonyms, macro-areas, document cues, semantic similarity, and
    fallback are internal retrieval coordinates; they do not become new
    dimensions of the calculation component identity.
    """
    return {
        "architecture_contract": {
            "component_construction_owner": "BOX_40",
            "tool_role": "RETRIEVE_ONE_ATOMIC_COMPONENT",
            "component_identity_dimensions": ["ticker", "time_period", "metric"],
            "local_multi_component_decomposition": False,
            "sections_are_identity_dimensions": False,
            "semantic_metadata_are_identity_dimensions": False
        },
        "identity_dimensions": ["ticker", "time_period", "metric"],
        "atomic_input_contract": {
            "ticker": "a single company/ticker per component",
            "time_period": "a single logical period per component",
            "metric": "a single metric/information type per component",
            "component_id": "identifier assigned by the workflow; optional for standalone use",
            "question": "text of the individual sub-question; semantic context, not a source of multiple decomposition"
        },
        "sections": PRESS_RELEASE_SECTION_CATALOG.copy(),
        "information_types": PRESS_RELEASE_INFORMATION_CATALOG.copy(),
        "kpi_families": SEMANTIC_KPI_FAMILIES.copy(),
        "macro_areas": MACRO_AREA_RELATED_KPIS.copy(),
        "search_catalog": PRESS_RELEASE_SEARCH_CATALOG.copy(),
        "source_document_terms": SOURCE_BULLET_KEYWORDS.copy(),
        "all_document_terms": BULLET_KEYWORDS.copy(),
        "retrieval_ladder": [
            "EXPLICIT_METRIC", "EXACT_ALIAS", "EXACT_KPI_OR_SYNONYM",
            "DOCUMENT_TERM", "SEMANTIC_SIMILARITY",
            "MACRO_AREA_FALLBACK", "SECTION_FALLBACK"
        ],
        "retrieval_metadata": [
            "metric_class", "macro_area", "preferred_sections",
            "fallback_sections", "matched_section", "match_type",
            "retrieval_status", "requested_metric", "matched_metric",
            "semantic_similarity", "evidence_text", "source_url"
        ],
        "output_identity": [
            "component_id", "ticker", "time_period", "metric"
        ],
        "output_evidence_metadata": [
            "metric_class", "matched_section", "match_type",
            "retrieval_status", "requested_metric", "matched_metric",
            "semantic_similarity", "evidence_text", "source_url", "status"
        ]
    }


# ============================================================
# COMPANY NORMALIZATION AND RESOLUTION
# ============================================================

def normalize_text(value: Any) -> str:
    text = "" if value is None else str(value)
    text = unicodedata.normalize("NFKD", text)
    text = "".join(char for char in text if not unicodedata.combining(char))
    text = text.replace("’", "'").replace("–", "-").replace("—", "-")
    text = re.sub(r"[^a-zA-Z0-9%&'./$€-]+", " ", text)
    return re.sub(r"\s+", " ", text).strip().lower()


COMPANY_ALIASES = {}
for ticker, company_name in COMPANY_NAMES.items():
    aliases = {
        ticker, company_name, company_name.replace("&", "and"),
        company_name.replace("-", " "), company_name.replace("'", "")
    }
    manual_aliases = {
        "MMM": ["3m company"], "AMZN": ["amazon.com", "amazon"],
        "AXP": ["amex"], "KO": ["coca cola", "the coca-cola company"],
        "DIS": ["the walt disney company", "walt disney"],
        "GS": ["goldman sachs group"], "HD": ["the home depot"],
        "JNJ": ["j&j", "johnson and johnson"],
        "JPM": ["jpmorgan", "jp morgan", "jp morgan chase"],
        "MCD": ["mcdonalds"], "PG": ["p&g", "procter and gamble"],
        "SHW": ["sherwin williams"],
        "UNH": ["unitedhealth", "united health group"]
    }
    aliases.update(manual_aliases.get(ticker, []))
    for alias in aliases:
        COMPANY_ALIASES[normalize_text(alias)] = ticker


def resolve_ticker(company: str) -> str:
    normalized_company = normalize_text(company)
    if not normalized_company:
        raise ValueError("The company cannot be empty.")
    ticker = COMPANY_ALIASES.get(normalized_company)
    if ticker is None:
        raise ValueError(f"Company '{company}' not recognized.")
    return ticker


# ============================================================
# VALIDATED DOWNLOAD
# ============================================================

def download_press_release(
    ticker: str,
    session: Optional[requests.Session] = None,
    timeout_seconds: int = REQUEST_TIMEOUT_SECONDS,
    max_retries: int = MAX_RETRIES
) -> Dict[str, Any]:
    if ticker not in PRESS_RELEASE_URLS:
        raise KeyError(f"No URL configured for ticker {ticker}.")

    request_session = session or requests.Session()
    url = PRESS_RELEASE_URLS[ticker]
    last_error = None

    for attempt in range(1, max_retries + 1):
        try:
            response = request_session.get(
                url,
                timeout=timeout_seconds,
                headers={"User-Agent": "Agentic-Financial-Markets/1.0"}
            )
            response.raise_for_status()
            text = response.text.replace("\r\n", "\n").replace("\r", "\n").strip()
            if len(text) < 200:
                raise ValueError("The press release is empty or too short.")
            return {
                "ticker": ticker, "company": COMPANY_NAMES[ticker], "url": url,
                "status_code": response.status_code, "characters": len(text),
                "text": text, "download_error": None
            }
        except Exception as error:
            last_error = error
            if attempt < max_retries:
                time.sleep(0.75 * attempt)

    return {
        "ticker": ticker, "company": COMPANY_NAMES[ticker], "url": url,
        "status_code": None, "characters": 0, "text": "",
        "download_error": str(last_error)
    }


# ============================================================
# AGENTIC DOCUMENT PARSING
# ============================================================

def split_blocks(text: str) -> List[str]:
    return [
        block.strip()
        for block in re.split(r"\n\s*\n", text.replace("\r", "\n"))
        if block.strip()
    ]


def classify_title(block: str) -> Optional[str]:
    first_line = normalize_text(block.split("\n", 1)[0])
    if any(normalize_text(key) in first_line for key in TITLE1):
        return "TITLE1"
    if any(normalize_text(key) in first_line for key in TITLE2):
        return "TITLE2"
    if any(normalize_text(key) in first_line for key in TITLE3):
        return "TITLE3"
    return None


def extract_bullets(block: str) -> List[str]:
    bullets = []
    for line in block.splitlines():
        cleaned = re.sub(r"\s+", " ", line).strip()
        if re.match(r"^(?:[•●▪◦*-]|\d+[.)])\s+", cleaned):
            bullets.append(cleaned)
    return bullets


def extract_quotes(text: str, role_keys: Sequence[str]) -> List[str]:
    quotes = []
    for match in re.finditer(r'["“]([^"”]{20,2500})["”]', text, flags=re.DOTALL):
        context = normalize_text(text[max(0, match.start()-350):match.end()+350])
        if any(normalize_text(key) in context for key in role_keys):
            quote = re.sub(r"\s+", " ", match.group(1)).strip()
            if quote not in quotes:
                quotes.append(quote)
    return quotes


def build_section_units(section_name: str, blocks: Sequence[str]) -> List[Dict[str, Any]]:
    units = []
    for block_index, block in enumerate(blocks, start=1):
        lines = [re.sub(r"\s+", " ", line).strip() for line in block.splitlines()]
        lines = [line for line in lines if line]
        title = lines[0] if lines else ""
        for line_index, line in enumerate(lines, start=1):
            units.append({
                "section": section_name,
                "section_title": title,
                "block_index": block_index,
                "line_index": line_index,
                "line": line,
                "normalized_line": normalize_text(line)
            })
    return units


def parse_press_release(download_record: Dict[str, Any]) -> Dict[str, Any]:
    text = download_record.get("text", "")
    if not text:
        return {
            **download_record,
            "sections": {"TITLE1": [], "TITLE2": [], "TITLE3": [], "OTHER": []},
            "section_units": [], "bullets": [], "indexed_keywords": [],
            "ceo_quotes": [], "cfo_quotes": []
        }

    sections = {"TITLE1": [], "TITLE2": [], "TITLE3": [], "OTHER": []}
    current_section = "OTHER"

    for block in split_blocks(text):
        detected_section = classify_title(block)
        if detected_section:
            current_section = detected_section
        sections[current_section].append(block)

    section_units = []
    for section_name, section_blocks in sections.items():
        section_units.extend(build_section_units(section_name, section_blocks))

    bullets = [
        {"section": section_name, "text": bullet}
        for section_name, section_blocks in sections.items()
        for block in section_blocks
        for bullet in extract_bullets(block)
    ]

    indexed_keywords = sorted({
        keyword
        for unit in section_units
        for keyword in BULLET_KEYWORDS
        if normalize_text(keyword) in unit["normalized_line"]
    })

    return {
        **download_record,
        "sections": sections,
        "section_units": section_units,
        "bullets": bullets,
        "indexed_keywords": indexed_keywords,
        "ceo_quotes": extract_quotes(text, CEO_KEYS),
        "cfo_quotes": extract_quotes(text, CFO_KEYS)
    }


# ============================================================
# ARCHIVE CREATION
# ============================================================

def build_press_release_archive(
    state: Dict[str, Any],
    force_refresh: bool = False
) -> Dict[str, Any]:
    if not isinstance(state, dict):
        raise TypeError("state must be a dictionary.")

    archive = state.get("press_release_archive")
    if (
        not force_refresh and isinstance(archive, dict)
        and set(archive) == set(PRESS_RELEASE_URLS)
        and all(archive[ticker].get("text") for ticker in archive)
    ):
        return state

    archive = {}
    validation_rows = []
    session = requests.Session()

    for position, ticker in enumerate(PRESS_RELEASE_URLS, start=1):
        parsed = parse_press_release(download_press_release(ticker, session=session))
        archive[ticker] = parsed
        validation_rows.append({
            "Ticker": ticker,
            "Company": parsed["company"],
            "Download": "OK" if not parsed["download_error"] else "ERROR",
            "Characters": parsed["characters"],
            "TITLE1_Paragraphs": len(parsed["sections"]["TITLE1"]),
            "TITLE2_Paragraphs": len(parsed["sections"]["TITLE2"]),
            "TITLE3_Paragraphs": len(parsed["sections"]["TITLE3"]),
            "Indexed_Keywords": len(parsed["indexed_keywords"]),
            "CEO": "YES" if parsed["ceo_quotes"] else "NO",
            "CFO": "YES" if parsed["cfo_quotes"] else "NO",
            "Error": parsed["download_error"]
        })
        if position < len(PRESS_RELEASE_URLS):
            time.sleep(REQUEST_PAUSE_SECONDS)

    state["press_release_archive"] = archive
    state["press_release_validation"] = pd.DataFrame(validation_rows)
    state["press_release_keywords"] = BULLET_KEYWORDS.copy()
    state["press_release_semantic_kpi_families"] = (
        SEMANTIC_KPI_FAMILIES.copy()
    )
    state["press_release_information_catalog"] = PRESS_RELEASE_INFORMATION_CATALOG.copy()
    state["press_release_section_catalog"] = PRESS_RELEASE_SECTION_CATALOG.copy()
    state["press_release_search_catalog"] = PRESS_RELEASE_SEARCH_CATALOG.copy()
    state["press_release_catalog_index"] = build_press_release_catalog_index()
    state["press_release_tool_contract"] = state["press_release_catalog_index"][
        "architecture_contract"
    ].copy()
    return state


# ============================================================
# USER QUESTION INTERPRETATION
# ============================================================

def contains_any(text: str, keys: Sequence[str]) -> bool:
    return any(normalize_text(key) in text for key in keys)


def _catalog_aliases(metric_name: str) -> List[str]:
    spec = PRESS_RELEASE_SEARCH_CATALOG.get(metric_name, {})
    return list(dict.fromkeys(
        spec.get("aliases", [])
        + spec.get("aliases_en", [])
        + [metric_name, spec.get("label", "")]
    ))


def detect_press_release_information_types(
    question: str,
    explicit_metric: Optional[str] = None
) -> List[Dict[str, Any]]:
    """Multi-label recognition of document information types."""
    matches: List[Dict[str, Any]] = []
    seen = set()
    explicit_key = str(explicit_metric or "").strip().upper()

    if explicit_key in PRESS_RELEASE_INFORMATION_CATALOG:
        spec = PRESS_RELEASE_INFORMATION_CATALOG[explicit_key]
        return [{
            "metric": explicit_key,
            **spec,
            "selection_type": "EXPLICIT_METRIC",
            "semantic_similarity": 1.0,
            "matched_query_terms": [str(explicit_metric)]
        }]

    for metric_name, spec in PRESS_RELEASE_INFORMATION_CATALOG.items():
        if metric_name == "GENERAL_FUNDAMENTAL":
            continue
        matched_terms = [
            term for term in _catalog_aliases(metric_name)
            if term and _contains_semantic_phrase(question, term)
        ]
        if matched_terms and metric_name not in seen:
            seen.add(metric_name)
            matches.append({
                "metric": metric_name,
                **spec,
                "selection_type": "EXACT_ALIAS",
                "semantic_similarity": 1.0,
                "matched_query_terms": matched_terms
            })
    return matches


def infer_press_release_information_type(
    question: str,
    minimum_similarity: float = 0.12
) -> Optional[Dict[str, Any]]:
    """TF-IDF fallback for general requests not recognized exactly."""
    normalized_question = normalize_text(question)
    if not normalized_question:
        return None

    metric_names = [
        name for name in PRESS_RELEASE_INFORMATION_CATALOG
        if name != "GENERAL_FUNDAMENTAL"
    ]
    documents = []
    for name in metric_names:
        spec = PRESS_RELEASE_INFORMATION_CATALOG[name]
        values = [
            name, spec.get("label", ""),
            *spec.get("aliases_en", []),
            *spec.get("document_cues", [])
        ]
        documents.append(" ".join(normalize_text(v) for v in values if v))

    vectorizer = TfidfVectorizer(
        analyzer="char_wb", ngram_range=(3, 5), lowercase=True, min_df=1
    )
    matrix = vectorizer.fit_transform([normalized_question] + documents)
    similarities = cosine_similarity(matrix[0:1], matrix[1:]).ravel()
    best_index = int(similarities.argmax())
    best_similarity = float(similarities[best_index])
    if best_similarity < minimum_similarity:
        return None

    metric_name = metric_names[best_index]
    spec = PRESS_RELEASE_INFORMATION_CATALOG[metric_name]
    return {
        "metric": metric_name,
        **spec,
        "selection_type": "SEMANTIC_INFORMATION_TYPE",
        "semantic_similarity": round(best_similarity, 4),
        "matched_query_terms": []
    }


def resolve_press_release_information_types(
    question: str,
    explicit_metric: Optional[str] = None,
    allow_semantic_fallback: bool = True
) -> List[Dict[str, Any]]:
    exact = detect_press_release_information_types(question, explicit_metric)
    if exact:
        return exact

    explicit_key = str(explicit_metric or "").strip().upper()
    if explicit_key in SEMANTIC_KPI_FAMILIES:
        return []

    if allow_semantic_fallback:
        inferred = infer_press_release_information_type(question)
        return [inferred] if inferred else []
    return []


def detect_query_sections(
    question: str,
    explicit_metric: Optional[str] = None
) -> List[str]:
    """Additive section selection: no exclusive rule."""
    normalized_question = normalize_text(question)
    sections: List[str] = []

    # If the metric is already defined in the calculation component, its catalog entry takes precedence over the full text
    # of the question: this prevents words belonging to other
    # components from improperly broadening the search scope.
    explicit_metric_key = str(explicit_metric or "").strip().upper()
    explicit_spec = PRESS_RELEASE_SEARCH_CATALOG.get(explicit_metric_key)
    if explicit_spec and explicit_metric_key != "GENERAL_FUNDAMENTAL":
        return list(explicit_spec.get("preferred_sections", [])) or [
            "TITLE1", "TITLE2", "TITLE3"
        ]

    for info in resolve_press_release_information_types(
        question, explicit_metric, allow_semantic_fallback=False
    ):
        for section in info.get("preferred_sections", []):
            if section not in sections:
                sections.append(section)

    if contains_any(normalized_question, CEO_QUERY_KEYS) and "CEO" not in sections:
        sections.append("CEO")
    if contains_any(normalized_question, CFO_QUERY_KEYS) and "CFO" not in sections:
        sections.append("CFO")
    if (contains_any(normalized_question, FY2026_KEYS) or
            contains_any(normalized_question, STRATEGY_KEYS)) and "TITLE3" not in sections:
        sections.append("TITLE3")
    if contains_any(normalized_question, REASON_KEYS):
        for section in ["TITLE2", "TITLE1"]:
            if section not in sections:
                sections.append(section)
    if contains_any(normalized_question, FY2025_KEYS) and "TITLE1" not in sections:
        sections.append("TITLE1")

    if explicit_metric:
        metric_key = str(explicit_metric).strip().upper()
        spec = PRESS_RELEASE_SEARCH_CATALOG.get(metric_key)
        if spec:
            for section in spec.get("preferred_sections", []):
                if section not in sections:
                    sections.append(section)

    return sections or ["TITLE1", "TITLE2", "TITLE3"]


def _contains_semantic_phrase(text: str, phrase: str) -> bool:
    normalized_text = normalize_text(text)
    normalized_phrase = normalize_text(phrase)
    if not normalized_phrase:
        return False
    return re.search(r"(?<!\w)" + re.escape(normalized_phrase) + r"(?!\w)", normalized_text) is not None


def detect_financial_concepts(question: str) -> List[Dict[str, Any]]:
    """Recognizes the precise KPI through English synonyms."""
    matches: Dict[str, Dict[str, Any]] = {}

    terms_index = []
    for family_name, family in SEMANTIC_KPI_FAMILIES.items():
        for term in family["query"] + family["document_terms"]:
            terms_index.append((term, family_name))

    for term, family_name in sorted(terms_index, key=lambda item: len(item[0]), reverse=True):
        if not _contains_semantic_phrase(question, term):
            continue
        family = SEMANTIC_KPI_FAMILIES[family_name]
        record = matches.setdefault(
            family_name,
            {
                "concept": family_name,
                "label": family["label"],
                "macro_area": family["macro_area"],
                "sector": family["sector"],
                "matched_query_terms": [],
                "search_terms": family["document_terms"].copy()
            }
        )
        if term not in record["matched_query_terms"]:
            record["matched_query_terms"].append(term)

    # Specific expressions take precedence over generic ones.
    if "EARNINGS_PER_SHARE" in matches:
        matches.pop("NET_INCOME", None)

    return list(matches.values())


def _build_family_semantic_document(concept: str, family: Dict[str, Any]) -> str:
    values = [
        concept,
        family.get("label", ""),
        family.get("macro_area", ""),
        family.get("sector", ""),
        *family.get("query", []),
        *family.get("document_terms", [])
    ]
    return " ".join(normalize_text(value) for value in values if value)


def infer_financial_concept_by_area(
    question: str,
    minimum_similarity: float = 0.08
) -> Optional[Dict[str, Any]]:
    """
    Used only when the question does not contain an exact keyword or synonym.
    Selects the closest financial family through TF-IDF and cosine similarity
    on the English descriptions already defined in the graph.
    """
    normalized_question = normalize_text(question)
    if not normalized_question:
        return None

    concept_names = list(SEMANTIC_KPI_FAMILIES.keys())
    family_documents = [
        _build_family_semantic_document(
            concept, SEMANTIC_KPI_FAMILIES[concept]
        )
        for concept in concept_names
    ]

    vectorizer = TfidfVectorizer(
        analyzer="char_wb",
        ngram_range=(3, 5),
        lowercase=True,
        min_df=1
    )
    matrix = vectorizer.fit_transform(
        [normalized_question] + family_documents
    )
    similarities = cosine_similarity(
        matrix[0:1], matrix[1:]
    ).ravel()

    best_index = int(similarities.argmax())
    best_similarity = float(similarities[best_index])
    if best_similarity < minimum_similarity:
        return None

    concept = concept_names[best_index]
    family = SEMANTIC_KPI_FAMILIES[concept]
    return {
        "concept": concept,
        "label": family["label"],
        "macro_area": family["macro_area"],
        "sector": family.get("sector", ""),
        "matched_query_terms": [],
        "search_terms": family["document_terms"].copy(),
        "selection_type": "SEMANTIC_AREA_TFIDF",
        "semantic_similarity": round(best_similarity, 4)
    }


def resolve_financial_concepts(question: str) -> List[Dict[str, Any]]:
    """
    1. Exact keyword or synonym.
    2. Only if absent, the semantically closest family.
    """
    exact_concepts = detect_financial_concepts(question)
    if exact_concepts:
        for concept in exact_concepts:
            concept["selection_type"] = "KEYWORD_O_SINONIMO_ESATTO"
            concept["semantic_similarity"] = 1.0
        return exact_concepts

    inferred = infer_financial_concept_by_area(question)
    return [inferred] if inferred else []


def search_units_for_terms(
    units: Sequence[Dict[str, Any]],
    search_terms: Sequence[str]
) -> List[Dict[str, Any]]:
    matches = []
    seen = set()
    ordered_terms = sorted(
        list(dict.fromkeys(search_terms)),
        key=len,
        reverse=True
    )

    for unit in units:
        matched_terms = [
            term for term in ordered_terms
            if _contains_semantic_phrase(unit.get("line", ""), term)
        ]
        if not matched_terms:
            continue

        key = (
            unit.get("section"),
            unit.get("block_index"),
            unit.get("line_index"),
            normalize_text(unit.get("line", ""))
        )
        if key in seen:
            continue

        seen.add(key)
        matches.append({
            **unit,
            "matched_document_terms": matched_terms
        })

    return matches


def get_macro_area_fallbacks(concept: str) -> List[Dict[str, Any]]:
    """Returns only KPIs belonging to the same macro-area."""
    family = SEMANTIC_KPI_FAMILIES[concept]
    related_names = MACRO_AREA_RELATED_KPIS.get(family["macro_area"], [])

    return [
        {
            "concept": related_name,
            "label": SEMANTIC_KPI_FAMILIES[related_name]["label"],
            "search_terms": SEMANTIC_KPI_FAMILIES[related_name]["document_terms"].copy()
        }
        for related_name in related_names
        if related_name != concept
    ]


def validate_semantic_graph() -> Dict[str, Any]:
    source_normalized = [normalize_text(term) for term in SOURCE_BULLET_KEYWORDS]
    graph_normalized = [normalize_text(term) for term in BULLET_KEYWORDS]

    keyword_to_families: Dict[str, List[str]] = {}
    for family_name, family in SEMANTIC_KPI_FAMILIES.items():
        for term in family["document_terms"]:
            keyword_to_families.setdefault(normalize_text(term), []).append(family_name)

    report = {
        "source_keywords_count": len(SOURCE_BULLET_KEYWORDS),
        "graph_keywords_count": len(BULLET_KEYWORDS),
        "missing_keywords": sorted(set(source_normalized) - set(graph_normalized)),
        "extra_keywords": sorted(set(graph_normalized) - set(source_normalized)),
        "duplicate_source_keywords": sorted({
            term for term in source_normalized if source_normalized.count(term) > 1
        }),
        "duplicate_graph_keywords": sorted({
            term for term in graph_normalized if graph_normalized.count(term) > 1
        }),
        "multiple_family_assignments": {
            term: names for term, names in keyword_to_families.items()
            if len(names) > 1
        }
    }
    report["validation_ok"] = not any([
        report["missing_keywords"],
        report["extra_keywords"],
        report["duplicate_source_keywords"],
        report["duplicate_graph_keywords"],
        report["multiple_family_assignments"]
    ])
    return report


def infer_temporal_label(
    section: str,
    section_title: str = ""
) -> str:
    """Returns the document period consistent with the section."""
    normalized = normalize_text(f"{section} {section_title}")
    if "title3" in normalized or "2026" in normalized or "guidance" in normalized:
        return "FY2026 / guidance"
    return "FY2025"


def normalize_press_release_time_periods(
    values: Optional[Sequence[Any]] = None
) -> List[str]:
    """Normalizes the time constraint of the fundamental component."""
    if values is None:
        return []
    if isinstance(values, (str, int, float)):
        values = [values]

    normalized_values: List[str] = []
    for value in values:
        text = str(value).strip()
        if not text:
            continue
        key = normalize_text(text)
        if "2026" in key or "guidance" in key:
            label = "FY2026 / guidance"
        elif "2025" in key or key in {"fy", "ultimo anno fiscale", "last fiscal year"}:
            label = "FY2025"
        else:
            label = text
        if label not in normalized_values:
            normalized_values.append(label)
    return normalized_values


def resolve_press_release_metric(
    explicit_metric: Optional[str],
    concepts: Sequence[Dict[str, Any]],
    information_types: Optional[Sequence[Dict[str, Any]]] = None
) -> str:
    """Priority: explicit metric -> information type -> KPI -> general."""
    metric = str(explicit_metric or "").strip()
    metric_key = metric.upper()
    if metric and normalize_text(metric) not in {"fundamental", "fondamentale"}:
        return metric_key if metric_key in PRESS_RELEASE_SEARCH_CATALOG else metric
    if information_types:
        info_metric = str(information_types[0].get("metric", "")).strip()
        if info_metric:
            return info_metric
    if concepts:
        concept_name = str(concepts[0].get("concept", "")).strip()
        if concept_name:
            return concept_name
    raise ValueError(
        "No canonical Press Release tool metric identified."
    )

def build_press_release_component_id(
    ticker: str,
    time_periods: Sequence[str],
    metric: str,
    component_id: Optional[str] = None
) -> str:
    if component_id:
        return str(component_id)
    period_key = "+".join(str(item) for item in time_periods) or "FY2025"
    return f"PRESS_RELEASE::{ticker}::{period_key}::{metric}"


def filter_press_release_sections_by_time(
    sections: Sequence[str],
    time_periods: Sequence[str]
) -> List[str]:
    """Applies the period only when it is explicit and compatible with the document."""
    if not time_periods:
        return list(sections)

    normalized_periods = " ".join(normalize_text(item) for item in time_periods)
    wants_2026 = "2026" in normalized_periods or "guidance" in normalized_periods
    wants_2025 = "2025" in normalized_periods

    if wants_2026 and not wants_2025:
        filtered = [section for section in sections if section == "TITLE3"]
        return filtered or ["TITLE3"]

    if wants_2025 and not wants_2026:
        filtered = [section for section in sections if section != "TITLE3"]
        return filtered or ["TITLE1", "TITLE2"]

    return list(sections)


def _press_document_content_matches(metric: str, text: str, periods=None) -> bool:
    """Validate documentary content, independently of its requested category.

    A section title or a year alone cannot certify an outlook. This is a
    conservative textual check, not an assertion that every guidance is numeric.
    """
    import re
    content = str(text or "").casefold()
    if not content.strip():
        return False
    if metric == "GUIDANCE_OUTLOOK":
        forward = re.search(
            r"\b(guidance|outlook|forecast(?:s|ed)?|expect(?:s|ed|ations)?|"
            r"project(?:s|ed|ions)?|anticipat(?:es|ed|ion)|"
            r"full[- ]year (?:guidance|outlook)|financial outlook)\b",
            content
        )
        if not forward:
            return False
        requested = " ".join(str(p) for p in (periods or [])).casefold()
        # When FY2026 is explicitly requested, reject purely FY2025 commentary.
        if "2026" in requested and "2026" not in content:
            return False
        return True
    if metric == "FY_RESULTS":
        return bool(re.search(
            r"\b(results|revenue|sales|earnings|income|eps|cash flow|"
            r"fiscal year|full[- ]year|financial results)\b", content
        ))
    return True


def classify_press_release_retrieval_status(
    item: Dict[str, Any],
    requested_metric: str
) -> str:
    """
    Explicitly classifies retrieval quality without confusing
    equivalence with semantic proximity. The metric requested in the calculation component remains
    the one constructed upstream by the workflow; BOX 36 only declares HOW
    the evidence was retrieved.
    """
    match_type = str(item.get("retrieval_match_type", "")).upper()
    selection_type = str(item.get("concept_selection_type", "")).upper()
    requested_concept = str(
        item.get("requested_concept") or requested_metric or ""
    ).upper()
    matched_concept = str(
        item.get("concept") or requested_concept or ""
    ).upper()

    if match_type == "MACRO_AREA_FALLBACK":
        return "RELATED_IN_SAME_MACRO_AREA"

    if match_type == "SEMANTIC_MACRO_AREA":
        if matched_concept == requested_concept:
            return "SEMANTIC_EQUIVALENT"
        return "RELATED_IN_SAME_MACRO_AREA"

    if match_type == "SECTION_FALLBACK":
        return "SECTION_FALLBACK"

    if selection_type == "AREA_SEMANTICA_TFIDF":
        if matched_concept == requested_concept:
            return "SEMANTIC_EQUIVALENT"
        return "RELATED_IN_SAME_MACRO_AREA"

    if selection_type == "KEYWORD_O_SINONIMO_ESATTO":
        return "SYNONYM_MATCH"

    if selection_type in {"EXPLICIT_METRIC", "CATALOG_INFORMATION_TYPE"}:
        return "EXACT_MATCH"

    if match_type in {
        "DEDICATED_MANAGEMENT_SECTION",
        "INFORMATION_CUE",
        "KPI_DOCUMENT_TERM"
    }:
        return "EXACT_MATCH"

    return "EXACT_MATCH"


def aggregate_press_release_retrieval_status(
    evidence: Sequence[Dict[str, Any]]
) -> str:
    """Returns the most conservative overall status of the component."""
    if not evidence:
        return "NOT_FOUND"

    statuses = [str(item.get("retrieval_status", "")) for item in evidence]
    priority = [
        "EXACT_MATCH",
        "SYNONYM_MATCH",
        "SEMANTIC_EQUIVALENT",
        "RELATED_IN_SAME_MACRO_AREA",
        "SECTION_FALLBACK"
    ]
    for status in priority:
        if status in statuses:
            return status
    return "NOT_FOUND"


def answer_press_release_question(
    state: Dict[str, Any],
    company: Optional[str] = None,
    question: Optional[str] = None,
    ticker: Optional[str] = None,
    time_periods: Optional[Sequence[Any]] = None,
    metric: Optional[str] = None,
    component_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Queries ONE individual calculation component: ticker + period + metric.
    Preserves the existing KPI search and adds general document retrieval
    through the unified catalog.
    """
    resolved_question = str(
        question
        or state.get("user_question")
        or state.get("normalized_question")
        or metric
        or ""
    ).strip()
    if not resolved_question:
        raise ValueError("The question cannot be empty.")

    state = build_press_release_archive(state, force_refresh=False)

    company_or_ticker = ticker or company
    if not company_or_ticker:
        extracted = state.get("extracted_entities", {})
        extracted_tickers = extracted.get("tickers", []) if isinstance(extracted, dict) else []
        if len(extracted_tickers) == 1:
            company_or_ticker = extracted_tickers[0]
    if not company_or_ticker:
        raise ValueError("Company/ticker not identified for the fundamental component.")

    resolved_ticker = resolve_ticker(str(company_or_ticker))
    record = state["press_release_archive"][resolved_ticker]
    normalized_time_periods = normalize_press_release_time_periods(time_periods)

    information_types = resolve_press_release_information_types(
        resolved_question, metric, allow_semantic_fallback=False
    )

    explicit_metric_key = str(metric or "").strip().upper()
    if explicit_metric_key in SEMANTIC_KPI_FAMILIES:
        family = SEMANTIC_KPI_FAMILIES[explicit_metric_key]
        concepts = [{
            "concept": explicit_metric_key,
            "label": family["label"],
            "macro_area": family["macro_area"],
            "sector": family["sector"],
            "matched_query_terms": [str(metric)],
            "search_terms": family["document_terms"].copy(),
            "selection_type": "EXPLICIT_METRIC",
            "semantic_similarity": 1.0
        }]
    else:
        concepts = resolve_financial_concepts(resolved_question)

    resolved_metric = resolve_press_release_metric(metric, concepts, information_types)
    resolved_component_id = build_press_release_component_id(
        resolved_ticker,
        normalized_time_periods,
        resolved_metric,
        component_id
    )
    metric_spec = PRESS_RELEASE_SEARCH_CATALOG.get(str(resolved_metric).upper(), {})
    metric_class = metric_spec.get(
        "metric_class",
        "KPI" if resolved_metric in SEMANTIC_KPI_FAMILIES else "DOCUMENT_INFORMATION"
    )

    if record["download_error"]:
        answer = f"Unable to access the press release: {record['download_error']}"
        result = {
            "component_id": resolved_component_id,
            "ticker": resolved_ticker,
            "company": record["company"],
            "time_periods": normalized_time_periods,
            "metric": resolved_metric,
            "metric_class": metric_class,
            "question": resolved_question,
            "sections": [],
            "information_types": [item.get("metric") for item in information_types],
            "concepts": [item.get("concept") for item in concepts],
            "catalog_entry": metric_spec,
            "evidence": [],
            "answer": answer,
            "url": record["url"],
            "status": "UNAVAILABLE"
        }
        state["press_release_last_answer"] = result
        state["press_release_query"] = {
            "component_id": resolved_component_id,
            "ticker": resolved_ticker,
            "time_periods": normalized_time_periods,
            "metric": resolved_metric,
            "metric_class": metric_class,
            "question": resolved_question
        }
        state["press_release_result"] = result
        return result

    requested_sections = detect_query_sections(resolved_question, resolved_metric)
    requested_sections = filter_press_release_sections_by_time(
        requested_sections,
        normalized_time_periods
    )

    evidence: List[Dict[str, Any]] = []

    if resolved_metric == "CEO_COMMENTARY":
        evidence = [{
            "section": "CEO",
            "section_title": "Dichiarazione CEO",
            "line": quote,
            "evidence_type": "RISPOSTA_ESATTA",
            "retrieval_match_type": "DEDICATED_MANAGEMENT_SECTION"
        } for quote in record["ceo_quotes"]]

    elif resolved_metric == "CFO_COMMENTARY":
        evidence = [{
            "section": "CFO",
            "section_title": "Dichiarazione CFO",
            "line": quote,
            "evidence_type": "RISPOSTA_ESATTA",
            "retrieval_match_type": "DEDICATED_MANAGEMENT_SECTION"
        } for quote in record["cfo_quotes"]]

    else:
        candidate_units = [
            unit for unit in record["section_units"]
            if unit["section"] in requested_sections
        ]

        # 1) GENERAL DOCUMENT METRIC
        if metric_class == "DOCUMENT_INFORMATION" and resolved_metric != "GENERAL_FUNDAMENTAL":
            # Section classification is a candidate locator, not proof that
            # the text satisfies the requested information category.
            preferred = metric_spec.get("preferred_sections", requested_sections)
            fallback_sections = metric_spec.get("fallback_sections", [])
            fallback_units = [
                unit for unit in record["section_units"]
                if unit["section"] in fallback_sections
            ]
            ordered_units = sorted(
                candidate_units or fallback_units,
                key=lambda unit: (
                    preferred.index(unit["section"])
                    if unit["section"] in preferred else len(preferred),
                    unit.get("block_index", 0), unit.get("line_index", 0)
                )
            )
            # For guidance, also inspect other sections: a company may put
            # its outlook in a results or highlights section.
            if resolved_metric == "GUIDANCE_OUTLOOK":
                ordered_units.extend(
                    unit for unit in record["section_units"]
                    if unit not in ordered_units
                )
            for unit in ordered_units:
                # DOCUMENT_INFORMATION: the BOX 36 catalog/section selection is
                # authoritative; do not reclassify each line by its wording.
                evidence.append({
                    **unit,
                    "concept": resolved_metric,
                    "requested_concept": resolved_metric,
                    "returned_label": metric_spec.get("label", resolved_metric),
                    "macro_area": None,
                    "evidence_type": "RISPOSTA_SEZIONE",
                    "concept_selection_type": "CONTENT_VERIFIED",
                    "semantic_similarity": None,
                    "retrieval_match_type": "INFORMATION_CUE"
                })

        # 2) KPI: logica originaria preservata integralmente
        if metric_class == "KPI" or (resolved_metric == "GENERAL_FUNDAMENTAL" and concepts):
            for concept in concepts:
                selection_type = concept.get("selection_type", "KEYWORD_O_SINONIMO_ESATTO")

                if selection_type in {"KEYWORD_O_SINONIMO_ESATTO", "EXPLICIT_METRIC"}:
                    exact_matches = search_units_for_terms(candidate_units, concept["search_terms"])
                    if exact_matches:
                        for match in exact_matches:
                            evidence.append({
                                **match,
                                "concept": concept["concept"],
                                "requested_concept": concept["concept"],
                                "returned_label": concept["label"],
                                "macro_area": concept["macro_area"],
                                "evidence_type": "RISPOSTA_ESATTA",
                                "concept_selection_type": selection_type,
                                "semantic_similarity": 1.0,
                                "retrieval_match_type": "KPI_DOCUMENT_TERM"
                            })
                    else:
                        for related in get_macro_area_fallbacks(concept["concept"]):
                            for match in search_units_for_terms(candidate_units, related["search_terms"]):
                                evidence.append({
                                    **match,
                                    "concept": related["concept"],
                                    "requested_concept": concept["concept"],
                                    "returned_label": related["label"],
                                    "macro_area": concept["macro_area"],
                                    "evidence_type": "APPROFONDIMENTO_CORRELATO",
                                    "concept_selection_type": selection_type,
                                    "semantic_similarity": 1.0,
                                    "retrieval_match_type": "MACRO_AREA_FALLBACK"
                                })
                else:
                    area_candidates = [
                        {
                            "concept": name,
                            "label": family["label"],
                            "search_terms": family["document_terms"]
                        }
                        for name, family in SEMANTIC_KPI_FAMILIES.items()
                        if family["macro_area"] == concept["macro_area"]
                    ]
                    for related in area_candidates:
                        for match in search_units_for_terms(candidate_units, related["search_terms"]):
                            evidence.append({
                                **match,
                                "concept": related["concept"],
                                "requested_concept": concept["concept"],
                                "returned_label": related["label"],
                                "macro_area": concept["macro_area"],
                                "evidence_type": "APPROFONDIMENTO_CORRELATO",
                                "concept_selection_type": selection_type,
                                "semantic_similarity": concept.get("semantic_similarity"),
                                "retrieval_match_type": "SEMANTIC_MACRO_AREA"
                            })

        # 3) FONDAMENTALE GENERALE
        if resolved_metric == "GENERAL_FUNDAMENTAL" and not evidence:
            for unit in candidate_units:
                evidence.append({
                    **unit,
                    "concept": "GENERAL_FUNDAMENTAL",
                    "requested_concept": "GENERAL_FUNDAMENTAL",
                    "returned_label": "General fundamental information",
                    "macro_area": None,
                    "evidence_type": "RISPOSTA_SEZIONE",
                    "concept_selection_type": "SECTION_FALLBACK",
                    "semantic_similarity": None,
                    "retrieval_match_type": "SECTION_FALLBACK"
                })

    unique_evidence: List[Dict[str, Any]] = []
    seen_lines = set()
    for item in evidence:
        key = normalize_text(item.get("line", ""))
        if key and key not in seen_lines:
            seen_lines.add(key)
            temporal_label = infer_temporal_label(
                str(item.get("section", "")),
                str(item.get("section_title", ""))
            )
            unique_evidence.append({
                **item,
                "component_id": resolved_component_id,
                "ticker": resolved_ticker,
                "time_period": temporal_label,
                "time_periods": normalized_time_periods or [temporal_label],
                "metric": resolved_metric,
                "metric_class": metric_class,
                "matched_section": item.get("section"),
                "match_type": item.get(
                    "retrieval_match_type",
                    item.get("concept_selection_type", item.get("evidence_type"))
                ),
                "retrieval_status": classify_press_release_retrieval_status(
                    item, resolved_metric
                ),
                "requested_metric": resolved_metric,
                "matched_metric": item.get("concept", resolved_metric),
                "evidence_text": item.get("line", ""),
                "source_tool": "press_release_fy2025",
                "source_url": record["url"]
            })
    evidence = (unique_evidence if metric_class == "DOCUMENT_INFORMATION" else unique_evidence[:MAX_ANSWER_EVIDENCE])

    retrieval_status = aggregate_press_release_retrieval_status(evidence)

    if not evidence:
        answer = "Information not available in the press release."
        status = "UNAVAILABLE"
    else:
        status = "AVAILABLE"
        section_labels = {
            key: value["label"]
            for key, value in PRESS_RELEASE_SECTION_CATALOG.items()
        }
        answer_lines = [f"{record['company']} ({resolved_ticker})"]
        if retrieval_status == "RELATED_IN_SAME_MACRO_AREA":
            answer_lines.append(
                "The requested metric was not found directly; "
                "related information is available within the same semantic area."
            )
        elif retrieval_status == "SEMANTIC_EQUIVALENT":
            answer_lines.append(
                "The exact term was not found; "
                "semantically equivalent information was identified."
            )
        elif retrieval_status == "SECTION_FALLBACK":
            answer_lines.append(
                "A direct match was not identified; "
                "the evidence comes from the most relevant document section."
            )
        for item in evidence:
            section_label = section_labels.get(
                item.get("section"), item.get("section_title", item.get("section", ""))
            )
            temporal_label = item.get("time_period", "FY2025")
            if item.get("evidence_type") == "APPROFONDIMENTO_CORRELATO":
                answer_lines.append(
                    "APPROFONDIMENTO CORRELATO | "
                    f"Area: {item.get('macro_area', '')} | "
                    f"Available KPI: {item.get('returned_label', item.get('concept', ''))} | "
                    f"Period: {temporal_label} | [{section_label}] {item['line']}"
                )
            else:
                answer_lines.append(
                    f"Period: {temporal_label} | [{section_label}] {item['line']}"
                )
        answer = "\n".join(answer_lines)

    result = {
        "component_id": resolved_component_id,
        "ticker": resolved_ticker,
        "company": record["company"],
        "time_periods": normalized_time_periods,
        "metric": resolved_metric,
        "metric_class": metric_class,
        "retrieval_status": retrieval_status,
        "question": resolved_question,
        "sections": requested_sections,
        "information_types": [item.get("metric") for item in information_types],
        "concepts": [item.get("concept") for item in concepts],
        "catalog_entry": metric_spec,
        "evidence": evidence,
        "answer": answer,
        "url": record["url"],
        "status": status
    }

    state["press_release_last_answer"] = result
    state.setdefault("press_release_query_history", []).append(result)
    state["press_release_results"] = pd.DataFrame(evidence)
    state["press_release_query"] = {
        "component_id": resolved_component_id,
        "ticker": resolved_ticker,
        "time_periods": normalized_time_periods,
        "metric": resolved_metric,
        "metric_class": metric_class,
        "retrieval_status": retrieval_status,
        "requested_metric": resolved_metric,
        "matched_metrics": list(dict.fromkeys(
            item.get("matched_metric", resolved_metric) for item in evidence
        )),
        "question": resolved_question,
        "sections": requested_sections,
        "catalog_key": str(resolved_metric).upper()
    }
    state["press_release_result"] = result
    return result

# ============================================================
# TOOL AGENTICO
# ============================================================

def _resolve_single_press_release_metric_for_tool(
    question: str,
    metric: Optional[str] = None
) -> str:
    """
    Resolves ONE metric only for a single tool call.

    Architectural rule:
    - BOX 41 constructs the ticker + time + metric components;
    - BOX 36 never decomposes a compound question into multiple components;
    - if the metric is explicit and present in the catalog, it is used;
    - if it is missing, semantic fallback is allowed only when it leads to a
      single unambiguous metric, useful for standalone/historical compatibility;
    - if the text contains multiple distinct metrics, the workflow is required
      to decompose the question first into the necessary calculation components, rather than duplicating BOX 41's work.
    """
    explicit = str(metric or "").strip()
    explicit_key = explicit.upper()

    if explicit_key in PRESS_RELEASE_SEARCH_CATALOG:
        return explicit_key

    generic_metric = normalize_text(explicit) in {
        "", "fundamental", "fondamentale", "fundamentals",
        "fundamental information", "informazioni fondamentali"
    }
    if explicit and not generic_metric:
        raise ValueError(
            f"Metric '{metric}' not present in the Press Release tool catalog."
        )

    candidate_metrics: List[str] = []

    # Tipi informativi documentali riconosciuti esattamente.
    for info in resolve_press_release_information_types(
        question,
        explicit_metric=None,
        allow_semantic_fallback=False
    ):
        candidate = str(info.get("metric", "")).strip().upper()
        if candidate and candidate not in candidate_metrics:
            candidate_metrics.append(candidate)

    # KPIs explicitly named or recognized through synonyms.
    for concept in detect_financial_concepts(question):
        candidate = str(concept.get("concept", "")).strip().upper()
        if candidate and candidate not in candidate_metrics:
            candidate_metrics.append(candidate)

    if len(candidate_metrics) > 1:
        raise ValueError(
            "The request contains multiple metrics/components: "
            + ", ".join(candidate_metrics)
            + ". Multiple decomposition belongs to BOX 41; "
              "the Press Release tool executes a single calculation component per call."
        )

    if len(candidate_metrics) == 1:
        return candidate_metrics[0]

    # NON-decompositional semantic fallback: selects at most one metric.
    semantic_candidates: List[Dict[str, Any]] = []

    inferred_information = infer_press_release_information_type(question)
    if inferred_information:
        semantic_candidates.append({
            "metric": str(inferred_information.get("metric", "")).upper(),
            "score": float(inferred_information.get("semantic_similarity") or 0.0)
        })

    inferred_kpi = infer_financial_concept_by_area(question)
    if inferred_kpi:
        semantic_candidates.append({
            "metric": str(inferred_kpi.get("concept", "")).upper(),
            "score": float(inferred_kpi.get("semantic_similarity") or 0.0)
        })

    semantic_candidates = [
        item for item in semantic_candidates
        if item["metric"] in PRESS_RELEASE_SEARCH_CATALOG
    ]

    if semantic_candidates:
        semantic_candidates.sort(key=lambda item: item["score"], reverse=True)
        return semantic_candidates[0]["metric"]

    raise ValueError(
        "No unique canonical Press Release tool metric "
        "was identified. Decomposition must be resolved "
        "upstream by BOX 41."
    )


def press_release_agentic_tool(
    state: Dict[str, Any],
    company: Optional[str] = None,
    question: Optional[str] = None,
    force_refresh: bool = False,
    ticker: Optional[str] = None,
    tickers: Optional[Sequence[str]] = None,
    time_period: Optional[Any] = None,
    time_periods: Optional[Sequence[Any]] = None,
    metric: Optional[str] = None,
    component_id: Optional[str] = None,
    **kwargs: Any
) -> Dict[str, Any]:
    """
    Press Release tool adapter aligned with the project architecture.

    Executes ONE calculation component per call:

        ticker + time_period + metric

    It does not create sub-questions, does not generate metric lists, and does not duplicate
    BOX 41 decomposition. The full semantic richness of BOX 36 is used
    exclusively to locate and certify the requested information.
    """
    state = build_press_release_archive(state, force_refresh=force_refresh)

    resolved_question = str(
        question
        or state.get("user_question")
        or state.get("normalized_question")
        or metric
        or ""
    ).strip()
    if not resolved_question:
        raise ValueError("The question/component cannot be empty.")

    # --------------------------------------------------------
    # 1. TICKER: a single instrument dimension per component.
    # --------------------------------------------------------
    targets: List[str] = []
    if ticker:
        targets.append(str(ticker))
    if tickers:
        targets.extend(str(item) for item in tickers if str(item).strip())
    if company:
        targets.append(str(company))

    if not targets:
        extracted_entities = state.get("extracted_entities", {})
        if isinstance(extracted_entities, dict):
            targets.extend(
                str(item)
                for item in extracted_entities.get("tickers", [])
                if str(item).strip()
            )

    unique_targets: List[str] = []
    for target in targets:
        resolved_target = resolve_ticker(target)
        if resolved_target not in unique_targets:
            unique_targets.append(resolved_target)

    if not unique_targets:
        raise ValueError("No ticker identified for the Press Release tool.")
    if len(unique_targets) != 1:
        raise ValueError(
            "The Press Release tool received multiple tickers ("
            + ", ".join(unique_targets)
            + "). Each call must represent a single calculation component; "
              "multi-ticker decomposition belongs to BOX 41."
        )
    resolved_ticker = unique_targets[0]

    # --------------------------------------------------------
    # 2. TIME: a single logical period per component.
    # --------------------------------------------------------
    requested_periods = time_periods
    if requested_periods is None and time_period is not None:
        requested_periods = [time_period]
    if requested_periods is None:
        extracted_entities = state.get("extracted_entities", {})
        if isinstance(extracted_entities, dict):
            requested_periods = extracted_entities.get("time_periods", [])

    normalized_periods = normalize_press_release_time_periods(requested_periods)
    if len(normalized_periods) > 1:
        raise ValueError(
            "The Press Release tool received multiple periods ("
            + ", ".join(normalized_periods)
            + "). Each call must represent a single calculation component; "
              "multi-period decomposition belongs to BOX 41."
        )

    # --------------------------------------------------------
    # 3. METRIC: a single metric per component.
    # --------------------------------------------------------
    resolved_metric = _resolve_single_press_release_metric_for_tool(
        resolved_question,
        metric=metric
    )

    # --------------------------------------------------------
    # 4. EXECUTION OF THE SINGLE COMPONENT.
    # --------------------------------------------------------
    result = answer_press_release_question(
        state=state,
        ticker=resolved_ticker,
        question=resolved_question,
        time_periods=normalized_periods,
        metric=resolved_metric,
        component_id=component_id
    )

    # Native tool output: a single result for the individual component.
    # component_id is preserved for workflow compatibility, but
    # the semantic identity remains ticker + time_period + metric.
    state["press_release_query"] = {
        "component_id": result.get("component_id"),
        "ticker": result.get("ticker"),
        "time_periods": result.get("time_periods", []),
        "metric": result.get("metric"),
        "metric_class": result.get("metric_class"),
        "question": resolved_question,
        "catalog_identity_dimensions": ["ticker", "time_period", "metric"],
        "component_construction_owner": "BOX_40"
    }
    state["press_release_result"] = result
    state["press_release_results"] = pd.DataFrame(result.get("evidence", []))

    # Truly compact calculation output for the workflow.
    # The tool's internal logic and the complete result in the state remain
    # unchanged; only what is needed passes through subprocess/Queue
    # for normalization and synthesis of the individual component.
    compact_evidence = []

    for item in result.get("evidence", []):
        if not isinstance(item, dict):
            continue

        evidence_text = (
            item.get("evidence_text")
            or item.get("line")
            or item.get("normalized_line")
            or ""
        )

        compact_item = {
            "section": item.get("section"),
            "section_title": item.get("section_title"),
            "evidence_text": evidence_text,
            "retrieval_status": item.get("retrieval_status"),
            "requested_metric": item.get(
                "requested_metric",
                result.get("metric")
            ),
            "matched_metric": item.get(
                "matched_metric",
                item.get("concept", result.get("metric"))
            ),
            "content_verified": (
                bool(str(evidence_text).strip())
                if result.get("metric_class") == "DOCUMENT_INFORMATION"
                else _press_document_content_matches(
                    str(result.get("metric") or ""), evidence_text,
                    result.get("time_periods", [])
                )
            ),
            "match_type": item.get("match_type"),
        }

        compact_evidence.append(
            {
                key: value
                for key, value in compact_item.items()
                if value not in (None, "", [], {})
            }
        )

    compact_result = {
        "component_id": result.get("component_id"),
        "ticker": result.get("ticker"),
        "time_periods": result.get("time_periods", []),
        "metric": result.get("metric"),
        "metric_class": result.get("metric_class"),
        "retrieval_status": result.get("retrieval_status"),
        "requested_metric": result.get("metric"),
        "matched_metrics": list(dict.fromkeys(
            item.get(
                "matched_metric",
                item.get("concept", result.get("metric"))
            )
            for item in result.get("evidence", [])
            if isinstance(item, dict)
        )),
        "evidence": compact_evidence,
        "status": result.get("status")
    }

    return {
        "press_release_query": copy.deepcopy(state["press_release_query"]),
        "press_release_result": compact_result
    }


# ============================================================
# NATURAL-LANGUAGE QUERY MINI-TOOL
# ============================================================

SEMANTIC_GRAPH_VALIDATION = validate_semantic_graph()
if not SEMANTIC_GRAPH_VALIDATION["validation_ok"]:
    raise RuntimeError(
        "Error in the semantic graph: "
        f"{SEMANTIC_GRAPH_VALIDATION}"
    )

if "final_state" not in globals() or not isinstance(final_state, dict):
    final_state = {}

final_state = build_press_release_archive(final_state, force_refresh=False)

if IPYWIDGETS_AVAILABLE:
    company_widget = widgets.Dropdown(
        options=[
            (f"{COMPANY_NAMES[ticker]} ({ticker})", ticker)
            for ticker in PRESS_RELEASE_URLS
        ],
        description="Company:",
        layout=widgets.Layout(width="520px")
    )

    question_widget = widgets.Textarea(
        value="",
        placeholder="Enter the question about the press release",
        description="Question:",
        layout=widgets.Layout(width="760px", height="90px")
    )

    query_button = widgets.Button(
        description="Query the Press Release",
        button_style="primary",
        icon="search"
    )

    query_output = widgets.Output()

    def run_press_release_query(_):
        with query_output:
            clear_output(wait=True)
            try:
                result = answer_press_release_question(
                    state=final_state,
                    company=company_widget.value,
                    question=question_widget.value
                )
                print(result["answer"])
                print(f"\nSource: {result['url']}")
            except Exception as error:
                print(f"Error: {error}")

    query_button.on_click(run_press_release_query)

    display(
        widgets.VBox([
            widgets.HTML("<b>Press Release Agent — FY2025 / Guidance 2026</b>"),
            company_widget,
            question_widget,
            query_button,
            query_output
        ])
    )
else:
    print(
        "ipywidgets is not available."
    )

# ============================================================
# PRESENTATION FORMAT FOR AGENTIC RESPONSES
# ============================================================
# Documentary evidence preserves the precision and units
# with which values are expressed in the corporate source.
# ============================================================

final_state.setdefault(
    "response_display_formats",
    {}
)

final_state[
    "response_display_formats"
][
    "press_release_fy2025"
] = {
    "__source_precision__": True
}


# Agentic Financial Intelligence

## Project access and reproducibility

Agentic Financial Intelligence is an AI-powered financial research system designed to integrate quantitative market analysis, corporate financial documentation, and agentic reasoning across 30 Dow Jones Industrial Average companies.

The project is built on a modular Python architecture that supports multidimensional financial analysis, comparative evaluation, and natural-language interaction. It combines financial market data with corporate disclosures to provide a unified framework for investigating company performance, risk characteristics, and financial outlooks.

The complete implementation is maintained in a public GitHub repository. The Python modules constitute the core executable system. Two separate Google Colab notebooks provide access to the interactive Gradio prototype and to the project's technical and methodological development documentation, respectively.

- **Repository:** [Agentic Financial Intelligence — GitHub](https://github.com/Valeria-Raele/agentic-financial-intelligence)
- **Demo Prototype (Google Colab):** [Open the interactive demo](https://colab.research.google.com/drive/1SnWH01vcSzxw_62JpNLrsEQNh0neHs77?usp=sharing)
- **Technical and methodological notebook:** [Agentic Financial Intelligence — Google Colab](https://colab.research.google.com/github/Valeria-Raele/agentic-financial-intelligence/blob/main/notebooks/Agentic_Financial_Intelligence.ipynb)
- **License:** MIT (OSI-approved)

## Live Demo — Demo Prototype

Access **AI Financial Intelligence**, the interactive Gradio interface for multidimensional financial research across 30 Dow Jones Industrial Average companies.

**[Launch Demo Prototype in Google Colab](https://colab.research.google.com/drive/1SnWH01vcSzxw_62JpNLrsEQNh0neHs77?usp=sharing)**

**Demo access instructions**

Open the Demo Prototype notebook in Google Colab. Configure the required API credentials using your own Google Colab Secrets, and grant the notebook access to those secrets. Run the notebook's launch cell using its start button, then allow a few minutes for initialization. Once the Gradio link appears, open it to access the interactive landing page and submit financial research questions.

The application provides a unified interface for exploring quantitative market indicators, corporate financial disclosures, and AI-powered financial analysis through natural-language queries.

## Installation and execution

The system is implemented through six Python modules that separate environment configuration, data acquisition, financial analytics, documentary processing, agentic reasoning, and interactive execution. The Gradio interface is implemented in `gradio_app.py`, which calls `hf_engine.py` to initialize and invoke the underlying computational modules.

The **Demo Prototype** notebook is the streamlined entry point for launching the Gradio interface. The separate **Agentic Financial Intelligence** notebook in `notebooks/` documents the development process and analytical methodology.

### 1. Clone the repository

Clone the public repository and navigate to the project directory:

```bash
git clone https://github.com/Valeria-Raele/agentic-financial-intelligence.git
cd agentic-financial-intelligence
```

### 2. Set up the Python environment

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment.

**Windows:**

```bash
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 3. Configure API credentials

The system integrates external services for financial market data, AI model inference, and optional execution tracing.

Configure the following API credentials in the execution environment, using **Google Colab Secrets** when launching the Demo Prototype:

- `NEBIUS_API_KEY` — access to Nebius-hosted AI models, including NVIDIA open-source models.
- `TWELVE_DATA` — retrieval of financial market data.
- `LANGSMITH_API_KEY` — execution tracing and observability, when enabled.

Credentials must be supplied securely through the configuration mechanism supported by the execution environment. The demo uses the user's own credentials; do not enter API keys directly into the public notebook or repository.

### 4. Run the system

**Interactive Gradio demo:** Open the [Demo Prototype notebook](https://colab.research.google.com/drive/1SnWH01vcSzxw_62JpNLrsEQNh0neHs77?usp=sharing), configure the required secrets, and use its launch button. The notebook prepares the runtime, loads the repository-based application, and starts the Gradio landing page. The interface uses `gradio_app.py` and `hf_engine.py` to invoke the underlying financial analysis workflow.

**Modular command-line execution:** The core implementation is organized in the `modules/` directory, with `run.py` serving as the command-line execution entry point. From the repository root, run:

```bash
python run.py
```

A compatible Python environment, installed dependencies, and valid API credentials are required for independent execution.

### 5. Explore the financial research capabilities

The agentic system supports financial research across multiple analytical dimensions:

- **Quantitative market analysis:** annualized returns, volatility, Sharpe Ratios, Return-to-Risk Ratios, momentum, Pearson correlations, CAPM metrics, trend-following signals, and trading volume.
- **Corporate financial analysis:** FY2025 financial and operating results, management commentary, strategic priorities, and disclosed financial outlooks.
- **Comparative financial evaluation:** analysis across companies, observation periods, risk-return profiles, and corporate financial disclosures.
- **Multidimensional reasoning:** integration of quantitative metrics and documentary evidence to support financial interpretation and comparative assessment.
- **Agentic analytical tasks:** natural-language requests involving comparison, ranking, evaluation, explanation, and synthesis.
- **Conversational memory and contextual retrieval:** persistent tracking of previous questions and answers, enabling the system to retrieve relevant conversation history, maintain context across interactions, and interpret follow-up queries within a continuous financial research dialogue.

## Google Colab Notebooks

The project provides two distinct Google Colab notebooks:

- **Demo Prototype:** [Open the Gradio demo launcher](https://colab.research.google.com/drive/1SnWH01vcSzxw_62JpNLrsEQNh0neHs77?usp=sharing). This is the interactive prototype's entry point and is intended to be listed at the repository root.
- **Agentic Financial Intelligence:** [Open the technical and methodological notebook](https://colab.research.google.com/github/Valeria-Raele/agentic-financial-intelligence/blob/main/notebooks/Agentic_Financial_Intelligence.ipynb). This notebook is located in the repository's `notebooks/` directory and documents the original development workflow, implementation decisions, analytical methods, code explanations, and supporting commentary.

The technical notebook is a complementary reference for examining the system's architecture, financial methodologies, and development process. It is not required to launch the Demo Prototype. For independent execution of the technical notebook, configure its required API credentials through **Google Colab Secrets**, grant access to those secrets, and run the relevant cells in their documented order.

## NVIDIA Nemotron 3 Ultra 550B - Model Integration and Prompt-Engineering Approach

Nemotron 3 Ultra 550B proved to be the most suitable model among those tested, particularly for complex financial reasoning and comparative analysis. The main challenges involved handling complex, multi-step requests, ensuring evidence completeness, and maintaining response consistency.

Particularly, I adopted an advanced prompt-engineering and custom multi-agent orchestration approach, without fine-tuning Nemotron's model weights.

Using LangGraph, I progressively adapted the workflow to Nemotron 3 Ultra 550B through several architectural and prompt-level refinements:

- Structured reasoning and planning (Boxes 40-bis and 41-bis): refined the interpretation of complex financial questions, decomposition of question and composition of answers into atomic analytical requirements, as for requested companies, metrics, observation periods, and sources.
- Tailored the flow for a better understanding of quantitative and documental data, distinguishing retrieved evidence from missing, failed, or non-comparable information.
- Domain-specific few-shot prompting (Preliminary Box 45): developed approved financial analysis examples to guide Nemotron toward substantive comparisons rather than isolated figures or generic summaries.
- Integrated financial synthesis (Box 45): designed detailed instructions for commentary, including comparing corporate performance, quantitative indicators, and management guidance, identifying positive, negative, or mixed signals and explaining convergences and divergences.
- Critical validation and revision (Boxes 46-47): reinforced checks for analytical completeness, consistency with retrieved evidence, unsupported conclusions, and appropriate handling of missing information.
- Reasoning consistency: implemented interpretation to verify consistency in the identification of financial metrics, securities, time periods, and analytical requirements. The development was supported by iterative testing on 32 complex financial questions in English and Italian, using Google Gemini 2.5 Flash as a comparative benchmark to identify opportunities for improving Nemotron's orchestration and analytical output. The objective was not to retrain the model, but to build a specialized reasoning environment around it, combining deterministic financial calculations, tailored prompts, and critical validation to improve the completeness, consistency, and analytical depth of its responses.

## Nebius Token Factory - Development Support and Platform Capabilities

Nebius provides access to a valuable selection of AI models through a relatively intuitive and accessible Token Factory platform. API integration and model configuration are straightforward, making it practical to test different Nemotron models and integrate them into Python and LangGraph workflows.

The dashboard is useful, offering clear and detailed visibility into credit balances, token consumption, and usage costs across different models, which helps monitor experimentation expenses. Overall, Nebius provides a solid and functional environment for developing and testing multi-agent AI applications.

## Tavily - Exploratory Company Research

Tavily was used for exploratory research on the companies in the Dow Jones universe, including an investigation of their industry sectors. The resulting sector-oriented research output is documented in the **Agentic Financial Intelligence** technical and methodological Google Colab notebook, located in the repository's `notebooks/` directory.


## Project Specifications and Conversational Question Flow

### Agentic Financial Intelligence Project

#### Inspiration and Objective

Data analysis can go beyond calculating individual indicators. An in-depth financial assessment may require combining multiple analytical dimensions, including market performance, risk metrics, technical signals, and corporate disclosures. Fundamentally, the objective is to look beyond the numbers, understand the underlying context and heterogeneous factors, interpret their relationships, and identify the different drivers influencing financial performance.

The Agentic Financial Intelligence project was developed to address this challenge through a multi-agent AI system focused on the historical price time series and corporate financial documents of the 30 constituent stocks of the Dow Jones Industrial Average (DJIA).


#### Objective

To develop an AI-powered financial intelligence platform that supports investment research and financial decision-making by integrating quantitative market analytics with qualitative corporate financial information.

The platform enables users to investigate multiple companies, financial indicators, observation periods, and corporate disclosures through natural-language questions, generating structured, comparative, and evidence-based financial assessments.

Its primary objective is to **reduce the complexity of multidimensional financial analysis**, moving beyond isolated metrics toward an integrated understanding of financial performance, risk, corporate fundamentals, and management expectations.

#### Target Users

##### Primary Target — Financial and Investment Professionals

- **Financial Analysts and Equity Research Analysts:** conducting company research, financial performance assessments, peer comparisons, and analysis of corporate disclosures.
- **Investment Analysts and Portfolio Managers:** evaluating investment opportunities, risk-return profiles, market indicators, and the consistency between stock performance and company fundamentals.
- **Investment Strategists and Asset Allocation Professionals:** investigating market trends, comparing securities, and identifying relationships across financial indicators and analytical dimensions.

##### Secondary Target — Financial Research and Advisory Professionals

- **Wealth Management and Investment Advisory Professionals:** supporting investment research, product analysis, and evidence-based investment discussions.
- **Financial Researchers:** exploring relationships between quantitative market data, corporate financial results, and management expectations.
- **Advanced Individual Investors:** conducting structured financial research using natural-language queries without having to manually combine multiple analytical tools and information sources.
  

#### How It Was Built

The project was developed in Python using Google Colab and LangGraph, with NVIDIA Nemotron 3 Ultra 550B, accessed through Nebius Token Factory.

The project supports two distinct analytical workflows: deterministic quantitative calculations and semantic analysis of corporate financial documents. These components are architecturally separated, with calculations performed independently of the processing of qualitative financial disclosures.

#### Quantitative Financial Analysis - Deterministic Calculation Tools

The first workflow establishes a validated quantitative foundation for the Dow Jones stock universe.

Specialized agents process financial market data through deterministic Python/Pandas calculations, organized into the following analytical areas, producing verified and certified results:

- Market & Risk Analytics: Annualized return (CAGR), annualized volatility, Sharpe Ratio, Return-to-Risk Ratio, Pearson correlation, correlation matrices, and identification of stock pairs with correlations above 75%.

- Momentum & Market Analysis: Momentum, Dollar Volume, and comparative stock rankings based on momentum.

- Asset Pricing - CAPM: Beta, annualized Alpha, R-squared, observed annualized return, CAPM expected annual return, and the difference between observed and expected returns.

#### Integration of Corporate Financial Documentation

Results 2025 Press Releases (usually published in March - April 2026) are ingested into the workflow and transformed into a queryable information base containing financial results, performance drivers, business highlights, management guidance, strategic priorities, milestones, and management commentary.

Information retrieval is supported by a structured catalog of financial metrics, synonyms, keywords, and information categories, combined with semantic interpretation of the user's request. When direct lexical matching is insufficient, a semantic fallback based on TF-IDF and cosine similarity helps identify relevant underlying information.

This approach allows the system to retrieve and interpret corporate evidence even when companies operating in different industries use different terminology to describe comparable financial concepts.

As a result, heterogeneous corporate documents become accessible through a unified analytical framework.

#### Multi-Factor Financial Reasoning

NVIDIA Nemotron plays a central role in orchestrating specialized agents and their quantitative and document-based tools, interpreting complex financial requests, supporting response validation, and generating insightful commentary based on multiple sources.

A fundamental architectural principle is the separation between LLM-based reasoning and deterministic financial computation. The model neither performs nor modifies numerical calculations. Instead, it interprets calculated results, compares quantitative and documentary evidence, and develops integrated financial assessments, following an approach similar to that of a human financial analyst.

Furthermore, a single question may involve several companies, different observation periods, multiple quantitative indicators, and information extracted from multiple sources.

To manage this complexity, the system decomposes each request into atomic analytical requirements, identifying the relevant companies or tickers, observation periods, metrics, selection criteria (such as the highest-ranked stock or top five securities), and calculation tools.

Each requirement is assigned to the appropriate analytical component, and the resulting evidence is subsequently integrated into a structured comparative response.

For example, users can ask a quantitative question such as:

"Compare Apple and Microsoft in terms of risk, momentum, and CAPM."

Or formulate a more complex question combining financial statements, stock performance, and management expectations, such as:

"Can you compare IBM's 2025 earnings, its stock performance in 2025 and 2026, and assess whether this evidence is consistent with the growth guidance communicated by management for 2026?"

#### Context Retrieval and Conversational Continuity

Once the quantitative and documentary information has been acquired, the second workflow manages natural-language queries.

The workflow accesses the results stored in final_state and verifies their compatibility with the requested information to determine whether each component can be retrieved from previous computations (REUSE) or requires a new execution (EXECUTE).

This mechanism preserves analytical consistency across successive questions while improving computational efficiency and supporting a more natural, context-aware interaction.

#### Research Reliability and Validation

The project incorporates complementary validation mechanisms throughout the analytical workflow.

Market data undergoes a dual-source certification process, using a primary provider and an independent cross-validation source. Quantitative calculations are performed through deterministic Python/Pandas tools and subjected to consistency checks.

The separation between numerical computation and LLM reasoning ensures that financial indicators remain traceable to their underlying calculations rather than being generated or modified by the language model.

The architecture also includes a configurable fallback model, a three-stage critical response validation mechanism, and controlled revision procedures designed to identify inconsistencies, incomplete interpretations, and unsupported conclusions.

Each calculation retains its analytical identity, allowing the system to associate results with their corresponding signatures, which contain information about sources, tools, securities, observation periods, and metrics.

The broader objective is to establish a modular, transparent, and reliable architecture, in which each component performs a clearly defined responsibility and contributes to a certified, reusable, and queryable body of financial evidence.

#### Development Challenges and Iterative Refinement

A major challenge in developing Agentic Financial Intelligence was interpreting combined requests and producing complete analyses of complex financial questions.

An important part of the development process involved cross-model benchmarking using Google Gemini 2.5 Flash as a comparative reference.

Comparing Gemini's and Nemotron's responses to complex financial questions helped identify differences in analytical interpretation, completeness, and the quality of multi-factor comparative commentary.

Rather than relying on the model's default behavior, these observations informed an iterative refinement process aimed at strengthening Nemotron's ability to interpret complex requests, retrieve relevant evidence, and identify differences across multiple analytical factors.

#### What I Learned

Developing Agentic Financial Intelligence reinforced my belief in the importance of treating financial data with methodological rigor, ensuring that information is properly acquired, cleaned, validated, and interpreted within a broader analytical framework rather than reduced to isolated numerical calculations.

The project also demonstrated the importance of designing workflows around the specific capabilities and limitations of individual language models.

Differences between models extend beyond the accuracy of individual responses. This work highlighted the need to continuously adapt the system to the model's behavior and capabilities, improving its ability to interpret complex requests and operate within an increasingly sophisticated, multidimensional analytical environment.


### REAL EXAMPLE OF THE PROJECT'S CONVERSATIONAL FLOW - 20 Questions and Answers

```text
====================================================================================================

QUESTION >

1. What has Verizon annualized volatility been over the last 2 years?

ANSWER >

Verizon's annualized volatility over the last 2 years (2024-10-26 to 2026-10-26) has been
24.06%.

====================================================================================================

====================================================================================================

QUESTION >

2. Over the same period, what was Verizon's annualized return, and what was its
Return-to-Risk Ratio?

ANSWER >

Over the period from 2024-10-26 to 2026-10-26, Verizon's annualized return was 11.04% and
its Return-to-Risk Ratio (raw) was 0.46.

====================================================================================================

====================================================================================================

QUESTION >

3. Compare Verizon and Cisco over the last 12 months in terms of annual return, annualized
volatility and Sharpe Ratio. Which company has the stronger risk-adjusted performance
according to these metrics?

ANSWER >

Over the last 12 months (2025-10-26 to 2026-10-26), the risk-return metrics for Verizon
(VZ) and Cisco (CSCO) are as follows:

Cisco (CSCO):
- Annual Return: 54.11%
- Annualized Volatility: 35.5%
- Sharpe Ratio: 1.13

Verizon (VZ):
- Annual Return: 22.9%
- Annualized Volatility: 26.69%
- Sharpe Ratio: 0.66

Comparing the two companies, Cisco demonstrates stronger risk-adjusted performance. Its
Sharpe Ratio of 1.13 is substantially higher than Verizon's 0.66, indicating superior
return per unit of risk. While Cisco's annualized volatility is higher (35.5% vs 26.69%),
its much higher annual return (54.11% vs 22.9%) more than compensates for the additional
risk, resulting in a better risk-return profile overall.

====================================================================================================

====================================================================================================

QUESTION >

4. Which pair of Dow Jones stocks has the highest Pearson correlation? Report its
correlation coefficient.

ANSWER >

The pair of Dow Jones stocks with the highest Pearson correlation is GS and JPM, with a
correlation coefficient of 0.8009. This correlation is calculated over the full available
historical dataset.

====================================================================================================

====================================================================================================

QUESTION >

5. Which are the 5 Dow Jones stocks with the highest 6-month momentum? For each stock,
report its momentum, Dollar Volume and position in the ranking.

ANSWER >

The 5 Dow Jones stocks with the highest 6-month momentum are:

1. CRM: Momentum of 41.42%, Average Dollar Volume of $ 1,878,489,355.
2. MRK: Momentum of 34.80%, Average Dollar Volume of $ 1,404,820,399.
3. TRV: Momentum of 31.52%, Average Dollar Volume of $ 518,480,891.
4. MSFT: Momentum of 29.15%, Average Dollar Volume of $ 10,633,352,254.
5. AMGN: Momentum of 28.57%, Average Dollar Volume of $ 1,162,012,801.

Momentum is calculated over a time horizon of 6 months.

====================================================================================================

====================================================================================================

QUESTION >

6. Among these five stocks, which one has the highest Sharpe Ratio over the same 6-month
period? Compare the Sharpe Ratios of all five stocks.

ANSWER >

Over the 6-month period from 2026-04-23 to 2026-10-23, Travelers (TRV) has the highest
Sharpe Ratio among the five stocks at 2.24. The Sharpe Ratios for each stock are:
- TRV: 2.24
- MRK: 1.55
- AMGN: 1.52
- MSFT: 1.00
- CRM: 0.96

TRV's Sharpe Ratio is substantially higher than the others, reflecting its strong
risk-adjusted return with an annualized return of 75.39% and the lowest annualized
volatility of 23.71% in the group. MRK and AMGN show similar risk-adjusted performance
(1.55 and 1.52 respectively), while MSFT and CRM trail with Sharpe Ratios near 1.0.

====================================================================================================

====================================================================================================

QUESTION >

7. Between Goldman Sachs and JPMorgan Chase, which one simultaneously has lower annualized
volatility, a higher Sharpe Ratio and a lower Beta over the last 12 months? Report all
three metrics for both companies and state whether either satisfies all three conditions.

ANSWER >

Over the last 12 months (2025-10-23 to 2026-10-23):

Goldman Sachs (GS):
- Annualized Volatility: 31.93%
- Sharpe Ratio: 0.48
- CAPM Beta (vs ^DJI): 1.818818

JPMorgan Chase (JPM):
- Annualized Volatility: 22.11%
- Sharpe Ratio: 0.49
- CAPM Beta (vs ^DJI): 1.139631

Comparing the three conditions:
- Lower annualized volatility: JPMorgan Chase (22.11%) is lower than Goldman Sachs
(31.93%).
- Higher Sharpe Ratio: JPMorgan Chase (0.49) is higher than Goldman Sachs (0.48).
- Lower Beta: JPMorgan Chase (1.139631) is lower than Goldman Sachs (1.818818).

JPMorgan Chase simultaneously satisfies all three conditions: it has lower annualized
volatility, a higher Sharpe Ratio, and a lower Beta compared to Goldman Sachs over the
observed 12-month period.

====================================================================================================

====================================================================================================

QUESTION >

8. What financial and operating results did Caterpillar report for FY2025? Identify the
main drivers of revenue, profitability and cash flow according to the company's official
financial release.

ANSWER >

Caterpillar reported record full-year sales and revenues of $67.6 billion for FY2025, a 4%
increase from $64.8 billion in 2024. The revenue growth was driven by higher sales volume
of $3.4 billion, primarily from higher equipment sales to end users, partially offset by
unfavorable price realization of $0.8 billion.

Profitability metrics declined year over year: operating profit margin was 16.5% versus
20.2% in 2024, and adjusted operating profit margin was 17.2% versus 20.7%. Full-year
profit per share was $18.81 compared with $22.05 in 2024; adjusted profit per share was
$19.06 versus $21.90.

Enterprise operating cash flow for the full year was $11.7 billion, and the company ended
the fourth quarter with $10.0 billion of enterprise cash. During the year, Caterpillar
deployed $5.2 billion for share repurchases and $2.7 billion for dividends, returning a
total of $7.9 billion to shareholders.

According to CEO Joe Creed, the results reflect the strength of end markets and
disciplined execution, with a record backlog providing strong momentum entering the new
year. The Financial Products segment reported fourth-quarter revenues of $1.095 billion
and segment profit of $262 million, though these are quarterly rather than full-year
figures.

====================================================================================================

====================================================================================================

QUESTION >

9. What did Walmart's management communicate about its 2026 outlook? Distinguish the CEO's
strategic priorities from the CFO's financial expectations, where separately disclosed.

ANSWER >

Walmart's CEO, in the FY2025 press release, communicated strategic priorities for FY2026
centered on sustaining growth momentum, improving operating margins, and strengthening
return on investment while continuing to invest in serving customers and members. The CEO
highlighted current strengths including market share gains, a healthy top line, and
favorable inventory positioning, with momentum driven by low prices, an expanding
assortment, and faster eCommerce delivery. The retrieved FY2025 press release contains
only a CEO section; no CFO commentary covering FY2026 financial expectations or guidance
was disclosed in this document, and no other management communications were retrieved for
this query.

====================================================================================================

====================================================================================================

QUESTION >

10. Compare the FY2025 financial results of Cisco and IBM using their respective official
earnings releases. Examine revenue growth, profitability, business segment performance and
the principal factors identified by management.

ANSWER >

Fiscal Year 2025 Comparative Assessment: Cisco vs. IBM

Revenue Growth
- Cisco reported FY 2025 revenue of $56.7 billion, up 5% year over year. Operating cash
flow rose 30% to $14.2 billion from $10.9 billion in fiscal 2024.
- IBM reported FY 2025 revenue of $67.5 billion, up 8% (6% at constant currency). Software
revenue grew 11% (9% constant currency), Consulting rose 2% (flat at constant currency),
and Infrastructure increased 12% (10% constant currency). Net cash from operating
activities was $13.2 billion; free cash flow reached $14.7 billion.
- Comparison: IBM's top-line growth (8%) outpaced Cisco's (5%), and IBM generated slightly
lower operating cash flow ($13.2B vs $14.2B) but higher free cash flow ($14.7B).

Profitability
- Cisco: GAAP EPS $2.61 (up 3% YoY); Non-GAAP EPS $3.81 (up 2% YoY). Management noted Q4
revenue, gross margin, and operating margin were at the high end of guidance ranges.
- IBM: GAAP gross profit margin 58.2%, up 150 basis points; Non-GAAP operating margin
59.5%, up 170 basis points. The company highlighted double-digit profit and free cash flow
growth for the full year.
- Comparison: IBM disclosed explicit margin expansion (both GAAP and non-GAAP), while
Cisco reported EPS growth percentages without stating margin levels. IBM's margin
improvement was quantified; Cisco's was described qualitatively as at the high end of
guidance.

Business Segment Performance
- Cisco's press release does not break out segment revenues; the primary segment-level
highlight is AI Infrastructure orders from webscale customers exceeding $800 million in
Q4, bringing the FY 2025 total to over $2 billion, more than double the original $1
billion target.
- IBM provided detailed segment results: Software $9.0B (up 14%, 11% constant currency in
Q4; full-year up 11%, 9% constant currency), Consulting $5.3B (up 3%, 1% constant currency
in Q4; full-year up 2%, flat constant currency), Infrastructure $5.1B (up 21%, 17%
constant currency in Q4; full-year up 12%, 10% constant currency).
- Comparison: IBM offers granular, quantified segment performance with constant-currency
metrics; Cisco's segment disclosure is limited to the AI Infrastructure order metric.

Principal Factors Identified by Management
- Cisco (CEO Chuck Robbins, CFO Mark Patterson): Accelerated innovation and solid
execution; AI infrastructure demand from webscale customers far exceeding the $1B target;
strategic investments in innovation to drive durable, profitable growth; Q4 results at or
above the high end of guidance ranges.
- IBM (Chairman/CEO Arvind Krishna, CFO James Kavanaugh): Portfolio mix, integrated value,
and rapid innovation driving higher revenue growth and double-digit profit and free cash
flow growth; generative AI book of business over $12.5B; robust adoption of
next-generation mainframe platform fueling Infrastructure strength; disciplined execution
and productivity focus enabling investment and shareholder returns; confidence in >5%
constant currency revenue growth and ~$1B YoY free cash flow increase for 2026.
- Comparison: Both cite AI-related demand as a key driver (Cisco's webscale AI
infrastructure orders; IBM's generative AI book and mainframe adoption). IBM emphasizes
portfolio mix, productivity, and explicit 2026 quantitative expectations; Cisco emphasizes
innovation investment and guidance-beating execution.

Overall: IBM delivered faster revenue growth (8% vs 5%), quantified margin expansion, and
detailed segment results with constant-currency transparency. Cisco posted strong cash
flow growth (30% operating cash flow) and highlighted outsized AI infrastructure demand
relative to its internal target. Management commentary from both companies points to AI
infrastructure as a pivotal growth vector, with IBM providing more specific
forward-looking quantitative targets.

====================================================================================================

====================================================================================================

QUESTION >

11. Compare Disney's FY2025 financial results with its stock's annualized return and
annualized volatility from the beginning of calendar year 2026 to date. What observations
can be made by examining the 2025 financial results, management's statements about the
2026 outlook, and the stock's observed market performance?

ANSWER >

Disney's FY2025 financial results showed moderate top-line growth and strong segment-level
profitability. Revenue reached $94.4 billion, a 3% increase from $91.4 billion in the
prior year. The Entertainment segment delivered a 19% rise in full-year operating income
to $4.7 billion, while Experiences posted a record $10.0 billion in segment operating
income, up $723 million. Cash provided by operations totaled $19 billion, capital
expenditures were $9 billion, and the board declared a $1.50 per share dividend payable in
two installments. The CEO characterized the year as "great progress" with a strengthened
company, meaningful direct-to-consumer progress, a strong balance sheet, and increasing
returns to shareholders.

Management's FY2026 outlook signals continued growth ambitions. Guidance calls for
double-digit percentage segment operating income growth versus fiscal 2025, weighted to
the second half of the year, a 10% operating margin target for Entertainment DTC SVOD,
double-digit adjusted EPS growth, $19 billion in cash from operations, $9 billion in
capital expenditures, and a doubling of share repurchases to $7 billion. The dividend of
$1.50 per share is maintained. However, the Q4 FY2025 segment operating income declined 5%
to $3.5 billion, and Entertainment Q4 operating income fell $376 million year-over-year
due to theatrical slate comparisons, introducing a near-term cautionary note.

The stock's 2026 year-to-date market performance diverges from the favorable business and
guidance signals. From the beginning of calendar year 2026 to the current date, Disney's
annualized_return_annualized_volatility metric shows an annualized return of -0.42%,
annualized volatility of 27.04%, Return-to-Risk Ratio of -0.02, and Sharpe Ratio of -0.12,
indicating negative risk-adjusted performance over the observed period.

Overall assessment: The business and press-release dimension is POSITIVE, supported by
revenue growth, strong segment operating income expansion, robust cash generation, and
shareholder-return commitments. The management guidance dimension is POSITIVE, with
explicit double-digit growth targets for segment operating income and adjusted EPS, margin
objectives, and increased capital returns, though tempered by the Q4 deceleration
disclosed in the same release. The quantitative market dimension is NEGATIVE, showing a
slightly negative annualized return, elevated volatility, and unfavorable risk-adjusted
ratios. The three dimensions diverge: despite favorable fundamentals and a constructive
outlook, the stock has not reflected that strength in 2026 to date, delivering
flat-to-negative returns with high volatility. The available evidence does not establish a
causal link; it only documents the coexistence of positive business signals and weak
market performance over the observed window.

====================================================================================================

====================================================================================================

QUESTION >

12. Compare Johnson & Johnson, Merck, and UnitedHealth Group using their 12-month
momentum, Sharpe Ratio, and the most recent available management guidance for 2026.
Identify the differences in their quantitative risk-return profiles and reported business
outlooks.

ANSWER >

Here's a comparison of Johnson & Johnson (JNJ), Merck (MRK), and UnitedHealth Group (UNH)
based on their 12-month momentum, Sharpe Ratio, and available management guidance for
2026:

Momentum:
- 12-month Momentum (measured as of 2026-10-31):
 - Merck (MRK): 73.92%
 - Johnson & Johnson (JNJ): 42.83%
 - UnitedHealth Group (UNH): 25.67%

Sharpe Ratio (12M, Risk-Free Rate: 3%, period: 2025-10-23 to 2026-10-23):
- Merck (MRK): Sharpe Ratio 1.73 (Annual Return 70.68%, Annualized Volatility 29.18%)
- Johnson & Johnson (JNJ): Sharpe Ratio 1.48 (Annual Return 39.81%, Annualized Volatility
20.71%)
- UnitedHealth Group (UNH): Sharpe Ratio 0.4 (Annual Return 18.74%, Annualized Volatility
35.89%)

Management Guidance for 2026:
- Johnson & Johnson (JNJ): Adjusted EPS of $11.53 or 6.9% at the midpoint. CEO Joaquin
Duato stated 2025 was a "catapult year" with "accelerated growth driven by medical
innovation" across six key businesses.
- Merck (MRK): Anticipates worldwide sales between $65.5 billion and $67.0 billion.
Expects non-GAAP EPS between $5.00 and $5.15, reflecting a one-time charge of
approximately $3.65 per share for the Cidara acquisition. CEO Robert M. Davis highlighted
portfolio transformation driven by KEYTRUDA, new launches, and Animal Health strength.
- UnitedHealth Group (UNH): Revenue greater than $439.0 billion. Earnings from operations
greater than $24.0 billion. Adjusted earnings greater than $17.75 per share. CEO Stephen
Hemsley noted the company "confronted challenges directly and finished 2025 as a much
stronger company."

Differences in Quantitative Risk-Return Profiles:
- Momentum: Merck shows the strongest 12-month momentum at 73.92%, significantly ahead of
Johnson & Johnson's 42.83% and UnitedHealth's 25.67%. This indicates Merck's stock price
has appreciated most rapidly over the trailing year.
- Risk-Adjusted Returns (Sharpe Ratio): Merck also leads with a Sharpe Ratio of 1.73,
reflecting the highest annualized return (70.68%) despite elevated volatility (29.18%).
Johnson & Johnson follows at 1.48, achieving a strong return (39.81%) with the lowest
volatility (20.71%) of the three. UnitedHealth lags at 0.4, with the lowest return
(18.74%) and highest volatility (35.89%), indicating the least favorable risk-return
trade-off.
- Volatility Profile: UnitedHealth's 35.89% annualized volatility is markedly higher than
both peers, while Johnson & Johnson's 20.71% is the lowest, suggesting different risk
characteristics despite all three being large-cap healthcare names.

Differences in Reported Business Outlooks:
- Johnson & Johnson frames 2026 as continuation of "accelerated growth" from a "catapult
year," emphasizing portfolio breadth across six therapeutic areas and pipeline-driven
innovation. Guidance centers on adjusted EPS growth of 6.9%.
- Merck provides specific revenue and EPS ranges ($65.5–67.0B sales, $5.00–5.15 non-GAAP
EPS), highlighting KEYTRUDA's ongoing strength, new product launches, and Animal Health
performance, while flagging a one-time acquisition-related charge.
- UnitedHealth sets floor targets (revenue >$439B, operating earnings >$24B, adjusted EPS
>$17.75) after a 2025 marked by cyberattack remediation, divestitures, and restructuring.
The outlook emphasizes operational strengthening and value-based care integration at
Optum.

Cross-Company Assessment:
- Merck demonstrates the strongest alignment: highest momentum, best risk-adjusted
returns, and specific quantitative guidance reflecting portfolio transformation.
- Johnson & Johnson shows solid risk-adjusted performance (second-highest Sharpe) with
moderate momentum and guidance emphasizing sustainable innovation-driven growth.
- UnitedHealth exhibits a divergence: weakest quantitative profile (lowest momentum,
lowest Sharpe, highest volatility) but forward guidance setting high absolute earnings
floors after a restructuring year. The stock's risk-return profile has not yet reflected
the operational strengthening management describes.

Overall, the three companies differ materially in how recent market performance,
risk-adjusted returns, and management expectations align. Merck leads across quantitative
dimensions with corresponding specific guidance. Johnson & Johnson balances moderate
momentum with strong risk-adjusted returns and innovation-focused outlook. UnitedHealth
presents a contrast where favorable management expectations (high earnings floors
post-restructuring) coexist with the weakest trailing risk-return profile of the three.

====================================================================================================

====================================================================================================

QUESTION >

13. Compare JPMorgan and Goldman Sachs over the last 12 months in terms of momentum and
Sharpe Ratio. Does the stock with stronger momentum also have the better risk-adjusted
performance?

ANSWER >

Over the last 12 months (2025-10-23 to 2026-10-23), the comparison between JPMorgan (JPM)
and Goldman Sachs (GS) shows the following:

Momentum (12-month formation period, measured at 2026-10-31):
- GS: 13.12%
- JPM: 8.63%
Momentum is calculated over a time horizon of 12 months. GS exhibits stronger momentum.

Sharpe Ratio (same 12-month interval, 2025-10-23 to 2026-10-23):
- GS: 0.48 (Annual Return 19.92%, Annualized Volatility 31.93%)
- JPM: 0.49 (Annual Return 14.91%, Annualized Volatility 22.11%)
JPM has a marginally higher Sharpe Ratio, indicating slightly better risk-adjusted
performance despite lower raw return and lower volatility.

Conclusion: The stock with stronger momentum (GS) does not have the better risk-adjusted
performance; JPM's Sharpe Ratio is slightly higher (0.49 vs 0.48). The divergence arises
because GS's higher return is accompanied by substantially higher volatility, which
reduces its risk-adjusted metric relative to JPM.

====================================================================================================

====================================================================================================

QUESTION >

14. Which of Apple, Microsoft, and Amazon has experienced the largest change in annualized
volatility between the last 3 months and the last 12 months?

ANSWER >

Over the last 3 months (2026-07-23 to 2026-10-23) and the last 12 months (2025-10-23 to
2026-10-23), the Annualized Volatility (%) for each company is:

Apple (AAPL):
- 3M Annualized Volatility (%): 25.05%
- 12M Annualized Volatility (%): 24.10%
- Change (3M minus 12M): +0.95 percentage points

Microsoft (MSFT):
- 3M Annualized Volatility (%): 36.64%
- 12M Annualized Volatility (%): 32.55%
- Change (3M minus 12M): +4.09 percentage points

Amazon (AMZN):
- 3M Annualized Volatility (%): 41.23%
- 12M Annualized Volatility (%): 34.17%
- Change (3M minus 12M): +7.06 percentage points

Amazon has experienced the largest change in annualized volatility between the two
periods, with an increase of 7.06 percentage points, compared to Microsoft's 4.09 and
Apple's 0.95 percentage points.

====================================================================================================

====================================================================================================

QUESTION >

15. Identify the 5 Dow Jones stocks with the highest Sharpe Ratio over the last year and
compare their annualized returns over the same period. Determine whether the stocks with
the highest Sharpe Ratios also have the highest annualized returns and whether the
risk-adjusted performance ranking matches the return ranking.

ANSWER >

Over the 12-month period from 2025-10-23 to 2026-10-23, the Sharpe Ratios and annualized
returns for all 30 Dow Jones stocks are:

| Ticker | Sharpe Ratio | Annualized Return (%) |
|--------|--------------|----------------------|
| TRV | 1.86 | 50.61 |
| MRK | 1.73 | 70.68 |
| CVX | 1.72 | 55.81 |
| JNJ | 1.48 | 39.81 |
| KO | 1.41 | 34.41 |
| AMGN | 1.33 | 52.53 |
| CSCO | 1.13 | 53.51 |
| AAPL | 1.12 | 35.04 |
| V | 0.66 | 19.06 |
| CAT | 0.66 | 34.50 |
| VZ | 0.56 | 19.68 |
| JPM | 0.49 | 14.91 |
| GS | 0.48 | 19.92 |
| UNH | 0.40 | 18.74 |
| NVDA | 0.35 | 17.30 |
| WMT | 0.35 | 12.84 |
| PG | 0.30 | 9.63 |
| AMZN | 0.29 | 13.79 |
| HON | 0.26 | 10.41 |
| MMM | 0.10 | 5.64 |
| MSFT | -0.04 | 1.59 |
| SHW | -0.04 | 1.93 |
| DIS | -0.07 | 0.95 |
| CRM | -0.11 | -2.32 |
| IBM | -0.25 | -9.52 |
| BA | -0.50 | -13.04 |
| AXP | -0.52 | -10.02 |
| HD | -0.74 | -15.45 |
| MCD | -1.15 | -17.82 |
| NKE | -1.68 | -44.22 |

The five stocks with the highest Sharpe Ratios are:
- Travelers (TRV): Sharpe Ratio 1.86, annualized return 50.61%
- Merck (MRK): Sharpe Ratio 1.73, annualized return 70.68%
- Chevron (CVX): Sharpe Ratio 1.72, annualized return 55.81%
- Johnson & Johnson (JNJ): Sharpe Ratio 1.48, annualized return 39.81%
- Coca-Cola (KO): Sharpe Ratio 1.41, annualized return 34.41%

Comparing their annualized returns, the ranking by return is: MRK (70.68%) > CVX (55.81%)
> TRV (50.61%) > JNJ (39.81%) > KO (34.41%). The stock with the highest Sharpe Ratio (TRV)
does not have the highest annualized return; MRK has the highest return but the
second-highest Sharpe Ratio. The risk-adjusted performance ranking (Sharpe Ratio) does not
fully match the return ranking. While KO ranks fifth in both, the top four positions
differ: TRV leads in Sharpe but is third in return, MRK is second in Sharpe but first in
return, CVX is third in Sharpe but second in return, and JNJ is fourth in both. Thus, the
highest Sharpe Ratio stocks do not uniformly correspond to the highest annualized returns,
and the two rankings diverge.

====================================================================================================

====================================================================================================

QUESTION >

16. Calculate the CAPM metrics for Apple and Microsoft over the last 5 years. For each
company, compare its actual annualized return with its CAPM expected return and comment on
the results.

ANSWER >

Over the last 5 years (2021-10-23 to 2026-10-23), the CAPM analysis for Apple (AAPL) and
Microsoft (MSFT) using the Dow Jones Industrial Average (^DJI) as benchmark and a
risk-free rate of 3% yields the following metrics:

Beta:
- Apple (AAPL): 1.1827
- Microsoft (MSFT): 1.0726

Alpha (annual):
- Apple (AAPL): 8.89%
- Microsoft (MSFT): 3.29%

CAPM Expected Annual Return:
- Apple (AAPL): 8.85%
- Microsoft (MSFT): 8.31%

Actual Annualized Return (2021-10-23 to 2026-10-23):
- Apple (AAPL): 19.20%
- Microsoft (MSFT): 12.12%

Comparison:
- Apple's actual annualized return of 19.20% exceeds its CAPM expected return of 8.85% by
10.35 percentage points, indicating significant outperformance relative to the CAPM
prediction. Its positive alpha of 8.89% confirms excess risk-adjusted return. The beta of
1.1827 shows Apple's stock was more volatile than the benchmark.
- Microsoft's actual annualized return of 12.12% exceeds its CAPM expected return of 8.31%
by 3.81 percentage points, also outperforming the CAPM expectation. Its alpha of 3.29% is
positive but lower than Apple's. The beta of 1.0726 indicates Microsoft's stock was also
more volatile than the benchmark, though less so than Apple.

Both companies delivered actual returns well above their CAPM expected returns over the
5-year period, with Apple showing a larger margin of outperformance and higher
risk-adjusted excess return (alpha).

====================================================================================================

====================================================================================================

QUESTION >

17. Compare the Beta and annualized volatility of JPMorgan, Goldman Sachs, and American
Express over the last 3 years. Do the two risk measures provide a consistent picture of
their relative risk?

ANSWER >

Over the last 3 years (2023-10-23 to 2026-10-23), the CAPM Beta and annualized volatility
for JPMorgan (JPM), Goldman Sachs (GS), and American Express (AXP) are as follows:

CAPM Beta (benchmark ^DJI):
- Goldman Sachs (GS): 1.6460
- American Express (AXP): 1.4719
- JPMorgan (JPM): 1.1703

Annualized Volatility:
- Goldman Sachs (GS): 29.63%
- American Express (AXP): 27.19%
- JPMorgan (JPM): 23.10%

Both risk measures rank the three companies in the same order: GS shows the highest risk,
AXP shows intermediate risk, and JPM shows the lowest risk. The two measures provide a
consistent picture of their relative risk over the observed 3-year period.

====================================================================================================

====================================================================================================

QUESTION >

18. Compare Coca-Cola and McDonald's over the last 2 years using annualized return,
volatility, Sharpe Ratio, and Beta. In which dimensions do their risk-return profiles
differ most clearly?

ANSWER >

Over the 2-year period from 2024-10-23 to 2026-10-23, Coca-Cola (KO) and McDonald's (MCD)
show the following quantitative risk-return metrics:

Coca-Cola (KO):
- Annualized Return: 18.89%
- Annualized Volatility: 18.22%
- Sharpe Ratio: 0.79
- CAPM Beta (vs ^DJI): 0.1236

McDonald's (MCD):
- Annualized Return: -9.0%
- Annualized Volatility: 19.19%
- Sharpe Ratio: -0.65
- CAPM Beta (vs ^DJI): 0.3782

The dimensions where their risk-return profiles diverge most clearly are:
- Annualized Return: KO delivered a strong positive return while MCD posted a negative
return, a gap of nearly 28 percentage points.
- Sharpe Ratio: KO's positive ratio (0.79) indicates returns adequately compensated for
risk taken, whereas MCD's negative ratio (-0.65) signals that risk was not rewarded.
- CAPM Beta: MCD's beta (0.38) is roughly three times KO's (0.12), meaning MCD has been
noticeably more sensitive to movements in the Dow Jones Industrial Average benchmark,
though both betas are low in absolute terms.
- Annualized Volatility is similar (18.22% vs 19.19%), so the divergence is not driven by
a large difference in total risk but by the direction and risk-adjusted quality of returns
and by differing market sensitivity.

All requested metrics (annualized return, volatility, Sharpe Ratio, Beta) for both KO and
MCD over the 2-year period have been explicitly compared using the certified evidence.

====================================================================================================

====================================================================================================

QUESTION >

19. What were Procter & Gamble's (PG) main results in FY2025, and what outlook did
management highlight? Compare the statements in the FY2025 earnings release with the
stock's performance since the beginning of calendar year 2026. What conclusions can be
drawn?

ANSWER >

Procter & Gamble's FY2025 results showed a resilient business performance in a challenging
environment. Net sales were $84.3 billion, unchanged versus the prior year, while organic
sales grew 2% excluding foreign exchange and portfolio changes. Diluted net EPS rose 8% to
$6.51, and core EPS increased 4% to $6.83 on a currency-neutral basis. Operating cash flow
reached $17.8 billion, with adjusted free cash flow productivity at 87%. The company
returned over $16 billion to shareholders through $9.9 billion in dividends and $6.5
billion in share repurchases, marking the 69th consecutive year of dividend increases.
These results indicate a positive fundamental signal: profitability improved, cash
generation remained strong, and capital return to shareholders was substantial despite
flat reported revenue.

Management's FY2026 outlook, conveyed in the same press release and attributed to
Chairman, President and CEO Jon Moeller, is positive with specific numerical guidance. The
company expects all-in sales growth of 1-5% (including a 1% benefit from foreign exchange
and acquisitions/divestitures), organic sales growth of flat to up 4% (including a 30-50
basis point headwind from brand and product form discontinuations), and diluted net EPS
growth of 3-9% versus the FY2025 GAAP EPS of $6.51 (including an expected gain from the
Glad joint venture exit of $0.10-$0.13 per share and non-core restructuring charges of
$0.12-$0.25 per share). Moeller emphasized continued organic sales growth, core EPS
growth, and strong adjusted free cash flow productivity, underpinned by the integrated
strategy of portfolio focus, superiority, productivity, constructive disruption, and
organizational agility. This guidance constitutes a positive forward-looking signal,
though it explicitly includes identified headwinds and one-time items.

In 2026, the stock delivered an annualized return of 19.64% with annualized volatility of
21.41%, a return-to-risk ratio of 0.92, and a Sharpe ratio of 0.70. This represents a
positive quantitative signal: the return is solidly positive, volatility is moderate for a
large-cap consumer staples name, and risk-adjusted metrics, while not exceptionally high,
are favorable.

Comparing the three dimensions, the business fundamentals, management guidance, and market
performance are broadly aligned in a positive direction. FY2025 demonstrated earnings
growth and cash strength despite flat top-line revenue; management guided for continued
organic growth and EPS expansion in FY2026 while flagging specific headwinds; and the
stock has appreciated meaningfully in 2026 with reasonable risk-adjusted returns. The
convergence suggests the market has responded favorably to the combination of resilient
2025 execution and a constructive 2026 outlook. The positive stock performance is
consistent with the positive business and guidance signals, though the moderate Sharpe and
return-to-risk ratios indicate the advance has not been exceptionally strong on a
risk-adjusted basis. No material divergence is evident across the three requested
dimensions based on the available evidence.

====================================================================================================

====================================================================================================

QUESTION >

20. Compare Salesforce and Microsoft using their respective FY2025 financial results and
their stock performance over the last 12 months. Examine the annualized return, annualized
volatility, and Sharpe Ratio of both stocks. What conclusions can be drawn from comparing
the companies' financial results with their respective risk-return profiles?

ANSWER >

Over the last 12 months (2025-10-23 to 2026-10-23), Salesforce (CRM) posted an annual
return of -2.32%, annualized volatility of 46.15%, and a Sharpe ratio of -0.11. Microsoft
(MSFT) posted an annual return of 1.59%, annualized volatility of 32.55%, and a Sharpe
ratio of -0.04.

Salesforce's FY25 fundamentals show revenue of $37.9 billion, up 9% year-over-year, with
subscription and support revenue of $35.7 billion, up 10%. GAAP operating margin was 19.0%
and non-GAAP operating margin 33.0%. Operating cash flow was $13.1 billion, up 28%, and
free cash flow was $12.4 billion, up 31%. The company returned $7.8 billion via share
repurchases and $1.5 billion in dividends, totaling $9.3 billion returned to stockholders.
CEO Marc Benioff highlighted strong performance across key metrics and the highest cash
flow in company history, while CFO Amy Weaver noted a capital return program delivering
$21 billion since inception. For FY26, Salesforce initiates revenue guidance of $40.5
billion to $40.9 billion (up 7%-8%), subscription and support revenue growth guidance of
approximately 8.5% year-over-year (approximately 9% in constant currency), GAAP operating
margin guidance of 21.6% and non-GAAP of 34.0%, and operating cash flow growth guidance of
approximately 10%-11% year-over-year.

Microsoft's FY25 fundamentals show revenue of $281.7 billion, up 15%. Operating income was
$128.5 billion, up 17% (up 18% in constant currency). Net income was $101.8 billion, up
16% (up 15% in constant currency). Diluted earnings per share was $13.64, up 16%.
Microsoft returned $9.4 billion to shareholders in the form of dividends and share
repurchases in the fourth quarter of FY25. CFO Amy Hood highlighted Microsoft Cloud
revenue reaching $46.7 billion, up 27% (up 25% in constant currency) year-over-year.

Comparing the two, Microsoft's stock delivered a positive annual return while Salesforce's
was negative, despite both companies exhibiting strong fundamental growth and
profitability. Salesforce's higher volatility (46.15% vs 32.55%) contributed to a more
negative risk-adjusted performance (Sharpe -0.11 vs -0.04). Although Salesforce's
fundamentals robust revenue expansion, margin improvement, and substantial cash
generation are favorable, its stock price did not reflect this strength over the observed
period, suggesting the market may have discounted the shares due to elevated risk or other
factors. Microsoft's more moderate volatility and modest positive return indicate a closer
alignment between its solid fundamentals and market performance, though its Sharpe ratio
remains negative because the return does not exceed the risk-free rate used in the
calculation. Overall, Microsoft shows a better risk-return profile over the last 12
months, while Salesforce demonstrates stronger underlying business results that have not
yet been fully rewarded by its stock performance.

====================================================================================================
```

## Major Code-Level Developments - Original Source Text

Major Code-Level Developments

NEBIUS x NVIDIA GLOBAL AI HACKATHON

Agentic Financial Intelligence

Agentic Financial Intelligence has evolved as a continuous research and development project, initially integrating deterministic, verifiable quantitative financial analytics with the retrieval and semantic analysis of corporate press releases. Its development entered a major phase of architectural advancement on August 26, 2026, coinciding with the Nebius x NVIDIA Global AI Hackathon, representing a natural yet substantial evolution of the existing system around NVIDIA Nemotron.

Since August 26, 2026, the project has undergone a major transformation through the integration of NVIDIA Nemotron 3 Ultra 550B. Although the project already existed, this development phase marked two fundamental advances: the achievement of stable, consistent and reproducible responses over time, replacing previously variable and unpredictable outputs, and the ability to address complex, multidimensional financial questions, integrating quantitative market analysis with qualitative evidence from corporate financial press releases. The model became capable of comparing different analytical dimensions, generating sophisticated, structured, evidence-based financial commentary rather than basic observations.
In fact, the project evolved beyond the accurate retrieval and reporting of quantitative and documentary information into an integrated financial reasoning system capable of addressing complex questions combining market indicators, corporate financial results, and qualitative disclosures. Through extensive refinement of evidence-grounded synthesis, dynamic few-shot prompting, and explicit financial commentary instructions, Nemotron was guided to evaluate positive, negative, and mixed evidence, identify convergences and divergences between quantitative performance and corporate fundamentals, and formulate structured, comparative, and analytically supported conclusions consistent with the analytical approach of a financial analyst.

These core advances were supported by further architectural enhancements designed to consolidate the project's reliability, including efficient data retrieval, atomic requirement decomposition, canonical result reuse, conversational continuity, advanced temporal reasoning, evidence validation and workflow orchestration.


## Code-level development summary

New modules, major redesigns and BOX-level implementation

### 1. Atomic decomposition and canonical result identity

**MAJOR ARCHITECTURAL REDESIGN — BOX 38, 39, 40, 41, 42, 43, 44, 45, 46**

Complex financial questions are decomposed into independently identifiable analytical requirements: Tool × Ticker/Universe × Metric × Time Period.

**BOX 38**

Formalized the distinction between atomic_id and result_signature, separating requirement identity from result identity.

**BOX 39**

Centralized canonical identity construction through build_atomic_id(), build_canonical_result_signature() and build_result_signature_id().

**BOX 40**

Aligned retrieval of previous results with canonical identifiers.

**BOX 41**

Introduced atomic decomposition across companies, metrics, tools and time periods.

**BOX 42**

Propagated atomic_id into execution-plan steps.

**BOX 43**

Aligned result retrieval, execution, compatibility checks and persistence with canonical signatures.

**BOX 44**

Propagated atomic identifiers into normalized evidence.

**BOX 45**

Connected response generation to exact requirements and corresponding evidence.

**BOX 46**

Added atomic-level coverage and numerical consistency checks.

**Technical contribution:** consistent requirement identity across semantic analysis, planning, execution, evidence construction, synthesis and validation.

### 1. Atomic decomposition — code

**REPRESENTATIVE IMPLEMENTATION**

**KEY CODE / REPRESENTATIVE IMPLEMENTATION**

```python
atomic_identity = {
    "tool_name": tool_name,
    "tickers": tickers,
    "metric": metric,
    "time_period": time_period,
}

result_signature = {
    **atomic_identity,
    "result_selection": result_selection,
    "parameters": parameters,
}

atomic_id = build_atomic_id(
    tool_name=tool_name,
    tickers=tickers,
    metric=metric,
    time_period=time_period,
)

result_signature = build_canonical_result_signature(
    tool_name=tool_name,
    tickers=tickers,
    metric=metric,
    time_period=time_period,
    result_selection=result_selection,
    parameters=parameters,
)

signature_id = build_result_signature_id(result_signature)
```

### 2. Intelligent result reuse and conversational continuity

**MAJOR WORKFLOW REDESIGN — BOX 38–43, 49**

A component-level reuse mechanism enables Nemotron to work with previously calculated results rather than repeatedly requesting the same operations.

**BOX 38–39**

Canonical result signatures for matching requested and stored analytical components.

**BOX 40**

Retrieval of compatible historical results and previously identified groups of financial instruments.

**BOX 41**

Semantic decomposition and REUSE versus EXECUTE decisions for individual components.

**BOX 42**

Planning preserves reuse decisions without reopening semantic interpretation.

**BOX 43**

Deterministic compatibility checks; execution only for missing components.

**BOX 49**

Persistence of result ticker groups through extract_answer_ticker_group().

**KEY CODE / REPRESENTATIVE IMPLEMENTATION**

```python
matched_result_id
reuse_output
result_signature
requirement_id
group_is_binding
execution_scope["tickers"]
result_ticker_group
```

**Technical contribution:** structured analytical memory, selective execution, reduced redundant tool calls and consistency across multi-turn reasoning.

### 3. Advanced temporal reasoning

**MAJOR CHANGES — BOX 30, 40, 41, 42, 43**

The temporal interpretation layer supports rolling windows, multiple observation periods and metric-specific intervals within the same question.

**BOX 30, 40**

Recognition and normalization of rolling periods and contextual temporal references.

**BOX 41**

Changed quantitative component identity from metric to (metric, time_period).

**BOX 42**

Normalize_time_periods() preserves structured period objects rather than converting them into strings.

**BOX 42**

Removed inappropriate global start_date/end_date propagation; resolved dates for each period.

**BOX 43**

Aligned execution and result matching with normalized temporal identities.

**KEY CODE / REPRESENTATIVE IMPLEMENTATION**

```python
# Previous component identity
metric

# Updated component identity
(metric, time_period)

# Previous behavior
str(value)

# Updated behavior
copy.deepcopy(value)
```

**Technical contribution:** multi-company, multi-metric and multi-period questions without temporal cross-contamination.

### 4. NEW BOX 40 BIS

**NEW CODE MODULE — DUAL-DOMAIN FINANCIAL QUESTION RECOGNITION**

A dedicated preprocessing module detects questions requiring both quantitative analytics and qualitative evidence from corporate financial documentation.

**40 BIS — NEW**

Introduced DUAL_DOMAIN_ENGLISH_ALIASES to recognize domains and associated tool terminology.

**40 BIS — NEW**

Implemented dual_domain_question_check(question) to identify combined quantitative and documentary requirements.

**40 BIS — NEW**

Introduced tool_request_matrix to track requested tools, metrics and components.

**BOX 41**

Integrated dual-domain recognition into semantic analysis and workflow state.

**BOX 42**

Integrated dual_domain_internal_report() into the Planner context for relevant questions.

**KEY CODE / REPRESENTATIVE IMPLEMENTATION**

```python
DUAL_DOMAIN_ENGLISH_ALIASES

dual_domain_question_check(question)

dual_domain_internal_report()

tool_request_matrix
```

**Technical contribution:** explicit recognition of questions that require both numerical market analysis and financial-document evidence.

### 5. NEW BOX 41 BIS

**NEW CODE MODULE — EVIDENCE COVERAGE AND COMPLETENESS**

A separate validation layer verifies whether quantitative and documentary components requested by the user have actually been retrieved.

**41 BIS — NEW**

Introduced dual_domain_post_validation_check(state).

**41 BIS — NEW**

Compared requested components in tool_request_matrix against selected_evidence.

**41 BIS — NEW**

Added granular requested/retrieved checks by tool, metric, ticker and period.

**BOX 44**

Preserved documentary evidence and source identifiers.

**BOX 45**

Connected evidence coverage to answer generation.

**BOX 46**

Integrated documentary completeness signals into final answer validation.

**KEY CODE / REPRESENTATIVE IMPLEMENTATION**

```python
document_retrieved[ticker] = int(
    document_successfully_retrieved
)

all_documents_retrieved = int(
    all(document_retrieved.values())
)
```

**Technical contribution:** deterministic completeness checks supporting Nemotron with explicit evidence-availability information.

### 5. Evidence coverage — code

**REPRESENTATIVE VALIDATION LOGIC**

**KEY CODE / REPRESENTATIVE IMPLEMENTATION**

```python
check = dual_domain_post_validation_check(state)

validation["document_retrieved"] = (
    check["document_retrieved"]
)

validation["all_documents_retrieved"] = (
    check["all_documents_retrieved"]
)

if check["all_documents_retrieved"] == 0:
    validation["complete_given_available_evidence"] = False
```

### 6. NEW preliminary BOX 45

**ENTIRELY NEW CODE MODULE — DYNAMIC FEW-SHOT PROMPTING**

A new few-shot reference system improves answer consistency, completeness, financial reasoning structure and formatting.

**PRE-45 — NEW**

Introduced BOX45_APPROVED_EXAMPLES with 20 curated financial question-answer examples.

**PRE-45 — NEW**

Implemented select_box45_reference_examples() to select relevant examples based on the current question and execution plan.

**PRE-45 — NEW**

Added conversational context where necessary.

**BOX 45**

Integrated selected examples into the synthesis prompt alongside actual retrieved evidence.

**BOX 46–47**

Reinforced consistency checks and controlled revision behavior.

**KEY CODE / REPRESENTATIVE IMPLEMENTATION**

```python
BOX45_APPROVED_EXAMPLES

select_box45_reference_examples(
    user_question,
    execution_plan=None,
    count=2,
)
```

**Technical contribution:** dynamic, domain-specific in-context guidance for Nemotron; examples guide structure, not financial facts.

### 7. BOX 45 — major reconstruction

**EXTENSIVELY REDESIGNED CORE MODULE**

The synthesis layer was substantially rebuilt to produce complete, comparative financial answers grounded in quantitative results and qualitative corporate disclosures.

**SYSTEM**

ANSWER_SYNTHESIZER_SYSTEM_INSTRUCTION: strengthened instructions for complete, evidence-grounded financial answers.

**PROMPT**

build_answer_synthesis_prompt(): structured question, plan, selected evidence, missing information and few-shot references.

**ATOMIC**

Linked metrics and periods to their retrieved evidence.

**COMPARE**

Explicit handling of compare, rank, evaluate, explain and assess.

**CONTROL**

Prevented the model from independently changing tool-generated filters, rankings or selected ticker groups.

**HYBRID EVIDENCE SYNTHESIS**

Integrated quantitative indicators with corporate financial results, management guidance and press-release information.

**COMMENTARY**

FINAL_INTEGRATED_COMMENTARY_INSTRUCTIONS: required a reasoned final financial assessment grounded in available evidence.

**Technical contribution:** extensive customization of Nemotron for structured, comparative and evidence-grounded financial analysis.

**EVIDENCE PRESERVATION**

Strengthened the treatment of documentary evidence and selected few-shot examples during prompt construction.

### 7. BOX 45 — financial commentary

**MAJOR MODEL-FACING CODE CHANGES**

The commentary instructions guide Nemotron to identify positive, negative and mixed evidence; explain how quantitative and qualitative findings converge or diverge; and formulate a sophisticated, supported financial interpretation.

**BOX 45**

Distinguishes observed quantitative performance from forward-looking corporate statements.

**BOX 45**

Requires explanation of favorable, unfavorable or mixed financial signals rather than a simple list of metrics.

**BOX 45**

Integrates the final comparative conclusion with the specific evidence retrieved for each company.

**PRE-45**

Provides curated examples for answer structure and financial commentary consistency.

**KEY CODE / REPRESENTATIVE IMPLEMENTATION**

```python
ANSWER_SYNTHESIZER_SYSTEM_INSTRUCTION

FINAL_INTEGRATED_COMMENTARY_INSTRUCTIONS

build_answer_synthesis_prompt()

selected_evidence
missing_information
reference_examples
execution_plan
```

**Technical contribution:** grounded reasoning about what the evidence means, including mixed signals and divergences between market data and corporate disclosures.

### 8. Deterministic financial filtering

**MAJOR CHANGES — BOX 41, 42, 43, 44, 45, 46, 47**

Quantitative selection remains deterministic; Nemotron interprets and explains the results without independently recalculating rankings or filters.

**BOX 41**

Recognizes quantitative conditions and requested selections.

**BOX 42**

Binds conditions to source_step_id, source_tool and source_period.

**BOX 43**

Performs deterministic, period-aware filtering and intersections.

**BOX 44**

Propagates condition_filter_result and filtered_tickers as authoritative evidence.

**BOX 45**

Explains filtered results without reselecting instruments.

**BOX 46**

Prevents validation from recalculating filters, rankings and Top-N.

**BOX 47**

Restricts revision from changing deterministic selections.

**KEY CODE / REPRESENTATIVE IMPLEMENTATION**

```python
source_step_id
source_tool
source_period

condition_filter_result
filtered_tickers
```

**Technical contribution:** separation of LLM interpretation from deterministic financial calculation.

### 9. Evidence-grounded validation

**MAJOR STRENGTHENING — BOX 44, 45, 46, 47**

The answer pipeline verifies completeness, numerical consistency and correspondence between the original question and the retrieved evidence.

**BOX 44**

Evidence normalization, source attribution, atomic identifiers and missing-information tracking.

**BOX 45**

Synthesis grounded in relevant analytical and documentary components.

**BOX 46**

Atomic-by-atomic verification of metrics, periods, numerical values and documentary coverage.

**BOX 47**

Controlled revision based on validation findings and existing evidence.

**KEY CODE / REPRESENTATIVE IMPLEMENTATION**

```python
atomic_id
selected_evidence
missing_information

requires_revision
complete_given_available_evidence
```

**Technical contribution:** multi-stage synthesis, validation and revision to reduce incomplete or unsupported answers.

### Submission priorities

**MAJOR DEVELOPMENTS TO EMPHASIZE**

1. BOX 45 — Major synthesis redesign: model-facing financial reasoning and sophisticated commentary.
2. NEW Preliminary BOX 45 — Dynamic few-shot: domain-specific response guidance.
3. NEW BOX 40 BIS — Combined quantitative/documentary question recognition.
4. NEW BOX 41 BIS — Evidence completeness and coverage validation.
5. Atomic decomposition and canonical signatures — requirement identity across the workflow.
6. Intelligent REUSE/EXECUTE — structured result memory and selective execution.
7. Temporal reasoning — correct multi-period financial analysis.
8. Validation and controlled revision — traceability, completeness and reliability.

These developments distinguish the hackathon-era agentic architecture from the pre-existing financial analytics foundation.


## Methodological Formulas

### 1. Semantic Search and Corporate Document Analysis

BOX 36 - NLP, Document Retrieval and Semantic Matching

Objective: Recognize and retrieve relevant financial information from corporate documents, even when companies use different terminology to describe comparable concepts.

#### TF-IDF - Term Frequency-Inverse Document Frequency

```text
TFIDF(t, d) = TF(t, d) * IDF(t)
```

Components: Term Frequency (TF) and Inverse Document Frequency (IDF).

Application: The method assigns weights to terms and expressions in financial documents, giving greater importance to the most distinctive ones. In the project, it is used to numerically represent terms and descriptions of information categories, supporting the recognition of financial concepts even when terminology differs.

#### Cosine Similarity

```text
sim(x, y) = dot(x, y) / (norm_L2(x) * norm_L2(y))
```

Components: Dot product, Euclidean L2 norm and TF-IDF vector representations.

Application: It uses a geometric measure of similarity between vectors to compare the lexical meaning of requests with the available information categories.

In the project, it is used as a semantic fallback when direct matching between keywords and synonyms is insufficient. It thus supports the identification of relevant financial information to retrieve from corporate documents.

The method uses character n-grams of length 3-5 through scikit-learn.

Methodological relationship: TF-IDF constructs vector representations; cosine similarity measures their proximity. They are not two independent methods, but two components of the same matching procedure.

---

### 2. Financial Data Quality, Consistency and Certification

BOX 12, 13, 15, 16 - Data Preparation and Validation

Objective: Ensure that the historical series used for quantitative calculations are sufficiently complete, temporally consistent and verified through independent sources.

#### Data Quality Score

```text
QualityScore = 100 * N_passed_checks / N_total_checks
```

Application: It summarizes the results of quality checks performed on the data, including availability, completeness and consistency of historical series.

#### Cross-source Price Validation

```text
D_t = 100 * abs(P_Yahoo_t - P_Twelve_t) / abs(P_Yahoo_t)
```

Application: It verifies the agreement between prices from Yahoo Finance and Twelve Data, using percentage deviations and tolerance thresholds.

Complementary methods: Checks for missing values and observations lost during temporal alignment. There is no need to report their individual formulas: they are preparatory procedures for dataset certification.

---

### 3. Quantitative Financial Analysis

BOX 14, 30, 31, 33, 34, 35 - Quantitative Financial Analytics

Objective: Process verifiable quantitative indicators to analyze returns, risk, correlations, momentum and the sensitivity of stocks to the market, across different time windows.

#### A. Performance and Risk - BOX 14, 30

##### CAGR - Compound Annual Growth Rate

```text
CAGR = exp(252 * mean_r) - 1
```

Measures the annualized geometric return of a stock. It uses the mean of daily logarithmic returns and is also used in the Return-to-Risk Ratio.

##### Annualized Volatility

```text
sigma_ann = s_r * sqrt(252)
```

Measures the annualized dispersion of logarithmic returns through the sample standard deviation. It is used in risk comparisons and in the Return-to-Risk Ratio.

##### Sharpe Ratio

```text
Sharpe = ((mean_r - rf_daily) / s_r) * sqrt(252)
```

Measures excess return over the risk-free rate per unit of risk. In the notebook, the default annual risk-free rate is 3%, converted into daily logarithmic terms.

##### Return-to-Risk Ratio

```text
RRR = CAGR / sigma_ann
```

Combines CAGR and annualized volatility to assess return relative to overall risk.

---

#### B. Correlation between Stocks - BOX 31

##### Pearson Correlation Coefficient

```text
rho_XY = Cov(X, Y) / (sigma_X * sigma_Y)
```

Measures the linear relationship between the returns of two stocks.

Application: Construction of the correlation matrix for the 30 Dow Jones stocks, identification of the most highly correlated pairs and selection of positive correlations above 75%.

---

#### C. Momentum and Liquidity - BOX 33

##### Cumulative Momentum

```text
M_k = product(i=1 to k) [1 + R_i] - 1
```

Measures cumulative performance over different time windows by compounding monthly returns.

Application: Ranking stocks by Momentum and comparing the relative strength of their performance.

##### Average Dollar Volume

```text
ADV_20 = (1 / 20) * sum(t=1 to 20) [P_t * V_t]
```

Measures the average daily monetary value of trading over 20 sessions.

Application: Indicator of trading activity and complementary ranking criterion in Momentum rankings.

---

#### D. CAPM and Statistical Regression - BOX 34-35

##### Ordinary Least Squares (OLS)

```text
r_i,t = alpha_i + beta_i * r_m,t + epsilon_t
```

Linear regression model used to estimate the relationship between the returns of a stock and those of the market.

##### Beta

```text
beta_i = Cov(r_i, r_m) / Var(r_m)
```

Measures the sensitivity of a stock to market movements. It is estimated through OLS regression.

##### Annualized Alpha

```text
alpha_ann = exp(252 * alpha_daily) - 1
```

Annualizes the daily regression intercept, providing a measure of the return component not explained by the estimated linear relationship with the market.

##### Coefficient of Determination - R Squared

```text
R_squared = 1 - RSS / TSS
```

Measures the explanatory power of the regression, i.e., the proportion of variation in stock returns explained by the model.

##### CAPM Expected Return

```text
E(R_i) = Rf + beta_i * (R_m_ann - Rf)
```

Estimates the expected return of a stock based on systematic risk and the market risk premium.

##### Observed vs Expected Return

```text
Delta_R_i = R_i_ann - E(R_i)
```

Compares the observed annualized return with that expected under the CAPM.

Methodological relationship: OLS regression produces Alpha, Beta and R²; Beta feeds the CAPM expected return, which is subsequently compared with the observed return.

---

### 4. Dynamic Few-Shot Example Selection

Preliminary BOX 45 - Dynamic Few-Shot Selection

Objective: Automatically identify the financial analysis examples most relevant to the current question, to support Nemotron in constructing structured, comparative and consistent responses.

#### Weighted Structural Matching Score

```text
S(q, e) = sum(w(t) for t in intersection(Tq, Te))
          / max(1, sqrt(cardinality(Te)))
```

Weighting:

```text
w(t) = 4  for structural analytical terms
w(t) = 1  for other terms
```

Application: The system compares the terms in the question and execution plan with those in the available examples, assigning greater relevance to financial concepts and analytical structures.

Examples are ranked by score, and the most relevant are integrated into the synthesis prompt of BOX 45.

This mechanism is distinct from cosine similarity: semantic search uses TF-IDF and vector geometry; few-shot selection uses a weighted lexical score, specifically designed for the characteristics of financial questions.

---

### 5. Summary Overview

| Methodological Area | BOX References | Methods |
|---|---|---|
| Semantic Search | BOX 36 | TF-IDF, Cosine Similarity, L2 Vector Normalization |
| Data Quality | BOX 12-16 | Data Quality Score, Cross-source Price Validation, Temporal Alignment |
| Performance and Risk | BOX 14, 30 | CAGR, Annualized Volatility, Sharpe Ratio, Return-to-Risk Ratio |
| Correlation | BOX 31 | Pearson Correlation |
| Momentum and Liquidity | BOX 33 | Cumulative Momentum, Average Dollar Volume |
| Asset Pricing | BOX 34-35 | OLS, Beta, Alpha, R Squared, CAPM Expected Return, Observed vs Expected Return |
| Few-Shot Selection | Preliminary BOX 45 | Weighted Structural Matching Score |

This methodological framework highlights the principal mathematical methods implemented in the project, clarifies their relationships and identifies the specific system functions they support.

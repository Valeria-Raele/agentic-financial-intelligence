import base64
import html
from pathlib import Path
import streamlit as st
import hmac

st.set_page_config(
    page_title="AI Financial Intelligence | AI-Powered Financial Research",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Password gate: store ACCESS_PASSWORD in Streamlit Secrets, never in GitHub.
def check_password() -> bool:
    if st.session_state.get("authenticated", False):
        return True

    st.title("AI Financial Intelligence")
    st.subheader("Private Research Access")
    entered_password = st.text_input("Access password", type="password", key="access_password")
    if st.button("Access Research System"):
        try:
            expected_password = st.secrets["ACCESS_PASSWORD"]
        except (KeyError, FileNotFoundError):
            st.error("Access is not configured. Set ACCESS_PASSWORD in Streamlit Secrets.")
            return False
        if hmac.compare_digest(entered_password, str(expected_password)):
            st.session_state["authenticated"] = True
            st.rerun()
        else:
            st.error("Invalid password")
    return False


if not check_password():
    st.stop()


BASE = Path(__file__).resolve().parent
ASSETS = BASE / "assets"

def image_data(name: str) -> str:
    path = ASSETS / name
    if not path.exists():
        return ""
    return "data:image/png;base64," + base64.b64encode(path.read_bytes()).decode("ascii")

def picture(name: str, class_name: str = "") -> str:
    uri = image_data(name)
    return f'<img class="visual {class_name}" src="{uri}" alt="" />' if uri else ""

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@400;500;600&display=swap');

:root { --navy:#031B35; --cream:#F3F0E9; --gold:#D5B46D; --muted:#BAC6D2; }
html, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
    background:var(--navy) !important; color:var(--cream) !important;
}
header[data-testid="stHeader"] { background:transparent !important; }
[data-testid="stToolbar"], [data-testid="stDecoration"], #MainMenu, footer { visibility:hidden; }
section[data-testid="stSidebar"] { display:none; }
.block-container {
    max-width:1160px !important;
    padding:1.8rem 3.3rem 5rem !important;
}
html { scroll-behavior:smooth; }
.a-page, .a-page * { box-sizing:border-box; }
.a-page { font-family:'DM Sans',sans-serif; color:var(--cream); }
.a-page p { color:var(--muted); font-size:clamp(14px,1.4vw,17px); line-height:1.85; font-weight:400; }
.a-page h1,.a-page h2 {
    font-family:'Playfair Display',Georgia,serif;
    color:var(--cream); font-weight:400; letter-spacing:-.035em;
    line-height:1.12; margin:0 0 25px;
}
.a-page h1 { font-size:clamp(49px,6.6vw,89px); }
.a-page h2 { font-size:clamp(41px,5.1vw,70px); }
.a-page .gold { color:var(--gold); }
.a-page .eyebrow { color:var(--gold); font-size:11px; font-weight:700; letter-spacing:.19em; text-transform:uppercase; margin:0 0 24px; }
.a-page .brand { font-family:'Playfair Display',Georgia,serif; font-size:26px; margin-bottom:62px; }
.a-page .brand span { color:var(--gold); }
.a-page .hero, .a-page .section-grid {
    display:grid; grid-template-columns:1fr 1fr; gap:30px; align-items:center;
}
.a-page .hero { min-height:570px; position:relative; }
.a-page .hero-copy { position:relative; z-index:2; }
.a-page .hero { grid-template-columns:1fr 1fr; overflow:visible; }
.a-page .hero h1 { font-size:clamp(49px,6.6vw,89px); max-width:none; overflow:visible; }
.a-page .hero h1 .no-break { display:block; width:max-content; max-width:none; white-space:nowrap; font-size:inherit; position:relative; z-index:3; }
.a-page .hero-copy p { max-width:520px; }
.a-page .visual { width:100%; height:auto; object-fit:contain; display:block; }
.a-page .hero-image { margin-left:-8%; width:118%; opacity:.93; transform:translateY(-90px); }
.a-page .visual-right { width:112%; margin-left:-4%; }
.a-page .visual-left { width:112%; margin-left:-8%; }
.a-page .section { border-top:1px solid rgba(197,212,227,.25); padding:56px 0 65px; }
.a-page .section-index { font-size:12px; color:var(--gold); letter-spacing:.12em; margin-bottom:27px; }
.a-page .section-grid { min-height:275px; }
.a-page .section-copy { max-width:550px; }
.a-page .section-copy p { margin:0; }
.a-page .strip { color:var(--gold); font-size:11px; letter-spacing:.15em; text-transform:uppercase; font-weight:700; line-height:2; margin-top:28px; }
.a-page .company-list { color:#C7D1DB; font-size:13px; line-height:2.15; margin-top:24px; }
.a-page .hero-strip { margin:42px 0 40px; }
.a-page .research-copy { padding-bottom:12px; }
.a-page .research-shell { border:1px solid rgba(213,180,109,.52); background:rgba(10,34,60,.42); border-radius:5px; padding:24px; }
.a-page .research-heading { font-family:'Playfair Display',Georgia,serif; color:var(--cream); font-size:23px; margin-bottom:15px; }
.a-page .example { font-size:12px; color:var(--muted); line-height:1.6; margin-top:13px; }
[data-testid="stTextArea"] textarea {
    background:#0B2A48 !important; color:#F3F0E9 !important;
    border:1px solid rgba(213,180,109,.48) !important; border-radius:3px !important;
    font-family:'DM Sans',sans-serif !important; font-size:15px !important;
}
[data-testid="stTextArea"] textarea::placeholder { color:#AABAC9 !important; }
[data-testid="stTextArea"] label { color:var(--cream) !important; }
div.stButton > button[kind="primary"] {
    background:var(--gold) !important; color:var(--navy) !important;
    border:none !important; border-radius:3px !important; font-weight:700 !important;
}
.a-page .foot { color:#7E94AA; font-size:12px; padding:30px 0; }
@media(max-width:800px) {
    .block-container { padding:1.3rem 1.15rem 4rem !important; }
    .a-page .brand { margin-bottom:35px; }
    .a-page .hero,.a-page .section-grid { grid-template-columns:1fr; gap:10px; }
    .a-page .hero { min-height:0; }
    .a-page .hero h1 { font-size:clamp(37px,8vw,58px); max-width:100%; }
    .a-page .hero h1 .no-break { font-size:inherit; max-width:100%; white-space:normal; width:auto; }
    .a-page .hero-image { margin:0; width:100%; transform:none; }
    .a-page .section { padding:35px 0 43px; }
    .a-page .section-grid .image-col { order:2; }
    .a-page .section-grid .section-copy { order:1; }
    .a-page h1 { font-size:clamp(44px,10vw,68px); }
    .a-page h2 { font-size:clamp(38px,8vw,55px); }
    .a-page .hero-strip { margin:24px 0 32px; }
}

/* Example questions: readable controls in both idle and hover states */
[data-testid="stExpander"] {
    background:#08233F !important;
    border:1px solid rgba(213,180,109,.48) !important;
    border-radius:7px !important;
    overflow:hidden;
}
[data-testid="stExpander"] details > summary,
[data-testid="stExpander"] [data-testid="stExpanderToggleIcon"] {
    background:#173653 !important;
    color:#F3F0E9 !important;
}
[data-testid="stExpander"] details > summary:hover {
    background:#234866 !important;
}
[data-testid="stExpander"] details > summary p,
[data-testid="stExpander"] details > summary span,
[data-testid="stExpander"] details > summary svg {
    color:#F3F0E9 !important;
    fill:currentColor;
}
[data-testid="stExpander"] [data-testid="stCaptionContainer"] p {
    color:#C8D5E2 !important;
}
[data-testid="stExpander"] [data-testid="stRadio"] label,
[data-testid="stExpander"] [data-testid="stRadio"] label p,
[data-testid="stExpander"] [data-testid="stRadio"] [role="radiogroup"] p,
[data-testid="stExpander"] [data-testid="stRadio"] > label p {
    color:#F3F0E9 !important;
    opacity:1 !important;
}
[data-testid="stExpander"] [data-testid="stRadio"] [role="radiogroup"] label {
    color:#F3F0E9 !important;
}
[data-testid="stExpander"] [data-testid="stVerticalBlockBorderWrapper"] {
    border-color:rgba(169,192,211,.28) !important;
}
[data-testid="stExpander"] div.stButton > button,
[data-testid="stExpander"] div.stButton > button[kind="secondary"] {
    background:#D5B46D !important;
    color:#031B35 !important;
    border:1px solid #D5B46D !important;
    border-radius:5px !important;
    font-weight:700 !important;
    opacity:1 !important;
}
[data-testid="stExpander"] div.stButton > button p,
[data-testid="stExpander"] div.stButton > button span {
    color:#031B35 !important;
    opacity:1 !important;
}
[data-testid="stExpander"] div.stButton > button:hover {
    background:#E6C987 !important;
    border-color:#E6C987 !important;
}
[data-testid="stExpander"] div.stButton > button:focus-visible {
    outline:2px solid #F3F0E9 !important;
    outline-offset:2px;
}


/* Research example library: dark, high-contrast, always-readable */
.research-divider { border-top:1px solid rgba(197,212,227,.25); margin:24px 0 20px; }
.question-meta { color:#D5B46D; font-size:11px; font-weight:700; letter-spacing:.10em; margin:0 0 10px; }
.question-body { color:#F3F0E9; font-size:14px; line-height:1.65; }
[data-testid="stExpander"] { background:#08233F !important; border:1px solid #36516B !important; border-radius:7px !important; overflow:hidden; }
[data-testid="stExpander"] details > summary { background:#173653 !important; color:#F3F0E9 !important; }
[data-testid="stExpander"] details > summary:hover { background:#234866 !important; }
[data-testid="stExpander"] details > summary *,
[data-testid="stExpander"] details > summary p,
[data-testid="stExpander"] details > summary span { color:#F3F0E9 !important; }
[data-testid="stExpander"] [data-testid="stCaptionContainer"] p { color:#C8D5E2 !important; }
[data-testid="stExpander"] [data-testid="stRadio"] label,
[data-testid="stExpander"] [data-testid="stRadio"] label p,
[data-testid="stExpander"] [data-testid="stRadio"] [role="radiogroup"] label,
[data-testid="stExpander"] [data-testid="stRadio"] [role="radiogroup"] p { color:#F3F0E9 !important; opacity:1 !important; }
[data-testid="stExpander"] [data-testid="stVerticalBlockBorderWrapper"] { border-color:rgba(169,192,211,.28) !important; background:#06213C !important; }
[data-testid="stExpander"] div.stButton > button,
[data-testid="stExpander"] div.stButton > button[kind="secondary"] { background:#D5B46D !important; color:#031B35 !important; border:1px solid #D5B46D !important; border-radius:5px !important; font-weight:700 !important; opacity:1 !important; }
[data-testid="stExpander"] div.stButton > button *,
[data-testid="stExpander"] div.stButton > button p { color:#031B35 !important; opacity:1 !important; }
[data-testid="stExpander"] div.stButton > button:hover { background:#E6C987 !important; border-color:#E6C987 !important; }


/* Natural marker strokes: readable on navy, without rectangular backgrounds. */
.a-page .marker-lead {
    display: inline-block;
    position: relative;
    isolation: isolate;
    color: #031B35;
    font-weight: 700;
    font-size: 17px;
    letter-spacing: .015em;
    line-height: 1.5;
    margin: 4px 0 8px;
}

.a-page .marker-lead::before {
    content: "";
    position: absolute;
    z-index: -1;
    left: -.12em;
    right: -.12em;
    top: 8%;
    bottom: 5%;
    background: #F9E76E;
    opacity: 1;
    transform: rotate(-0.3deg);
    border-radius: 3px 5px 4px 3px;
    clip-path: polygon(1% 7%, 99% 2%, 100% 90%, 2% 100%, 0 85%);
}
.a-page .memory-description { max-width:800px; margin:0 0 18px; font-size:15px; line-height:1.7; color:#C9D5E1; }
.question-body .marker-inline { color:#031B35; font-weight:700; padding:0 .07em; position:relative; isolation:isolate; white-space:normal; }
.question-body .marker-inline::before {
    content:""; position:absolute; z-index:-1;
    left:-.07em; right:-.08em; top:13%; bottom:6%;
    background:linear-gradient(176deg,#F9E76E 3%,#F5DF57 72%,#F8E76D 96%);
    clip-path:polygon(0 13%,97% 0,100% 20%,99% 88%,3% 100%,0 83%);
    transform:rotate(-.5deg);
}

</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="a-page">
  <div class="brand">AI Financial <span>Intelligence</span></div>
  <section class="hero">
    <div class="hero-copy">
      <div class="eyebrow">AI-Powered Financial Research</div>
      <h1>From Market<br>Data<br><span class="gold">to Financial<br><span class="no-break">Understanding.</span></span></h1>
      <p>An AI research system connecting quantitative analysis, corporate intelligence and management perspectives to deliver deeper financial understanding.</p>
    </div>
    <div class="image-col">{picture('hero_fade.png', 'hero-image')}</div>
  </section>
  <div class="strip hero-strip">Quantitative Analysis &nbsp; • &nbsp; Corporate Intelligence &nbsp; • &nbsp; Integrated Research</div>

  <section class="section">
    <div class="section-index">01</div>
    <div class="section-grid">
      <div class="section-copy">
        <div class="eyebrow">A Single Tool Connects You to the Real World</div>
        <h2>Connect <span class="gold">the Evidence.</span></h2>
        <p>A broader perspective emerges when market data meets corporate evidence. Compare companies and time periods, connect risk and performance with reported results, and interpret management outlook in one research workflow.</p>
      </div>
      <div class="image-col">{picture('integrated_fade.png', 'visual-right')}</div>
    </div>
    <div class="strip">Market Data &nbsp; + &nbsp; Corporate Disclosures &nbsp; = &nbsp; Integrated Insight</div>
  </section>

  <section class="section">
    <div class="section-index">02</div>
    <div class="section-grid">
      <div class="image-col">{picture('universe_fade.png', 'visual-left')}</div>
      <div class="section-copy">
        <div class="eyebrow">The Universe</div>
        <h2>30 Dow Jones Companies.<br><span class="gold">Multiple Perspectives.</span></h2>
        <p>The 30 constituents of the Dow Jones Industrial Average, spanning industries, business models and market dynamics.</p>
      </div>
    </div>
    <div class="company-list">3M · Amazon · American Express · Amgen · Apple · Boeing · Caterpillar · Chevron · Cisco · Coca-Cola · Disney · Goldman Sachs · Home Depot · Honeywell · IBM · Johnson &amp; Johnson · JPMorgan Chase · McDonald’s · Merck · Microsoft · Nike · NVIDIA · Procter &amp; Gamble · Salesforce · Sherwin-Williams · Travelers · UnitedHealth · Verizon · Visa · Walmart</div>
  </section>

  <section class="section">
    <div class="section-index">03</div>
    <div class="section-grid">
      <div class="section-copy">
        <div class="eyebrow">Quantitative Intelligence</div>
        <h2>Measure Performance.<br><span class="gold">Understand Risk.</span></h2>
        <p>Evaluate price behavior and risk-adjusted performance across companies and observation periods.</p>
      </div>
      <div class="image-col">{picture('quant_fade.png', 'visual-right')}</div>
    </div>
    <div class="strip">Annualized Return &nbsp; • &nbsp; Volatility &nbsp; • &nbsp; Sharpe Ratio &nbsp; • &nbsp; Momentum &nbsp; • &nbsp; Correlations &nbsp; • &nbsp; CAPM &nbsp; • &nbsp; Trading Volume</div>
  </section>

  <section class="section">
    <div class="section-index">04</div>
    <div class="section-grid">
      <div class="image-col">{picture('corporate_fade.png', 'visual-left')}</div>
      <div class="section-copy">
        <div class="eyebrow">Corporate Intelligence</div>
        <h2>Beyond <span class="gold">the Numbers.</span></h2>
        <p>Financial results, FY2025 corporate releases, management communications, strategic priorities and outlook: the evidence behind the market figures.</p>
      </div>
    </div>
  </section>
  <section class="section" style="padding-bottom:18px">
    <div class="section-index">05</div>
    <div class="section-grid">
      <div class="section-copy research-copy">
        <div class="eyebrow">Live Research</div>
        <h2>Your Question.<br><span class="gold">A Deeper Perspective.</span></h2>
        <p>Explore the Dow Jones 30 through quantitative metrics, company disclosures, comparisons and integrated financial questions.</p>
      </div>
      <div class="section-copy">
        <div class="research-shell">
          <div class="research-heading">Ask the Research System</div>
          <div class="example">Enter your financial research question below.</div>
        </div>
      </div>
    </div>
  </section>
</div>
""", unsafe_allow_html=True)

# Example-question library: source questions only (no benchmark answers).
EXAMPLE_QUESTIONS = [
    (1, 'Quantitative Analysis', 'What has CompanyA annualized volatility been over the last 2 years?'),
    (2, 'Quantitative Analysis', "Over the same period, what was CompanyA's annualized return, and what was its Return-to-Risk Ratio?"),
    (3, 'Quantitative Analysis', 'Compare CompanyA and CompanyB over the last 12 months in terms of annual return, annualized volatility and Sharpe Ratio. Which company has the stronger risk-adjusted performance according to these metrics?'),
    (4, 'Quantitative Analysis', 'Which pair of Dow Jones stocks has the highest Pearson correlation? Report its correlation coefficient.'),
    (5, 'Quantitative Analysis', 'Which are the 5 Dow Jones stocks with the highest 6-month momentum? For each stock, report its momentum, Dollar Volume and position in the ranking.'),
    (6, 'Quantitative Analysis', 'Among these five stocks, which one has the highest Sharpe Ratio over the same 6-month period? Compare the Sharpe Ratios of all five stocks.'),
    (7, 'Quantitative Analysis', 'Between CompanyA and CompanyB, which one simultaneously has lower annualized volatility, a higher Sharpe Ratio and a lower Beta over the last 12 months? Report all three metrics for both companies and state whether either satisfies all three conditions.'),
    (8, 'Corporate Intelligence', "What financial and operating results did CompanyA report for FY2025? Identify the main drivers of revenue, profitability and cash flow according to the company's official financial release."),
    (9, 'Corporate Intelligence', "What did CompanyA's management communicate about its 2026 outlook? Distinguish the CEO's strategic priorities from the CFO's financial expectations, where separately disclosed."),
    (10, 'Corporate Intelligence', 'Compare the FY2025 financial results of CompanyA and CompanyB using their respective official earnings releases. Examine revenue growth, profitability, business segment performance and the principal factors identified by management.'),
    (11, 'Integrated Financial Research', "Compare CompanyA's FY2025 financial results with its stock's annualized return and annualized volatility from the beginning of calendar year 2026 to date. What observations can be made by examining the 2025 financial results, management's statements about the 2026 outlook, and the stock's observed market performance?"),
    (12, 'Integrated Financial Research', 'Compare CompanyA, CompanyB, and CompanyC using their 12-month momentum, Sharpe Ratio, and the most recent available management guidance for 2026. Identify the differences in their quantitative risk-return profiles and reported business outlooks.'),
    (13, 'Quantitative Analysis', 'Compare CompanyA and CompanyB over the last 12 months in terms of momentum and Sharpe Ratio. Does the stock with stronger momentum also have the better risk-adjusted performance?'),
    (14, 'Quantitative Analysis', 'Which of CompanyA, CompanyB, and CompanyC has experienced the largest change in annualized volatility between the last 3 months and the last 12 months?'),
    (15, 'Quantitative Analysis', 'Identify the 5 Dow Jones stocks with the highest Sharpe Ratio over the last year and compare their annualized returns over the same period. Determine whether the stocks with the highest Sharpe Ratios also have the highest annualized returns and whether the risk-adjusted performance ranking matches the return ranking.'),
    (16, 'Quantitative Analysis', 'Calculate the CAPM metrics for CompanyA and CompanyB over the last 5 years. For each company, compare its actual annualized return with its CAPM expected return and comment on the results.'),
    (17, 'Quantitative Analysis', 'Compare the Beta and annualized volatility of CompanyA, CompanyB, and CompanyC over the last 3 years. Do the two risk measures provide a consistent picture of their relative risk?'),
    (18, 'Quantitative Analysis', 'Compare CompanyA and CompanyB over the last 2 years using annualized return, volatility, Sharpe Ratio, and Beta. In which dimensions do their risk-return profiles differ most clearly?'),
    (19, 'Integrated Financial Research', "What were CompanyA's  main results in FY2025, and what outlook did management highlight? Compare the statements in the FY2025 earnings release with the stock's performance since the beginning of calendar year 2026. What conclusions can be drawn?"),
    (20, 'Integrated Financial Research', "Compare CompanyA and CompanyB using their respective FY2025 financial results and their stock performance over the last 12 months. Examine the annualized return, annualized volatility, and Sharpe Ratio of both stocks. What conclusions can be drawn from comparing the companies' financial results with their respective risk-return profiles?"),
]

st.markdown("""
<div class="a-page">
  <div class="marker-lead">Ask. Explore. Follow up.</div>
  <p class="memory-description">The system remembers the context of your conversation! Use it to ask follow-up questions, refine your analysis, and explore new financial dimensions without repeating previous information.</p>
</div>
""", unsafe_allow_html=True)

def select_example(question_text):
    st.session_state["research_question"] = question_text

question = st.text_area(
    "Financial research question",
    placeholder="Enter your financial research question…",
    height=125,
    key="research_question",
)

# The research engine is loaded only after authentication and on the first query.
@st.cache_resource(show_spinner=False)
def load_research_engine():
    from streamlit_engine import initialize_engine
    return initialize_engine(st.secrets)

if "research_turns" not in st.session_state:
    st.session_state["research_turns"] = []

if st.button("Analyze", type="primary"):
    current_question = st.session_state.get("research_question", "").strip()
    if not current_question:
        st.warning("Please enter a financial research question.")
    else:
        try:
            with st.spinner("Analyzing financial evidence…"):
                engine = load_research_engine()
                from streamlit_engine import ask
                current_state = st.session_state.get("agentic_state")
                if current_state is None:
                    import copy
                    current_state = copy.deepcopy(engine["final_state"])
                answer, updated_state = ask(engine, current_question, current_state)
                st.session_state["agentic_state"] = updated_state
                st.session_state["research_turns"].append((current_question, answer))
        except Exception as exc:
            st.error(f"Research engine error: {exc}")

if st.session_state["research_turns"]:
    st.markdown("### Research Answers")
    with st.container(height=460, border=True):
        for i, (asked, answered) in enumerate(st.session_state["research_turns"], 1):
            st.markdown(f"**Question {i}:** {asked}")
            st.markdown(answered)
            st.divider()

st.markdown('<div class="research-divider"></div>', unsafe_allow_html=True)
with st.expander("Explore example questions · 20 research ideas", expanded=False):
    st.caption("Choose a question to insert it into the research field. You can edit it before analyzing.")
    category = st.radio(
        "Research dimension",
        ["All", "Quantitative Analysis", "Corporate Intelligence", "Integrated Financial Research"],
        horizontal=True,
        key="example_category",
    )
    visible = [item for item in EXAMPLE_QUESTIONS if category == "All" or item[1] == category]
    for number, dimension, sample in visible:
        with st.container(border=True):
            left, right = st.columns([8, 1], vertical_alignment="center", gap="small")
            with left:
                st.markdown(
                    f"<div class='question-meta'>{number:02d} · {html.escape(dimension.upper())}</div>",
                    unsafe_allow_html=True,
                )
                # Highlight only the two contextual references, leaving question wording unchanged.
                rendered = html.escape(sample)
                if number == 2:
                    rendered = rendered.replace("Over the same period", '<span class="marker-inline">Over the same period</span>', 1)
                elif number == 6:
                    rendered = rendered.replace("Among these five stocks", '<span class="marker-inline">Among these five stocks</span>', 1)
                st.markdown(f"<div class='question-body'>{rendered}</div>", unsafe_allow_html=True)
            with right:
                st.button(
                    "Use",
                    key=f"example_use_{number}",
                    on_click=select_example,
                    args=(sample,),
                    use_container_width=True,
                )

st.markdown('<div class="a-page" style="margin-top:32px"><p style="color:#8B9AAA;font-size:11px;line-height:1.65;margin:0">Research Processing Time: Due to the highly sophisticated and structured nature of the financial analysis, the system requires approximately 10–20 minutes to generate a response. Please allow this time for the analysis to complete.</p></div>', unsafe_allow_html=True)

st.markdown('<div class="a-page"><div class="foot">AI Financial Intelligence · Powered by NVIDIA Nemotron and Nebius</div></div>', unsafe_allow_html=True)

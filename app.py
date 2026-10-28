import base64
from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="Analysta Intelligence | AI-Powered Financial Research",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="collapsed",
)

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
.a-page .hero h1 { max-width:740px; }
.a-page .hero-copy p { max-width:520px; }
.a-page .visual { width:100%; height:auto; object-fit:contain; display:block; }
.a-page .hero-image { margin-left:-8%; width:118%; opacity:.93; }
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
    .a-page .hero-image { margin:0; width:100%; }
    .a-page .section { padding:35px 0 43px; }
    .a-page .section-grid .image-col { order:2; }
    .a-page .section-grid .section-copy { order:1; }
    .a-page h1 { font-size:clamp(44px,10vw,68px); }
    .a-page h2 { font-size:clamp(38px,8vw,55px); }
    .a-page .hero-strip { margin:24px 0 32px; }
}
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="a-page">
  <div class="brand">Analysta <span>Intelligence</span></div>
  <section class="hero">
    <div class="hero-copy">
      <div class="eyebrow">AI-Powered Financial Research</div>
      <h1>From Market Data<br><span class="gold">to Financial Understanding.</span></h1>
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
    <div class="strip">Annualized Return &nbsp; • &nbsp; Volatility &nbsp; • &nbsp; Sharpe Ratio &nbsp; • &nbsp; Momentum &nbsp; • &nbsp; Correlations &nbsp; • &nbsp; CAPM &nbsp; • &nbsp; Trend Following &nbsp; • &nbsp; Trading Volume</div>
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

# The input remains a native Streamlit widget, ready for FastAPI integration.
question = st.text_area(
    "Financial research question",
    placeholder="Enter your financial research question…",
    height=125,
    key="research_question",
)
st.caption("Example: Compare a company’s risk-adjusted performance and FY2025 outlook.")
if st.button("Analyze", type="primary"):
    if not question.strip():
        st.warning("Please enter a financial research question.")
    else:
        st.info("The landing page is ready. The live agentic research system will be connected to FastAPI in the next phase.")

st.markdown('<div class="a-page"><div class="foot">Analysta Intelligence · Powered by NVIDIA Nemotron and Nebius</div></div>', unsafe_allow_html=True)


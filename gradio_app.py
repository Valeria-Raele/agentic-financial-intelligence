"""Gradio landing page for Agentic Financial Intelligence."""
import base64
import copy
import html
import logging
import os
import threading
from functools import partial
from pathlib import Path
import gradio as gr

BASE = Path(__file__).resolve().parent
ASSETS = BASE / "assets"
ENGINE_LOCK = threading.RLock()
_engine = None

def picture(name, class_name=""):
    path = ASSETS / name
    if not path.is_file():
        return ""
    uri = "data:image/png;base64," + base64.b64encode(path.read_bytes()).decode("ascii")
    return f'<img class="visual {class_name}" src="{uri}" alt="" />'

def initialize_engine_once():
    global _engine
    with ENGINE_LOCK:
        if _engine is None:
            from hf_engine import initialize_engine
            _engine = initialize_engine(os.environ)
        return _engine

def run_question(question, current_state, turns):
    question = (question or "").strip()
    turns = list(turns or [])
    if not question:
        raise gr.Error("Please enter a financial research question.")
    try:
        engine = initialize_engine_once()
        with ENGINE_LOCK:
            state = current_state if isinstance(current_state, dict) else copy.deepcopy(engine["final_state"])
            from hf_engine import ask
            answer, updated_state = ask(engine, question, state)
        turns.append((question, answer))
        transcript = "\n\n---\n\n".join(
            f"**Question {i}:** {q}\n\n{a}" for i, (q, a) in enumerate(turns, 1)
        )
        return transcript, updated_state, turns
    except Exception:
        logging.exception("Agentic research failed")
        raise gr.Error("The research engine could not complete this question. Check the Render logs.")

def example_choices(category):
    visible = [f"{n:02d} · {question}" for n, dimension, question in EXAMPLE_QUESTIONS
               if category == "All" or dimension == category]
    return gr.update(choices=visible, value=visible[0] if visible else None)

def use_example(choice):
    if not choice:
        return ""
    return choice.split(" · ", 1)[1]

EXAMPLE_QUESTIONS = [(1, 'Quantitative Analysis', 'What has CompanyA annualized volatility been over the last 2 years?'), (2, 'Quantitative Analysis', "Over the same period, what was CompanyA's annualized return, and what was its Return-to-Risk Ratio?"), (3, 'Quantitative Analysis', 'Compare CompanyA and CompanyB over the last 12 months in terms of annual return, annualized volatility and Sharpe Ratio. Which company has the stronger risk-adjusted performance according to these metrics?'), (4, 'Quantitative Analysis', 'Which pair of Dow Jones stocks has the highest Pearson correlation? Report its correlation coefficient.'), (5, 'Quantitative Analysis', 'Which are the 5 Dow Jones stocks with the highest 12-month momentum? For each stock, report its momentum, Dollar Volume and position in the ranking.'), (6, 'Quantitative Analysis', 'Among these five stocks, which one has the highest Sharpe Ratio over the same 12-month period? Compare the Sharpe Ratios of all five stocks.'), (7, 'Quantitative Analysis', 'Between CompanyA and CompanyB, which one simultaneously has lower annualized volatility, a higher Sharpe Ratio and a lower Beta over the last 12 months? Report all three metrics for both companies and state whether either satisfies all three conditions.'), (8, 'Corporate Intelligence', "What financial and operating results did CompanyA report for FY2025? Identify the main drivers of revenue, profitability and cash flow according to the company's official financial release."), (9, 'Corporate Intelligence', "What did CompanyA's management communicate about its 2026 outlook? Distinguish the CEO's strategic priorities from the CFO's financial expectations, where separately disclosed."), (10, 'Corporate Intelligence', 'Compare the FY2025 financial results of CompanyA and CompanyB using their respective official earnings releases. Examine revenue growth, profitability, business segment performance and the principal factors identified by management.'), (11, 'Integrated Financial Research', "Compare CompanyA's FY2025 financial results with its stock's annualized return and annualized volatility from the beginning of calendar year 2026 to date. What observations can be made by examining the 2025 financial results, management's statements about the 2026 outlook, and the stock's observed market performance?"), (12, 'Integrated Financial Research', 'Compare CompanyA, CompanyB, and CompanyC using their 12-month momentum, Sharpe Ratio, and the most recent available management guidance for 2026. Identify the differences in their quantitative risk-return profiles and reported business outlooks.'), (13, 'Quantitative Analysis', 'Compare CompanyA and CompanyB over the last 12 months in terms of momentum and Sharpe Ratio. Does the stock with stronger momentum also have the better risk-adjusted performance?'), (14, 'Quantitative Analysis', 'Which of CompanyA, CompanyB, and CompanyC has experienced the largest change in annualized volatility between the last 3 months and the last 12 months?'), (15, 'Quantitative Analysis', 'Identify the 5 Dow Jones stocks with the highest Sharpe Ratio over the last year and compare their annualized returns over the same period. Determine whether the stocks with the highest Sharpe Ratios also have the highest annualized returns and whether the risk-adjusted performance ranking matches the return ranking.'), (16, 'Quantitative Analysis', 'Calculate the CAPM metrics for CompanyA and CompanyB over the last 5 years. For each company, compare its actual annualized return with its CAPM expected return and comment on the results.'), (17, 'Quantitative Analysis', 'Compare the Beta and annualized volatility of CompanyA, CompanyB, and CompanyC over the last 3 years. Do the two risk measures provide a consistent picture of their relative risk?'), (18, 'Quantitative Analysis', 'Compare CompanyA and CompanyB over the last 2 years using annualized return, volatility, Sharpe Ratio, and Beta. In which dimensions do their risk-return profiles differ most clearly?'), (19, 'Integrated Financial Research', "What were CompanyA's  main results in FY2025, and what outlook did management highlight? Compare the statements in the FY2025 earnings release with the stock's performance since the beginning of calendar year 2026. What conclusions can be drawn?"), (20, 'Integrated Financial Research', "Compare CompanyA and CompanyB using their respective FY2025 financial results and their stock performance over the last 12 months. Examine the annualized return, annualized volatility, and Sharpe Ratio of both stocks. What conclusions can be drawn from comparing the companies' financial results with their respective risk-return profiles?")]

CSS = '\n@import url(\'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@400;500;600&display=swap\');\n\n:root { --navy:#031B35; --cream:#F3F0E9; --gold:#D5B46D; --muted:#BAC6D2; }\nhtml, body, .stApp, \nheader\n\nsection\n.gradio-container {\n    max-width:1160px !important;\n    padding:1.8rem 2.2rem 5rem 1.4rem !important;\n}\nhtml { scroll-behavior:smooth; }\n.a-page, .a-page * { box-sizing:border-box; }\n.a-page { font-family:\'DM Sans\',sans-serif; color:var(--cream); }\n.a-page p { color:var(--muted); font-size:clamp(14px,1.4vw,17px); line-height:1.85; font-weight:400; }\n.a-page h1,.a-page h2 {\n    font-family:\'Playfair Display\',Georgia,serif;\n    color:var(--cream); font-weight:400; letter-spacing:-.035em;\n    line-height:1.12; margin:0 0 25px;\n}\n.a-page h1 { font-size:clamp(49px,6.6vw,89px); }\n.a-page h2 { font-size:clamp(41px,5.1vw,70px); }\n.a-page .gold { color:var(--gold); }\n.a-page .eyebrow { color:var(--gold); font-size:11px; font-weight:700; letter-spacing:.19em; text-transform:uppercase; margin:0 0 24px; }\n.a-page .brand { font-family:\'Playfair Display\',Georgia,serif; font-size:26px; margin-bottom:62px; }\n.a-page .brand span { color:var(--gold); }\n.a-page .hero, .a-page .section-grid {\n    display:grid; grid-template-columns:1fr 1fr; gap:30px; align-items:center;\n}\n.a-page .hero { min-height:570px; position:relative; }\n.a-page .hero-copy { position:relative; z-index:2; }\n.a-page .hero { grid-template-columns:1fr 1fr; overflow:visible; }\n.a-page .hero h1 { font-size:clamp(49px,6.6vw,89px); max-width:none; overflow:visible; }\n.a-page .hero h1 .no-break { display:block; width:max-content; max-width:none; white-space:nowrap; font-size:inherit; position:relative; z-index:3; }\n.a-page .hero-copy p { max-width:520px; }\n.a-page .visual { width:100%; height:auto; object-fit:contain; display:block; }\n.a-page .hero-image { margin-left:-8%; width:118%; opacity:.93; transform:translateY(-90px); }\n.a-page .visual-right { width:112%; margin-left:-4%; }\n.a-page .visual-left { width:112%; margin-left:-8%; }\n.a-page .section { border-top:1px solid rgba(197,212,227,.25); padding:56px 0 65px; }\n.a-page .section-index { font-size:12px; color:var(--gold); letter-spacing:.12em; margin-bottom:27px; }\n.a-page .section-grid { min-height:275px; }\n.a-page .section-copy { max-width:550px; }\n.a-page .section-copy p { margin:0; }\n.a-page .strip { color:var(--gold); font-size:11px; letter-spacing:.15em; text-transform:uppercase; font-weight:700; line-height:2; margin-top:28px; }\n.a-page .company-list { color:#C7D1DB; font-size:13px; line-height:2.15; margin-top:24px; }\n.a-page .hero-strip { margin:42px 0 40px; }\n.a-page .research-copy { padding-bottom:12px; }\n.a-page .research-shell { border:1px solid rgba(213,180,109,.52); background:rgba(10,34,60,.42); border-radius:5px; padding:24px; }\n.a-page .research-heading { font-family:\'Playfair Display\',Georgia,serif; color:var(--cream); font-size:23px; margin-bottom:15px; }\n.a-page .example { font-size:12px; color:var(--muted); line-height:1.6; margin-top:13px; }\n\n\n\n\n.a-page .foot { color:#7E94AA; font-size:12px; padding:30px 0; }\n@media(max-width:800px) {\n    .gradio-container { padding:1.3rem 1.15rem 4rem !important; }\n    .a-page .brand { margin-bottom:35px; }\n    .a-page .hero,.a-page .section-grid { grid-template-columns:1fr; gap:10px; }\n    .a-page .hero { min-height:0; }\n    .a-page .hero h1 { font-size:clamp(37px,8vw,58px); max-width:100%; }\n    .a-page .hero h1 .no-break { font-size:inherit; max-width:100%; white-space:normal; width:auto; }\n    .a-page .hero-image { margin:0; width:100%; transform:none; }\n    .a-page .section { padding:35px 0 43px; }\n    .a-page .section-grid .image-col { order:2; }\n    .a-page .section-grid .section-copy { order:1; }\n    .a-page h1 { font-size:clamp(44px,10vw,68px); }\n    .a-page h2 { font-size:clamp(38px,8vw,55px); }\n    .a-page .hero-strip { margin:24px 0 32px; }\n}\n\n/* Example questions: readable controls in both idle and hover states */\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n/* Research example library: dark, high-contrast, always-readable */\n.research-divider { border-top:1px solid rgba(197,212,227,.25); margin:24px 0 20px; }\n.question-meta { color:#D5B46D; font-size:11px; font-weight:700; letter-spacing:.10em; margin:0 0 10px; }\n.question-body { color:#F3F0E9; font-size:14px; line-height:1.65; }\n\n\n\n\n\n\n\n\n\n\n\n\n/* Natural marker strokes: readable on navy, without rectangular backgrounds. */\n.a-page .marker-lead {\n    display: inline-block;\n    position: relative;\n    isolation: isolate;\n    color: #031B35;\n    font-weight: 700;\n    font-size: 17px;\n    letter-spacing: .015em;\n    line-height: 1.5;\n    margin: 4px 0 8px;\n}\n\n.a-page .marker-lead::before {\n    content: "";\n    position: absolute;\n    z-index: -1;\n    left: -.12em;\n    right: -.12em;\n    top: 8%;\n    bottom: 5%;\n    background: #F9E76E;\n    opacity: 1;\n    transform: rotate(-0.3deg);\n    border-radius: 3px 5px 4px 3px;\n    clip-path: polygon(1% 7%, 99% 2%, 100% 90%, 2% 100%, 0 85%);\n}\n.a-page .memory-description { max-width:800px; margin:0 0 18px; font-size:15px; line-height:1.7; color:#C9D5E1; }\n.question-body .marker-inline { color:#F3F0E9; font-weight:700; padding:0 .07em; position:relative; isolation:isolate; white-space:normal; }\n.question-body .marker-inline::before {\n    content:""; position:absolute; z-index:-1;\n    left:-.07em; right:-.08em; top:auto; bottom:-.08em; height:.18em;\n    background:linear-gradient(176deg,#F9E76E 3%,#F5DF57 72%,#F8E76D 96%);\n    clip-path:polygon(0 25%,97% 0,100% 70%,3% 100%);\n    transform:rotate(-.5deg);\n}\n\n\nhtml,body,.gradio-container{background:#031B35!important;color:#F3F0E9!important;}\n.gradio-container{max-width:1160px!important;width:100%!important;margin-left:auto!important;margin-right:auto!important;padding:1.8rem 2.2rem 5rem 1.4rem!important;}\n.gradio-container .prose,.gradio-container .prose *{color:#F3F0E9;}\n#research_question textarea{background:#0B2A48!important;color:#F3F0E9!important;border:1px solid rgba(213,180,109,.48)!important;}\n#analyze{background:#D5B46D!important;color:#031B35!important;border:none!important;font-weight:700!important;}\n#research_answer{background:#08233F!important;border:1px solid #36516B!important;border-radius:6px;padding:15px;}\n#research_answer *{color:#F3F0E9!important;}\n#example_accordion{background:#08233F!important;border:1px solid #36516B!important;}\n#example_accordion *{color:#F3F0E9;}\n#example_accordion #example_category label span {\n    color:#031B35!important;\n}\n#example_accordion button{color:#031B35!important;}\n@media(max-width:800px){.gradio-container{padding:1.3rem 1.15rem 4rem!important;}}\n'

LANDING_HTML = f"""
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
        <div class="eyebrow">A SINGLE TOOL CONNECTS YOU TO THE FINANCIAL WORLD</div>
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
"""

RESEARCH_CSS = r'''
/* Scoped research area: navy throughout, no default white cards */
#research_area {max-width: 940px; margin: 24px auto 0;}
#research_area, #research_area .block, #research_area .form,
#research_area .wrap, #research_area .gr-group,
#research_area .gr-box {background:transparent!important;box-shadow:none!important;}
#research_area .research-intro {font-family:'DM Sans',sans-serif;margin-bottom:22px;}
#research_area .research-intro strong {font-size:17px;color:#031B35;background:#F9E76E;padding:2px 5px;}
#research_area .research-intro p {color:#C9D5E1;font-size:15px;line-height:1.75;max-width:850px;margin:13px 0 0;}
#research_area label, #research_area .label-wrap {color:#D5B46D!important;font-weight:600!important;}
#research_area #research_question {border:1px solid #63778A!important;border-radius:7px!important;background:#092744!important;padding:12px!important;}
#research_area #research_question textarea {background:#092744!important;color:#F3F0E9!important;border:0!important;box-shadow:none!important;font-size:16px!important;line-height:1.65!important;}
#research_area #research_question textarea::placeholder {color:#9DB0C2!important;}
#research_area #analyze {background:#D5B46D!important;color:#031B35!important;border:0!important;min-height:48px!important;font-weight:700!important;font-size:15px!important;}
#research_area #research_answer {background:#092744!important;border:1px solid #395570!important;border-radius:7px!important;padding:18px!important;min-height:55px;}
#research_area #research_answer .prose, #research_area #research_answer .prose * {color:#F3F0E9!important;}
#research_area .research-separator {border-top:1px solid #395570;margin:38px 0 28px;}
#research_area .research-universe {text-align:center;padding:8px 16px 30px;}
#research_area .research-universe .eyebrow {color:#D5B46D;letter-spacing:.15em;font-size:11px;font-weight:700;text-transform:uppercase;}
#research_area .research-universe p {color:#C7D1DB;font-size:13px;line-height:2.2;}
#research_area #example_accordion {background:#092744!important;border:1px solid #395570!important;border-radius:7px!important;padding:12px!important;}
#research_area #example_accordion button, #research_area #example_accordion .label-wrap {background:transparent!important;color:#F3F0E9!important;}
#research_area #example_accordion .prose, #research_area #example_accordion .prose * {color:#C9D5E1!important;}
#research_area #example_category {background:transparent!important;border:0!important;}
#research_area #example_category label {\n    color: #F3F0E9 !important;\n}\n\n#research_area #example_category label span,\n#research_area #example_category label .label,\n#research_area #example_category label .prose,\n#research_area #example_category label .prose * {\n    color: #031B35 !important;\n}\n\n#research_area #example_category input[type="radio"] {\n    accent-color: #246BEB;\n}
#research_area #example_category button, #research_area #example_category button *, #research_area #example_category label:has(input) {color:#031B35!important;}
#research_area .example-row {background:#0D304F!important;border:1px solid #395570!important;border-radius:6px!important;padding:16px 14px!important;margin:8px 0!important;align-items:center!important;}
#research_area .example-row .question-meta {color:#D5B46D!important;font-size:11px!important;letter-spacing:.10em!important;font-weight:700!important;margin-bottom:9px;}
#research_area .example-row .question-body {color:#F3F0E9!important;font-size:14px!important;line-height:1.7!important;}
#research_area .example-use {background:#D5B46D!important;color:#031B35!important;border:0!important;font-weight:700!important;min-width:68px!important;}
#research_area .processing-note {color:#9EADBC;font-size:11px;line-height:1.7;margin-top:30px;}
@media(max-width:800px){#research_area{margin:14px 0 0;}#research_area .example-row{padding:12px!important;}}
.gradio-container{width:100%!important;max-width:1160px!important;margin-left:auto!important;margin-right:auto!important;margin-inline:auto!important;}
'''

CSS += RESEARCH_CSS

with gr.Blocks(css=CSS, title="AI Financial Intelligence | AI-Powered Financial Research", theme=gr.themes.Base()) as demo:
    gr.HTML(LANDING_HTML)
    with gr.Column(elem_id="research_area"):
        gr.HTML('''<div class="research-intro"><strong>Ask. Explore. Follow up.</strong>
          <p>The system remembers the context of your conversation! Use it to ask follow-up questions,
          refine your analysis, and explore new financial dimensions without repeating previous information.</p></div>''')

        question = gr.Textbox(label="Financial research question",
                              placeholder="Enter your financial research question…",
                              lines=4, elem_id="research_question")
        analyze = gr.Button("Analyze", variant="primary", elem_id="analyze")
        answer = gr.Markdown(elem_id="research_answer")
        session_state = gr.State(value=None)
        session_turns = gr.State(value=[])
        analyze.click(run_question,
                      inputs=[question, session_state, session_turns],
                      outputs=[answer, session_state, session_turns],
                      concurrency_limit=1)

        gr.HTML('<div class="research-separator"></div>')
        gr.HTML('''<div class="research-universe"><div class="eyebrow">Available Companies · Dow Jones 30</div>
        <p>3M · Amazon · American Express · Amgen · Apple · Boeing · Caterpillar · Chevron · Cisco · Coca-Cola · Disney · Goldman Sachs · Home Depot · Honeywell · IBM · Johnson &amp; Johnson · JPMorgan Chase · McDonald’s · Merck · Microsoft · Nike · NVIDIA · Procter &amp; Gamble · Salesforce · Sherwin-Williams · Travelers · UnitedHealth · Verizon · Visa · Walmart</p></div>''')

        with gr.Accordion("Explore example questions · 20 research ideas", open=False,
                          elem_id="example_accordion"):
            gr.Markdown("Choose a question to insert it into the research field. You can edit it before analyzing.")
            category = gr.Radio(
                ["All", "Quantitative Analysis", "Corporate Intelligence", "Integrated Financial Research"],
                value="All", label="Research dimension", elem_id="example_category")
            example_rows = []
            for number, dimension, sample in EXAMPLE_QUESTIONS:
                with gr.Row(visible=True, elem_classes=["example-row"]) as example_row:
                    rendered = html.escape(sample)
                    if number == 2:
                        rendered = rendered.replace("Over the same period", '<span class="marker-inline">Over the same period</span>', 1)
                    elif number == 6:
                        rendered = rendered.replace("Among these five stocks", '<span class="marker-inline">Among these five stocks</span>', 1)
                    with gr.Column(scale=8):
                        gr.HTML(f'<div class="question-meta">{number:02d} · {html.escape(dimension.upper())}</div><div class="question-body">{rendered}</div>')
                    with gr.Column(scale=1, min_width=85):
                        use_button = gr.Button("Use", elem_classes=["example-use"])
                        use_button.click(fn=partial(lambda q: q, sample), outputs=question)
                example_rows.append((dimension, example_row))

            def filter_example_rows(selected):
                return [gr.update(visible=(selected == "All" or dimension == selected))
                        for dimension, _ in example_rows]
            category.change(filter_example_rows, inputs=category,
                            outputs=[item[1] for item in example_rows])


    gr.HTML('<div class="a-page"><div class="foot">AI Financial Intelligence · Powered by NVIDIA Nemotron and Nebius</div></div>')

if __name__ == "__main__":
    # Optional password. Set ACCESS_PASSWORD as a Render environment variable.
    # Without it, the app is public (recommended for hackathon judges).
    password = os.environ.get("ACCESS_PASSWORD", "").strip()
    authentication = [("research", password)] if password else None
    demo.queue(default_concurrency_limit=1).launch(auth=authentication, ssr_mode=False, server_name="0.0.0.0", server_port=int(os.environ.get("PORT", "7860")))

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
#research_area #example_category label {color:#F3F0E9!important;}
#research_area .example-row {background:#0D304F!important;border:1px solid #395570!important;border-radius:6px!important;padding:16px 14px!important;margin:8px 0!important;align-items:center!important;}
#research_area .example-row .question-meta {color:#D5B46D!important;font-size:11px!important;letter-spacing:.10em!important;font-weight:700!important;margin-bottom:9px;}
#research_area .example-row .question-body {color:#F3F0E9!important;font-size:14px!important;line-height:1.7!important;}
#research_area .example-use {background:#D5B46D!important;color:#031B35!important;border:0!important;font-weight:700!important;min-width:68px!important;}
#research_area .processing-note {color:#9EADBC;font-size:11px;line-height:1.7;margin-top:30px;}
@media(max-width:800px){#research_area{margin:14px 0 0;}#research_area .example-row{padding:12px!important;}}
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

        gr.HTML('''<p class="processing-note">Research Processing Time: Due to the highly sophisticated and structured nature of the financial analysis, the system requires approximately 10–20 minutes to generate a response. Please allow this time for the analysis to complete.</p>''')

    gr.HTML('<div class="a-page"><div class="foot">AI Financial Intelligence · Powered by NVIDIA Nemotron and Nebius</div></div>')

if __name__ == "__main__":
    # Optional password. Set ACCESS_PASSWORD as a Render environment variable.
    # Without it, the app is public (recommended for hackathon judges).
    password = os.environ.get("ACCESS_PASSWORD", "").strip()
    authentication = [("research", password)] if password else None
    demo.queue(default_concurrency_limit=1).launch(auth=authentication, ssr_mode=False, server_name="0.0.0.0", server_port=int(os.environ.get("PORT", "7860")))

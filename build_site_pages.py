#!/usr/bin/env python3
"""Generate the Urban AI class and lab pages for the Jekyll site."""
import os, textwrap

SITE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")

CLASSES = [
 dict(id="1-1", slug="class-1-1", order=1, meeting=1, lead="Si Chen", dur="60 min",
   title="Urban Analytics, Smart Cities, and Urban AI",
   subtitle="How cities already decide — and where AI enters the process.",
   deck="class1-1_urban_ai.pptx",
   objectives=[
     "Trace the line from urban analytics to smart cities to Urban AI, and say what is genuinely new at each step.",
     "Describe a real planning decision process: who initiates it, who is consulted, who signs off, and what evidence counts.",
     "Define a decision support system (DSS) and distinguish support from automation.",
     "Name three urban tasks where AI is already deployed and one where it clearly should not be.",
   ],
   outline=[
     ("What urban analytics has always done", "Counting, mapping, forecasting, and comparing. The questions are old; the data volume and speed are new."),
     ("The smart city promise and its critics", "Sensors, dashboards, and platforms — plus the recurring critique that instrumentation is not the same as governance."),
     ("From analytics to Urban AI", "Pattern recognition on imagery and text, scenario generation, and language models entering the planner's workflow."),
     ("How planning decisions actually get made", "Problem framing, alternatives, criteria, public comment, tradeoffs, and the moment a human signs their name to a recommendation."),
     ("What a DSS is", "A system that structures information so a person can decide well. Support, not substitution."),
     ("Three live cases", "Street-view imagery for condition assessment, text mining of public comment, and scenario platforms in long-range planning."),
   ],
   activity="**Breakout (20 min).** In pairs, take a decision your campus or hometown made recently — a bus route change, a rezoning, a bike lane. Map it onto the decision process: who framed the problem, what alternatives existed, what criteria decided it, and where an AI tool could have helped or hurt. Post one sentence to Discussion Forum A.",
   next_up="Discussion Forum A opens: *Urban AI in the wild*. Find one real deployment, describe what it decides, and say who is affected.",
 ),
 dict(id="1-2", slug="class-1-2", order=2, meeting=2, lead="Jie Hou", dur="75 min",
   title="AI Basics for Urban Problems",
   subtitle="What a model is, what training means, and why the answer is sometimes confidently wrong.",
   deck="class1-2_ai_basics.pptx",
   objectives=[
     "Explain data, features, model, training, and inference in plain language, using an urban example throughout.",
     "Tell supervised from unsupervised learning and match each to a planning question.",
     "Explain in one sentence why a language model can produce fluent text that is factually false.",
     "Recognize overfitting, data leakage, and biased training data when shown an example.",
   ],
   outline=[
     ("The vocabulary, once", "Row, column, label, feature, model, parameter, training, inference — each defined against a table of city parcels."),
     ("Supervised learning", "You have labels and want to predict them: which buildings are in poor condition, which permits will be delayed."),
     ("Unsupervised learning", "You have no labels and want structure: which neighborhoods resemble each other, what themes appear in public comment."),
     ("How a model is evaluated", "Train/test split, accuracy versus the base rate, and why a single accuracy number hides who the model fails."),
     ("Where language models differ", "Next-token prediction, why fluency is not accuracy, and what grounding means."),
     ("Four failure modes to memorize", "Overfitting, leakage, distribution shift, and biased labels — each with an urban example."),
   ],
   activity="**Breakout (20 min).** You are given two model report cards for the same building-condition model: one shows 91% accuracy overall, the other shows accuracy by neighborhood. Decide as a group whether you would deploy it and write the one condition you would attach.",
   next_up="**Lab 0 — AI in the Browser + First Colab.** Your first AI Use Log entry is due at the end of the lab.",
 ),
 dict(id="2-1", slug="class-2-1", order=3, meeting=3, lead="Si Chen", dur="60 min",
   title="Urban Analytic Models I — Site Analysis and Simulation",
   subtitle="Suitability, accessibility, and models that let you ask what-if before you build.",
   deck="class2-1_urban_models_1.pptx",
   objectives=[
     "Build a suitability analysis from criteria, weights, and layers, and defend each weight.",
     "Read an accessibility measure and say what it assumes about how people move.",
     "Describe what an urban simulation model does and what it necessarily leaves out.",
     "Identify the point in a site analysis where a value judgment is disguised as a technical choice.",
   ],
   outline=[
     ("Site analysis as a structured argument", "Layers, constraints, and opportunities — and the fact that every overlay encodes a preference."),
     ("Weighted suitability", "Criteria selection, normalization, weighting, and sensitivity. Why the weights are the politics."),
     ("Accessibility and reach", "Isochrones, gravity measures, and the difference between distance and access."),
     ("Simulation families", "Cellular-automata land-use models, agent-based models of movement, and system-dynamics views of growth."),
     ("Calibration and validation", "Fitting a model to the past, and the honest limits of projecting it forward."),
     ("Reading a model critically", "Six questions to ask any modeler before you trust an output."),
   ],
   activity="**Breakout (20 min).** Given five suitability criteria for siting a new community center, assign weights as a team. Then swap weights with another team and see whether the winning site changes. Report what changed and why.",
   next_up="**Lab 1 — Text Mining Community Voice.** Bring one urban issue your team may want to work on.",
 ),
 dict(id="2-2", slug="class-2-2", order=4, meeting=4, lead="Si Chen", dur="60 min",
   title="Urban Analytic Models II — Optimization and Scenario Testing",
   subtitle="When there is no single best answer, structure the tradeoff instead of hiding it.",
   deck="class2-2_urban_models_2.pptx",
   objectives=[
     "State an urban problem as an objective, decision variables, and constraints.",
     "Explain why most planning problems are multi-objective and what a Pareto tradeoff means.",
     "Design a scenario set that spans real uncertainty rather than decorating a preferred outcome.",
     "Run a sensitivity check and interpret rank instability.",
   ],
   outline=[
     ("Optimization, stated plainly", "Objective, variables, constraints — with facility siting and route design as the running examples."),
     ("One objective is rarely enough", "Cost versus access versus emissions; Pareto fronts; why 'optimal' needs a subscript."),
     ("Scenario planning", "Scenarios as structured disagreements about the future, not as best/worst/likely decoration."),
     ("Building a defensible scenario set", "Driving forces, plausible ranges, and the discipline of including a scenario you dislike."),
     ("Sensitivity and robustness", "Sweeping the weights, watching the ranking move, and reporting when the answer is fragile."),
     ("Communicating a tradeoff", "Presenting three defensible options instead of one recommendation with hidden assumptions."),
   ],
   activity="**Breakout (20 min).** Your team has $2M for a corridor: bus priority, protected bike lane, or sidewalk repair. Write the objective, the constraint, and the criterion that would flip your choice.",
   next_up="**Lab 2 — Clustering Analysis.** Your team's stakeholder map and criteria matrix are due at the start of Meeting 5.",
 ),
 dict(id="3-1", slug="class-3-1", order=5, meeting=6, lead="Jie Hou & Si Chen", dur="75 min",
   title="Decision Support Systems I — Categories and Cases",
   subtitle="Five kinds of DSS, and how to tell which one your problem actually needs.",
   deck="class3-1_dss_cases_1.pptx",
   objectives=[
     "Classify a DSS as data-driven, model-driven, knowledge-driven, communication-driven, or document-driven.",
     "Trace the history from 1970s decision support research to today's AI-enhanced workflows.",
     "Match an urban problem to the DSS category that fits it, and justify the match.",
     "Identify the human decision point in a described system.",
   ],
   outline=[
     ("Where DSS came from", "Management information systems, the 1970s decision-support tradition, and the enduring claim that the human stays in the loop."),
     ("Data-driven DSS", "Dashboards, query and reporting, operational awareness — and dashboard fatigue."),
     ("Model-driven DSS", "Simulation and optimization behind a usable interface; scenario platforms in long-range planning."),
     ("Knowledge-driven DSS", "Rules, expert systems, and modern classifiers offering recommendations."),
     ("Communication- and document-driven DSS", "Participation platforms, deliberation tools, and retrieval over plan documents."),
     ("Case walk-throughs", "Two deployed systems examined end to end: what data went in, what the system output, who decided, and what went wrong."),
   ],
   activity="**Breakout (20 min).** Take your team's urban issue. Which DSS category fits it? Sketch the inputs, the output, and — most importantly — mark the exact point where a human must decide.",
   next_up="**Lab 5 — Risk-Response DSS.** You will build and stress-test a weighted decision matrix.",
 ),
 dict(id="3-2", slug="class-3-2", order=6, meeting=7, lead="Jie Hou", dur="60 min",
   title="Decision Support Systems II — AI-Enhanced Workflows",
   subtitle="Designing the human-in-the-loop, and the failure modes that show up when you don't.",
   deck="class3-2_dss_cases_2.pptx",
   objectives=[
     "Design an AI-enhanced decision workflow with explicit human checkpoints.",
     "Choose an evaluation approach for a DSS that goes beyond model accuracy.",
     "Name and recognize automation bias, feedback loops, and proxy-variable failures.",
     "Write an oversight plan that says who checks what, when, and against which source.",
   ],
   outline=[
     ("From model to workflow", "The model is 10% of the system. The other 90% is inputs, interfaces, escalation, and review."),
     ("Human-in-the-loop patterns", "Human-in-command, human-on-the-loop, and review-by-exception — with the conditions each requires."),
     ("Evaluating a DSS", "Decision quality, time to decision, equity of outcomes, contestability, and whether anyone can explain a result to a resident."),
     ("Failure modes", "Automation bias, proxy variables standing in for the thing you care about, and feedback loops that manufacture their own evidence."),
     ("Documentation that survives audit", "Process logs, model cards, and the AI Use Log you have been keeping."),
     ("Designing your team's workflow", "A worked example built live from a student issue."),
   ],
   activity="**Breakout (20 min).** Take the workflow you sketched in Class 3-1 and add three human checkpoints. For each, write what the human is checking and what evidence they need to do it.",
   next_up="**Lab 6 — DSS AI Lab.** Your Scenario Comparison Matrix comes out of this lab.",
 ),
 dict(id="4-1", slug="class-4-1", order=7, meeting=8, lead="Jie Hou", dur="30 min",
   title="Large Language Models in Decision Support",
   subtitle="What LLMs are good for in a planning workflow, and how to keep them tethered to evidence.",
   deck="class4-1_llm_dss.pptx",
   objectives=[
     "Describe what an LLM does and why grounding changes its reliability.",
     "Use retrieval-augmented prompting over a real plan document.",
     "Write a prompt that requests sources and flags uncertainty.",
     "Detect and log a hallucination.",
   ],
   outline=[
     ("What the model is doing", "Prediction over text, why it sounds certain, and where the knowledge actually lives."),
     ("Useful jobs in planning", "Summarizing public comment, drafting plain-language explanations, structuring criteria, translating jargon for residents."),
     ("Jobs to refuse", "Inventing data, deciding, and anything where a wrong answer reaches a resident unreviewed."),
     ("Grounding and retrieval", "Giving the model the document and requiring quotes. Grounded versus ungrounded, side by side."),
     ("Prompt patterns that help", "Role, task, constraints, format, sources, and an explicit 'say I don't know' instruction."),
     ("The hallucination log", "How to record what the model got wrong, so the next cohort inherits your findings."),
   ],
   activity="**Breakout (15 min).** Ask the same question of a grounded and an ungrounded assistant. Record both answers and mark every claim you cannot verify in the source document.",
   next_up="**Lab 7 — LLM Lab**, then Class 4-2 on ethics and the final presentations.",
 ),
 dict(id="4-2", slug="class-4-2", order=8, meeting=8, lead="Jie Hou", dur="30 min",
   title="AI Ethics for Urban Decisions",
   subtitle="Bias, privacy, transparency, accountability — as design requirements, not as a closing slide.",
   deck="class4-2_ai_ethics.pptx",
   objectives=[
     "Locate bias at each stage: problem framing, data collection, labeling, modeling, deployment, and interpretation.",
     "Apply a privacy and data-minimization check to an urban dataset.",
     "State what transparency requires for a system a resident can contest.",
     "Connect the course's practices to MSU's generative AI guidelines and to professional planning ethics.",
   ],
   outline=[
     ("Bias is not one thing", "Six places it enters, with an urban example for each."),
     ("Equity in outcomes, not just in code", "Whose error rate, whose wait time, whose neighborhood gets the intervention."),
     ("Privacy and surveillance in public space", "Aggregation, re-identification, consent that no one gave, and data minimization as a default."),
     ("Transparency and contestability", "Being able to tell a resident what decided their case, and giving them a way to challenge it."),
     ("Accountability", "Who is responsible when the system is wrong: procurement, oversight, and the named human."),
     ("Participation as a safeguard", "Involving affected communities early enough that the framing itself can still change."),
   ],
   activity="**Discussion Forum B — *Whose city does the model see?*** Post one place in your team's own workflow where a group was under-represented, and the specific change you made or would make.",
   next_up="Final team presentations, reflection, and post-survey close the course.",
 ),
]

LABS = [
 dict(n=0, slug="lab-0", meeting=2, lead="Jie Hou / Sean", dur="75 min",
   title="AI in the Browser + First Colab",
   subtitle="Your first supervised encounter with an AI tool, and your first notebook.",
   nb="lab0_ai_in_the_browser.ipynb",
   goal="Use an approved AI assistant on a real urban question, then open a notebook and run it without fear.",
   a=["Open an approved AI assistant and ask it one urban question you actually care about.",
      "Ask it for its sources. Check two of them.",
      "Record the exchange in the AI Use Log: prompt, output, what you changed, what you verified."],
   b=["Run a 10-cell guided tour: load a city service-request dataset, plot it, and inspect it.",
      "Change the neighborhood filter and the date range, and watch the picture change.",
      "Compare what the chart says with what the AI assistant said."],
   artifact="AI Use Log entry #1 (one row, fully completed).",
   ra="You will find at least one claim the assistant could not support. Log it. That habit is the whole course in miniature.",
 ),
 dict(n=1, slug="lab-1", meeting=3, lead="Sean", dur="60 min",
   title="Text Mining Community Voice",
   subtitle="Turning hundreds of reviews and comments into themes — and noticing who is missing.",
   nb="lab1_text_mining.ipynb",
   goal="Extract themes from geolocated reviews and public comment, and quantify whose voices dominate.",
   a=["Paste the supplied review corpus into an approved text-analysis tool.",
      "Produce a theme list and a sentiment summary.",
      "Fill in the representation table by neighborhood."],
   b=["Run TF-IDF, sentiment scoring, and keyword-based topic extraction over the corpus.",
      "Change the stopword list and the number of topics; watch the themes shift.",
      "Compute comments per capita by neighborhood."],
   artifact="Top-themes table plus one written bias note naming an under-represented group.",
   ra="The notebook shows one neighborhood contributing roughly half the comments per resident that another does. Any theme ranking inherits that imbalance.",
 ),
 dict(n=2, slug="lab-2", meeting=4, lead="Sean", dur="90 min",
   title="Clustering Analysis",
   subtitle="Building a neighborhood typology — and seeing how the choice of k redraws the map.",
   nb="lab2_clustering.ipynb",
   goal="Group census tracts into types from socioeconomic and built-environment indicators, and justify the number of groups.",
   a=["Use the interactive cluster explorer with the supplied tract indicators.",
      "Move the group-count slider from 3 to 6 and note which tracts change groups.",
      "Name each cluster in plain language."],
   b=["Standardize features, run k-means, and read a silhouette plot.",
      "Change k and the feature set with the marked parameters.",
      "Track which tracts move between clusters as k changes."],
   artifact="Neighborhood typology table plus a written justification for your chosen k.",
   ra="Cluster membership is not a fact about a neighborhood. It is a consequence of your feature choice and your k. Show the tracts that moved.",
 ),
 dict(n=3, slug="lab-3", meeting=5, lead="Sean", dur="60 min",
   title="Time Series Analysis",
   subtitle="Trend, seasonality, and the forecast that breaks the moment the world changes.",
   nb="lab3_time_series.ipynb",
   goal="Decompose an hourly urban series, produce a short forecast, and state the conditions under which it fails.",
   a=["Filter the supplied traffic and air-quality series in a chart tool.",
      "Identify the daily and weekly cycles by eye.",
      "Mark the point where the pattern breaks."],
   b=["Decompose the series into trend, seasonality, and residual.",
      "Fit a simple forecast and change the horizon.",
      "Forecast across a deliberate regime change and measure the error."],
   artifact="Trend brief (150 words) with an explicit forecast caveat.",
   ra="The series contains a structural break. A model fit before it forecasts confidently and wrongly after it. That is what a pandemic, a new transit line, or a closed bridge does to your data.",
 ),
 dict(n=4, slug="lab-4", meeting=5, lead="Sean", dur="60 min",
   title="Classification",
   subtitle="Predicting building condition — then asking whose buildings the model gets wrong.",
   nb="lab4_classification.ipynb",
   goal="Train a classifier on parcel data and audit its errors by subgroup.",
   a=["Use a no-code classifier interface on the supplied parcel table.",
      "Read the confusion matrix.",
      "Fill in the subgroup error table."],
   b=["Fit logistic regression and a decision tree; compare them.",
      "Change the decision threshold and watch precision and recall trade off.",
      "Compute error rate, false-positive rate, and false-negative rate by income group."],
   artifact="Subgroup error table plus a fairness note in plain language.",
   ra="Overall accuracy hides the gap. In the supplied data the error rate for low-income tracts runs roughly twice that of high-income tracts. A single accuracy number would have told you nothing.",
 ),
 dict(n=5, slug="lab-5", meeting=6, lead="Yura", dur="75 min",
   title="Risk-Response DSS",
   subtitle="A weighted decision matrix for flood and heat risk — and the sweep that shows it is fragile.",
   nb="lab5_risk_response_dss.ipynb",
   goal="Rank response alternatives against weighted criteria, then test whether the ranking survives a change in weights.",
   a=["Fill the weighted decision matrix template with the supplied risk data.",
      "Score three response alternatives against five criteria.",
      "Change the weights by hand and see whether the winner changes."],
   b=["Compute weighted scores across a full sweep of weight combinations.",
      "Plot how often each alternative wins.",
      "Identify the criterion that controls the outcome."],
   artifact="Ranked alternatives with a sensitivity chart.",
   ra="If your recommendation flips when equity weight moves from 0.2 to 0.3, your recommendation is a statement about your weights, not about the city. Say so.",
 ),
 dict(n=6, slug="lab-6", meeting=7, lead="Yura", dur="90 min",
   title="DSS AI Lab",
   subtitle="Run two real scenarios end to end. This lab produces a graded deliverable.",
   nb="lab6_dss_ai_lab.ipynb",
   goal="Test at least two planning scenarios for your team's issue and document the comparison.",
   a=["Configure two scenarios in an approved no-code DSS platform.",
      "Record inputs, assumptions, and outputs for each.",
      "Complete the Scenario Comparison Matrix template."],
   b=["Set scenario parameters in the notebook's scenario engine.",
      "Compare outcomes side by side under two different weight sets.",
      "Export the comparison table."],
   artifact="**Deliverable 4** — AI/DSS Process Log and Scenario Comparison Matrix (team).",
   ra="The notebook is built so that Transit-Oriented Development wins under one weight set and Status Quo wins under another. Both runs are correct. Only one gets presented — say which weights you chose and why.",
 ),
 dict(n=7, slug="lab-7", meeting=8, lead="Jie Hou & Yura", dur="30 min",
   title="LLM Lab",
   subtitle="Grounded versus ungrounded answers over a real planning document.",
   nb="lab7_llm_lab.ipynb",
   goal="Produce a stakeholder memo grounded in a supplied plan excerpt, and log every claim the model could not support.",
   a=["Use structured prompting against the supplied comprehensive-plan excerpt.",
      "Require quotes and page references in every answer.",
      "Run the hallucination hunt: ask three questions the document cannot answer."],
   b=["Run the retrieval-and-template demo: grounded answers with a confidence threshold.",
      "Change the threshold and watch questions move between 'answered' and 'cannot answer'.",
      "Compare grounded output against a naive ungrounded answer."],
   artifact="Grounded stakeholder memo plus a hallucination log.",
   ra="Three of the six test questions cannot be answered from the document. A well-configured system says so. An unconfigured one answers all six fluently.",
 ),
]

REFLECT = ["What did the tool assume?",
           "Who is missing from this data?",
           "What would change your recommendation?",
           "What must a human verify before this is used?"]

def w(path, text):
    full = os.path.join(SITE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(text)

# ── class pages ────────────────────────────────────────────────
for i, c in enumerate(CLASSES):
    prev = CLASSES[i-1] if i > 0 else None
    nxt  = CLASSES[i+1] if i < len(CLASSES)-1 else None
    obj = "\n".join(f"{n}. {o}" for n, o in enumerate(c["objectives"], 1))
    out = "\n".join(f"**{t}.** {d}\n" for t, d in c["outline"])
    body = f"""---
layout: default
title: "Class {c['id']} — {c['title']}"
parent: "Classes"
subtitle: "{c['subtitle']}"
eyebrow: "Class {c['id']} · Meeting {c['meeting']}"
permalink: /classes/{c['slug']}/
---

<ul class="meta">
  <li><strong>Meeting</strong> {c['meeting']}</li>
  <li><strong>Lead</strong> {c['lead']}</li>
  <li><strong>Length</strong> {c['dur']}</li>
  <li><strong>Slides</strong> <a href="{{{{ '/assets/slides/{c['deck']}' | relative_url }}}}">{c['deck']}</a></li>
</ul>

## Learning objectives

By the end of this class you will be able to:

{obj}

## Session outline

{out}

## In-class activity

{c['activity']}

## What comes next

{c['next_up']}

<div class="prevnext">
  <span>{f'''<a href="{{{{ "/classes/{prev["slug"]}/" | relative_url }}}}">← Class {prev["id"]}</a>''' if prev else '<a href="{{ "/classes/" | relative_url }}">← All classes</a>'}</span>
  <span>{f'''<a href="{{{{ "/classes/{nxt["slug"]}/" | relative_url }}}}">Class {nxt["id"]} →</a>''' if nxt else '<a href="{{ "/deliverables/" | relative_url }}">Deliverables →</a>'}</span>
</div>
"""
    w(f"classes/{c['slug']}.md", body)

# ── lab pages ──────────────────────────────────────────────────
for i, l in enumerate(LABS):
    prev = LABS[i-1] if i > 0 else None
    nxt  = LABS[i+1] if i < len(LABS)-1 else None
    # Literal HTML lists: kramdown does not process markdown inside raw HTML blocks.
    a = "<ol>\n" + "\n".join(f"      <li>{s}</li>" for s in l["a"]) + "\n    </ol>"
    b = "<ol>\n" + "\n".join(f"      <li>{s}</li>" for s in l["b"]) + "\n    </ol>"
    refl = "\n".join(f"- {r}" for r in REFLECT)
    body = f"""---
layout: default
title: "Lab {l['n']} — {l['title']}"
parent: "Labs"
subtitle: "{l['subtitle']}"
eyebrow: "Lab {l['n']} · Meeting {l['meeting']}"
permalink: /labs/{l['slug']}/
---

<ul class="meta">
  <li><strong>Meeting</strong> {l['meeting']}</li>
  <li><strong>TA lead</strong> {l['lead']}</li>
  <li><strong>Length</strong> {l['dur']}</li>
  <li><strong>Produces</strong> {l['artifact'].replace('**','')}</li>
</ul>

{l['goal']}

<div class="tracks">
  <div class="track">
    <h3>Track A <span class="badge">No code · default</span></h3>
    <p>Web tools only. No installation, no Python. Produces the same artifact as Track B.</p>
    {a}
  </div>
  <div class="track track-b">
    <h3>Track B <span class="badge">Colab · go deeper</span></h3>
    <p>A pre-filled notebook. You run cells and change the parameters marked <code># ▶ CHANGE ME</code>. You never write code from scratch.</p>
    {b}
    <p><a class="btn btn-sm" href="https://colab.research.google.com/github/jiehou-lab/urban-ai/blob/main/notebooks/{l['nb']}">Open in Colab</a></p>
  </div>
</div>

## What you turn in

{l['artifact']}

<div class="warn">
  <strong>Responsible AI moment</strong>
  <p>{l['ra']}</p>
</div>

## Reflection prompts

Every lab ends with the same four questions. Answer them in your lab submission.

{refl}

<div class="prevnext">
  <span>{f'''<a href="{{{{ "/labs/{prev["slug"]}/" | relative_url }}}}">← Lab {prev["n"]}</a>''' if prev else '<a href="{{ "/labs/" | relative_url }}">← All labs</a>'}</span>
  <span>{f'''<a href="{{{{ "/labs/{nxt["slug"]}/" | relative_url }}}}">Lab {nxt["n"]} →</a>''' if nxt else '<a href="{{ "/deliverables/" | relative_url }}">Deliverables →</a>'}</span>
</div>
"""
    w(f"labs/{l['slug']}.md", body)

# ── class index ────────────────────────────────────────────────
cards = "\n".join(
    f"""  <a class="card" href="{{{{ '/classes/{c['slug']}/' | relative_url }}}}">
    <span class="card-num">CLASS {c['id']}</span>
    <h3>{c['title']}</h3>
    <p>{c['subtitle']}</p>
    <p class="muted">Meeting {c['meeting']} · {c['lead']} · {c['dur']}</p>
  </a>""" for c in CLASSES)
w("classes/index.md", f"""---
layout: default
title: "Classes"
subtitle: "Eight classes across four sections, from what Urban AI is to what it owes the people it affects."
eyebrow: "Course content"
permalink: /classes/
---

Each class page lists objectives, the session outline, the in-class activity, and a link to the slide deck.
Slides are starter decks — instructors adapt them each cohort.

<div class="grid grid-2">
{cards}
</div>
""")

# ── lab index ──────────────────────────────────────────────────
lcards = "\n".join(
    f"""  <a class="card" href="{{{{ '/labs/{l['slug']}/' | relative_url }}}}">
    <span class="card-num">LAB {l['n']}</span>
    <h3>{l['title']}</h3>
    <p>{l['subtitle']}</p>
    <p class="muted">Meeting {l['meeting']} · {l['lead']} · {l['dur']}</p>
  </a>""" for l in LABS)
w("labs/index.md", f"""---
layout: default
title: "Labs"
subtitle: "Eight hands-on labs. Every one runs two ways — click-through or notebook — and both produce the same artifact."
eyebrow: "Hands-on"
permalink: /labs/
---

<div class="note">
  <strong>You do not need to code</strong>
  <p>Track A is the default and uses web tools only. Track B is a pre-filled Google Colab notebook where you
  run cells and change clearly marked parameters. Choose either. Switch between them at any time. The
  artifact you turn in is identical.</p>
</div>

<div class="grid grid-2">
{lcards}
</div>

## Notebook requirements

Track B notebooks run in Google Colab with no installation and no API keys. They use synthetic-but-realistic
urban datasets generated inside the notebook, so they work offline and produce the same results for everyone.
Instructor notes in each notebook name the real open-data sources to swap in — city open-data portals,
the U.S. Census American Community Survey, EPA air-quality data, OpenStreetMap, and local plan documents.
""")

print("generated", len(CLASSES), "class pages and", len(LABS), "lab pages")

# Urban AI — Canonical Course Design Spec
**Single source of truth. All syllabus, website, notebook, and slide content must match this file.**

Course: **Urban AI: AI-Driven Decision Support for Real-World Urban Challenges**
Institution: Michigan State University · MSU AI-Ready Initiative, Category 3 (Non-credit Learning Experience)
Format: Online (synchronous meetings + D2L Brightspace shell) · 20 contact hours · Non-credit
PI: Si Chen, Ph.D. (School of Planning, Design and Construction)
Co-PI: Jie Hou, Ph.D. (Computational Mathematics, Science and Engineering)
Teaching assistants: Sean (analytics labs), Yura (DSS labs)
Cohort size: 42–50 students · 10–12 cohorts/year target · No prerequisites, all majors

## Delivery pattern
- 8 meetings × 2.5 hours = 20.0 hours total
- Twice per week for 4 weeks; offered twice per semester
- Each meeting: ~1 h concept/lecture → 20–30 min TA demo → 20 min breakout + mini-task → reflection/wrap
- TA grades weekly mini-tasks; final team presentation (top 5 teams receive gift cards)

## Reconciliation rule (proposal ↔ teaching schedule)
The funded proposal defines six blocks (Orientation, Sessions 1–4, Reflection) totaling 20 hours and six
deliverables. The teaching plan defines 8 classes + 8 labs + 2 discussion forums. Both are preserved.
Hours per block as **delivered** differ from the proposal by at most ±0.5 h; total is exactly 20.0 h.

| Proposal block | Proposal hrs | Delivered hrs | Δ |
|---|---|---|---|
| Orientation | 1.0 | 1.0 | 0 |
| S1 What is Urban AI? | 5.0 | 4.5 | −0.5 |
| S2 Decision-Making Processes in Planning | 5.0 | 5.0 | 0 |
| S3 DSSs and AI Applications | 5.0 | 5.5 | +0.5 |
| S4 Scenario Simulation & Design Jam | 3.0 | 3.0 | 0 |
| Reflection | 1.0 | 1.0 | 0 |
| **Total** | **20.0** | **20.0** | **0** |

## Meeting map (authoritative)

| # | Meeting title | Segments (hrs) | Lead | Block hrs |
|---|---|---|---|---|
| M1 | Welcome & What Is Urban AI? | Orientation 1.0 · Class 1-1 Urban analytics, smart cities → Urban AI, decision-making processes, DSS 1.0 · Discussion Forum A launch 0.5 | Si (Jie) | Or 1.0 · S1 1.5 |
| M2 | AI Basics for Urban Problems | Class 1-2 AI Basics 1.25 · Lab 0 AI in the Browser + First Colab 1.25 | Jie / Sean | S1 2.5 |
| M3 | Auditing AI + Urban Analytic Models I | AI Output Audit studio & Forum A debrief 0.5 · Class 2-1 Urban Analytic Models I: site analysis & simulation 1.0 · Lab 1 Text Mining 1.0 | Si / Sean | S1 0.5 · S2 2.0 |
| M4 | Urban Analytic Models II | Class 2-2 Urban Analytic Models II: optimization & scenario testing 1.0 · Lab 2 Clustering Analysis 1.5 | Si / Sean | S2 2.5 |
| M5 | Patterns Over Time and Categories | Team checkpoint (stakeholder map + criteria matrix due) 0.5 · Lab 3 Time Series Analysis 1.0 · Lab 4 Classification 1.0 | Sean (Si) | S2 0.5 · S3 2.0 |
| M6 | Decision Support Systems I | Class 3-1 DSS categories and cases I 1.25 · Lab 5 Risk-Response DSS 1.25 | Jie & Si / Yura | S3 2.5 |
| M7 | Decision Support Systems II | Class 3-2 DSS categories and cases II 1.0 · Lab 6 DSS AI Lab 1.5 | Jie / Yura | S3 1.0 · S4 1.5 |
| M8 | LLMs, Ethics, and the Design Jam | Class 4-1 LLMs in decision support 0.5 · Lab 7 LLM Lab 0.5 · Class 4-2 AI Ethics + Forum B 0.5 · Final team presentations & Reflection 1.0 | Jie / Yura | S4 1.5 · Refl 1.0 |

Class inventory (8): 1-1, 1-2, 2-1, 2-2, 3-1, 3-2, 4-1, 4-2.
Lab inventory (8): Lab 0 AI Basics mini-lab; Lab 1 Text Mining; Lab 2 Clustering; Lab 3 Time Series;
Lab 4 Classification; Lab 5 Risk-Response DSS; Lab 6 DSS AI Lab; Lab 7 LLM Lab.
Forums (2): Forum A "Urban AI in the wild" (M1→M3); Forum B "Whose city does the model see?" (M8).

## Six required deliverables (unchanged from proposal)
1. Orientation — Responsible AI Agreement + AI readiness pre-survey (individual)
2. S1 — Individual AI Output Audit Worksheet
3. S2 — Team Stakeholder Map + Decision Criteria Matrix
4. S3 — AI/DSS Process Log + Scenario Comparison Matrix (team)
5. S4 — Urban AI Decision-Support Brief + 5-minute presentation (team)
6. Reflection — Individual reflection + post-survey

## Assessment (100%)
| Criterion | Weight |
|---|---|
| Urban problem framing and stakeholder analysis | 20% |
| Appropriate AI/DSS workflow and documentation | 20% |
| Scenario comparison and evidence quality | 20% |
| Evaluation of AI outputs, bias, uncertainty, and limitations | 20% |
| Responsible AI safeguards, human oversight, and communication clarity | 20% |

Completion (non-credit certificate + Spartan Experience Record): attend ≥7 of 8 meetings, submit all six
deliverables, maintain the AI Use Log. Weekly mini-tasks are graded complete/incomplete by the TA.

## Learning outcomes (from proposal §4.1)
1. Define Urban AI and AI-driven DSSs and explain how they support evidence-based urban decisions.
2. Describe planning decision processes: problem framing, stakeholders, criteria, alternatives, tradeoffs, human judgment.
3. Use approved AI tools responsibly for urban analytic tasks.
4. Evaluate AI outputs for accuracy, bias, uncertainty, missing context, privacy risk, and relevance.
5. Develop a human-centered decision-support workflow with transparent assumptions and human review.
6. Produce an Urban AI Decision-Support Brief demonstrating critical, ethical, creative AI use.

## Competency framework (from proposal §2.2)
AI and DSS foundations · Urban problem framing · AI-directed inquiry · Scenario analysis ·
Responsible AI evaluation · Communication for decision-making.

## Two-track lab rule (applies to every lab)
- **Track A — No code (default).** Web tool or hosted app; click-through worksheet; produces the same
  artifact as Track B. No installation, no Python.
- **Track B — Colab (go deeper).** Pre-filled Google Colab notebook. Students run cells and change clearly
  marked `# ▶ CHANGE ME` parameters, then answer interpretation questions. No code writing required.
- Every lab ends with the same 4 reflection prompts: What did the tool assume? Who is missing from this
  data? What would change your recommendation? What must a human verify before this is used?

## Lab specifications

| Lab | Title | Track A (no code) | Track B (Colab) | Urban data | Artifact |
|---|---|---|---|---|---|
| 0 | AI in the Browser + First Colab | Chat-based AI tool: prompt, critique, and log one urban question | Run a 10-cell tour: load a city dataset, plot it, ask an LLM to summarize it | City 311 service requests (sample) | AI Use Log entry #1 |
| 1 | Text Mining Community Voice | Web word-cloud / sentiment tool on supplied review text | TF-IDF + sentiment + topic keywords over geolocated reviews | Public park/transit reviews (synthetic + open) | Top-themes table + one bias note |
| 2 | Clustering Analysis | Interactive cluster explorer with sliders | k-means + silhouette on census-tract indicators; change k | ACS tract indicators for one metro | Neighborhood typology map + k justification |
| 3 | Time Series Analysis | Chart tool: filter a traffic/AQI series, spot the trend | Decompose trend/seasonality, simple forecast, change horizon | Hourly traffic counts / AQI | Trend brief + forecast caveat |
| 4 | Classification | No-code classifier UI: label, train, inspect errors | Logistic regression / tree on parcel or building-condition data; confusion matrix + subgroup error rates | Building condition / land use labels | Error table by subgroup + fairness note |
| 5 | Risk-Response DSS | Fill a weighted decision matrix in a spreadsheet template | Weighted-sum + sensitivity sweep on flood/heat risk criteria | Flood & heat exposure by tract | Ranked alternatives + sensitivity chart |
| 6 | DSS AI Lab | Run two scenarios in an approved no-code DSS platform | Scenario engine: change parameters, compare outcomes side by side | Land use / mobility scenario inputs | Scenario Comparison Matrix (deliverable 4) |
| 7 | LLM Lab | Structured prompting for stakeholder summaries + hallucination hunt | LLM API/local model: RAG over a supplied planning document, grounded vs ungrounded answers | Comprehensive plan excerpt | Grounded stakeholder memo + hallucination log |

## Responsible AI policy (course-wide)
- Use only MSU-approved AI tools; any new tool passes MSU IT review (feasibility, security, FERPA, accessibility).
- The **AI Use Log** is mandatory: tool, date, prompt/input, what the output was used for, what the human changed.
- AI may draft; humans decide. Every submitted claim must be verifiable by a human against a named source.
- No personal, identifiable, or restricted data in prompts. Public or synthetic data only.
- Uncited AI text is a violation of the Responsible AI Agreement; disclosure is never penalized, concealment is.

## Website information architecture
Home · Schedule (8 meetings) · Classes (8 pages) · Labs (8 pages, two tracks each) ·
Deliverables & Rubrics · Responsible AI · Resources · Team · FAQ

## Cohort dates (placeholder — confirm before publishing)
Cohort 1 (Fall 2026): Tue & Thu, 4:00–6:30 PM ET, Sept 8 – Oct 1, 2026 (M1…M8).
Cohort 2 (Spring 2027): TBD.

## Placeholders that must be replaced before publishing
`jiehou-lab` (site baseurl/url), cohort dates, D2L course link, Zoom link, approved-tool list,
TA full names (Sean, Yura), instructor photos, registration form URL.

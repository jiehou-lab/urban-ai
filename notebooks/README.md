# Urban AI — Colab Labs (Track B)

Eight Google Colab notebooks, one per course lab. Every notebook is self-contained, runs fully
offline (no network calls, no API keys), and generates its own synthetic-but-realistic urban
dataset in-notebook with a fixed random seed, so every student gets identical results.

Each lab follows the **two-track rule** from `spec/COURSE_SPEC.md`: Track A (no-code, default) and
Track B (this notebook) both produce the *same artifact*, and both end with the same 4 reflection
prompts: *What did the tool assume? Who is missing from this data? What would change your
recommendation? What must a human verify before this is used?*

Students only ever run pre-written cells and edit parameters marked `# ▶ CHANGE ME` — they never
write code from scratch.

## Lab index

| # | Notebook | Title | Track A (no code) | Artifact | Required packages |
|---|---|---|---|---|---|
| 0 | `lab0_ai_in_the_browser.ipynb` | AI in the Browser + First Colab | Chat-based AI tool: prompt, critique, and log one urban question | AI Use Log entry #1 | numpy, pandas, matplotlib |
| 1 | `lab1_text_mining.ipynb` | Text Mining Community Voice | Web word-cloud / sentiment tool on supplied review text | Top-themes table + one bias note | numpy, pandas, matplotlib, scikit-learn |
| 2 | `lab2_clustering.ipynb` | Clustering Analysis | Interactive cluster explorer with sliders | Neighborhood typology map + k justification | numpy, pandas, matplotlib, scikit-learn |
| 3 | `lab3_time_series.ipynb` | Time Series Analysis | Chart tool: filter a traffic/AQI series, spot the trend | Trend brief + forecast caveat | numpy, pandas, matplotlib, statsmodels |
| 4 | `lab4_classification.ipynb` | Classification | No-code classifier UI: label, train, inspect errors | Error table by subgroup + fairness note | numpy, pandas, matplotlib, scikit-learn |
| 5 | `lab5_risk_response_dss.ipynb` | Risk-Response DSS | Fill a weighted decision matrix in a spreadsheet template | Ranked alternatives + sensitivity chart | numpy, pandas, matplotlib |
| 6 | `lab6_dss_ai_lab.ipynb` | DSS AI Lab | Run two scenarios in an approved no-code DSS platform | Scenario Comparison Matrix (deliverable 4) | numpy, pandas, matplotlib |
| 7 | `lab7_llm_lab.ipynb` | LLM Lab | Structured prompting for stakeholder summaries + hallucination hunt | Grounded stakeholder memo + hallucination log | numpy, pandas, scikit-learn |

All notebooks additionally require Python 3 and run cleanly in the default Google Colab runtime
with no extra `pip install` needed (numpy, pandas, matplotlib, scikit-learn, and statsmodels are
all preinstalled on Colab).

## Embedded responsible-AI moments

Per notebook, as required by the course design:

- **Lab 0** — students critique a simulated AI summary before logging it (AI Use Log habit).
- **Lab 1** — compares review-volume share to population share by neighborhood to surface whose
  voices are over/under-represented in the "community voice" data.
- **Lab 2** — sweeps k from 3–6 and shows a sample of tracts whose cluster (and therefore whose
  "neighbors" in the typology) changes depending on the chosen k.
- **Lab 3** — trains a forecast on data before a synthetic road-closure event and shows it fail
  during the regime change, with a measured MAE/MAPE.
- **Lab 4** — computes accuracy, error rate, false-positive rate, and false-negative rate by
  neighborhood-income tier, driven by built-in label noise that mimics uneven code-enforcement
  data quality.
- **Lab 5** — sweeps the population-vulnerability weight and plots how each alternative's rank
  changes (and crosses over other alternatives) as the weight shifts.
- **Lab 6** — scores the same three scenarios under two different, equally defensible weight sets
  and shows they produce two different "winning" scenarios.
- **Lab 7** — logs a grounded (retrieval + confidence threshold) system next to a naive
  always-answer system across 6 test questions, 3 of which are not covered in the source document,
  producing a hallucination log.

## Instructor notes: swapping in real data

Every data-generation cell is preceded by a markdown note ("Synthetic-but-realistic data") that
names real sources students/instructors can swap in for their own city. Summary by lab:

- **Lab 0 / 3** — City 311/traffic Open Data portals (search "[city] open data"), `data.gov`,
  EPA Air Quality System (AQS) hourly monitor data.
- **Lab 1** — Public review platforms (collected per their terms of service), city
  engagement-survey exports, open transit-agency rider surveys.
- **Lab 2** — US Census ACS 5-year estimates via `data.census.gov` or the Census API, city/county
  GIS tract shapefiles, EPA EJScreen / CDC-ATSDR Social Vulnerability Index.
- **Lab 4** — County property-assessor parcel data, code-enforcement violation records, HUD or
  local housing-condition surveys.
- **Lab 5** — FEMA flood hazard layers, NOAA/EPA heat-vulnerability data, CDC/ATSDR SVI, city
  hazard-mitigation plans.
- **Lab 6** — Regional MPO travel-demand model outputs, city comprehensive plans, institutional
  scenario-planning tools (e.g., UrbanFootprint, Envision Tomorrow).
- **Lab 7** — The actual city/county Comprehensive Plan PDF (use the course's PDF-extraction
  workflow to pull real text into the `plan_excerpt` string) or MPO long-range transportation plans.

To swap in real data, replace only the data-generation cell in each notebook (clearly marked with
a `## 2. Load the data` header) — every downstream cell reads from the same DataFrame column names,
so the rest of the notebook does not need to change as long as the replacement DataFrame keeps the
same columns.

## Before publishing

- Replace the literal `jiehou-lab` placeholder in each "Open in Colab" badge with the real
  GitHub org/user once the repo is public (see `spec/COURSE_SPEC.md`, "Placeholders that must be
  replaced before publishing").
- Confirm TA names (Sean = analytics labs 0–4, Yura = DSS/LLM labs 5–7) against the current
  teaching team before each cohort.

## Verification

All 8 notebooks were executed end-to-end headlessly with
`jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=300`,
confirmed error-free, then had outputs cleared with `jupyter nbconvert --clear-output --inplace`
and re-validated as nbformat v4 JSON before being committed to this directory.

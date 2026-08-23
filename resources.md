---
layout: default
title: "Resources"
subtitle: "Templates, notebooks, datasets, and where to go after the course ends."
eyebrow: "Materials"
permalink: /resources/
---

## Student templates

<div class="table-scroll">
<table>
<thead><tr><th>Template</th><th>Used in</th><th>Download</th></tr></thead>
<tbody>
<tr><td>AI Use Log</td><td>Every meeting</td><td><a href="{{ '/assets/templates/AI_Use_Log.xlsx' | relative_url }}">.xlsx</a></td></tr>
<tr><td>AI Output Audit Worksheet</td><td>Meeting 3 · Deliverable 2</td><td><a href="{{ '/assets/templates/AI_Output_Audit_Worksheet.docx' | relative_url }}">.docx</a></td></tr>
<tr><td>Stakeholder Map + Decision Criteria Matrix</td><td>Meeting 5 · Deliverable 3</td><td><a href="{{ '/assets/templates/Stakeholder_Map_and_Criteria_Matrix.xlsx' | relative_url }}">.xlsx</a></td></tr>
<tr><td>Scenario Comparison Matrix</td><td>Meeting 7 · Deliverable 4</td><td><a href="{{ '/assets/templates/Scenario_Comparison_Matrix.xlsx' | relative_url }}">.xlsx</a></td></tr>
<tr><td>Decision-Support Brief template</td><td>Meeting 8 · Deliverable 5</td><td><a href="{{ '/assets/templates/Decision_Support_Brief_Template.docx' | relative_url }}">.docx</a></td></tr>
<tr><td>Grading rubric</td><td>Reference</td><td><a href="{{ '/assets/templates/Grading_Rubric.docx' | relative_url }}">.docx</a></td></tr>
<tr><td>Responsible AI Agreement</td><td>Orientation · Deliverable 1</td><td><a href="{{ '/assets/templates/Responsible_AI_Agreement.docx' | relative_url }}">.docx</a></td></tr>
</tbody>
</table>
</div>

## Instructor materials

- **[Facilitator Guide]({{ '/assets/templates/Facilitator_Guide.docx' | relative_url }})** — run-of-show for a
  2.5-hour meeting, breakout facilitation, grading the weekly mini-tasks, common student questions, UDL
  practices, what to do when a tool is down, and a pre-cohort checklist.
- **[Syllabus]({{ '/assets/Urban_AI_Syllabus.docx' | relative_url }})** — the full course syllabus.
- **Slide decks** — one starter deck per class, on each [class page]({{ '/classes/' | relative_url }}).
  Speaker notes are written for a TA who did not build the deck.
- **Notebooks** — in the [`notebooks/`]({{ site.course.repo_url }}/tree/main/notebooks) folder of the course repo.

## Lab notebooks

All eight Track B notebooks run in Google Colab with no installation, no API keys, and no network access. They
generate synthetic-but-realistic urban data in-notebook with a fixed seed, so every student sees the same
results and the labs work even when a data portal is down.

<div class="table-scroll">
<table>
<thead><tr><th>Lab</th><th>Notebook</th><th>Packages</th></tr></thead>
<tbody>
<tr><td><a href="{{ '/labs/lab-0/' | relative_url }}">Lab 0 · AI in the Browser</a></td><td><code>lab0_ai_in_the_browser.ipynb</code></td><td>pandas, matplotlib</td></tr>
<tr><td><a href="{{ '/labs/lab-1/' | relative_url }}">Lab 1 · Text Mining</a></td><td><code>lab1_text_mining.ipynb</code></td><td>pandas, scikit-learn, matplotlib</td></tr>
<tr><td><a href="{{ '/labs/lab-2/' | relative_url }}">Lab 2 · Clustering</a></td><td><code>lab2_clustering.ipynb</code></td><td>pandas, scikit-learn, matplotlib</td></tr>
<tr><td><a href="{{ '/labs/lab-3/' | relative_url }}">Lab 3 · Time Series</a></td><td><code>lab3_time_series.ipynb</code></td><td>pandas, statsmodels, matplotlib</td></tr>
<tr><td><a href="{{ '/labs/lab-4/' | relative_url }}">Lab 4 · Classification</a></td><td><code>lab4_classification.ipynb</code></td><td>pandas, scikit-learn, matplotlib</td></tr>
<tr><td><a href="{{ '/labs/lab-5/' | relative_url }}">Lab 5 · Risk-Response DSS</a></td><td><code>lab5_risk_response_dss.ipynb</code></td><td>numpy, pandas, matplotlib</td></tr>
<tr><td><a href="{{ '/labs/lab-6/' | relative_url }}">Lab 6 · DSS AI Lab</a></td><td><code>lab6_dss_ai_lab.ipynb</code></td><td>numpy, pandas, matplotlib</td></tr>
<tr><td><a href="{{ '/labs/lab-7/' | relative_url }}">Lab 7 · LLM Lab</a></td><td><code>lab7_llm_lab.ipynb</code></td><td>scikit-learn (TF-IDF retrieval)</td></tr>
</tbody>
</table>
</div>

## Real data to swap in

The notebooks ship with synthetic data so they always run. When you adapt them to your own city, these are the
sources to reach for:

- **City open-data portals** — 311 service requests, permits, code violations, crash records, parcel data.
- **U.S. Census / American Community Survey** — tract-level demographic and socioeconomic indicators.
- **EPA Air Quality System** — hourly and daily monitor data.
- **OpenStreetMap** — street networks, land use, points of interest.
- **State and regional agencies** — traffic counts, transit ridership, flood and heat exposure layers.
- **Local plan documents** — comprehensive plans, area plans, and public-comment records for retrieval and text mining.

<div class="warn">
  <strong>Before you use real data</strong>
  <p>Check the license, check for identifiable individuals, and check what the collection process left out. A
  dataset of 311 calls is a dataset of people who called 311.</p>
</div>

## Where to go next

- Further coursework at MSU in urban planning, data science, and computational modeling.
- Undergraduate research and living-learning communities working on urban and environmental problems.
- Professional pathways: planning agencies, transportation and environmental consulting, public administration,
  real estate development, and civic technology.
- Student facilitator roles in future Urban AI cohorts — completing students are eligible to apply.

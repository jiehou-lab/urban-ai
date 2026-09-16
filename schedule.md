---
layout: default
title: "Schedule"
subtitle: "Eight meetings of 2 hours, twice a week for four weeks. Sixteen hours total."
eyebrow: "Cohort 1 · Fall 2026"
permalink: /schedule/
---

{% assign teams = site.course.teams_url %}

<div class="note">
  <strong>{{ site.course.cohort_dates }}</strong>
  <p>{{ site.course.cohort_status }}. All meetings are online. Recordings and materials post to the
  {% if teams != "" %}<a href="{{ teams }}">course Teams site</a>{% else %}<span class="pending-link">course Teams site</span>{% endif %}
  within 24 hours.</p>
</div>

## The eight meetings

<ol class="timeline">

<li>
  <p class="when">Meeting 1 · Week 1</p>
  <h3>Welcome &amp; What Is Urban AI?</h3>
  <p><strong>Orientation (30 min)</strong> — how the course runs, approved AI tools, privacy and data rules,
  the AI readiness pre-survey, and the AI Use Log you will keep for four weeks.<br>
  <strong>Class 1-1 (60 min)</strong> — Urban analytics and smart cities to urban AI; how planning decisions
  actually get made; what a decision support system is. <em>Si Chen</em><br>
  <strong>Discussion Forum A launches (30 min)</strong> — real-world cases: where is Urban AI already deciding
  things? Post one case and summarize your group's discussion into a short slide.</p>
</li>

<li>
  <p class="when">Meeting 2 · Week 1</p>
  <h3>AI Basics for Urban Problems</h3>
  <p><strong>Class 1-2 (60 min)</strong> — Data, features, models, training and inference in plain language;
  supervised versus unsupervised; how language models differ; the failure modes worth memorizing. <em>Jie Hou</em><br>
  <strong>Lab (60 min)</strong> — Hands-on with ready-made AI apps — image classification, generation, text
  mining — plus a first k-means clustering run. <em>Jie Hou · Sean</em></p>
</li>

<li>
  <p class="when">Meeting 3 · Week 2</p>
  <h3>Urban Analytic Models I</h3>
  <p><strong>Class 2-1 (60 min)</strong> — Site analysis, weighted suitability, accessibility and simulation:
  what these models assume, and where a value judgment hides inside a technical choice. <em>Si Chen</em><br>
  <strong>Lab (60 min)</strong> — Spatial analysis and clustering: build a neighborhood typology and watch how
  the number of groups changes who gets grouped with whom. <em>Sean</em></p>
</li>

<li>
  <p class="when">Meeting 4 · Week 2</p>
  <h3>Urban Analytic Models II</h3>
  <p><strong>Class 2-2 (60 min)</strong> — Optimization, multi-objective tradeoffs, scenario testing and
  sensitivity: when the ranking flips, the answer was about your weights. <em>Si Chen</em><br>
  <strong>Lab (60 min)</strong> — Time series analysis on an urban signal, including a forecast that breaks
  when the underlying conditions change. <em>Sean</em></p>
</li>

<li>
  <p class="when">Meeting 5 · Week 3</p>
  <h3>Decision Support Systems I</h3>
  <p><strong>Class 3-1 (60 min)</strong> — DSS categories — data-driven, model-driven, knowledge-driven,
  communication-driven, document-driven — with deployed cases examined end to end. <em>Jie Hou &amp; Si Chen</em><br>
  <strong>Lab (60 min)</strong> — Risk-response DSS: score alternatives against weighted criteria, then stress
  test whether the ranking survives a change in those weights. <em>Yura</em></p>
</li>

<li>
  <p class="when">Meeting 6 · Week 3</p>
  <h3>Decision Support Systems II</h3>
  <p><strong>Class 3-2 (60 min)</strong> — AI-enhanced decision support: human-in-the-loop patterns, how to
  evaluate a system beyond model accuracy, and the failure modes that show up in practice. <em>Jie Hou</em><br>
  <strong>Lab (60 min)</strong> — DSS AI Lab: run two scenarios end to end and compare them on the same
  criteria. <em>Yura</em></p>
</li>

<li>
  <p class="when">Meeting 7 · Week 4</p>
  <h3>Language Models in Decision Support</h3>
  <p><strong>Class 4-1 (60 min)</strong> — What language models are useful for in a planning workflow,
  grounding answers in real documents, prompting patterns, and how to catch a confident wrong answer.
  <em>Jie Hou</em><br>
  <strong>Lab (60 min)</strong> — Text mining and clustering on community voice: surface the themes, then
  check whose voices are over- and under-represented. <em>Jie Hou &amp; Sean</em></p>
</li>

<li>
  <p class="when">Meeting 8 · Week 4</p>
  <h3>LLM Lab, Ethics, and Wrap-Up</h3>
  <p><strong>Lab (45 min)</strong> — LLM Lab: grounded versus ungrounded answers over a real planning document,
  and a hallucination log. <em>Jie Hou &amp; Yura</em><br>
  <strong>Class 4-2 (45 min)</strong> — AI ethics: bias, equity, privacy, transparency, accountability. <em>Jie Hou</em><br>
  <strong>Discussion Forum B and reflection (30 min)</strong> — whose city does the model see? Team share-outs,
  reflection, and the post-survey.</p>
</li>

</ol>

## What a meeting looks like

<div class="table-scroll">
<table>
<thead><tr><th>Time</th><th>Segment</th><th>Who</th></tr></thead>
<tbody>
<tr><td>0:00 – 0:05</td><td>Arrival and recap of where we are</td><td>Instructor</td></tr>
<tr><td>0:05 – 0:55</td><td>Concept class, with two check-for-understanding pauses</td><td>Instructor</td></tr>
<tr><td>0:55 – 1:05</td><td>Break</td><td>—</td></tr>
<tr><td>1:05 – 1:25</td><td>TA demo and explanation of the lab</td><td>TA</td></tr>
<tr><td>1:25 – 1:50</td><td>Breakout: teams run the lab and change parameters</td><td>Teams + TA</td></tr>
<tr><td>1:50 – 2:00</td><td>Report-outs and reflection prompts</td><td>All</td></tr>
</tbody>
</table>
</div>

Every lab runs in the browser. There is nothing to install and no coding required.

## Attendance and participation

Attend at least 7 of the 8 meetings. Short write-ups and lab outputs are **encouraged but not required** — the
teaching team gives feedback on anything you submit, and submitting is the fastest way to get it. Completing
students receive a non-credit certificate and a Spartan Experience Record entry.

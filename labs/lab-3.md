---
layout: default
title: "Lab 3 — Time Series Analysis"
parent: "Labs"
subtitle: "Trend, seasonality, and the forecast that breaks the moment the world changes."
eyebrow: "Lab 3 · Meeting 5"
permalink: /labs/lab-3/
---

<ul class="meta">
  <li><strong>Meeting</strong> 5</li>
  <li><strong>TA lead</strong> Sean</li>
  <li><strong>Length</strong> 60 min</li>
  <li><strong>Produces</strong> Trend brief (150 words) with an explicit forecast caveat.</li>
</ul>

Decompose an hourly urban series, produce a short forecast, and state the conditions under which it fails.

<div class="tracks">
  <div class="track">
    <h3>Track A <span class="badge">No code · default</span></h3>
    <p>Web tools only. No installation, no Python. Produces the same artifact as Track B.</p>
    <ol>
      <li>Filter the supplied traffic and air-quality series in a chart tool.</li>
      <li>Identify the daily and weekly cycles by eye.</li>
      <li>Mark the point where the pattern breaks.</li>
    </ol>
  </div>
  <div class="track track-b">
    <h3>Track B <span class="badge">Colab · go deeper</span></h3>
    <p>A pre-filled notebook. You run cells and change the parameters marked <code># ▶ CHANGE ME</code>. You never write code from scratch.</p>
    <ol>
      <li>Decompose the series into trend, seasonality, and residual.</li>
      <li>Fit a simple forecast and change the horizon.</li>
      <li>Forecast across a deliberate regime change and measure the error.</li>
    </ol>
    <p><a class="btn btn-sm" href="https://colab.research.google.com/github/jiehou-lab/urban-ai/blob/main/notebooks/lab3_time_series.ipynb">Open in Colab</a></p>
  </div>
</div>

## What you turn in

Trend brief (150 words) with an explicit forecast caveat.

<div class="warn">
  <strong>Responsible AI moment</strong>
  <p>The series contains a structural break. A model fit before it forecasts confidently and wrongly after it. That is what a pandemic, a new transit line, or a closed bridge does to your data.</p>
</div>

## Reflection prompts

Every lab ends with the same four questions. Answer them in your lab submission.

- What did the tool assume?
- Who is missing from this data?
- What would change your recommendation?
- What must a human verify before this is used?

<div class="prevnext">
  <span><a href="{{ "/labs/lab-2/" | relative_url }}">← Lab 2</a></span>
  <span><a href="{{ "/labs/lab-4/" | relative_url }}">Lab 4 →</a></span>
</div>

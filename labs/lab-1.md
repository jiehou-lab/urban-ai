---
layout: default
title: "Lab 1 — Text Mining Community Voice"
parent: "Labs"
subtitle: "Turning hundreds of reviews and comments into themes — and noticing who is missing."
eyebrow: "Lab 1 · Meeting 3"
permalink: /labs/lab-1/
---

<ul class="meta">
  <li><strong>Meeting</strong> 3</li>
  <li><strong>TA lead</strong> Sean</li>
  <li><strong>Length</strong> 60 min</li>
  <li><strong>Produces</strong> Top-themes table plus one written bias note naming an under-represented group.</li>
</ul>

Extract themes from geolocated reviews and public comment, and quantify whose voices dominate.

<div class="tracks">
  <div class="track">
    <h3>Track A <span class="badge">No code · default</span></h3>
    <p>Web tools only. No installation, no Python. Produces the same artifact as Track B.</p>
    <ol>
      <li>Paste the supplied review corpus into an approved text-analysis tool.</li>
      <li>Produce a theme list and a sentiment summary.</li>
      <li>Fill in the representation table by neighborhood.</li>
    </ol>
  </div>
  <div class="track track-b">
    <h3>Track B <span class="badge">Colab · go deeper</span></h3>
    <p>A pre-filled notebook. You run cells and change the parameters marked <code># ▶ CHANGE ME</code>. You never write code from scratch.</p>
    <ol>
      <li>Run TF-IDF, sentiment scoring, and keyword-based topic extraction over the corpus.</li>
      <li>Change the stopword list and the number of topics; watch the themes shift.</li>
      <li>Compute comments per capita by neighborhood.</li>
    </ol>
    <p><a class="btn btn-sm" href="https://colab.research.google.com/github/jiehou-lab/urban-ai/blob/main/notebooks/lab1_text_mining.ipynb">Open in Colab</a></p>
  </div>
</div>

## What you turn in

Top-themes table plus one written bias note naming an under-represented group.

<div class="warn">
  <strong>Responsible AI moment</strong>
  <p>The notebook shows one neighborhood contributing roughly half the comments per resident that another does. Any theme ranking inherits that imbalance.</p>
</div>

## Reflection prompts

Every lab ends with the same four questions. Answer them in your lab submission.

- What did the tool assume?
- Who is missing from this data?
- What would change your recommendation?
- What must a human verify before this is used?

<div class="prevnext">
  <span><a href="{{ "/labs/lab-0/" | relative_url }}">← Lab 0</a></span>
  <span><a href="{{ "/labs/lab-2/" | relative_url }}">Lab 2 →</a></span>
</div>

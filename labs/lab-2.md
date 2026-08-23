---
layout: default
title: "Lab 2 — Clustering Analysis"
parent: "Labs"
subtitle: "Building a neighborhood typology — and seeing how the choice of k redraws the map."
eyebrow: "Lab 2 · Meeting 4"
permalink: /labs/lab-2/
---

<ul class="meta">
  <li><strong>Meeting</strong> 4</li>
  <li><strong>TA lead</strong> Sean</li>
  <li><strong>Length</strong> 90 min</li>
  <li><strong>Produces</strong> Neighborhood typology table plus a written justification for your chosen k.</li>
</ul>

Group census tracts into types from socioeconomic and built-environment indicators, and justify the number of groups.

<div class="tracks">
  <div class="track">
    <h3>Track A <span class="badge">No code · default</span></h3>
    <p>Web tools only. No installation, no Python. Produces the same artifact as Track B.</p>
    <ol>
      <li>Use the interactive cluster explorer with the supplied tract indicators.</li>
      <li>Move the group-count slider from 3 to 6 and note which tracts change groups.</li>
      <li>Name each cluster in plain language.</li>
    </ol>
  </div>
  <div class="track track-b">
    <h3>Track B <span class="badge">Colab · go deeper</span></h3>
    <p>A pre-filled notebook. You run cells and change the parameters marked <code># ▶ CHANGE ME</code>. You never write code from scratch.</p>
    <ol>
      <li>Standardize features, run k-means, and read a silhouette plot.</li>
      <li>Change k and the feature set with the marked parameters.</li>
      <li>Track which tracts move between clusters as k changes.</li>
    </ol>
    <p><a class="btn btn-sm" href="https://colab.research.google.com/github/jiehou-lab/urban-ai/blob/main/notebooks/lab2_clustering.ipynb">Open in Colab</a></p>
  </div>
</div>

## What you turn in

Neighborhood typology table plus a written justification for your chosen k.

<div class="warn">
  <strong>Responsible AI moment</strong>
  <p>Cluster membership is not a fact about a neighborhood. It is a consequence of your feature choice and your k. Show the tracts that moved.</p>
</div>

## Reflection prompts

Every lab ends with the same four questions. Answer them in your lab submission.

- What did the tool assume?
- Who is missing from this data?
- What would change your recommendation?
- What must a human verify before this is used?

<div class="prevnext">
  <span><a href="{{ "/labs/lab-1/" | relative_url }}">← Lab 1</a></span>
  <span><a href="{{ "/labs/lab-3/" | relative_url }}">Lab 3 →</a></span>
</div>

---
layout: default
title: "Lab 5 — Risk-Response DSS"
parent: "Labs"
subtitle: "A weighted decision matrix for flood and heat risk — and the sweep that shows it is fragile."
eyebrow: "Lab 5 · Meeting 6"
permalink: /labs/lab-5/
---

<ul class="meta">
  <li><strong>Meeting</strong> 6</li>
  <li><strong>TA lead</strong> Yura</li>
  <li><strong>Length</strong> 75 min</li>
  <li><strong>Produces</strong> Ranked alternatives with a sensitivity chart.</li>
</ul>

Rank response alternatives against weighted criteria, then test whether the ranking survives a change in weights.

<div class="tracks">
  <div class="track">
    <h3>Track A <span class="badge">No code · default</span></h3>
    <p>Web tools only. No installation, no Python. Produces the same artifact as Track B.</p>
    <ol>
      <li>Fill the weighted decision matrix template with the supplied risk data.</li>
      <li>Score three response alternatives against five criteria.</li>
      <li>Change the weights by hand and see whether the winner changes.</li>
    </ol>
  </div>
  <div class="track track-b">
    <h3>Track B <span class="badge">Colab · go deeper</span></h3>
    <p>A pre-filled notebook. You run cells and change the parameters marked <code># ▶ CHANGE ME</code>. You never write code from scratch.</p>
    <ol>
      <li>Compute weighted scores across a full sweep of weight combinations.</li>
      <li>Plot how often each alternative wins.</li>
      <li>Identify the criterion that controls the outcome.</li>
    </ol>
    <p><a class="btn btn-sm" href="https://colab.research.google.com/github/jiehou-lab/urban-ai/blob/main/notebooks/lab5_risk_response_dss.ipynb">Open in Colab</a></p>
  </div>
</div>

## What you turn in

Ranked alternatives with a sensitivity chart.

<div class="warn">
  <strong>Responsible AI moment</strong>
  <p>If your recommendation flips when equity weight moves from 0.2 to 0.3, your recommendation is a statement about your weights, not about the city. Say so.</p>
</div>

## Reflection prompts

Every lab ends with the same four questions. Answer them in your lab submission.

- What did the tool assume?
- Who is missing from this data?
- What would change your recommendation?
- What must a human verify before this is used?

<div class="prevnext">
  <span><a href="{{ "/labs/lab-4/" | relative_url }}">← Lab 4</a></span>
  <span><a href="{{ "/labs/lab-6/" | relative_url }}">Lab 6 →</a></span>
</div>

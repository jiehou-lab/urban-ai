---
layout: default
title: "Lab 4 — Classification"
parent: "Labs"
subtitle: "Predicting building condition — then asking whose buildings the model gets wrong."
eyebrow: "Lab 4 · Meeting 5"
permalink: /labs/lab-4/
---

<ul class="meta">
  <li><strong>Meeting</strong> 5</li>
  <li><strong>TA lead</strong> Sean</li>
  <li><strong>Length</strong> 60 min</li>
  <li><strong>Produces</strong> Subgroup error table plus a fairness note in plain language.</li>
</ul>

Train a classifier on parcel data and audit its errors by subgroup.

<div class="tracks">
  <div class="track">
    <h3>Track A <span class="badge">No code · default</span></h3>
    <p>Web tools only. No installation, no Python. Produces the same artifact as Track B.</p>
    <ol>
      <li>Use a no-code classifier interface on the supplied parcel table.</li>
      <li>Read the confusion matrix.</li>
      <li>Fill in the subgroup error table.</li>
    </ol>
  </div>
  <div class="track track-b">
    <h3>Track B <span class="badge">Colab · go deeper</span></h3>
    <p>A pre-filled notebook. You run cells and change the parameters marked <code># ▶ CHANGE ME</code>. You never write code from scratch.</p>
    <ol>
      <li>Fit logistic regression and a decision tree; compare them.</li>
      <li>Change the decision threshold and watch precision and recall trade off.</li>
      <li>Compute error rate, false-positive rate, and false-negative rate by income group.</li>
    </ol>
    <p><a class="btn btn-sm" href="https://colab.research.google.com/github/jiehou-lab/urban-ai/blob/main/notebooks/lab4_classification.ipynb">Open in Colab</a></p>
  </div>
</div>

## What you turn in

Subgroup error table plus a fairness note in plain language.

<div class="warn">
  <strong>Responsible AI moment</strong>
  <p>Overall accuracy hides the gap. In the supplied data the error rate for low-income tracts runs roughly twice that of high-income tracts. A single accuracy number would have told you nothing.</p>
</div>

## Reflection prompts

Every lab ends with the same four questions. Answer them in your lab submission.

- What did the tool assume?
- Who is missing from this data?
- What would change your recommendation?
- What must a human verify before this is used?

<div class="prevnext">
  <span><a href="{{ "/labs/lab-3/" | relative_url }}">← Lab 3</a></span>
  <span><a href="{{ "/labs/lab-5/" | relative_url }}">Lab 5 →</a></span>
</div>

---
layout: default
title: "Lab 7 — LLM Lab"
parent: "Labs"
subtitle: "Grounded versus ungrounded answers over a real planning document."
eyebrow: "Lab 7 · Meeting 8"
permalink: /labs/lab-7/
---

<ul class="meta">
  <li><strong>Meeting</strong> 8</li>
  <li><strong>TA lead</strong> Jie Hou & Yura</li>
  <li><strong>Length</strong> 30 min</li>
  <li><strong>Produces</strong> Grounded stakeholder memo plus a hallucination log.</li>
</ul>

Produce a stakeholder memo grounded in a supplied plan excerpt, and log every claim the model could not support.

<div class="tracks">
  <div class="track">
    <h3>Track A <span class="badge">No code · default</span></h3>
    <p>Web tools only. No installation, no Python. Produces the same artifact as Track B.</p>
    <ol>
      <li>Use structured prompting against the supplied comprehensive-plan excerpt.</li>
      <li>Require quotes and page references in every answer.</li>
      <li>Run the hallucination hunt: ask three questions the document cannot answer.</li>
    </ol>
  </div>
  <div class="track track-b">
    <h3>Track B <span class="badge">Colab · go deeper</span></h3>
    <p>A pre-filled notebook. You run cells and change the parameters marked <code># ▶ CHANGE ME</code>. You never write code from scratch.</p>
    <ol>
      <li>Run the retrieval-and-template demo: grounded answers with a confidence threshold.</li>
      <li>Change the threshold and watch questions move between 'answered' and 'cannot answer'.</li>
      <li>Compare grounded output against a naive ungrounded answer.</li>
    </ol>
    <p><a class="btn btn-sm" href="https://colab.research.google.com/github/jiehou-lab/urban-ai/blob/main/notebooks/lab7_llm_lab.ipynb">Open in Colab</a></p>
  </div>
</div>

## What you turn in

Grounded stakeholder memo plus a hallucination log.

<div class="warn">
  <strong>Responsible AI moment</strong>
  <p>Three of the six test questions cannot be answered from the document. A well-configured system says so. An unconfigured one answers all six fluently.</p>
</div>

## Reflection prompts

Every lab ends with the same four questions. Answer them in your lab submission.

- What did the tool assume?
- Who is missing from this data?
- What would change your recommendation?
- What must a human verify before this is used?

<div class="prevnext">
  <span><a href="{{ "/labs/lab-6/" | relative_url }}">← Lab 6</a></span>
  <span><a href="{{ "/deliverables/" | relative_url }}">Deliverables →</a></span>
</div>

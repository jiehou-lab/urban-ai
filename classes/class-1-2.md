---
layout: default
title: "Class 1-2 — AI Basics for Urban Problems"
parent: "Classes"
subtitle: "What a model is, what training means, and why the answer is sometimes confidently wrong."
eyebrow: "Class 1-2 · Meeting 2"
permalink: /classes/class-1-2/
---

<ul class="meta">
  <li><strong>Meeting</strong> 2</li>
  <li><strong>Lead</strong> Jie Hou</li>
  <li><strong>Length</strong> 75 min</li>
  <li><strong>Slides</strong> <a href="{{ '/assets/slides/class1-2_ai_basics.pptx' | relative_url }}">class1-2_ai_basics.pptx</a></li>
</ul>

## Learning objectives

By the end of this class you will be able to:

1. Explain data, features, model, training, and inference in plain language, using an urban example throughout.
2. Tell supervised from unsupervised learning and match each to a planning question.
3. Explain in one sentence why a language model can produce fluent text that is factually false.
4. Recognize overfitting, data leakage, and biased training data when shown an example.

## Session outline

**The vocabulary, once.** Row, column, label, feature, model, parameter, training, inference — each defined against a table of city parcels.

**Supervised learning.** You have labels and want to predict them: which buildings are in poor condition, which permits will be delayed.

**Unsupervised learning.** You have no labels and want structure: which neighborhoods resemble each other, what themes appear in public comment.

**How a model is evaluated.** Train/test split, accuracy versus the base rate, and why a single accuracy number hides who the model fails.

**Where language models differ.** Next-token prediction, why fluency is not accuracy, and what grounding means.

**Four failure modes to memorize.** Overfitting, leakage, distribution shift, and biased labels — each with an urban example.


## In-class activity

**Breakout (20 min).** You are given two model report cards for the same building-condition model: one shows 91% accuracy overall, the other shows accuracy by neighborhood. Decide as a group whether you would deploy it and write the one condition you would attach.

## What comes next

**Lab 0 — AI in the Browser + First Colab.** Your first AI Use Log entry is due at the end of the lab.

<div class="prevnext">
  <span><a href="{{ "/classes/class-1-1/" | relative_url }}">← Class 1-1</a></span>
  <span><a href="{{ "/classes/class-2-1/" | relative_url }}">Class 2-1 →</a></span>
</div>

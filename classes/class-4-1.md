---
layout: default
title: "Class 4-1 — Large Language Models in Decision Support"
parent: "Classes"
subtitle: "What LLMs are good for in a planning workflow, and how to keep them tethered to evidence."
eyebrow: "Class 4-1 · Meeting 8"
permalink: /classes/class-4-1/
---

<ul class="meta">
  <li><strong>Meeting</strong> 8</li>
  <li><strong>Lead</strong> Jie Hou</li>
  <li><strong>Length</strong> 30 min</li>
  <li><strong>Slides</strong> <a href="{{ '/assets/slides/class4-1_llm_dss.pptx' | relative_url }}">class4-1_llm_dss.pptx</a></li>
</ul>

## Learning objectives

By the end of this class you will be able to:

1. Describe what an LLM does and why grounding changes its reliability.
2. Use retrieval-augmented prompting over a real plan document.
3. Write a prompt that requests sources and flags uncertainty.
4. Detect and log a hallucination.

## Session outline

**What the model is doing.** Prediction over text, why it sounds certain, and where the knowledge actually lives.

**Useful jobs in planning.** Summarizing public comment, drafting plain-language explanations, structuring criteria, translating jargon for residents.

**Jobs to refuse.** Inventing data, deciding, and anything where a wrong answer reaches a resident unreviewed.

**Grounding and retrieval.** Giving the model the document and requiring quotes. Grounded versus ungrounded, side by side.

**Prompt patterns that help.** Role, task, constraints, format, sources, and an explicit 'say I don't know' instruction.

**The hallucination log.** How to record what the model got wrong, so the next cohort inherits your findings.


## In-class activity

**Breakout (15 min).** Ask the same question of a grounded and an ungrounded assistant. Record both answers and mark every claim you cannot verify in the source document.

## What comes next

**Lab 7 — LLM Lab**, then Class 4-2 on ethics and the final presentations.

<div class="prevnext">
  <span><a href="{{ "/classes/class-3-2/" | relative_url }}">← Class 3-2</a></span>
  <span><a href="{{ "/classes/class-4-2/" | relative_url }}">Class 4-2 →</a></span>
</div>

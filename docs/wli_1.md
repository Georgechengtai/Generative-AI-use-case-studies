---
title: "Why AI Disappoints: Prompt, Context, and Harness Engineering"
description: Three familiar frustrations with AI chatbots, and the engineering disciplines that have grown up around each one. A non-technical introduction.
---

# Why AI Disappoints: Prompt, Context, and Harness Engineering

!!! example "Editor's Word"

    You have probably felt three frustrations when talking to an AI. The first answer is plausible but generic. The next is on-topic, yet somehow misses what you actually needed. After a long back-and-forth, the model drifts, repeats a mistake you already corrected, and announces completion of something it never finished.

    Each of these has prompted its own engineering response: **prompt engineering**, **context engineering**, and **harness engineering**. The names sound technical, though the ideas behind them are not, and the vocabulary helps you read AI behaviour better even if you never build anything yourself.

The aim of this page is modest. It puts a label on something you have probably already noticed, points at the people who think about it for a living, and lets you decide how far to go. A [companion post](wli_2.md) takes the coding-flavoured angle for readers who want a real taste of the third discipline.

## When the answer is generic — *prompt engineering*

The chatbot's first answer reads like an encyclopaedia entry. Ask about supply and demand and you get the same paragraph any textbook would offer. The model has nothing in particular to aim at except the most average version of your question, so it gives you the most average answer back.

**Prompt engineering** is the craft of giving the model something to aim at: a role, a format, an audience, an example, a constraint — anything that narrows the field. The site has a [dedicated section on prompt engineering](pe_g.md) with four core techniques and a small library of templates.

Two habits cover most of the value here. Say what the output should look like, and tell the model who it is supposed to be. Beyond those, the rest is polish.

## When the answer is off-topic — *context engineering*

Once the phrasing is right, the next disappointment is subtler. The answer is fine in the abstract and useless to you. Your draft sits in a Hong Kong context, but the model quotes American statistics; you uploaded a syllabus, but the model recommends readings you already have. The phrasing was fine; the model simply could not see what it needed to see.

**Context engineering** is the craft of curating what the model has in working memory at the moment of answering: which documents to include, which prior messages to keep, which tool results to format and pass back, and what to drop when the conversation runs long. Retrieval and persistent memory both live here.

For most chat users, the discipline shows up as one practical habit. Paste the relevant material at the start of the conversation, and start a fresh chat when the topic changes. Those two moves cover roughly 90% of it.

## When the answer drifts, repeats, or lies about being done — *harness engineering*

The third frustration shows up in long conversations, especially the ones where the model performs many small tasks in sequence. The model forgets a constraint it agreed to ten messages ago. It makes the same mistake it just apologised for. It announces a task complete without checking. Researchers at Anthropic have a name for that last behaviour: *context anxiety*, the rushed-to-finish pattern that appears as a model's working memory fills up.

**Harness engineering** is the craft of building the operational envelope around the model — and the key word there is *operational*, not *advisory*. The harness is not a checklist for a human to apply by eye. It is the machinery that lets the system itself verify the model's work, enforce the rules the model must respect, and carry state forward across sessions. Concretely: which tools the model can call, which actions are off-limits, which checks must run *automatically* on its output before completion is granted, and what gets remembered the next time it returns to the task.

The most systematic published treatment so far comes from Birgitta Böckeler (ThoughtWorks), [writing on Martin Fowler's site](https://martinfowler.com/articles/harness-engineering.html) in April 2026. She frames a harness as two halves working together: **guides** that shape the agent before it acts (architecture rules, written conventions, linters), and **sensors** that catch the agent after the fact (tests, type checks, code review). Without the guides, the agent has no way to comply with rules it has never seen; without the sensors, the agent repeats its own mistakes because nothing tells it they were mistakes.

Where prompt engineering asks how to talk to the model, and context engineering asks what the model should see, harness engineering asks what runs around the model so that real work gets finished without a human watching every step.

??? note "Where these three names came from"

    Each term entered AI engineering at a different moment, usually in response to the limits of the discipline before it.

    - **Prompt engineering** spread once GPT-3 made phrasing matter, roughly 2022 to 2023. The site's [How to Prompt Chatbots](pe_g.md) page links the foundational guides from Anthropic, OpenAI, and Google.
    - **Context engineering** emerged through 2024 as conversations grew longer and tool use got noisier. Retrieval-augmented generation and long-context models pushed working-memory curation into the foreground.
    - **Harness engineering** circulated through 2025 blog posts and received its most systematic treatment when Birgitta Böckeler (ThoughtWorks) published her framework on Martin Fowler's site in April 2026. [Learn Harness Engineering](https://walkinglabs.github.io/learn-harness-engineering/en/) collects the lineage into a single guided path.

## What this means if you are not building anything

Building harnesses is a developer's job, and so is most of the day-to-day practice of context engineering. For most readers, the three disciplines will stay at the level of ideas — but the ideas still transfer.

A generic answer means the prompt needs more constraint. An off-topic answer means the model is missing material. A confident "I'm done" is the moment to ask what *a system*, not just you, would do to verify the claim — because in a serious harness, no completion is granted without an automatic check, and that habit of mind is the part of harness engineering worth borrowing. When AI lets you down, the better question is usually what was missing from its surroundings, rather than what was wrong with the model.

??? tip "One habit per discipline, if you only take three things away"

    Three reflexes cover most chat-user scenarios, each one borrowing from a different discipline. Each fits into a single question you can ask yourself before you press send or trust an answer.

    - **Prompt engineering** — *before sending:* who should the AI be, and what should the output look like?
    - **Context engineering** — *before sending:* what do I need to paste in so the answer is relevant to me?
    - **Harness engineering** — *before trusting:* what automatic check could a system run on this answer, that I would not need to read myself?

!!! info "Further reading"

    - [How to Prompt Chatbots — Section Overview](pe_g.md) — this site's existing toolkit, with four core techniques and ready-made templates.
    - [Learn Harness Engineering](https://walkinglabs.github.io/learn-harness-engineering/en/) — a structured learning path for readers who want to go deeper.
    - [Birgitta Böckeler — Harness engineering for coding agent users](https://martinfowler.com/articles/harness-engineering.html) — the guides/sensors framework summarised above.
    - [Mitchell Hashimoto — My AI Adoption Journey](https://mitchellh.com/writing/my-ai-adoption-journey) — a senior engineer's honest progression from sceptic to convert.
    - [What Is Harness Engineering — goat-flow](https://goat-flow.com/what-is-harness-engineering) — a concise reference focused on guardrails, memory, and workflows.

    A coding-flavoured follow-up: [What Harness Engineering Looks Like (And Why It Is Mostly Code)](wli_2.md).

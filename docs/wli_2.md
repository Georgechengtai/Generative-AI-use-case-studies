---
title: "What Harness Engineering Looks Like (And Why It Is Mostly Code)"
description: A non-technical taste of harness engineering — the recurring concerns it names, what coding teams have got working well, and where the field still cannot tell whether the AI did what was needed.
---

# What Harness Engineering Looks Like (And Why It Is Mostly Code)

!!! example "Editor's Word"

    A [previous post](wli_1.md) named three frustrations with AI chatbots and pinned each one to a discipline. This page zooms in on the third — harness engineering — and walks through what the field actually attempts, where coding has made it work, and where it still stops.

!!! note "Before you read"

    Public writing on harness engineering tends to emphasise the wins. This page gives the limits roughly equal room; both halves are necessary for an honest picture.

## Why coding became harness engineering's home

Harness engineering exists to make systems built with AI reliable enough to walk away from. To do that, you need a cheap way to ask, after each step the AI takes, *is the work right?* Coding is the rare place where part of that question can be answered by a machine. A computer can run the new code, see whether it crashes, see whether the existing checks still pass, and see whether the style matches the rest of the project. Most of the wins the field talks about live in this automatic-checking layer.

In early 2026 the researcher Can Bölük changed only the tool that one AI used to make small edits to code, while keeping the AI itself fixed. On the test he was running, the weakest model jumped from a 6.7% success rate to 68.3%. The test measured something specific: whether the AI could undo known small bugs in a fixed body of code. It says nothing about whether the AI could have *designed* the change. ([Can Bölük, *The Harness Problem*, Feb 2026](https://blog.can.ac/2026/02/12/the-harness-problem/).) That distinction returns further down.

## What harness engineering actually addresses

Read enough of the field and the same five concerns keep coming up. Each one names a thing the surroundings around the AI need to handle, and a failure that happens when they do not.

| Concern        | What it covers                                  | What fails without it                            |
| -------------- | ----------------------------------------------- | ------------------------------------------------ |
| Context        | What the AI gets to read before it acts         | The AI makes things up or pads with filler       |
| Constraints    | What the AI must never do                       | Destructive or irreversible actions slip through |
| Verification   | How the AI's work is checked after the fact     | Silent breakage; "I am done" without proof       |
| Recovery       | How work survives interruption                  | Losing the plot after a crash or restart         |
| Feedback loop  | How recurring mistakes become permanent fixes   | The same problem returns in a different form     |

A good setup addresses all five; most real systems are weak on at least two. When coding teams have written rules for the first, a short list of automatic checks for the third, and a habit of capturing past failures for the fifth, they reliably see real improvements — the kind Bölük measured, and the kind in the example further down this page. That is harness engineering at its strongest.

??? note "What 'automatic checks' actually look like"

    A few of the checks the field relies on:

    - **Tests** — small programs that exercise other programs and confirm they behave as expected.
    - **Linters** — tools that scan code for stylistic inconsistencies and suspicious patterns.
    - **Type checks** — tools that confirm the values flowing through a program are of the expected kinds.

    These show the code is not obviously broken. They are not a proof that the code is right.

## The harder question — did the AI build the right thing?

Of the five concerns above, *Verification* is the one the field has solved only partway. Automatic checks can tell you that the code runs, that the style is consistent, that the existing tests still pass. They cannot tell you whether the thing the AI built was the right thing — whether it solves the problem the user actually had, in the way the user actually needed.

Birgitta Böckeler (ThoughtWorks), in [the most systematic published framework so far](https://martinfowler.com/articles/harness-engineering.html), calls this *the elephant in the room*. A cross-reading of fifteen papers in the field finds that every one has tried a different approach to it, and none has given a convincing answer. ([Evaluation is the Elephant in the Room](https://github.com/deusyu/harness-engineering/blob/main/thinking/evaluation-elephant-in-the-room.md).)

Three reasons it stays open:

1. **Passing the checks is not the same as being right.** The checks only know what someone thought to ask about. One developer working with AI had more than 500 tests passing on his project and still found, weeks in, that several pieces had been designed wrong and had to be thrown away. If the AI also misread the original request, every check still passes — the checks verify what the AI decided to build, not what was asked for.
2. **The AI is not an honest examiner of its own work.** Anthropic's engineers reported that an AI asked to grade something it just produced tends to praise the work even when the quality is mediocre. The same model is not a useful second opinion on itself.
3. **A reliable AI examiner has to be at least as capable as the AI it is examining.** If you have something that strong, you no longer need the original. The circular problem (a regulator needs at least as much variety as the thing it regulates) is why the field treats this as deep, not merely unsolved.

The plain summary: a well-built setup can hand you a confident *I am done* without ever telling you whether the work was right. That confidence is exactly what makes the unverified case dangerous.

??? note "The framework behind these observations"

    Birgitta Böckeler organises the harness on two axes. The first axis is *guides* (things that shape the AI before it acts: written rules, conventions, automatic refusals) versus *sensors* (things that catch problems after the AI acts: tests, type checks, code review). The second axis is *computational* — deterministic checks like a linter or type checker, cheap and fast — versus *inferential*, which means using another AI as a judge, slower and more expensive and itself fallible. Most of what the field has reliably automated lives in the computational quadrant. Most of the recent excitement, and most of the unsolved problems, live in the inferential quadrant.

## A real example, and what it does and does not show

A small team asked an AI coding agent to add a new feature to an application they ran. The first instruction was one sentence. The agent spent close to half of its available memory exploring the project just to learn the conventions, then wrote something that looked plausible but used out-of-date code patterns and announced it was finished despite an error in the new feature.

The team then added three things, each strengthening one of the five concerns above: a short written description of how the project was organised (Context), an explicit list of automatic checks the agent had to run before claiming completion (Verification), and a record of past decisions about how the system was built (Feedback loop). The same task succeeded on three subsequent attempts, with the agent spending roughly 60% less effort on exploration. That is the strongest part of harness engineering working as advertised — three of the five concerns directly addressed, results that follow.

Notice the other side, though. The team's setup could tell them the new code matched the rest of the project, did not crash, and did not break any existing tests. It could not tell them whether the new feature did what the people using the application actually needed. For that, a human still had to read the code and try the result.

??? note "The same example with the technical details"

    The original task: *"Add a user-preferences endpoint at `/api/v2/users` in the existing FastAPI service."* The codebase was a Python web app of about 15,000 lines built on FastAPI, PostgreSQL, and Redis.

    The agent's failures:

    - It used **SQLAlchemy 1.x** syntax even though the project had migrated to 2.0.
    - It did not follow the project's existing error-handling pattern.
    - It declared the work complete despite a runtime exception in the new endpoint.

    The harness changes the team added:

    - **`AGENTS.md`** — a written file describing the architecture and tech-stack versions.
    - **Explicit verification commands** — for example `pytest tests/api/v2/ && python -m mypy src/`, run before declaring completion.
    - **Architecture decision records** — short notes explaining past design choices.

    Same model, same task, different harness. Drawn from harness-engineering field reports.

## What this means for you

Two habits worth keeping, and one caveat that keeps them honest.

The first habit is **deciding what "done" means before you start**, in a way the AI cannot just claim. What evidence would convince a sceptical reader? A checklist someone else could tick off? A specific output that exists or does not? A test that runs without your eyes on it? The model's confidence does not count. This is the habit closest to actual practice, even when borrowed without any of the supporting machinery.

The second is the **blameless** reflex. When the AI gets something wrong, the natural response is to blame the model, or yourself for phrasing the request badly. Try instead to change the surroundings so the same mistake cannot recur — add a written rule, add an automatic check, change the way the work is set up. Treat every failure as a missing guardrail rather than a missing instruction. The reflex transfers cleanly to writing, research, teaching, and most kinds of work where you collaborate with someone who will not always get it right.

The caveat is the elephant. Passing the checks tells you the work is not obviously broken; it does not tell you whether the work is *right*, in the sense of doing what someone actually needed. The field has no automated answer for that yet. Where AI hands you something that runs cleanly and sounds confident, the most useful question is the one the discipline cannot yet answer for you: **is this what was actually needed?**

!!! info "Further reading"

    - [Learn Harness Engineering](https://walkinglabs.github.io/learn-harness-engineering/en/) — a structured learning path, the most accessible starting point.
    - [Birgitta Böckeler — Harness engineering for coding agent users](https://martinfowler.com/articles/harness-engineering.html) — the most systematic published framework, with the guides/sensors taxonomy.
    - [Evaluation is the Elephant in the Room](https://github.com/deusyu/harness-engineering/blob/main/thinking/evaluation-elephant-in-the-room.md) — a cross-cutting critique of fifteen harness articles, focused on what the field has not yet solved.
    - [Can Bölük — The Harness Problem](https://blog.can.ac/2026/02/12/the-harness-problem/) — read with the caveat that the benchmark measures mechanical edits, not design correctness.
    - [Mitchell Hashimoto — My AI Adoption Journey](https://mitchellh.com/writing/my-ai-adoption-journey) — an experienced engineer's honest account of where AI helps and where it does not.

    For the broader frame this page sits inside, see the non-technical companion: [Why AI Disappoints: Prompt, Context, and Harness Engineering](wli_1.md).

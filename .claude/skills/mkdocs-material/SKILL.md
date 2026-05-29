---
name: mkdocs-material
description: Formatting conventions for the "Generative AI Use Case Studies" site (MkDocs 1.6 + Material 9.7). Use whenever drafting or editing a page for this site. Covers frontmatter, admonitions (including collapsible variants), code fences, tables, links, and the site's voice rules.
---

# MkDocs Material — Site Formatting Skill

This skill captures the conventions used by the **Generative AI Use Case Studies** site (CUHK Faculty of Social Science). Use it any time you draft, edit, or convert content for the site. The site runs **MkDocs 1.6.1** with **Material for MkDocs 9.7.1**.

> The site does **not** display author/byline. Leave `author` out of frontmatter unless the user explicitly asks for it.

---

## 1. Frontmatter

Keep frontmatter **minimal**. The site uses standard MkDocs page rendering — most metadata is generated automatically. The fields you should usually include:

```yaml
---
title: Short Page Title (matches the H1)
description: One-sentence summary; appears in social cards and search.
---
```

Optional fields, only if the user asks or the surrounding pages use them:

- `tags: [prompt-engineering, harness-engineering]` — only if the tags plugin is enabled
- `hide: [navigation]` or `hide: [toc]` — only for full-bleed pages

**Do not** add `author`, `date`, or `slug` unless the user instructs. They are not used elsewhere on the site.

---

## 2. Voice & spelling

- **British / Hong Kong English**: *specialise, personalise, summarise, behaviour, programme, organise*.
- **Direct address**: write "you" and "your", not "the reader" or "one".
- **Conversational and lightly opinionated**, never academic. Short paragraphs (2–4 sentences). Numbered lists with bold lead-ins are common.
- **Stateless paragraphs**: each section should be readable on its own. Readers land on individual pages from search; do not assume they read the previous post in a series unless the page explicitly says so.
- **Never try to explain a concept in full**. State the core, name the relationship to neighbouring terms, and link out for depth.

### 2a. Humane prose rules (from `pe_t6`)

The site has a dedicated [page on making AI text sound more human](pe_t6.md). When drafting for this site, follow these rules even when the LLM thinks otherwise.

**Avoid contrastive overuse, but do not cut all of it.** Patterns like *"X is not Y, it is Z"*, *"not X but Y"*, and *"the question is no longer X; it is Y"* feel rhythmic on the first read and mechanical after the third. A page with more than three such constructions reads as AI-shaped. At the same time, eliminating *all* contrastive structures kills cohesion — the prose starts to feel like a list of unconnected statements. Keep one or two genuinely load-bearing contrasts per page (a substantive correction, a key distinction). Replace the rest with direct positive statements or smoothly connected sentences.

**Use connectives for cohesion.** *but*, *though*, *yet*, *however*, *while*, *where X, Y*, *because*, *since* — these are how human prose holds together. Their absence is itself a tell.

**Discipline em-dashes.** Em-dashes feel literary, but on long pages they pile up and become a tell. Use a full stop or comma where you can. Reserve em-dashes for genuine asides where no comma would do.

**Vary sentence length deliberately.** Mix short, medium, and long. A paragraph of three medium sentences with identical openings will read as AI. A short opener followed by a longer expansion reads as human.

**Be certain when you can.** Drop *might*, *could*, *may*, *seems to*, *tends to* when the claim is firm. Hedging is a comfort blanket that the site explicitly warns against.

**No filler openers.** Avoid *"In today's fast-moving world"*, *"It is important to note that"*, *"This post is not exhaustive"*, and similar throat-clearing. If a sentence carries no information, delete it.

**Active voice.** *"The team submitted the report"*, never *"The report was submitted by the team."*

**Avoid AI clichés outright.** *Dive into*, *unlock*, *unleash*, *transform*, *revolutionary*, *navigating complexities*, *in the realm of*, *robust*, *bespoke*, *tailored*, *catalyst*, *enhancing*. See `pe_t6` for the full banned-word list.

**Quotations use attribution.** When you quote or paraphrase a source, attribute clearly: *"As Birgitta Böckeler (ThoughtWorks) put it in her 2026 framework on Martin Fowler's site…"*. If you are paraphrasing, do not put quote marks around your own words; if quoting verbatim, name the author with `— Author Name, Source`.

### 2b. The additive-callout rule

A `???` collapsed callout earns its place only if its content is **genuinely additive** — material the main flow does not already say. Two failure modes to watch for:

1. **Restated callout** — the callout dramatises or chronologises the same content as the main flow. Delete or replace.
2. **Decorative callout** — the callout exists for visual rhythm, not for content. Delete.

Good additive callouts include source/attribution traces, action checklists, real quotations with context, definitions of adjacent terms a reader will meet elsewhere, technical asides for curious readers in a non-technical post, and short worked vignettes that introduce something the main flow only names.

---

## 3. Admonitions — the core formatting tool

Material renders three flavours:

| Syntax | Behaviour | Use for |
|---|---|---|
| `!!! type "Title"` | Always expanded (no toggle) | Editor's word, key takeaways, warnings |
| `???+ type "Title"` | Expanded by default, collapsible | "Background you may already know" |
| `??? type "Title"` | **Collapsed** by default | Technical asides, deep examples, long quotes |

### Admonition types used on this site

- `example` — Editor's Word openings, worked examples, scenarios
- `note` — neutral side-notes, terminology clarifications
- `tip` — actionable advice or shortcuts
- `info` — closing "Further reading" blocks, supplementary references
- `quote` — borrowed lines from external sources (attribute inside)
- `warning` — pitfalls, things that look right but aren't
- `danger` — strong cautions (use sparingly)

### Formatting convention: blank line after the opener

Always leave a blank line between the admonition opener (`!!!`, `???`, or `???+`) and the first indented content line. MkDocs Material renders both forms identically, but the blank-line form is markedly easier to scan and review in Claude, VS Code, and other markdown editors. Apply to all three flavours, including nested admonitions.

```markdown
✅ Preferred — blank line after opener
!!! note "Title"

    First paragraph indented four spaces.

    Subsequent paragraphs also indented, separated by a blank line.

❌ Accepted by MkDocs but harder to inspect in editors
!!! note "Title"
    First paragraph indented four spaces.
```

### Syntax — full example

````markdown
!!! example "Editor's Word"

    Body text indented four spaces.

    Paragraphs separated by a blank line, still indented.

??? note "Background: how this language evolved"

    This is collapsed by default. Use for content that supports the main
    argument but should not block the main reading flow.

???+ tip "Already familiar with this?"

    Expanded by default, but collapsible.
````

### Nesting

Admonitions can contain lists, code blocks, tables, and other admonitions. Keep nesting shallow (one level) for readability. Apply the blank-line-after-opener rule to nested admonitions too.

---

## 4. Code fences

Use fenced code blocks with a **language hint** and, when helpful, a **title**:

````markdown
```python title="example.py"
def hello():
    print("world")
```
````

Inline code uses single backticks: `pip install`, `AGENTS.md`.

For long code or shell transcripts, put them inside a `???` collapsed admonition so non-technical readers can skip them.

---

## 5. Tables

Standard markdown tables. Keep them short (≤6 rows, ≤4 columns) and place a one-line intro above. Material renders them responsively.

---

## 6. Links

- **Internal**: `[Link text](pe_g.md)` — relative paths to other `.md` files in the same `docs/` tree.
- **External**: `[Anthropic's prompt engineering guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)`.
- **"Further reading" pattern**: close pages with an `!!! info "Further reading"` block listing 3–5 curated links, each one a short phrase + one-line description.

---

## 7. Structure template — a typical page

```markdown
---
title: Page Title
description: One-sentence summary.
---

# Page Title

!!! example "Editor's Word"

    A 2–4 sentence hook.

Short opening paragraph (3–5 sentences).

## First section heading

Body.

??? note "Aside: technical detail some readers will want"

    Collapsed content.

## Closing section — what to take away

A short, opinionated close.

!!! info "Further reading"

    - [Link 1](https://example.com) — one-line description.
```

---

## 8. Things to avoid

- **Long unbroken paragraphs.** Break every 3–4 sentences.
- **Hidden requirements / unwritten conventions.** Define inline or link out.
- **Author voice in frontmatter.** This site does not surface authors.
- **Bare URLs** in body text. Always wrap in `[label](url)`.
- **Promising completeness.** Posts here are entry points, not exhaustive treatments.

---

## 9. Quick checklist before publishing

1. Frontmatter: `title` and `description` only (unless instructed otherwise).
2. H1 matches `title`.
3. Opens with an `!!! example "Editor's Word"` (or equivalent) callout.
4. Every technical term unfamiliar to a general university reader is either defined in one clause, or wrapped in a `???` collapsed aside.
5. Closes with `!!! info "Further reading"`.
6. British / HK English spellings.
7. Word count near target (~1000 words for intro posts).
8. Internal links resolve to existing pages in the site's `docs/` tree (or are clearly placeholder).
9. **Contrastive-pattern check**: no more than two *"X is not Y, it is Z"*-style constructions per page, unless a contrast is load-bearing (correcting a likely misreading of a concept).
10. **Cohesion check**: connectives (*but*, *though*, *however*, *where*, *because*) are present where they earn their place. The prose is not a sequence of unconnected statements.
11. **Em-dash check**: fewer than five em-dashes in body prose per ~1000-word page.
12. **Callout audit**: every `???` callout adds material the main flow does not contain. Delete or replace restated/decorative callouts.
13. **Banned-word scan**: no *dive into*, *unlock*, *unleash*, *transform*, *robust*, *bespoke*, *tailored*, *navigating*, *in the realm of*.
14. **Admonition spacing**: every `!!!`/`???`/`???+` opener is followed by a blank line before the first indented content line. Applies to nested admonitions too.
15. **Attribution check**: quotations and paraphrased ideas carry an author name and source.

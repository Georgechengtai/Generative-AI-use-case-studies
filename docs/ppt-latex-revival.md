---
title: "Reviving Legacy Lecture Slides"
---

# Reviving Legacy Lecture Slides

???+ info "Case Study Information"

    *   **Context:** Personal Workflow / Teaching Assistant Support
    *   **Task:** Modernising Economics lecture slides
    *   **Tools:** Grok 4 (Vision), [IguanaTex](https://github.com/Jonathan-LeRoux/IguanaTex)

!!! quote "Editor's Note"

    We have all seen them: lecture slides containing blurry, pixelated screenshots of equations from 1990s textbooks. They look unprofessional and function as **dead data**. Editing a variable or fixing a typo requires retyping the whole thing. This use case shares a workflow to bring them back to life.

## The Challenge: The "Dead" Screenshot

I was tasked with revising a professor's slide deck for a new semester. The content was solid, but the presentation was locked in static images. When the professor asked to change a notation from $\beta$ to $\alpha$, I realised I would have to manually re-type complex matrices in LaTeX—a slow and error-prone process.

??? info "The Alternative: Manual Labour"

    Without this workflow, you have two bad options:

    1.  **Retype everything:** Manually typing complex LaTeX code (e.g., `\begin{pmatrix}...`) is tedious and easy to break.
    2.  **PowerPoint Equation Editor:** While easier, it lacks the professional typesetting of LaTeX and often breaks when moving between Mac and Windows.

## The Solution: AI as the Translator

I used a two-step workflow to "digitise" the math:

1.  **AI Vision:** I fed the screenshot to **Grok 4** (though any vision model like GPT-4o or Claude 3.5 Sonnet works), asking it to extract the LaTeX code.
2.  **IguanaTex:** I pasted that code into PowerPoint using the IguanaTex add-in.

The result was an instant conversion from a blurry image to a crisp, vector-based equation that behaves like a native PowerPoint object.

??? note "What is IguanaTex?"

    **[IguanaTex](https://github.com/Jonathan-LeRoux/IguanaTex)** is a free PowerPoint add-in that lets you insert LaTeX equations directly into slides. These equations remain **editable**—you can click them later to change the code, and they re-render instantly.

??? example "See the Workflow in Action (Tutorials)"

    I have recorded the process to show how fast this actually is:

    *   **[Part 1: Setup & Basic Conversion](https://app.guidde.com/playbooks/sJrRQNRmo6cWcTFdGXmVho)** - Getting the environment ready.
    *   **[Part 2: Handling Complex Equations](https://app.guidde.com/playbooks/baDmaxScaBeMWy8XraArE1)** - Dealing with matrices and multi-line math.
    *   **[Part 3: Formatting & Fine-tuning](https://app.guidde.com/playbooks/ba748GGAmo96hEsqLFXwgC)** - Matching the slide theme.

## The Outcome

The slides are now **future-proof**. Next year, if we need to change the equation again, it takes seconds. This upgrades old materials into a sustainable teaching asset.

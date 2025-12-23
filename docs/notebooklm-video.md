---
title: AI-Generated Video Explainers (NotebookLM)
---

???+ info "Case Study Information"

    - **Project:** NotebookLM Video Overview
    - **Context:** TA Support
    - **Status:** Experimental
    - **Purpose:** Accessible Problem Solving

!!! warning "Experimental Prototype"
    **Disclaimer:** This workflow uses Google's **NotebookLM** to generate audio and video content. While the voices sound incredibly human, they are AI-generated and may occasionally hallucinate details or misinterpret complex mathematical notation. Always verify the output against the textbook.

!!! quote "Motivation: Why I Built This"
    This experiment started with a challenge from my Professor: **"Can we transform a static textbook Q&A into an engaging video format without spending hours on editing?"**
    
    Textbook solutions are often dry and intimidating. Students frequently get stuck on the mathematical notation and miss the economic intuition. The goal was to use AI to turn a solitary reading experience into a dynamic viewing experience—in under 10 minutes.

## The Problem: The "Wall of Text"

In economics, problem sets often look like this:

> **Question 7.9:** Suppose the production of airframes is characterised by a Cobb–Douglas production function: \( Q = LK \). The marginal products are \( MPL = K \) and \( MPK = L \). Price of labour is $10, capital is $1. Find the cost-minimising combination for 121,000 airframes.
> <br><small>— *David Besanko, Ronald Braeutigam - Microeconomics (6th Edition)*</small>


??? info "Pain Points for Students"

    *   **Cognitive Overload:** The dense mathematical notation (\(MPL\), \(MPK\), \(\lambda\)) can be overwhelming.
    *   **Missing Intuition:** Written solutions often show the *steps* (the algebra) but skip the *logic* (why we set \(MPL/MPK = w/r\)).
    *   **Passive Learning:** Reading a PDF solution is a passive activity that is easy to zone out of.

## The Solution: The "Visual Podcast"

To solve this, we treat the textbook problem not as a document to be read, but as a script to be performed.

??? info "The Logic"

    ??? tip "Input vs Output"

        *   **Input:** A standard textbook question and its written solution (Text/PDF).
        *   **Intermediate:** NotebookLM's **Video Overview**, which creates a two-person dialogue (or one if properly prompted) and automatically designs relevant slides.
        *   **Output:** A 5-minute video explainer that walks through the intuition.

    ??? note "Why Video?"
        While the "Audio Overview" simulates a podcast, the **Video** feature adds a visual layer. It projects key terms and bullet points on screen, helping visual learners track the conversation without needing to stare at a blank screen.

## Implementation: From Text to Video

The process is entirely automated within the NotebookLM interface.

???+ example "The Process"

    **Step 1: Upload Materials**
    Upload the textbook question and the solution key into a new notebook.

    **Step 2: Choose Format**
    Open the **Studio** panel. Select "Video Overview" instead of the standard Audio Overview.

    **Step 3: Let AI do the work**
    Click "Generate". The AI analyses the maths, scripts a conversation, records the voices, and generates the accompanying visual slides in parallel. The whole process takes about 5-10 minutes.

## The Result

Below is the actual output generated from the Cobb-Douglas question above. Notice how the AI host explain the *concept* of cost minimisation while the video displays relevant keywords.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/2edUvqt5Lmg?si=hKFqNhskTn-L6Lb0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Outcomes & Evaluations

*   **Speed:** The entire production workflow took roughly 10 minutes. The manual works (editing, triming, uploading to Youtube) can be automated in future.
*   **Accessibility:** Complex mathematical concepts are broken down into plain English, with visual cues to reinforce the terminology. Modern "creators" can produce a video via natural language conversation with AI(vibe-coding)
*   **Engagement:** The conversational format holds attention far better than a static PDF, turning a homework problem into a "watchable" event. Because it requires low manual efforts, teachers and TAs can produce such videos for common FAQs, topics or problem sets that students struggles with in class/tutorial sessions.

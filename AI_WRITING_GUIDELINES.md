# AI Writing Guidelines for Generative AI Use Case Studies

## 1. Format Requirements
- **Platform:** MkDocs with Material theme.
- **File Format:** Markdown (`.md`).
- **Compatibility:** Must be readable in VS Code and render correctly on the MkDocs site.
- **Structure:**
    - **Paragraphs:** Provide basic foundational information and explanations on the topic.
    - **Callouts (Admonitions):** Used for Extensions, Comments, and Updates.
        - **Frequency:**
            - Maximum 2 Callouts per Paragraph.
            - Minimum 1 Callout per Section.
        - **Syntax:** Use standard MkDocs Material admonition syntax.
            - `!!! note "Title"` for general notes or editor's notes.
            - `!!! info "Title"` for informational extensions.
            - `!!! tip "Title"` for helpful tips or demos.
            - `!!! question "Title"` for thought-provoking questions or issue highlighting.
            - `??? info "Title"` (collapsible) for detailed examples or secondary information to keep the page clean.
            - `???- abstract "Title"` (collapsible, initially collapsed) for less critical details like site maps.

## 2. Content Requirements
- **Goal:** Provide fundamental insights into topics without overloading with technical details.
- **Readability:** Simple and quick to read.
- **Independence:** Each page/topic should be isolated; readers shouldn't need to refer back to source websites to understand.
- **Citations & Linking:**
    - **Citations:** No formal citations or reference lists. Use inline hyperlinks `[Source Name](url)` directly in the text if needed.
    - **Internal Linking:** Permitted for closely related topics within the site, but ensure the current page remains standalone understandable.
- **Workflow:**
    1. User provides Topic, Sections, Sub-sections, and Context (sources, data, etc.).
    2. AI fills in Paragraphs and Callouts based on the outline.
    3. AI uses provided context for source-based arguments but keeps the text self-contained.

## 3. Writing Style
### Do:
- **Focus on clarity:** Make messages easy to understand.
- **Be direct and concise:** Remove unnecessary words.
- **Use simple language:** Write plainly with short sentences.
- **Stay away from fluff:** Avoid unnecessary adjectives and adverbs.
- **Keep it real:** Be honest; don't force friendliness.
- **Maintain a natural/conversational tone:** It's okay to start sentences with "and" or "but".
- **Simplify grammar:** Don't stress about perfect grammar (e.g., lowercase "i" is acceptable if it fits the style).
- **Vary sentence structures:** Mix short, medium, and long sentences for rhythm.
- **Address readers directly:** Use "you" and "your".
- **Use active voice:** e.g., "The team submitted the report" instead of "The report was submitted by the team".

### Avoid:
- **Marketing language:** No hype or promotional words (e.g., "revolutionary", "transform your life").
- **AI-giveaway phrases:** Avoid clichés like "dive into", "unleash your potential", "game-changing", "landscape", "tapestry".
- **Filler phrases:** e.g., "It's important to note that...".
- **Clichés, jargon, hashtags, semicolons, emojis, asterisks.**
- **Conditional language:** Avoid "could", "might", "may" when certainty is possible.
- **Redundancy and repetition.**
- **Forced keyword placement.**
- **Generic Openings:** Avoid "In today’s fast moving world", "In our digital lives", etc.

## 4. Interaction Protocol
- **Input:** User provides Topic + Outline + Context.
- **Output:** AI generates Markdown content following the above guidelines.

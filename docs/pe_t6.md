# How to Make AI Text Sound More Human?

???+ note "Original Source"
    - Reddit thread: [I banned most overused words in ChatGPT responses](https://www.reddit.com/r/ChatGPTPro/comments/1dz8m9q/i_banned_most_overused_words_in_chatgpt_responses/)
    - Online tools: [AI Text Humanizer](https://ai-text-humanizer.com/) and [Rephrasy](https://www.rephrasy.ai/) (which lets you have a sense of how people prevent plagiarism detection)

    Update on Apr 8, 2025: Add two new prompts that prompts from top-down approach, negative and non-negative. From [This](https://www.reddit.com/r/ChatGPTPromptGenius/comments/1jslcwg/finally_found_the_prompt_that_makes_chatgpt_write/) and [That](https://www.reddit.com/r/ChatGPT/comments/1jspefk/i_finally_found_a_prompt_that_makes_chatgpt_write/)

!!! quote "Editor's word"
    AI detection remains a tough area with no perfect solutions. Most basic AI text is easy to spot, but no single method can catch all AI models' outputs with complete accuracy. Big claims about 100% detection rates (like those from Turnitin) often stretch the truth.
    
    Most detection now uses groups of models that each vote on whether text looks AI-made. These systems still fail on tricky cases and mainly catch only the most obvious examples.
    
    **We do not support or give methods to help readers avoid plagiarism detection.** The info below focuses only on making AI outputs read more like human writing, which uses similar methods but for different goals.
    
    If you want to test these ideas, the online tools listed above offer free trials.

    ???- quote "We're hesistate to show.. but this is the original inhumane version"

        AI detection is a complex and evolving field. While it's relatively easy to identify basic AI-generated text, there's no universal method that can detect outputs from all AI models with perfect accuracy. Claims of 100% detection rates (such as those made by Turnitin) are often exaggerated.
    
        Current detection typically relies on ensemble models that vote on whether text appears AI-generated. These systems remain unreliable for edge cases and primarily catch only the most obvious examples.
        
        **We do not endorse or provide methods to help readers avoid plagiarism detection.** The information below focuses solely on making AI outputs sound more naturally human-written, which shares methodological similarities but serves a different purpose.
        
        For those interested in testing these approaches, the online tools mentioned above offer trial versions.

AI text often sounds fake because of certain patterns and common phrases that show up again and again. By finding and removing these patterns, writers can make text that reads more like a real person wrote it.

The Reddit post author ran a simple yet brilliant test. They gathered a list of words that ChatGPT tends to overuse, then asked the AI to write with and without these terms. The results? The "cleaned" version sounded much more like human writing - still clear but less robotic.

For example, when asked to write about AI's impact, the standard output included phrases like "catalyst transforming ideas" and "enhancing human interactions." The version without banned words used more direct language like "a force that turns ideas into reality" and "adds a personal touch."

???+ warning "Simplified Prompt"
    This is a basic version of the prompts from the original source. The full method for making this prompt appears in full detail there.

    ```yaml
    <context>
    Rewrite below <TEXT> and keep the same structure, information and length. Only change the language used.
    </context>

    <prohibited_words>
    Do not use complex or abstract terms such as 'meticulous,' 'navigating,' 'complexities,' 'realm,' 'bespoke,' 'tailored,' 'towards,' 'underpins,' 'ever-changing,' 'ever-evolving,' 'the world of,' 'not only,' 'seeking more than just,' 'designed to enhance,' 'it's not merely,' 'our suite,' 'it is advisable,' 'daunting,' 'in the heart of,' 'when it comes to,' 'in the realm of,' 'amongst,' 'unlock the secrets,' 'unveil the secrets,' 'transforms' and 'robust.' This approach aims to streamline content production for enhanced NLP algorithm comprehension, ensuring the output is direct, accessible, and easily interpretable.
    </prohibited_words>

    <TEXT>
    [PASTE YOUR TEXT HERE]
    </TEXT>
    ```

---

???- note "Write naturally with negative prompt (like how Image Generation works)"

    ```yaml
    # Writing Style Prompt

    -   **Focus on clarity:** Make your message really easy to understand.
        -   _Example:_ "Please send the file by Monday."
    -   **Be direct and concise:** Get to the point; remove unnecessary words.
        -   _Example:_ "We should meet tomorrow."
    -   **Use simple language:** Write plainly with short sentences.
        -   _Example:_ "I need help with this issue."
    -   **Stay away from fluff:** Avoid unnecessary adjectives and adverbs.
        -   _Example:_ "We finished the task."
    -   **Avoid marketing language:** Don't use hype or promotional words.
        -   _Avoid:_ "This revolutionary product will transform your life."
        -   _Use instead:_ "This product can help you."
    -   **Keep it real:** Be honest; don't force friendliness.
        -   _Example:_ "I don't think that's the best idea."
    -   **Maintain a natural/conversational tone:** Write as you normally speak; it's okay to start sentences with "and" or "but."
        -   _Example:_ "And that's why it matters." 
    -   **Simplify grammar:** Don't stress about perfect grammar; it's fine not to capitalize "i" if that's your style.
        -   _Example:_ "i guess we can try that."
    -   **Avoid AI-giveaway phrases:** Don't use clichés like "dive into," "unleash your potential," etc.
        -   _Avoid:_ "Let's dive into this game-changing solution."
        -   _Use instead:_ "Here's how it works."
    -   **Vary sentence structures (short, medium, long) to create rhythm**
    -   **Address readers directly with "you" and "your"**
        -   Example: "This technique works best when you apply it consistently."  
    -   **Use active voice** 
        -   Instead of: "The report was submitted by the team."   
        -   Use: "The team submitted the report."
            
    # Avoid:

    -   **Filler phrases**
        -   Instead of: "It's important to note that the deadline is approaching."
        -   Use: "The deadline is approaching."
    -   **Clichés, jargon, hashtags, semicolons, emojis, and asterisks**
        -   Instead of: "Let's touch base to move the needle on this mission-critical deliverable."    
        -   Use: "Let's meet to discuss how to improve this important project."
    -   **Conditional language (could, might, may) when certainty is possible*.
        -   Instead of: "This approach might improve results."
        -   Use: "This approach improves results."
    -   **Redundancy and repetition (remove fluff!)**
    -   **Forced keyword placement** that disrupts natural reading.
    -   **Opening** like: “In today’s fast moving world” or “In our digital lives”. Such filler content confirms to be written by AI.
    ```

???- note "A non-negative version, in case you are afraid LLM are insensitive against negative prompts "avoiding" <br>(My opinion: a non-issue in frontier AI models)"

    ```yaml
    # Writing Guidelines

    Use Active Voice

    ✅ Example: "Management canceled the meeting." (Instead of: "The meeting was canceled by management.")

    2. Address Readers Directly

    ✅ Example: "You'll find these strategies save time."

    3. Be Direct and Concise

    ✅ Example: "Call me at 3pm."

    4. Use Simple, Clear Language

    ✅ Example: "We need to fix this problem."

    5. Stay Focused and Eliminate Unnecessary Words

    ✅ Example: "The project failed." (Instead of adding unnecessary explanation.)

    6. Prioritize Clarity

    ✅ Example: "Submit your expense report by Friday."

    7. Use a Natural, Conversational Tone

    ✅ Example: "But that's not how it works in real life."

    8. Create Engaging Rhythm with Varied Sentence Structures

    ✅ Example: "Stop. Think about what happened. Consider how we might prevent similar issues in the future."

    9. Keep It Real and Honest

    ✅ Example: "This approach has problems."

    10. Use Precise and Practical Language

    ✅ Example: "Our tool can help you track expenses." (Instead of exaggerated marketing claims.)

    11. Simplify Grammar and Maintain a Smooth Flow

    ✅ Example: "Yeah, we can do that tomorrow."

    12. Be Certain When Possible

    ✅ Example: "This approach improves results." (Instead of: "This approach might improve results.")

    13. Keep Writing Fresh and Avoid Overused Openings

    ✅ Example: "Technology is evolving fast—here’s what you need to know." (Instead of generic phrases like "In today’s fast-moving world.")

    14. Keep Formatting Clean and Professional

    ✅ Use clear headings, structured content, and avoid unnecessary symbols like dashes (-), asterisks (*), and hashtags.
    ```

    ```
    # Bonus: Optimizing for SEO & Readability

    ✅ Use Data & Trends (2024 & 2025) – Incorporate relevant statistics.

    ✅ Include Expert Quotations – Add 1-2 quotes from industry leaders.

    ✅ Use JSON-LD Article Schema – Implement structured data (Schema.org).

    ✅ Organize with Clear Headings – 4-6 H2s, 1-2 H3s per H2.

    ✅ Maintain a Direct and Factual Tone – No unnecessary fluff.

    ✅ Use Internal and External Links – 3-8 internal, 2-5 external (blended naturally).

    ✅ Optimize Metadata – Ensure clear, keyword-rich titles and descriptions.

    ✅ Include an FAQ Section – 5-6 common questions sourced from tools like AlsoAsked & AnswerSocrates.
    ```

???- note "Extra custom instruction"

    ```yaml
    Ensure heterogeneous paragraphs. Ensure heterogeneous sentence lengths.

    Be conversational, empathetic, and occasionally humorous. Use idioms, metaphors, anecdotes, and natural dialogue.
    ```
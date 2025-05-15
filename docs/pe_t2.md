# How Not to Get Useless Responses?

!!! note "Original Source"
    These advices are from a [post from reddit/com/r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/comments/1j5ymik/ai_prompting_tips_from_a_power_user_how_to_get/). 

    ???- tip "The Five Actionable Insights"
        1. **Use structured frameworks instead of vague requests.** Provide AI with clear, fill-in-the-blank template outlines--_just as you'd do when writing yourself._
        2. **Try the "Lazy Essay" method.** Structure your prompt clearly using four sections:
            - **Assignment:** Clearly state the task or question.
            - **Quotes:** Provide relevant quotes or references.
            - **Notes:** Add your own notes or key points.
            - **Instructions:** Clearly outline exactly what you want the AI to do.
        3. **Never settle for the first response.** Refine the AI's output with targeted follow-up prompts until satisfied.
        4. **Make the AI choose a side.** AI responses tend to be neutral by default--explicitly instruct the AI to argue a specific viewpoint or stance.
        5. **Fix poor responses by adjusting one variable at a time.** Systematically tweak your prompt to identify exactly what improves AI output.

???- quote "Editor's word"
    To get better, more engaging AI responses, avoid vague and generic prompts. In particular, remember to **provide clear structure** (use frameworks or templates) and **make AI pick a clear side** (use debate-style prompts)

    We advice you to check the source (more informative) if this area interests you.

---

???+ example "1. Stop Asking AI to 'Write X'--Give It a Framework Instead"
    
    AI excels at filling in blanks, but struggles when prompts are unclear. Provide a clear structure to guide it effectively.

    🚫 **Bad Prompt:**  
    `"Write an essay about automation."`

    ✅ **Good Prompt:**  
    ```yaml
    Title: [Insert Here]  
    Thesis: [Main Argument]  
    Arguments:  
    - [Key Point #1]  
    - [Key Point #2]  
    - [Key Point #3]  
    Counterarguments:  
    - [Opposing View #1]  
    - [Opposing View #2]  
    Conclusion: [Wrap-up Thought]
    ```

    Now, AI has a clear outline and won't produce rambling responses.

???+ tip "4. Force AI to Pick a Side (Neutrality is Boring)"
    
    AI responses that aim for neutrality often feel generic. Prompt it explicitly to adopt a clear stance.

    🚫 **Bad Prompt:**  
    `"Explain the pros and cons of universal basic income."`

    ✅ **Good Prompt:**  
    `"Defend universal basic income as a long-term economic solution and refute common criticisms."`

    ✅ **Even better:**  
    `"Make a strong argument in favour of UBI from a socialist perspective, then argue against it from a libertarian perspective."`

    This approach compels AI to generate meaningful arguments rather than just listing points.
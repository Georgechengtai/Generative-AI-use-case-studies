# Fix your Mind

## Meta-Prompting for Better Results

???+ info "Original Source"
    Adapted from common prompt engineering practice and community discussions about reflective AI usage techniques.

!!! quote "Editor's Note"
    Instead of guessing why your prompts aren't working, let the AI itself help you improve them. This lets you develop a better sense of how models interpret your requests—and how to phrase them for optimal results.

Many of us have experienced the frustration of crafting what seems like a perfect prompt, only to receive a mediocre response. Rather than continuing to guess what might work better, you can actually ask the AI to analyse its own outputs and your prompts.

This approach—called meta-prompting—turns the AI into your prompt coach. By showing it both your original prompt and the unsatisfactory response, you give it enough context to suggest specific improvements.

???- danger "What is Meta-Prompting"
    
    This page presents a basic version of meta-prompting. The full concept is like: "What if the AI created its own expert prompt and selected which expert to act as?" 
    
    True meta-prompting goes much deeper with state-of-the-art techniques like:

    - Using examples, expert personas, and voting systems
    - Running multiple trials automatically to compare results
    - Letting a group of frontier AI models judge the quality of outputs
    
    You can see a practical example with input and a result here: [Technical Project Planning Meta-Prompt](https://gist.github.com/pyros-projects/c77402249b5b45f0a501998870766ae9) (Shared in a reddit post [Meta Prompts - Because Your LLM Can Do Better Than Hello World](https://www.reddit.com/r/LocalLLaMA/comments/1i2b2eo/meta_prompts_because_your_llm_can_do_better_than/))

???+ note "When to Use This Technique"

    - When you're getting vague or off-target responses
    - When the AI misses key aspects of what you requested
    - When you want to learn how to craft better prompts in general
    - When you're working with a new AI model and learning its capabilities

???+ tip "The Meta-Prompting Template"
    ```yaml
    Here's what I asked [AI name]: [insert your original prompt]
    
    Here's the response I got: [paste the response]
    
    How can I improve the prompt to get better results for what I'm trying to accomplish?
    ```

???+ example "An Imaginary Example"
    
    🚫 **Original Prompt:**  
    "Write about climate change."
    
    🚫 **Disappointing Response:**  
    *[A generic overview of climate change with basic facts but no depth or particular angle]*
    
    ✅ **Meta-Prompt:**  
    ```yaml
    Here's what I asked ChatGPT: "Write about climate change."
    
    Here's the response I got: [paste generic response]
    
    How can I improve the prompt to get a more detailed analysis of potential economic impacts of climate change on coastal communities in the next 20 years?
    ```
    
    The AI will now help you craft a much more specific and effective prompt that targets exactly what you're looking for.

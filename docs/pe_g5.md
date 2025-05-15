# Prompting Skills: Now Baked Into AI

???+ info "Original Source"
    This article draws from various sources, but for details in CoT and CoD, check:
    - [Chain-of-Thought Prompting](https://www.promptingguide.ai/techniques/cot) from the Prompt Engineering Guide
    - [What is Chain of Drafts?](https://medium.com/data-science-in-your-pocket/what-is-chain-of-drafts-bye-bye-chain-of-thoughts-76658d913169) by Mehul Gupta

!!! quote "Editor's Note"
    You don't need to memorise most of what follows. If you want to check prompting techiques with better explanations, visit [promptingguide.ai](https://www.promptingguide.ai/).
    
    New AI models already have these prompting techniques built in. Custom GPTs save you from building specialised instructions from scratch. I picked CoT as an example because it shows how the field is changing—from techniques we had to learn to features that just work.
    
    This is just extra reading to see how things are improving, not something you need to use yourself.

## Prompting Tricks Are Becoming Standard Features

Prompting techniques that everyday users once had to apply themselves are now built into AI products. Chain of Thought (CoT) illustrates this pattern clearly—what started as a user prompt is now a standard model capability.

???- info "Why Prompting Engineering Techniques Still Matter?"
    As models get bigger, they become more responsive to user inputs and increasingly sensitive to prompt parameters. Their expanded capacity means proper prompt design remains crucial for getting reliable, structured outputs.
    
    The difference is that for everyday tasks, frontier LLMs will eventually perform well enough that average users won't notice the difference between an optimal prompt and a decent one. But for researchers, power users, and custom applications, these prompting skills remain crucial for pushing LLMs to the limit.

## Chain of Thought: Teaching AI to Show Its Work

???- warning "CoT in Machine Learning Development"
    CoT has been extremely useful in machine learning and remains valuable in Supervised Fine-Tuning (SFT), especially when you have sufficient labeled data. While DeepSeek's Reinforcement Learning approach has shown advantages when training reasoning models, CoT remains fundamental. It's just so fundamental that average users may not notice its presence—it's already baked into models by researchers and developers.
    
Chain of Thought (CoT) gets AI models to show their step-by-step thinking before giving an answer. The original technique requires you to add an extra prompt (*officially, it is classified as 'zero-shot CoT', but whatever*) after original prompt.

> "Let's think step by step". 

This once-manual technique has gone through four stages:



??? example "1. Manual Prompting"
    Simple phrase indeed, but it triggers much better reasoning and reduces errors on complex problems.
    
    ```yaml
    Prompt: The odd numbers in this group add up to an even number: 4, 8, 9, 15, 12, 2, 1. Let's think step by step.
    
    Response: Looking at the numbers: 4, 8, 9, 15, 12, 2, 1
    The odd numbers are: 9, 15, 1
    Adding them up: 9 + 15 + 1 = 25
    25 is odd, not even.
    The answer is False.
    ```

??? example "2. Ready-made Templates"
    As CoT became popular, online communities shared effective templates and use cases. Users could copy and modify.
    
    **Example template for math problems:**
    ```yaml
    I need to solve a math problem. I'll think through this step by step to find the correct answer.
    
    Problem: [INSERT PROBLEM HERE]
    
    Step 1: Identify what's being asked and what information we have.
    Step 2: Set up the appropriate calculation.
    Step 3: Solve the calculation carefully.
    Step 4: Check my work and state the final answer clearly.
    ```

??? example "3. Custom GPTs and Other Applications"
    We have pre-built tools with reasoning abilities already configured (not necessarily a reasoning layer, but a distalled/finetuned model can handle a specific task very well). Users no longer need to know about CoT. They just **select the right tool** for their task.
    
    For example, a "Math Tutor GPT" might have instructions like:

    - Always break down problems step by step
    - Show all work clearly
    - Check answers before providing them

??? example "4. Reasoning-Enhanced Models"
    Reasoning models have reasoning abilities built directly into their architecture.
    
    Models like Claude-3.7 Reasoning, OpenAI'o3, Grok-3, and DeepSeek-R1 are specifically trained to:

    - Break down complex problems automatically
    - Apply multi-step reasoning without explicit instructions
    - Show their thinking process even when not specifically asked to
    
    What started as a user technique is now part of the underlying reasoning models design. In fact, **explicitly stating "Let's think step by step" can now hinder the output performance.**

On February 2025, researchers published [Chain of Drafts (CoD)](https://arxiv.org/abs/2502.18600), offering the next efficiency improvement in AI reasoning. CoD keeps the reasoning benefits of CoT while using significantly fewer words and tokens.

What makes CoD interesting is that it doesn't mirror how humans typically explain their thoughts—instead, it captures how we often jot down minimal notes when solving problems. By reducing verbosity and focusing on critical critical information, CoD achieves comparable accuracy with as little as 7.6% of the tokens used by CoT.

To implement CoD, you can use this prompt template:

> "Think step by step, but only keep a minimum draft for each thinking step, with 5 words at most. Return the answer at the end of the response after a separator ####."

??? example "CoD: Thinking Faster by Writing Less"
    **Problem**: Jason had 20 lollipops. He gave Denny some. Now he has 12 left. How many did Jason give to Denny?
    
    **CoT Answer**:
    ```
    Jason started with 20 lollipops.
    After giving some away, he had 12 left.
    To find out how many he gave away, we subtract: 20–12.
    That gives us 8.
    ```
    
    **CoD Answer**:
    ```
    20–12 = 8 → Final Answer: 8.
    ```
    
    CoD gets the same result with fewer words and less processing time.

## How Prompting Has Changed: From User Skills to Built-In Features

This adoption shows a clear pattern in LLM development:

1. First, experts discover techniques that make AI work better
2. These techniques spread as templates and guides
3. The best techniques get built into newer AI models
4. Eventually, they become invisible features in LLMs

??? question "Why does this matter to you?"
    Understanding this evolution helps you:

    - Know which models will handle complex tasks well
    - Recognise when older AI might need more detailed prompting
    - See how the field is progressing—what's manual today may be automatic tomorrow
    - Make better choices about which AI tools to use for different tasks

## The Bottom Line

The journey from CoT to CoD to built-in reasoning shows how AI is becoming more capable and easier to use at the same time.

Instead of learning special prompting tricks, most users can now focus on picking the right AI tool that already has the capabilities they need—while advanced users can still apply these techniques to push the boundaries of what's possible.
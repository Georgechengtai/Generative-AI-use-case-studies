# How to Prompt Chatbots: Overview

!!! note "Editor's Word"

    ???+ info "Overview"
        The core guides build on each other: rich context → precise persona → defined structure → template refine & reuse. Follow this sequence for stable, accurate, and human-like chatbot responses without needing deep AI expertise.
        
    To get the best results, start by outlining your problem and data, telling the AI its expert role, setting your output format, and tweaking a proven online template. These four steps work together:

    1. **Begin with Context**  
       Give the AI all relevant background--data, goals, constraints--or explicitly invite it to question you if something’s missing. Without context, it can't tailor responses and will guess incorrectly.  

    2. **Assign Expert Personas**  
       Once context is set, define who should answer: "You are a financial analyst," "You are a legal advisor," etc. Clear roles ensure the AI calls the right specialist instead of defaulting to generic answers.  

    3. **Structure for the Desired Output**  
       Specify format (JSON, bullets, tables), length, tone, and examples. For better results, feed both your prompt and the AI's first response back into the model to improve clarity and accuracy.  

    4. **Leverage and Adapt Templates**  
       Start with community-vetted prompts. Pick a template close to your need and adjust it for your specific purpose rather than building from scratch.



    ???+ note "Reference & Supplementary Documentations From Official Sources"

        ???- info "Prompt Engineering Resources"

            ??? info "Anthropic's Prompt Engineering Overview"
                A free [guide to prompting Claude models](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview). Covers clear instructions, few-shot examples, Chain-of-Thought, XML tags, system prompts, and practical examples like content filters.

            ??? info "OpenAI's Cookbook"
                A [repository of 200+ "recipes"](https://cookbook.openai.com/) for API usage: chat completions, function calling, structured outputs, error handling, and performance tuning with sample code.

            ??? info "Google's Prompt Design Strategies"
                The official [Gemini API guide](https://ai.google.dev/gemini-api/docs/prompting-strategies) covering input types, constraints, response formats, zero/few-shot examples, search grounding, and response patterns.

        ???- info "Agent Building Resources"

            ??? info "Anthropic's Building Better Agents"
                A [blog post](https://www.anthropic.com/engineering/building-effective-agents) showing simple patterns for agentic systems: augmented LLMs, workflows (prompt chaining, routing, parallelisation), orchestrator-workers, and autonomous agents.

            ??? info "OpenAI's A Practical Guide to Building Agents"
                A [PDF guide to agent fundamentals](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf): definitions, model selection, tool design, instructions, orchestration patterns, guardrails, and human-in-loop workflows.

            ??? info "LangChain's Build an Agent Tutorial"
                A [Jupyter notebook tutorial](https://python.langchain.com/docs/tutorials/agents) showing how to install LangChain, define tools, bind an LLM, create a React-style agent, stream results, and add conversation memory.

## Core Guides

!!! question "Essential Prompt Engineering Techniques"

    1. [The Question-First Method](pe_g1.md): Teach the AI to ask clarifying questions when context is missing.  
    2. [Specialised AI Personas](pe_g2.md): Define exact roles (e.g., "legal advisor," "marketing strategist") for targeted expertise.  
    3. [Meta-Prompting](pe_g3.md): Feed your prompt and the AI's reply back into the model for better accuracy.  
    4. [Forget What's Been Said](pe_g4.md): Adapt community-built templates instead of starting from zero.  
    5. Further Reading: Explore advanced techniques built into modern reasoning LLMs (Chain-of-Thought for illrustrations) and methods for creating a "second brain" with ChatGPT's memory.

## Ready-Made Templates

!!! question "Practical Prompt Templates"

    1. [Master Any Topic via Reasoning Models](pe_t1.md)  
       Mentor roles, Socratic dialogues, teach-back exercises, and a 30-day learning plan.  

    2. [Avoid Useless Responses](pe_t2.md)  
       Fill-in-the-blank frameworks and stance-forcing prompts to eliminate vague replies.  

    3. [Skim-Read & Fact-Check](pe_t3.md)  
       A two-stage prompt: generate bullet-point summaries, then verify each point against sources.  

    4. [Control Word Count](pe_t4.md)  
       Shrink or expand text while preserving key points, style, and emphasis.  

    5. [Reusable Prompts via C.R.A.F.T.](pe_t5.md)  
       A six-part template (Context, Role, Action, Format, Audience, Template) for creating prompts you'll use repeatedly.  

    6. [Humanise AI Text](pe_t6.md)  
       Remove AI clichés and add natural language so the writing sounds more like you.  

    7. [Transfer Conversation Context](pe_t7.md)  
       Summarise tone, style, and key details to maintain coherence across new chats.  

    8. [Stop ChatGPT Being a Yes-Man](pe_t8.md)  
       An intellectual sparring-partner prompt that challenges assumptions and prevents automatic agreement.
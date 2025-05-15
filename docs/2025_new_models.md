# Recent AI Models after DeepSeek (March 2025)

## Leading Large Language Models

| Feature | DeepSeek-R1 | Claude 3.7 | Grok 3 | GPT-4.5 |
|---------|-------------|------------|---------|---------|
| **Company** | DeepSeek | Anthropic | xAI | OpenAI |
| **Base Model** | DeepSeek-V3-Base | Claude 3.5 architecture | Grok 3 | GPT-4 architecture |
| **Reasoning Model?** | Yes | Yes | Yes | No |
| **Knowledge Cutoff** | December 2024 | January 2025 | Real-time | January 2025 |
| **Context Window** | 128K tokens | 200K tokens | 128K tokens | 128K tokens |
| **Licensing** | Open-source (MIT) | Proprietary | Proprietary | Proprietary |
| **Access Method** | Self-hosted option available | Website or API | Website or API | Website or API |

!!! tip "What is a Reasoning Model?"

    A reasoning model has a specialised "thinking layer" that breaks complex problems into smaller steps. Rather than jumping directly to answers, these models explicitly work through problems methodically (similar to how humans show their work in maths). This approach typically yields better results for complex reasoning tasks like mathematics, coding, and logical analysis, as the model can verify its own thinking process.

## Beyond Benchmarks: Real-world Performance

When evaluating AI models, our personal impressions can be surprisingly unreliable. We might prefer responses that sound confident rather than accurate, or favour a model simply because its interface is more appealing. This "user experience bias" makes objective comparison difficult. Although we've included sample conversations on three topics in the final section, these should be viewed as illustrative examples rather than definitive evidence.

!!! warning "Benchmarks Are Problematic...Too"

    Most published benchmarks measure narrow, specific skills rather than holistic capabilities. Models can be explicitly optimised for these test scenarios while still struggling with everyday tasks. This creates a disconnect between impressive benchmark scores and actual usefulness. Understanding each metric and its limitation can give you a more accurate assessment.

### Chatbot Arena: The People's Evaluation

[Chatbot Arena](https://chat.lmsys.org/), since its launch in May 2023, offers a more balanced assessment by having real users compare models anonymously:

- Users send the same prompt to two different models (without knowing which is which)
- They choose which response they prefer based on quality, helpfulness, and accuracy
- Rankings emerge organically from thousands of these blind comparisons

According to recent Chatbot Arena data (March 2025), the competitive landscape has evolved:

- Models with reasoning capabilities often perform better on mathematical and coding challenges
- Deepseek-R1 entered the arena with a Elo point of 1361, reportedly achieved competitive performance with OpenAI's state-of-the-art o1 models, despite being trained at a fraction of the cost.
- Claude 3.7 is not getting higher Elo point (1304) than Deepseek-R1 although it is released after deepseek-R1's release. (Personal opinion: as a regular user of Claude 3.7, I believe their performance is actually similar, and not comparable by a single metric)
- Grok 3's breakthrough beyond 1400 Elo points in February 2025 and GPT-4.5's subsequent claim to the top position in March 2025 demonstrate the accelerating pace of innovation in this field.
- Noted that GPT-4.5 is a base model - perhaps a optimised reasoning model built on top of GPT-4.5 will yield a significant better result. But who knows?

We've entered an era where different models have distinct specialisations rather than a clear hierarchy of "better" models. When compared between frontier models, we must assess the response quality by task/category to give a somewhat "fairer" opinion.

## Side-by-Side Comparison

Below are example prompts that try to highlight each model's unique approach. We've included links to actual model responses to these identical prompts.

!!! note "DeepSeek Responses"
    
    Unlike other platforms, the DeepSeek website does not have an in-built share function. We've saved the responses into PDFs for comparison purposes, though the formatting is not visually consistent with the other platforms.

### Example Prompts with Commentary

#### Prompt 1: Knowledge and Explanatory Ability

> "Explain quantum entanglement to a 10-year-old in exactly three sentences."

This prompt tests how models handle complex scientific concepts in simple language. From the responses, we cannot determine which model performs better at balancing technical accuracy with child-friendly language. It is, indeed, a matter of taste.

#### Prompt 2: Creative Writing with Parameters

> "Write a 4-line poem about technology that contains both hope and caution for the future."

For this creative task, the differences between models are subtle and largely subjective. All models produce structurally sound poems that balance optimism with warnings about technology. The constraint of exactly four lines was followed by all models, showing their ability to adhere to specific formatting instructions.

#### Prompt 3: Technical Problem Solving

> "Write a function in Python to find prime numbers below 100 using the most efficient algorithm you know."

All models correctly implemented the Sieve of Eratosthenes algorithm, widely considered the most efficient approach for this problem. The implementations varied slightly in their optimisations and documentation style. Claude 3.7 provides the most extensive explanation of its reasoning process, while GPT-4.5 offers a more concise solution with clear comments. Grok 3's solution includes similar optimisations but with slightly different implementation details.

### Response Comparison

| | DeepSeek-R1 | Claude 3.7 | Grok 3 | GPT-4.5 |
|--|------------|------------|--------|----------|
| **Quantum Entanglement** | [Check Response](non_image_attachments/deepseek_response_prompt_1.pdf) | [Check Response](https://poe.com/s/LQDB4c3YqmWDrSglm5JX) | [Check Response](https://grok.com/share/bGVnYWN5_20c6130f-fbe1-4edf-b20a-d1fcff1857df) | [Check Response](https://poe.com/s/7iOIqQN1sB0iQShlb12Z) |
| **Technology Poem** | [Check Response](non_image_attachments/deepseek_response_prompt_2.pdf) | [Check Response](https://poe.com/s/xmM5YEGjN7ORWuhBzDcj) | [Check Response](https://grok.com/share/bGVnYWN5_bc7302cd-af8d-4a9f-8829-76fc44e044a6) | [Check Response](https://poe.com/s/Bk7A1jleJrjWuLOdTuTg) |
| **Prime Numbers Function** | [Check Response](non_image_attachments/deepseek_response_prompt_3.pdf) | [Check Response](https://poe.com/s/b12MjRgXQfLeIf1RRmmY) | [Check Response](https://grok.com/share/bGVnYWN5_4a3bb182-fc02-4682-a1f7-0e057d30c002) | [Check Response](https://poe.com/s/c3iWatLUHc9gz7e11Fge) |
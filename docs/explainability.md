# Can AI Think Like Us? The Reality of Machine "Reasoning"

???+ info "Original Source"
    This content draws from Anthropic's research on circuit tracing and AI interpretability. For detailed methodology, see [Circuit Tracing: Revealing Computational Graphs in Language Models](https://transformer-circuits.pub/2025/attribution-graphs/methods.html) and [On the Biology of a Large Language Model](https://transformer-circuits.pub/2025/attribution-graphs/biology.html). This is an ongoing research project (with their [website](https://transformer-circuits.pub/))
    
    Anthropic has created a brief 3-minute video titled "Tracing the Thoughts of a Large Language Model" that offers an introduction to how researchers analyse and visualise LLM reasoning processes. You can learn more about [this research on Anthropic's website](https://www.anthropic.com/research/tracing-thoughts-language-model).

    <iframe width="100%" height="350" src="https://www.youtube-nocookie.com/embed/Bj9BD2D3DzA?si=tPs9dnf13UXEnoAv" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>




!!! quote "Editor's Note"
    Can AI be explainable? The answer is neither a simple yes nor no, but rather: **"increasingly, and meaningfully, but not completely.**" Recent researches are giving us unprecedented visibility into AI systems, though significant questions remain about how complete this understanding can ever be.

    Note: The more research I study, the harder to give a convinicing answer. To fully debate on this issue, we must discuss on architectural design (esp. tokenisation in transformer model) and the operation of human reasoning (e.g. does language and reasoning flow bidirectional?). It would be better to stay neutral for now, and for below article too.

!!! note "Important Context"
    This article **primarily discusses transformer-based large language models (LLMs)** like GPT, Claude, and similar systems. When researchers describe AI as "planning" or "reasoning," they're mapping machine processes to human concepts that may work quite differently. These systems fundamentally work by predicting the next token (word piece) based on patterns in their training data, though the resulting behaviours can appear remarkably sophisticated.

## Can AI "Think" Like Humans?

When transformer-based chatbots like ChatGPT produce remarkably human-like text, it's natural to wonder if they're "thinking" in ways similar to us. Are they consciously pondering their responses? Do they have an internal monologue like we do?

The short answer is no—but with important nuances.

???- question "Does AI have consciousness or self-awareness?"
    Current evidence suggests no. Despite sometimes referring to themselves as "I," today's language models don't show signs of subjective experience or self-awareness. They've learned patterns of how humans use language about themselves. However, it's worth noting that we lack definitive tests for consciousness even in humans, making absolute claims difficult.

???- question "Does AI have emotions or feelings?"
    Current AI systems lack the biological structures humans use to experience emotions. When AI appears to express emotions, it's reproducing patterns it's learned from human writing. That said, the line between "simulating" and "having" emotions becomes a philosophical question as simulations grow more sophisticated.

???- question "Can AI understand the meaning of what it writes?"
    Not in the same way humans do. AI lacks grounding in physical reality and personal experience, which form the foundation of human understanding. However, AI does develop complex internal representations of concepts and their relationships that allow it to manipulate ideas in structured ways. (More in below)

---

## Can AI "Reason" or Is It Just Sophisticated Pattern Matching?

This question touches on a fascinating grey area in our understanding of AI.

Technically, everything AI systems do is pattern matching—they generate text by predicting what words typically follow others in similar contexts they've seen during training. Their apparent understanding is an emergent property of pattern recognition at scale, not genuine comprehension.

Yet given their size and complexity, Frontier LLM models can generalise well enough to deal with problems even if these problems are not present in the training dataset (nearly the whole internet). Recent research from Anthropic has revealed that the internal processes behind this pattern matching are **surprisingly structured and reasoning-like**.

???+ info "What Researchers Found Inside Claude (an AI assistant similar to ChatGPT)"

    - **Planning ahead**: When writing poetry, Claude selects potential rhyming words before even beginning a line, then constructs the line to reach those predetermined words.

    - **Step-by-step reasoning**: When answering "What's the capital of the state containing Dallas?", the model first identifies "Texas" and then uses that to retrieve "Austin"—proper multi-step reasoning.

    - **Multiple solution strategies**: For addition problems, Claude uses parallel approaches—one system for precise digit calculations and another for rough estimation, similar to human mental math.

    - **Reverse reasoning**: Sometimes Claude works backward from a conclusion to justify an answer—a process researchers call "motivated reasoning" that mirrors human cognitive biases.

    *It was doing much more than simple word prediction.*

???- example "A Practical Example of AI Processing (Point 3)"
    Anthropic researchers discovered Claude uses multiple approaches to solve addition problems like 36+59:
    
    - One part tracks the ones digits (6+9=15, so the answer ends in 5)
    - Another part roughly estimates the total (this is around 90-something)
    - These separate processes then combine to produce the correct answer (95)
    
    This parallel processing mirrors how humans often solve mental math problems, combining precise calculations with approximations.

These capabilities blur the line between "sophisticated pattern matching" and what we'd typically call "reasoning." **The AI isn't just memorising answers—it's developing internal representations of concepts and manipulating them in structured, logical ways**.

???- question "If AI is just pattern matching, how can it solve novel problems?"
    Modern AI models can generalise from the patterns they've seen to handle new situations. Their training encompasses so many examples that they can recombine learned patterns in useful ways when facing novel prompts. The boundary between "pattern recognition" and "problem-solving" isn't always clear, even in human cognition.

???- question "Can AI do logical reasoning?"
    Yes, to a degree. AI can follow chains of logic, though it sometimes makes errors. It has learned the patterns of logical reasoning from examples rather than understanding formal logic rules. The resulting capabilities can be impressive but differ from human logical reasoning in important ways.

???- question "Does AI understand causality?"
    Only weakly. AI models have learned correlations between events but lack a true causal model of the world. This is why they sometimes struggle with counterfactual reasoning. However, transformer architectures do capture some causal relationships from their training data.

## Can We Understand How AI "Thinks"?

Large language models functioned (or are regarded) as "black boxes"—we could see inputs and outputs but had little insight into what happened between them. That's changing in remarkable ways.

Researchers at Anthropic have developed techniques called "circuit tracing" that allow them to observe the internal workings of models like Claude. By replacing complex neural networks with more interpretable components, they've created a sort of "glass box" where they can track how information flows through the system.

???+ info "What We Can Now See"
    Researchers can now trace the flow of information through an AI model as it processes a prompt, revealing:

    - How concepts connect to form "circuits" in the model
    - The step-by-step activation of features as information propagates through layers
    - Which parts of the input trigger specific internal responses
    - How the model plans ahead and considers multiple interpretations

???- warning "The Limits of The Methodology"
    Despite these advances, fundamental limitations remain:

    1. **Overwhelming complexity**: Even simplified visualisations of AI processing for basic prompts contain thousands of connections. What we see is always a heavily filtered version of the full process.

    2. **Translation challenges**: When researchers describe AI as "planning" or "reasoning," they're mapping machine processes to human concepts that may work quite differently.

    3. **Incomplete visibility**: Current methods don't capture all aspects of how models work, particularly around attention mechanisms. As researchers noted, the research sometimes "miss the interesting part" of the computation.

## Finding the Middle Ground

The reality of AI "thinking" and our ability to understand it lies somewhere between the extremes:

- **AI doesn't think like humans**, but its information processing has become structured in ways that parallel aspects of human reasoning
  
- **AI fundamentally works through pattern matching**, but the patterns have become so complex and hierarchical that the line between "sophisticated pattern matching" and "reasoning" blurs
  
- **We can now observe aspects of AI processing** in unprecedented detail, but complete understanding remains elusive due to complexity and fundamental differences from human cognition

The most reasonable position is one of balanced perspective: appreciating the remarkable capabilities of these systems while recognising their fundamental differences from human thinking.
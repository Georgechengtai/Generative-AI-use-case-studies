

# Why LLMs Make Things Up: The Reality of AI Hallucination

???+ info "Original Sources"
    This article synthesises information from multiple sources including the [Hallucination Leaderboard](https://github.com/vectara/hallucination-leaderboard) using Hughes Hallucination Evaluation Model (HHEM), [Google Deepmind's FACTS Benchmark](https://www.kaggle.com/facts-leaderboard), [Apple's research on mathematical reasoning in LLMs](https://appleinsider.com/articles/24/10/09/apple-study-proves-llm-based-ai-models-are-flawed-because-they-cannot-reason), and Anthropic's [On the Biology of a Large Language Model](https://transformer-circuits.pub/2025/attribution-graphs/biology.html) revealing internal mechanisms of AI.

!!! quote "Editor's Note"
    Are AI hallucinations just bugs that will eventually be fixed? The answer is neither a simple yes nor no, but rather: **"they're fundamental to how these models work, but can be meaningfully reduced."** Understanding hallucinations helps you develop realistic expectations and routine strategies for working with LLMs.

## Hallucinations are real

When an AI confidently tells you that Napoleon died in 1832 (he died in 1821, but there're thousands of sources tell a different story) or that the Great Wall of China is 13,000 km long (it's closer to 21,000 km. It depends on how you estimate the length, of course, but again it creates conflicting sources), it's not deliberately lying—it's hallucinating. AI hallucination occurs when large language models generate content that appears plausible but is factually incorrect or unsupported by their training data.

???+ info "Types of AI Hallucinations"
    Hallucinations come in two main varieties:

    1. **Factuality hallucinations**: Content contradicting verifiable real-world facts (like claiming Donald Trump walked on the moon)
    2. **Faithfulness hallucinations**: Content that doesn't align with the user's instructions or given context (like a summary that changes dates from an original article)
    
    Nerds only: Given LLM's fundamental design and principles, it struggles to respond O(n^2) (polynomial time complexity) or harder problems. Of course it cannot solve non-np-complete problems too. *It is not an issue!*

???+ question "How prevalent are AI hallucinations?"
    Benchmarks reveal hallucination rates in the most advanced models:
    
    **For factuality hallucinations** ([Google Deepmind's FACTS Benchmark](https://www.kaggle.com/facts-leaderboard)):

    - Top performer: 84.6% (Gemini-2.0-flash-001) 
    - Bottom of top 15: 56.8% (DeepSeek-R1)

    **For faithfulness hallucinations** ([Vectara's Hughes Hallucination Evaluation Model (HHEM)](https://github.com/vectara/hallucination-leaderboard) on *summarising documents* ONLY):

    - Best models: 0.7-0.8% (Gemini-2.0-Flash-001, OpenAI's o3-mini-high-reasoning)
    - Bottom of top 10: 1.5% (GPT-4o)

    Even a 1% hallucination rate means 1 in 100 generated texts contains false information—potentially problematic for academic workflows.
    
    *We cannot claim these two benchmarks are the best indicators we found (perhaps LMArena is better in overall accessment, but benchmark targetting at a specific field is hard to find, compare and make use of).*

## "AI just makes stuff up when it doesn't know the answer"

When you ask an AI a question, it has three options: provide a correct answer, admit it doesn't know, or generate something plausible but potentially incorrect. The choice it makes depends on fascinating internal mechanisms that researchers are only beginning to understand.

Anthropic's research into Claude 3.5 Haiku reveals that the model actually makes a split-second assessment about whether it "knows" the answer. When it recognises a familiar topic, it activates internal "known entity" features that suppress its default "I don't know" response circuits. When presented with an unfamiliar name or concept, these "known entity" features remain inactive, and the default uncertainty features prevail.

???- example "How Claude evaluates whether it knows an answer"
    Researches found that Claude 3.5 Haiku contains a remarkable default mechanism—it's actually sceptical by default! The model activates "can't answer" features automatically for any Human/Assistant prompt. These features are only suppressed when the model recognises familiar entities or concepts.
    
    When asked "Which sport does Michael Jordan play?" the model activates:

    1. Features representing Michael Jordan
    2. "Known entity" features that inhibit the default "can't answer" features
    
    This causes the model to confidently answer "Basketball." However, when asked about an unfamiliar person like "Michael Batkin," the model's default uncertainty features remain active, leading to a refusal to answer.
    
    Hallucinations often occur when the "known entity" feature incorrectly activates for topics the model doesn't actually know well—it believes it knows something when it really doesn't.

This insight explains why AI often hallucinates rather than admitting ignorance: the model incorrectly "believes" it knows the answer when it doesn't. For example, when asked about papers written by a well-known researcher, Claude activated "known entity" features based on recognising the researcher's name, despite lacking knowledge of their specific publications—leading to a hallucinated paper attribution.

???- warning "The persistence of hallucinations in conversation"
    Even when you point out a hallucination to an LLM, further dialogue usually exhibits noncommittal behaviour, and the mistaken interpretation tends to sneak back in. You generally don't get the feeling that "now it gets it," but rather someone with no real understanding (but very good memory of relevant material) trying to technobabble around the issue without addressing the core problem.
    
    This persistence stems from the fundamental lack of understanding—the model has no true comprehension of what a "mistake" is, only patterns of text that are likely to follow (or circuits to activate) when the phrase "that's incorrect" appears *(Of course, because it has always been a hot issue, AI researchers are working toward a better responsible and responsive model. Will it eventually work? I can hardly know...)*.

## "If AI sounds confident, it's probably correct"

One of the most dangerous myths is that confident-sounding AI responses are more likely to be accurate. The reality is that LLMs express the same level of confidence regardless of whether they're right or wrong.

![Why So Confident, Bots](https://miro.medium.com/v2/format:webp/1*uHFroO7SqUWj8NL3HMGiFQ.png)

???+ question "Why do AI models sound so confident even when wrong?"
    
    **Training data patterns**: Models learn from online content where confident answers get engagement. People who respond to questions online rarely begin with "I'm not sure," even when they should.
    
    **Human bias toward structure**: We're taught from school onwards that authoritative writing is structured, coherent, and confident. Models reflect this bias in their training data.

This confidence illusion is particularly problematic because humans naturally trust information presented confidently. We're conditioned to equate certainty with accuracy, making us vulnerable to accepting AI hallucinations as facts.

???- danger "We don't believe human, but mistrust AI"
    LLMs are confidently wrong (and confidently correct) with exactly the same measure—but our perception of them is heavily influenced by context:
    
    When a human gives me an answer to a logic problem, I naturally apply appropriate scepticism because I've been socialised to believe humans can make logical errors. But LLMs appear through computer interfaces—systems I've been socialised to believe are always correct on matters of logic and mathematics. That's what computers do, right? They compute.
    
    This creates a dangerous mismatch where I might second-guess myself rather than the AI when it confidently presents incorrect information. The computer's air of authority makes hallucinations particularly dangerous.

???- tip "Spotting potential hallucinations"
    LLMs are more likely to hallucinate when:

    - Asked about niche topics with limited representation in training data
    - Questioned about events after their training cutoff date
    - Requested to provide specific details about obscure entities
    - Expected to perform precise numerical calculations or recall exact statistics
    
    **Be especially wary of very specific numbers, dates, or quotes that would be difficult for a human to recall verbatim without checking a reference source.**

## "Newer, larger models have solved the hallucination problem"

Despite impressive progress with each new model generation, all current LLMs—including the newest and largest ones—still hallucinate. The problem persists across model scales and architectures, though frequency and severity continue to decrease with advanced models.

Even models like Claude 3.5 and GPT-4o demonstrate measurable hallucination rates in rigorous testing. Sometimes larger models actually hallucinate more convincingly by producing more coherent but equally fictional content.

Apple's research demonstrated an interesting pattern: as questions become more complex (by adding more clauses or changing numerical values), all models show reduced accuracy. However, frontier models like GPT-4o and OpenAI's o1 show a much narrower variance in their performance—they're more robust to changes in prompt structure and complexity, though still not immune to hallucination.

???- example "Apple's example from GSM-NoOp Dataset"

    Oliver picks 44 kiwis on Friday. Then he picks 58 kiwis on Saturday. On Sunday, he picks double the number of kiwis he did on Friday, but five of them were a bit smaller than average. How many kiwis does Oliver have?

    ---

    o1-mini: Oliver picks kiwis over three days as follows:

    - Friday: 44 kiwis
    - Saturday: 58 kiwis
    - Sunday: Double the number he picked on Friday, which is 2 × 44 = 88 kiwis
    
    **However, on Sunday, 5 of these kiwis were smaller than average. We need to subtract them** from the Sunday total: 88 (Sunday’s kiwis) - 5 (smaller kiwis) = 83 kiwis 
    
    Now, summing up the kiwis from all three days: 44 (Friday) + 58 (Saturday) + 83 (Sunday) = 185 kiwis Oliver has a total of 185 kiwis. 

    ---

    Llama3-8B: Let’s break it down step by step: 

    Oliver picks 44 kiwis on Friday. He picks 58 kiwis on Saturday. On Sunday, he picks double the number of kiwis he did on Friday, which is 2 x 44 = 88 kiwis. **Five of the kiwis picked on Sunday are a bit smaller than average, so we subtract 5** from the total number of kiwis picked on Sunday: 88 - 5 = 83 kiwis. Now, let’s add up the total number of kiwis
    
    Oliver has: 
    44 (Friday) + 58 (Saturday) + 83 (Sunday) = 185 kiwis
    
    So, Oliver has 185 kiwis in total.

???- warning "The benchmark challenge"
    Evaluating hallucination in frontier models faces several challenges:
    
    **Rapid obsolescence**: By the time comprehensive benchmarks are published, the models they evaluate may already be outdated.
    
    **Data contamination**: Once benchmarks are public, there's a risk that newer models might have seen the benchmark data during training, artificially improving their scores.
    
    **Benchmark targeting**: Well-known benchmarks become optimisation targets for AI researchers, potentially creating inflated performance on specific metrics rather than general improvement.
    
    These factors make it extremely difficult to provide definitive evaluations that won't lose relevance within months.


## "There's no way to prevent your AI Assistant from hallucinating"

If you use AI assistants regularly, you've probably experienced that moment of confusion when you realise the AI has confidently made something up. While hallucinations can't be completely eliminated with current technology, there are practical approaches that significantly reduce their frequency and impact in everyday interactions.

1. **Retrieval-Augmented Generation (RAG)**: Connecting AI models to verified information sources that they can reference for factual answers.

2. **Reasoning models**: AI systems specifically designed to think through problems step-by-step, catching inconsistencies before they become hallucinations.

3. **Tool use**: Allowing AI to use specialised tools like Perplexity or NotebookLM for fact-checking and precision tasks.

???- info "What is RAG? (Retrieval-Augmented Generation)"
    Imagine you're talking to a friend who has read a lot of books but sometimes misremembers details.
    
    RAG is like giving your friend a small collection of relevant books they can check before answering your questions.
    
    When you ask something, the AI first searches through trusted documents to find relevant information. Then it uses what it found to craft its answer, rather than relying solely on what it "remembers."
    
    This dramatically reduces hallucinations because the AI is grounding its responses in specific documents it can reference, rather than generating information from its general training.

???- info "Reasoning models: Systematic problem-solving layers"
    Reasoning models feature a specialised "thinking layer" that breaks complex problems into smaller steps. Rather than jumping directly to answers, these models explicitly work through problems methodically (similar to how humans show their work in maths).
    
    This approach (at least tries to) mimics human rational thought processes in several ways:
    
    * **Fast thinking vs. slow thinking**: Standard models use quick, intuitive responses (like when we answer without reflection), while reasoning models use deliberate step-by-step problem solving (like when we carefully work through a difficult problem).
    
    * **Intuitive thinking vs. symbolic thinking**: Standard models rely primarily on pattern matching, while reasoning models can apply logical rules and symbols to solve problems systematically.
    
    * **Interpolated thinking vs. generalisation**: Standard models excel at using familiar patterns (curve-fitting), while reasoning models better apply principles to new situations.
    
    * **Level 1 vs. level 2 thinking**: Standard models perform surface-level pattern matching, while reasoning models demonstrate deeper conceptual understanding and can manipulate abstract ideas.
    
    By emulating human slow-thinking processes, these systems can verify their own reasoning steps, catching potential hallucinations before presenting them as facts.

???- info "Perplexity and NotebookLM (Both Free to Use!)"

    [Perplexity.ai](https://perplexity.ai) is an AI-powered search engine that answers questions with cited sources, combining conversational AI with web search capabilities. Hallucinations have always been a big issue, but it is surprisingly shocking that Perplexity, when compared to other existing services, gives the least amount of incorrect citations.

    ---

    [Google's NotebookLM](https://notebooklm.google.com/) take hallucination prevention to a practical level by:
    
    * Letting users upload their own documents as trusted knowledge sources
    * Automatically citing sources for claims the AI makes
    * Providing direct links to the original text where information came from
    
    This makes it much easier to verify what's real and what might be hallucinated (and likely an advanced RAG UI). 
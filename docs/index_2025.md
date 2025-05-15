---
hide:
  - navigation
  - toc
comments: false
---
<style>
  .md-typeset h1,
  .md-content__button {
    display: none;
  }
</style>


# Generative AI Use Case Studies

!!! note "Site Introduction"

    AI tools are like those Christmas presents you unwrap—you don't really know what they can do until you start messing around with them. It takes some tinkering, experimenting, and plain old playtime to figure out how to make the most of these tools.

    Our website covers five pillars--what LLMs can do today, where they fall short, how to engineer prompts that unlock their full power, hands-on case studies from CUHK and peers, and a forward look at next-gen models and the broader AI ecosystem. 
    
    **AI is in its blank canvas era—you need to use it, a lot, to see where it can actually be useful or helpful**. But before that, we wish you will find concrete examples, practical guides and real-world cases here to continue your journey.

    ???- abstract "Site Map"
        ??? info "What LLM Can Do"
            A showcase of current LLM features from NotebookLM to chatbot functionalities and potential educational applications.
            
            - [What LLMs Can Actually Do Today](common-capacities.md) -- A hands-on showcase of current LLM features: synthetic media, conversational agents, document analysis and creative acceleration, with demos and caveats.
            
            ??? example "Software Explainer"
                - [NotebookLM Explainer](notebookLM.md) -- Step-by-step tour of Google's NotebookLM: source ingestion, mind-map visualisation, Q&A and audio summaries for self-study.
            
            ??? example "Functionalities as Chatbot (2024)"
                - [Content Creation via Generative AI](content-creation.md) -- Recipes for drafting text, generating images, video and interactive exercises with GPT-4o and multimodal tools.
                - [AI-Assisted Grading and Feedback](grading-and-feedback.md) -- Blueprint for auto-grading pipelines: rubric encoding, chain-of-thought scoring and LMS-ready JSON outputs.
                - [Role-Playing via Generative AI](role-playing.md) -- Building virtual patient/NPC simulations with branching dialogues, emotional cues and immersive scenario prompts.
                - [AI Mentors in Education: A New Frontier](mentor.md) -- Framework for 24/7 AI advisors: goal-setting prompts, Socratic scaffolds, knowledge-base integration and custom workflows.
            
            ??? example "Applications for Educational Purposes (2024)"
                - [AI-powered Video Generation](aivideo.md) -- Avatar creation, voice cloning and deepfake pipelines for on-demand teaching videos.
                - [AI-Powered Search Engines](search-engine.md) -- Notable examples of semantic search engine for different purpose: Perplexity, Consensus, and Elicit
                - [Lifelike Virtual Characters for Scenario-Based Learning](virtual-character.md) -- From holograms to generative agents; prompt patterns for immersive role-play.
                - [Personalised and Adaptive Learning](palearning.md) -- Diagnostic quizzes, branching content, progress tracking and mastery-based feedback.
                - [A Literature Review of AI in Higher Education](literature-review.md) -- Survey of AI-enabled pedagogy: no-code ML, qualitative analysis, game-based learning and multimodal demos.
                - [Multimodality -- Any-to-Any Generation](multimodality.md) -- Cross-modal AI: text→image/video/audio, semantic search, UI prototyping and data visualisation.
                - [For SEN Students](sen.md) -- AI accommodations: real-time transcription, text simplification, voice assistants and UDL-aligned study aids.

        ??? info "What LLM Cannot Do"
            A reality check on LLM limitations covering common misconceptions, lack of true reasoning and the hallucination problem.
            
            - [What Teachers Actually Ask: AI Limitations](common-faqs.md) -- Answers to teacher FAQs on LLM reliability, cognition, policy and integrity.
            
            ??? example "Understanding LLMs -- Beyond the Black Box"
                - [Can AI Think Like Us? The Reality of Machine "Reasoning"](explainability.md) -- Balanced survey of interpretability research: circuit tracing, feature attribution and the gap between pattern-matching and reasoning.
                - [Why LLMs Make Things Up: The Reality of AI Hallucination](hallucination.md) -- Deep dive into hallucination mechanics: "known-entity" circuits, benchmark rates, confidence illusions and mitigation tactics.

        ??? info "How to Prompt Chatbots"
            A prompt engineering toolkit featuring 4 foundational principles and a curated set of 8 ready-made templates for various tasks.
            
            - [How to Prompt Chatbots: Overview](pe_g.md) -- Four-step prompt-engineering framework: context, personas, structure and template reuse, with resource links.
            
            ??? example "Guides"
                - [The Question-First Method: Building Two-Way Conversations](pe_g1.md) -- "Let the model ask clarifying questions first" to surface missing context.
                - [Creating Specialised AI Personas](pe_g2.md) -- Techniques to "summon" expert personas with tailored role sheets and sample dialogues.
                - [Fix Your Mind: Meta-Prompting for Better Results](pe_g3.md) -- Meta-prompt template: feed prompt+response back to the model for AI-driven improvement suggestions.
                - [Forget What's Been Said -- Use What's Already Here](pe_g4.md) -- Advice to adopt community-vetted prompt libraries and custom GPTs instead of reinventing prompts.
            
                ???+ example "Further Reading"
                    - [Prompting Skills: Now Baked Into AI](pe_g5.md) -- How chain-of-thought and chain-of-drafts moved from manual tricks to built-in features.
                    - [Creating a Second Brain with ChatGPT](pe_g6.md) -- DIY "C.L.E.A.R." memory system and community-shared persistent-memory prompts.
            
            ??? example "Ready-Made Templates"
                - [How to Master Any Topics via Reasoning Models](pe_t1.md) -- Six-prompt cohort: mentor roleplay, Socratic dialogues, teach-back and 30-day mastery plans.
                - [How Not to Get Useless Responses?](pe_t2.md) -- Five tactics: structured frameworks, side-by-side templates, forced stance and iterative refinement.
                - [How to Skim-read and Fact-check?](pe_t3.md) -- Two-stage prompt: extract bullet facts, then summarise and self-audit against source text.
                - [How to Control Output's Word Count?](pe_t4.md) -- Specify current/target lengths with flow-check steps for precise word-count control.
                - [How to Create a Reusable Prompt via C.R.A.F.T.](pe_t5.md) -- Six-part template (Context, Role, Action, Format, Audience, Template) for complex tasks.
                - [How to Make AI Text Sound More Human?](pe_t6.md) -- Prompt patterns and banned-word lists to remove clichés and mimic human writing rhythms.
                - [How to Transfer Past Conversation's Context](pe_t7.md) -- Single-prompt memory summary to migrate tone, style and context across sessions.
                - [How to Make ChatGPT Stop Being a Yes Man?](pe_t8.md) -- Intellectual sparring-partner prompt: analyse assumptions, test logic and offer counterpoints.

        ??? info "Learn From Those Who've Tried AI"
            ??? example "CUHK Use Case -- Dr. Mok (ECO)"
                Dr. Mok embeds AI across his economics curriculum with automated grading, and suggest ideas like research-question refinement, code translation, investment simulations and business-plan feedback.
                
                - [Benchmark Exam Answers in Economics](wallace_1.md) -- Dr. Mok's pipeline for converting exam papers to LaTeX and using AI-generated answers as teaching tools.
                - [Address Student Research Challenges in Projects](wallace_2.md) -- AI-guided regression tutoring, question refinement and methodology support for undergrads.
                - [Simplify, Understand and Convert Codes for Research](wallace_3.md) -- AI-driven code translation workflows: Fortran/MATLAB → Python/R with step-by-step explanations.
                - [Learn Investment Strategy Through AI-Guided Simulations](wallace_4.md) -- Controlled trading sandbox: daily AI prompts, transaction logs and portfolio analysis.
                - [Refining Business Proposals Through AI-Assisted Feedback](wallace_5.md) -- Shark-Tank simulation prompt for investor-panel critique and iterative proposal improvement.
            
            ??? example "Case Studies / Other Universities"
                Real-world higher education examples from journalism, psychology, social work and sociology showing AI-driven assignments, VR simulations and ethical explorations.
                
                - [Journalism and Communication](journalism-and-communication.md) -- AI tools for transcription, voice cloning, fact-checking workshops and AI-enhanced storytelling.
                - [Psychology](psychology.md) -- AI essay critique, simulation scenarios, interactive exercises and creative writing prompts.
                - [Social Work](social-work.md) -- VR simulations, AI mentors, case-management bots and resource recommender workflows.
                - [Sociology](sociology.md) -- AI-assisted curriculum mapping, reflexive dialogue analysis and social-network visualisation cases.

        ??? info "Where is AI Going"
            A forward look at frontier LLMs in 2025, a cost-efficient open-source model called DeepSeek, and AI breakthroughs beyond pure LLM capabilities.
            
            ??? example "Model Evolution"
                - [Recent AI Models after DeepSeek (March 2025)](2025_new_models.md) -- Side-by-side specs of DeepSeek-R1, Claude 3.7, Grok 3 and GPT-4.5, with real-world caveats.
                - [Notable Text-based AI Models Released After GPT-4o](flagship-models.md) -- Survey of Claude 3.5 Sonnet, Mixtral 2, Llama 3, Grok 2 and Apple's "Strawberry."
                - [Flagship LLM from OpenAI -- GPT-4o](gpt4o.md) -- In-depth on GPT-4o's voice, vision and screen-interaction features, plus benchmark comparisons.
            
            ??? example "DeepSeek"
                - [DeepSeek](deepseek.md) -- Introduction to DeepSeek R1: what it is, why it matters, and links to overview, impact, use-cases and privacy.
                - [Why DeepSeek-R1 Matters](deepseek-overview.md) -- Cost-performance analysis, open-source benefits and ecosystem-catalyst insights.
                - [DeepSeek's Market Impact](deepseek-impact.md) -- NVIDIA stock crash, 21 M app downloads and global adoption statistics.
                - [DeepSeek: Applications & Use Cases](deepseek-implications.md) -- Community projects: 3D games, music apps, PDF chat and custom search.
                - [DeepSeek: Privacy & Safety Considerations](deepseek-privacy.md) -- Data-collection policies, self-hosting trade-offs and best practices for sensitive docs.
                - [DeepSeek Resources -- Further Reading](deepseek-resources.md) -- Curated video tutorials and technical articles for DeepSeek integration.
            
            ??? example "AI Development (not just LLM)"
                - [AI Development Tracker: Latest Breakthroughs & Tools (since Mar 2025)](AI_development_tracker.md) -- Chronological diary of Runway Gen-4, GPT-4o image, Gemini 2.5, audio models and more.
                - [Personal Finding and Sharing (outdated, 2024)](blog.md) -- Personal lab notebook: o1 demos, Claude Artifacts, Qwen2-VL-72B, SocialAI, Copilot experiments and advanced prompt tips.



!!! tip "Getting Started with AI chatbots"
    New to AI? These tools are easier to use and work better than you think. Here's how to start.

    ??? question "What are AI chatbots?"
        AI assistants like ChatGPT, Claude, and Gemini function as intelligent conversation partners trained on massive text datasets. They process and generate human-like text to answer questions, create content, explore ideas, and condense information. 
        
        [Learn more about early-2025 AI models →](2025_new_models.md)

    ??? success "Three leading AI chatbots"
        - **ChatGPT:** Versatile and widely used. Excellent for creative writing, programming assistance, and everyday inquiries.
        - **Claude:** Specialises in thoughtful analysis. Particularly strong with document processing, nuanced writing, and natural-sounding responses.
        - **Gemini:** Google's research-focused assistant. Integrates well with Google's ecosystem and provides up-to-date information.

    ??? info "How to start"
        1. Visit [ChatGPT](https://chat.openai.com/), [Claude](https://claude.ai/), or [Gemini](https://gemini.google.com/). (Note: **VPN** required)
        2. In Hong Kong, you can also use [Poe](https://poe.com/) which provides access to multiple AI models in one interface
        3. Type your request in the text box
        4. Press enter to see the response

        [Watch our video tutorials →](https://www.iorad.com/help-center/162026?roleId=11284)

    ???- warning "Be specific to get better results"
        Focus your requests with details. Instead of "write about economics," try: **"Explain how supply chain disruptions affect inflation rates, with three historical examples."** 
        
        [Learn our prompt engineering framework →](pe_g.md)

    ??? example "Try these five academic tasks"
        - **Create content:** Generate lecture notes, slides, or assessment materials with specific learning objectives. [Content creation guide →](content-creation.md)
        - **Build AI mentors:** Develop AI advisors that use Socratic questioning and scaffold learning for students. [AI mentor framework →](mentor.md)
        - **Support research:** Refine research questions and methodologies for student projects using AI guidance. [Research applications →](wallace_2.md)
        - **Improve writing:** Transform AI-generated text to sound more natural by removing clichés and varying sentence structure. [Writing techniques →](pe_t6.md)
        - **Master new topics:** Use structured prompts like expert interviews and Socratic dialogues to learn complex subjects. [Learning methods →](pe_t1.md)

    ??? success "Why AI matters in academia"
        These tools help automate routine tasks, assist with research, create teaching materials, and enhance student learning experiences. [See how colleagues use AI →](journalism-and-communication.md)

    Start with one simple task today. The best way to understand AI's value is through direct experience.
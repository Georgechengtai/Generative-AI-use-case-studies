# What Teachers Actually Ask: AI Limitations

!!! note "Editor's Note"
    These FAQs reflect authentic questions we've collected from our Co-PIs. 
    It addresses four key areas of concern: **information reliability**, **cognitive impacts on students**, **content generation limitations**, and **academic integrity challenges**. To be specific, we use the term Large Language Model (LLM), instead of AI, to represent text-based AI systems like ChatGPT.

    We feature two issues in detail that teachers and students commonly ask about: [Can AI think?](explainability.md) and [Why AI make stuff up?](hallucination.md). These topics attract significant attention because they address fundamental misconceptions about **how LLMs actually work versus how they appear to work**. *Feel free to share these resources with your students when they ask these inevitable questions.*


## Understanding LLM Search and Information Reliability

!!! question "Is LLM search better than Google for my class research projects?"

    LLM search reads queries more deeply than traditional search, indexes webpages beyond keywords, and creates summaries instead of just links.
    
    ??? warning "My student cited an LLM search result that wasn't accurate. Why?"
        LLMs often make up sources or attribute information incorrectly when generating citations.
    
    ??? warning "I asked an LLM about recent policy but got outdated info. Why?"
        LLMs don't clearly tell you when their knowledge cuts off, so they answer confidently with outdated information.
    
    ??? warning "I corrected the LLM about a historical fact, but it made the same mistake later. Why?"
        Your corrections only apply to your current conversation - they don't permanently teach the LLM. In fact, LLM can "pretend" it agrees your currections but don't handle them.
    
    ??? warning "Can LLM search replace my subject matter expertise?"
        LLMs work best with general topics but lack depth in academic subjects. They might connect ideas across disciplines in interesting ways, but you'll need to verify these connections yourself.

## Cognitive Impact and Learning Process

!!! question "My students use LLMs for everything. Should I worry?" 
    Yes, when students rely too heavily on LLMs instead of thinking for themselves.
    
    ??? warning "Why do students understand less when LLMs explain everything to them?"
        This happens through cognitive offloading - students hand over their thinking to LLMs and skip crucial problem-solving steps. They outsource their thinking but get the job done.
    
    ??? warning "My students say LLM explanations are clearer than mine, but they still fail tests. Why?"
        LLMs simplify complex topics too much, giving students a false sense of understanding without real depth.
    
    ??? info "What does research say about how LLMs affect learning?" 
        Recent studies show that heavy LLM use reduces information retention and critical thinking skills. Research by Gerlich found younger people depend more on AI tools and show weaker critical thinking compared to older adults. Higher education levels help maintain critical thinking regardless of AI use. [Read the full study on cognitive offloading](https://www.mdpi.com/2075-4698/15/1/6).

## Content Generation Limitations

!!! question "Why can't I generate images of public figures in compromising situations when demonstrating content policies to my class?" 
    LLM platforms restrict certain content creation to prevent misuse.
    
    ??? warning "I want to show my class how content filters work. Why are these requests blocked?"
        LLM platforms block potentially misleading or inappropriate content of real people to prevent abuse and protect people's image rights.
    
    ??? warning "Are there tools with fewer restrictions for educational purposes?"
        
        While mainstream platforms have stricter policies, Open source model like Stable Diffusion have limited restrictions. Open source models are particularly susceptible to misuse because their decentralised nature makes content policies harder to enforce consistently. (To be honest, it is impossible to stop people use celebrities's media for training models, and sharing the model weights with the communities afterwards)
    
    ??? info "Are deepfakes made with the same tools I use in class?" 
        No. Deepfakes require specialised AI tools designed specifically for face-swapping, audio mimicking and video rendering. These tools work differently than mainstream LLMs, though people can jailbreak and use them in wrappers (which you shouldn't do).

!!! question "Can I turn my lecture slides into videos using LLMs?" 
    Yes, but expect serious limitations on what these tools produce.
    
    ??? warning "What can LLM video tools actually create from my materials?"
        They animate text, create basic scenes, and add narration, but struggle with anything complex.
    
    ??? warning "Why can't the LLM visualize my economic model properly?"
        Video generators work by creating frame-by-frame animations, not by understanding conceptual relationships. They don't know what your economic model means (or how it should be represented visually), so they can't translate abstract ideas into meaningful visuals. 

    ??? info "Which tools work best for turning teaching materials into video?" 
        Try [Pictory](https://pictory.ai/) for converting presentations to video or [Bookwatch](https://bookwatch.com/) for transforming books into video content.

## Assessment and Academic Integrity

!!! question "How can I tell if my students use LLMs for their essays?" 
    You probably can't detect it reliably unless lazy students make obvious mistakes.
    
    ??? warning "Do reliable LLM detectors exist for catching cheating?"
        No detector is 100% accurate. Current detectors have two major problems: they flag human-written content as AI-generated, creating a false sense of security (even historical documents like the Declaration of Independence), and they work much better on some LLMs than others. No detector works well across all systems.
    
    ??? info "How should I redesign assignments knowing students use LLMs?" 
        Focus on in-class work, process documentation, personal reflection, and applying concepts rather than just synthesizing information.
    
    ??? warning "Should I ban LLMs from my classroom?"
        Bans rarely work and don't prepare students for real-world technology use. Design assessments that test understanding rather than just polished output.
    
    ??? info "How do I keep things fair when some students have premium LLM access?" 
        Either provide equal access through your school, or evaluate students on their thinking process rather than how polished their work looks.
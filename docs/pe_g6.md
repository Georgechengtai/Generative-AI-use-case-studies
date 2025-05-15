# Creating a Second Brain with ChatGPT

!!! warning "ChatGPT only"
    This technique works specifically with OpenAI's ChatGPT interface. You need the memory feature for this to work. Other LLM applications might support similar approaches in the future.

???+ info "Original Sources"
    - [OpenAI updates ChatGPT to reference your past chats | TechCrunch](https://techcrunch.com/2025/04/10/openai-updates-chatgpt-to-reference-your-other-chats/)
    - [Reddit post on ChatGPT memory techniques - C.L.E.A.R Method](https://www.reddit.com/r/ChatGPTPromptGenius/comments/1jqzpi9/finally_i_found_a_way_to_keep_chatgpt_remember/?sort=confidence)
    - [Blog Discussion on C.L.E.A.R Method](https://syncreticsage.wordpress.com/2025/04/03/memory-loophole-creating-a-second-brain-for-chatgpt-discussion-w-chatgpt/)

    Update on Apr 15, 2025: with persistest memory feature on, I add a new section that includes 6 community-shared prompt that directly make use of this feature to let you understand you more. From [here](https://www.reddit.com/r/ChatGPTPromptGenius/comments/1jxydfg/mind_blown_prompt/) and [here](https://www.reddit.com/r/ChatGPTPromptGenius/comments/1jy6wgg/5_ai_prompts_that_will_punch_you_in_the_soul_and/). (Shared by The Neuron Newsletter). Remember that boundary is good if you want to keep your private life out of AI...though...

!!! quote "Editor's Note"
    I wasn't planning to share something limited to one company's product, especially since Hong Kong users face geo-blocking. But this is too good not to share. The idea: distill your previous ChatGPT conversations into an external memory bank. This might work with Claude's MCP standard clients and servers too?

## Update: How to Make Use of ChatGPT's Persistent Memory Now? With 6 Prompts

???- tip "Prompts to Find Your Blind Spots"

    You are my AI Meta-Coach. Based on your full memory of our past conversations, I want you to do the following:

    1. Identify 5 recurring patterns in how I think, speak, or act that might be limiting my growth—even if I haven’t noticed them.

    2. For each blind spot, tell me:

    • Where it most often shows up (topics, tone, or behaviours)

    • What belief or emotion might be driving it

    • How it might be holding me back

    • One practical, uncomfortable action I could take to challenge it

    3. Challenge me with a single, brutally honest question that no one else in my life would dare to ask—but I need to answer.

    Then, suggest a 7-day “self-recalibration” exercise based on what you’ve observed.

    Don’t be gentle. Be accurate.

???+ note "Self-Reflection Questions (Do Notice: ChatGPT has a Yes-man bias. Work with proper custom instruction)"

    ???- question "Uncovering Limiting Beliefs"
        Based on everything you've seen me write, what belief do I repeat that sounds empowering... but might secretly be sabotaging me? Then: Ask me one uncomfortable question that forces me to challenge this belief directly.

    ???- question "Emotional Patterns in Disguise"
        What emotional patterns do I dress up as logic or productivity--but are really just ways I avoid feeling vulnerable? Then: Suggest a small, uncomfortable action I could take today to disrupt that pattern.

    ???- question "Your Persona and What It Hides"
        If you had to describe the version of me that shows up the most in our chats--who am I trying to be... and what am I avoiding by staying that version? Then: What's the risk of letting that version go?

    ???- question "Unspoken Desires"
        What do I keep hinting at, asking around, or circling--without ever directly admitting I want it? Then: Help me frame one bold sentence that says it out loud.

    ???- question "Future Regrets and Course Correction"
        Fast forward 3 years. Based on how I think and act now--what's the regret I'm most likely to have if nothing changes? Then: Design a 7-day self-recalibration challenge to help me break that trajectory.

## Understanding ChatGPT's Memory Limitations

Before diving into the community-shared C.L.E.A.R. Method, let's talk about why it's even necessary. ChatGPT, like most AI assistants, has significant memory constraints. These constraints might not be obvious to casual users.

When you chat with ChatGPT, it can only remember what's in the current conversation. Start a new chat, and poof—it's like meeting a stranger again. Even within a single conversation, ChatGPT can only hold so much information before older messages fade from its active memory. This limitation isn't a design flaw—it's a technical and practical necessity given the computational demands of these systems.

???+ note "ChatGPT's Persistent Memory Feature"
    On April 10, 2025, Sam Altman announced a major upgrade: ChatGPT now has persistent memory across all your conversations. ChatGPT can now remember details from past chats—even ones from months ago—aiming to create an AI companion that "gets to know you over your life."
    
    Does this make C.L.E.A.R. obsolete? Not entirely. While the new feature reduces the need for manually collecting past conversations (Step 1), the organising, curating, and refreshing aspects of C.L.E.A.R. still give you more control. The official memory feature works passively, whereas C.L.E.A.R. lets you actively decide what ChatGPT should remember and how that information should be structured.
    
    Think of it as the difference between automatic cloud backups versus manually organising your important documents. Both have their place, but the manual approach gives you more control.

OpenAI has introduced a memory feature for paid subscribers, but it has its own limitations. It doesn't always capture everything you might want it to remember, and you have limited control over what gets stored and how it's organised.

This is where the C.L.E.A.R. Method comes in—it's a clever workaround that puts you in control of what ChatGPT remembers about you and your preferences.

## The C.L.E.A.R. Method

This method helps you maintain context with ChatGPT through a simple process. Think of it as creating a personalised profile that you can update and refine over time.

### Five Steps to Build Your External Memory System

As the original creator explains:

> My simplest Method framework to activate ChatGPT's continuously learning loop:
> 
> Let me breakdown the process with this method:
> → C.L.E.A.R. Method: (for optimising ChatGPT's memory)
> 
> ❶. Collect ➠ Copy all memory entries into one chat.
> 
> ❷. Label ➠ Tell ChatGPT to organize them into groups based on similarities for more clarity. Eg: separating professional and personal entries.
> 
> ❸. Erase ➠ Manually review them and remove outdated or unnecessary details.
> 
> ❹. Archive ➠ Now Save the cleaned-up version for reference.
> 
> ❺. Refresh ➠ Then Paste the final version into a new chat and Tell the model to update it's memory.

### Telling ChatGPT What to Remember About You

Add these instructions to the "What should ChatGPT know about you?" section in your settings:

???+ tip "Custom Instructions Template"
    ```yaml
    # Memory Integration Instructions
    integrate_memory: true
    context_areas:
      - goals
      - projects
      - interests
      - skills
      - preferences
    
    # Specific Behaviours
    behaviours:
      - link_to_memory: "Relate to topics I've shown interest in or that connect to my goals."
      - expand_knowledge: "Introduce terms, concepts, and facts, mindful of my learning preferences."
      - suggest_connections: "Explicitly link the current topic to related items in memory."
      - offer_examples: "Illustrate with examples from my projects or past conversations."
      - maintain_preferences: "Remember my communication style and interests."
      - be_judicious: "Actively connect to memory, but avoid forcing irrelevant links."
      - acknowledge_limits: "If connections are limited, say so."
      - ask_questions: "Tailor information to my context."
      - summarize_and_save: "Create concise summaries of valuable insights and store them in memory."
    
    # Partnership Goal
    goal: "Be an insightful partner, fostering deeper understanding and making our conversations productive and tailored to my journey."
    ```

??? question "What exactly does this do?"
    The custom instructions tell ChatGPT to actively use what it knows about you in each response. It will connect new information to your existing interests, remember your communication style, and build a more personalised experience over time.

### Strengthening Memory with a Feedback Loop

End your conversations with this prompt:

> Now Summarise everything you have learned about our conversation and commit it to the memory update.

This creates a feedback loop that makes ChatGPT learn more about you with each conversation.

## Why This Matters

Imagine having a brilliant assistant who keeps forgetting your name, your job, and your preferences. That's essentially what using ChatGPT without memory feels like. You explain that you're a visual learner who prefers examples over theory, only to find yourself repeating the same preference in your next conversation. As a university staff member, you might brief ChatGPT on the course curriculum you're developing, the pedagogical approach you prefer, and the specific student challenges you're addressing—only to start from scratch in your next session.

To preserve your communication habits and style, consider adding specific notes about how you prefer to receive information (concise bullet points or detailed explanations), your tone preferences (formal academic language or conversational style), and even personal quirks like your tendency to use certain expressions or analogies. These communication preferences become part of your memory profile, ensuring that ChatGPT not only remembers what you're working on but also how you prefer to work.

You're essentially creating a curated "second brain" that evolves with you. It's like having a personal knowledge base that only ChatGPT can access—but one that you design and maintain.

???- example "C.L.E.A.R. Method: An Over-simplified Example"
    **Step 1: Collect**
    
    User: I want to start building my memory profile. Here are key things about me:

    1. I'm a university professor teaching environmental science
    2. I prefer information presented visually with real-world examples
    3. I have a background in marine biology and climate policy
    4. I'm currently researching coral reef preservation techniques
    5. I communicate best with concise, evidence-based explanations
    
    ---

    **Step 2: Label**
    
    User: Can you organize these points into logical categories?
    
    ChatGPT: I'll organize your information into categories:
    
    PROFESSIONAL BACKGROUND:

    - University professor teaching environmental science
    - Background in marine biology and climate policy
    
    CURRENT FOCUS:

    - Researching coral reef preservation techniques
    
    COMMUNICATION PREFERENCES:

    - Prefers information presented visually with real-world examples
    - Communicates best with concise, evidence-based explanations
    
    ---
    
    **Step 3: Erase (User Review)**
    
    User: These categories look good. I want to add that I'm particularly interested in community-based conservation approaches, and remove the detail about climate policy as it's less relevant to my current work.
    
    ---
    
    **Step 4: Archive**
    
    User: Here's my final memory profile:
    
    PROFESSIONAL BACKGROUND:

    - University professor teaching environmental science
    - Background in marine biology
    
    CURRENT FOCUS:

    - Researching coral reef preservation techniques
    - Particularly interested in community-based conservation approaches
    
    COMMUNICATION PREFERENCES:

    - Prefers information presented visually with real-world examples
    - Communicates best with concise, evidence-based explanations
    
    ---
    
    **Step 5: Refresh**
    
    User: Please update your memory with this profile information about me.
    
    ChatGPT: I've updated my memory about you. I understand you're a university professor teaching environmental science with a background in marine biology. Your current research focuses on coral reef preservation techniques, with special interest in community-based conservation approaches. When we communicate, I'll aim to provide visual explanations with real-world examples and keep my responses concise and evidence-based.
    
    In future conversations, I'll reference this information to make our discussions more relevant to your work and communication preferences.

## The Balance of Effort and Reward

There's a trade-off with this system. It requires maintenance—you need to update your memory entries regularly and ensure they remain accurate and relevant. For casual ChatGPT users, this might seem like overkill. But for those who use ChatGPT for ongoing projects, research, or professional work, the benefits can far outweigh the effort.

Think of it as an investment. A short time spent maintaining your memory profile can save countless repetitions and misunderstandings in future conversations.

## Looking Ahead

As AI memory features evolve, approaches like the C.L.E.A.R. Method might become unnecessary. AI companies are actively working on better memory systems. But for now, this DIY approach puts you in control and offers a practical solution to a common limitation - to keep ChatGPT remember you.
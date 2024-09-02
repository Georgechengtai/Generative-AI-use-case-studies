### Introduction

In the rapidly evolving landscape of education, artificial intelligence is playing an increasingly significant role. One of the most exciting developments in this field is the emergence of AI mentors powered by generative AI technology. These AI mentors represent a new frontier in personalised learning, offering students in various disciplines, unprecedented access to knowledge and guidance.

Generative AI, exemplified by models like GPT-4, has the ability to understand context, generate human-like text, and engage in complex dialogues. When applied to education, this technology can create AI mentors that adapt to individual student needs, provide instant feedback, and offer explanations on a wide range of topics.

Unlike traditional educational software, AI mentors powered by generative AI can:

1. Engage in open-ended conversations, allowing students to explore topics in depth
2. Provide explanations tailored to the student's level of understanding
3. Generate examples, analogies, and hypothetical scenarios to illustrate complex concepts
4. Offer writing assistance and feedback across various academic disciplines
5. Help students develop critical thinking skills through Socratic questioning

While AI mentors are not meant to replace human teachers, they can serve as powerful supplementary tools, available 24/7 to support students in their learning journey.  In fields like social sciences, where critical thinking and nuanced understanding are crucial, AI mentors can help students practice analysis, debate ideas, and explore different perspectives.

### Scope

The journey of creating an AI mentor powered by generative AI involves several stages of increasing complexity and capability. This guide focuses primarily on the foundational first two levels, which are accessible to teachers and developers with varying degrees of technical expertise.

1. **Simple Chatbots**:
    - **Basic question-answering** capabilities
    - Limited to **pre-programmed responses**
    - Narrow scope of knowledge
2. **Chatbots with Context and Knowledge Bases**:
    - Ability to **maintain context** in conversations
    - Access to **broader and custom knowledge bases**
    - More **natural and fluid interactions**
    - Improved understanding of nuanced queries
3. **Enhanced Capabilities**:
    - **Web browsing**: Real-time access to current information
    - **Image generation**: Creating visual aids or diagrams on demand
    - **Code interpreter**: Assisting with data analysis or demonstrating computational concepts
4. **Integration with Third-Party Services**:
    - Retrieving information from **specialized databases** or academic repositories
    - Accessing **course management systems** for personalized student information
    - Interfacing with **external tools** (e.g., citation managers, data visualisation software)
5. **Fine-tuning and Personalisation**:
    - Setting **priorities** for search results and knowledge base utilisation
    - **Reviewing and updating** answers based on feedback
    - Incorporating **institution-specific information** and policies
6. **Continuous Learning and Improvement**:
    - **Updating knowledge** based on new academic publications
    - **Learning from interactions** to improve response quality
    - Adapting to **emerging trends** in educational methodologies


### Existing Products and Applications

The field of AI mentors and generative AI applications is rapidly evolving. The following selection represents a range of approaches, showcasing the diversity of tools available:

1. **OpenAI GPT Platform**:
    - Offers state-of-the-art language models like GPT-4
    - Provides powerful AI capabilities via API access
    - Includes GPTs (custom versions of ChatGPT) for tailored AI experiences
    - Best for: A wide range of users, from developers seeking direct API access to those creating custom AI assistants via GPTs
2. **Poe AI**:
    - Provides access to multiple AI models, including OpenAI's, in a user-friendly chat interface
    - Allows users to interact with and compare different AI assistants easily
    - Requires minimal technical knowledge to use
    - Best for: Teachers and individuals looking for an easy way to explore and use various AI models for experimental purposes
3. **Hugging Face**:
    - Open-source platform with a vast library of pre-trained AI models and tools
    - Provides a balance of accessibility and customisation options
    - Best for: Researchers and developers who want to experiment with a wide range of models and fine-tune them for specific purposes
4. **Rasa**:
    - Open-source framework for building conversational AI assistants
    - Allows for creation of more customised and context-aware chatbots
    - Focuses on building complete conversational AI systems
    - Best for: Those looking to create specialised AI assistants with specific conversational flows

### How to build an AI mentor using Custom GPTs

One exciting development in educational technology is the ability to create personalised AI mentors using Custom GPTs. This guide will walk you through the process. (POE allows you to create custom bots easily, but its functionalities and customisability are quite limited)
##### What is a Custom GPT?  
For those new to this concept, a Custom GPT is a personalised version of ChatGPT, an AI chatbot. It's like training a virtual assistant to be an expert in a particular area of social sciences. Don't worry if you're not tech-savvy - no coding is required! (Though admittedly, if you aim to incorporate third-party services within Custom GPTs, you have to understand the services and integration to make the API calls.)

**Step 1: Define Your AI Mentor's Purpose**

First, consider what kind of mentor would be most beneficial for your students. Some ideas include:

- **A research methodology advisor** to guide students through various research designs
- **A statistics tutor** to help with quantitative analysis
- **A career counsellor** specialising in career paths in Hong Kong
- **A writing coach** for academic papers and dissertations

Think about the challenges you or your peers face in your studies at CUHK and how an AI mentor could help.

**Step 2: Access the GPT Builder**

You'll need a **ChatGPT Plus subscription** to get started. Once logged in:

1. Look for the **'Create a GPT' option**.
2. Click to open the GPT Builder interface.

**Step 3: Start Creating**

You can either:

1. **Chat with the GPT Builder**, describing your ideal mentor for your students.
2. Use the **'Configure' options** to set things up manually.

For example, you might say, "I want to create a research methodology advisor that can guide CUHK social science students through various research designs, with a focus on local Hong Kong contexts."

**Step 4: Personalise Your Mentor**

Give your AI mentor a **name and personality** that resonates with your students. You could:

- Choose a name like 'CUHK SocSci Guide'
- Write a **brief description** of its expertise in social science disciplines taught at CUHK
- Select an **avatar** that represents CUHK or the Faculty of Social Sciences

**Step 5: Build Your Mentor's Knowledge Base**

This is where you 'educate' your AI mentor about your courses. You can:

- **Upload relevant documents** (e.g., CUHK course syllabi, faculty handbooks)
- Provide **links to CUHK Social Science Faculty websites**
- Give it specific instructions on **CUHK's academic policies and research ethics guidelines**

For instance, if you're creating a statistics tutor, you might upload materials from CUHK's quantitative methods courses.

**Step 6: Set Up Conversation Starters**

Create icebreakers relevant to CUHK social science students. For a research methodology advisor, these might include:

- "How do I choose between qualitative and quantitative methods for my Hong Kong-based study?"
- "Can you explain the ethical considerations for conducting interviews in Hong Kong?"
- "What are some effective ways to recruit participants for my study at CUHK?"

Be aware, without building knowledge base in step 5, the output can be too general and lack of relevant context. without finetuning and testing in step 7 and step 8, the output may be situationally relevant but in an unfavourable manner.

**Step 7: Fine-tune Your Mentor's Personality**

Shape your AI mentor to reflect your teaching philosophy. You might want it to be:

- **Encouraging and supportive**, understanding the pressures of university life in Hong Kong
- **Knowledgeable about both Western and Eastern social science perspectives**
- Able to provide **examples relevant to Hong Kong and Greater China contexts**

**Step 8: Test Thoroughly**

Before sharing your AI mentor with fellow students, **test it rigorously**. Ask it questions about your course contents, local research contexts, or current social issues in Hong Kong.

**Step 9: Add Extra Capabilities (Optional)**

Consider adding abilities like:

- **Web browsing** (to find up-to-date information)
- **Code interpreter** (for helping with SPSS, Python or R inputs and outputs)
- **Image Generation (Dall-E 3)** as well as other top-performing models like **Sora for video generation**, **Whisper for voice generation** (The advanced voice mode will be incorporated into the GPT interface in future by default)

**Step 10: Publish Your AI Mentor**

Decide how widely you want to share your creation:

- **Only me** (just for your personal use)
- **Only people with a link** (for your classmates or research group)
- **Public** (for all CUHK students or even wider)

Step 11: Gather Feedback and Improve

Collect feedback from your peers and professors in the Faculty of Social Sciences. Use their insights to refine your AI mentor, ensuring it remains relevant and helpful for CUHK students.

### Example Prompts of TutorAI workflow

Let's have a look TutorAI, an application that creates interactive education content on any topic. The developer has kindly share the 7 prompts used behind the hood:

**1. Generating the Modules**  
Prompt: **"A student wants to learn about a topic, generate 4 modules that a student can use to learn. A module consists of a title and a description, separated by a colon."**

**2. Generating the Lessons**  
Prompt: **"Create an outline with 4 sections for teaching a student about the topic and module"**

**3. Generating the lesson content**  
Prompt: **"Teach a student about the below topic and subtopic and by writing multiple paragraphs"**

**4. Simplify**  
Prompt: **"Summarise this for a second-grade student"**

**5. Examples**  
Prompt: **"Generate concrete examples for this to make it clearer"**

**6. Quiz**  
Prompt: **"Write one hard multiple choice question and its answer to make sure the reader understands the following content"**

**7. Ask a question**  
Prompt: **"Answer the question about the content"**

TutorAI integrates these prompts into a single, user-friendly web-based interface for quick interaction. Users do not type the prompts themselves; instead, they simply input a topic they want to learn about. The system then seamlessly utilises these prompts behind the scenes to generate a comprehensive learning experience. The interface presents users with modules, lessons, and interactive elements, allowing them to navigate through the content and engage with various learning aids at the click of a button.

To achieve similar results is not easy, and requires some level of coding knowledge. However, we would like to show how a simple yet useful application can be built in 7 layers of AI, knowing the prompts can be customised and the application can be used for various purposes and incorporated into many possible workflows.
### Appendix
- [Create Your Custom GPT Without Coding: A Step-by-Step Guide to Personalized AI | Dare To Be Better](https://medium.com/dare-to-be-better/how-i-created-custom-gpt-dsa-tutor-gpt-no-coding-b1227459aaf5)
- [Custom GPTs Unleashed: Creating a GPT-powered Math Tutor in a blink | by Rahul Pandey | DSciEr | Medium](https://medium.com/dscier/custom-gpts-unleashed-creating-a-gpt-powered-math-tutor-in-a-blink-323130c0903f)
- [Daniel Habib's X tweets on TutorAI](https://x.com/DannyHabibs/status/1598069511369867264)
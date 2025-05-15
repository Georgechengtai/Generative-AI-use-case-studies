# How to Skim-read and Fact-check?

!!! note "Original Source"
    From [The Neuron](https://www.theneurondaily.com/p/self-driving-showdown). A simple two-stage prompt when casually throwing documents in chat for understanding.

???+ quote "Editor's word"
    For serious work, we definitely recommended you to use NotebookLM though. Not only it prevent non-source-based output, it also have an in-built citation retrival features. But surely, sometimes you just want to spend 10 minutes to grasp a sense of something, then below prompt certainly helps.

???+ example "Skim-read"
    Copy and paste this prompt alongside your uploaded document to output a skimmable bullet point summary.
    
    `Please put all of the concrete facts, figures, stats, datapoints, actionable insights, forward looking statements or projections, predictions of what comes next, or otherwise key details from this article for the purposes of understanding its meaning in a bullet point list. `

    `You should at a minimum, have a list of 25-50 facts. If less than 25 facts are present, move on to the step below.`

    `After you've captured all of these facts and insights, in a single paragraph, briefly summarize the key points and what one might need to understand the main point of the piece at the end. Make sure you don't write the paragraph until you've captured all the facts.`

    `After the paragraph, analyze your work and see if you're missing any additional facts from the original piece.`

    `Think step by step to approach this task.` 
    

???+ tip "Fact-check"
    Copy and paste below prompt alongside the fact you want to check. With quoted text in source document, you can find and search for it in the original document for verification
    
    ```yaml
    Please give me the full context of this fact, directly quoted in context so I can fact check it: 
    
    [Fact here] 
    ```
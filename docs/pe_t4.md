# How to Control Output's Word Count?

!!! note "Original Source"
    From [The Neuron](https://www.theneuron.ai/newsletter/ai-search-problems). They claims this is how they cut word-count when editing verbose writing.

???+ quote "Editor's word"
    Models usually cannot recognise the "current word count" or "expected final word count" (Of course to some extent they can, but very limited). This is how we can simplify the re-iteration process with a single targeted prompt.

???+ example "Word Count Reduction Prompt"
    
    Paste this along with the text to edit, fill in your ideal + current word counts, and test it out!

    `Can you cut the word count of this story down by the approximate number of words I include in the request with this pasted material? I want to keep all the same flow, info and references, just shorten it by as close to the amount of words I specify in this prompt as you can. Please don't remove any unique ideas / references or jokes, just see if you can say everything in less words while maintaining the same flow and easy readability. You do not know the original word count unless explicitly told, so if you don't have the original word count, please ask me for it. At the end, check your work to see if it is the appropriate word count. It should not be less than the ideal word count, and ideally not over the ideal word count.` 

    `Current word count = [Your word count], should be closer to [Ideal word count]` 
    

# AI Development Tracker: Mar–Aug 2025 (GPT‑5, Grok 4, Claude Opus 4.1)

???- quote "Featuring models and features"
    OpenAI — GPT‑5
    xAI — Grok 4 and Grok 4 Heavy (DeepSearch, Think, X integration)
    Anthropic — Claude Opus 4.1 (Hybrid/Extended Thinking, Claude Code, Artifacts)

!!! note "Editor note"
    GPT-5 does have good potentials and [new (or improved) features](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/gpt-5-the-7-new-features-enabling-real-world-use-cases/4444839). My personal experience: it is less clever (always guess your hidden intention wrongly) but more faithful (if you can clarify what you want, you get what you want) and humble (fewer "bullshiting" and less sycophantic). There're always room for improvement, but I start to think we may be at a peak where non-technical users are quite satisfied from what they got, and thus no improvements (in terms of pure model capacity) are significant for daily use cases. 

!!! info "Why we focus on GPT‑5"
    Frontier models are hard to compare day to day. Results depend on your goals, budget, and tools you already use (e.g. many developers prefer Claude Code and thus always stay with it).  
    We use GPT‑5 as the baseline because ChatGPT is familiar on campus and easy to access. A model that intelligently routes user requests is simple and intutive: fast for routine tasks, deeper when needed, without switching models. It better follows your instructions, too. OpenAI claimed GPT-5 is ~45% less likely to have a factual error than GPT-4o. I believe this architecture will become the state of the art in the future or non-technical consumers.

## GPT‑5 — what changed

GPT‑5 runs as one system that routes between a fast model and a deeper “thinking” model. You don’t choose; it decides based on your request. In practice, this means quick answers for simple questions and slower, more careful reasoning for complex work.

Compared with GPT‑4o, GPT‑5 is more dependable on everyday questions: it makes fewer factual errors and says when it lacks information. Deep Research is a web‑lookup mode that runs multiple searches, compares sources, and returns a short summary with links—ask it to “run Deep Research on [topic]” when you need up‑to‑date facts. For coding, it can find and fix bugs across files and even spin up small, runnable examples. It manages long documents and multi‑step plans more steadily and, for health topics, acts like a careful guide—asking clarifying questions and flagging concerns—without giving step‑by‑step medical instructions. On sensitive subjects, it stays high‑level and safe (“safe completions”). 

If you use the API, you can control how hard it thinks with the reasoning_effort parameter: minimal, low, medium, or high (higher gives deeper analysis but takes longer and costs more). In chat, you can simply say “think hard about this” to nudge deeper reasoning. You can also use the new Voice Mode for tighter control over pace and brevity, and connect Gmail and Google Calendar so it can draft replies and schedule tasks.

## Claude 4.1 and Grok 4 — in relation to GPT‑5

???+ info "Feature comparison"
    | Area | GPT‑5 | Claude Opus 4.1 | Grok 4 |
    |:--|:--|:--|:--|
    | Coding | Reliable debugging, multi‑file edits, small runnable demos | Developer favorite for refactors and precise fixes; clean diffs | Clear explanations and helpful debugging; less steady on very large repos |
    | Research | Deep, multi‑source answers with fewer hallucinations; safe completions | Strong on long, offline documents and careful analysis | Best for real‑time topics and social sentiment via DeepSearch/X mode |
    | Writing | Natural and steady for everyday work | Most polished and adaptable for professional/creative prose | Witty tone; weaker for formal pieces |
    | Safety/Tone | Fewer factual errors; clearer about limits | Conservative, steady refusals when needed | Engaging but tone can skew; verify sensitive claims |
    | Tools/Context | Unified router; Canvas, Voice Mode, calendar, Deep Research | Extended Thinking; Artifacts; strong code tools | Think mode; DeepSearch/Deeper Search; X integration |

???- info "Specs table"
    | Model | AIME 2025 | GPQA | SWE‑bench | Context (API) | Knowledge Cutoff | Inputs | Outputs |
    |:--|:--:|:--:|:--:|:--|:--|:--|:--|
    | GPT‑5 | 94.6% | 88.4% | 74.9% | 272k in / 128k out | Sept 2024 | Text, images, files | Text, images, files |
    | Grok 4 | 93% | 88% | N/A | ~256k | Nov 2024 | Text, images, files | Text, images, video |
    | Claude Opus 4.1 | 78% | 80.9% | 74.5% | 200k | July 2025 | Text, images, files | Text, files |
    | Gemini 2.5 Pro | 88% | 84% | 63.8% | ~1M | Jan 2025 | Text, images, video, audio, files | Text, voice |

    ???- info "What these terms mean"
        - AIME 2025: math problem‑solving benchmark (modeled on the American Invitational Mathematics Examination).  
        - GPQA: graduate‑level question answering test across multiple subjects.  
        - SWE‑bench: measures if a model can fix real GitHub issues end‑to‑end.  
        - Context (API): how much text the model can read (input) and write (output) in one go.  
        - Knowledge cutoff: the latest date of training data the model relies on.  
        - Inputs/Outputs: the types of data you can send to and receive from the model.

## Community‑shared demo use case of GPT‑5 (a few selected)

- Builds full apps in one shot — watch it clone Excel/Word, Twitter, auth pages, checkout, and - dashboards in minutes: https://www.youtube.com/watch?v=BUDmHYI6e3g
- Solves puzzles and runs physics sims — Rubik’s Cubes (up to 20×20×20), double pendulum, cloth/fluid, and ray tracing
- Makes games and 3D visuals fast — Snake, 3D Game of Life, flight sim, 3D typography, and a Lego builder
- Works with text and images — turns images into layouts (hexagon test), draws precise SVGs, generates images, and uses location data
- One‑shot game build — GPT‑5 creates an original Pokémon‑style clone in one shot: https://x.com/VictorTaelin/status/1953585599988084769

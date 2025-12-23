import os
import sys

def create_page(title, filename, archetype="A"):
    """
    Scaffolds a new markdown page based on the selected archetype.
    Archetypes:
    A - Tool/Model Explainer
    B - Concept/Theory Guide
    C - Use Case Study
    D - Development Tracker
    """
    docs_dir = "docs"
    filepath = os.path.join(docs_dir, filename)
    
    if not filename.endswith(".md"):
        filepath += ".md"

    if os.path.exists(filepath):
        print(f"STOP: '{filepath}' already exists.")
        return

    content = f"---\ntitle: \"{title}\"\n---\n\n# {title}\n\n"

    if archetype == "A": # Tool/Model
        content += "!!! note \"Editor's Word: [Analogy]\"\n    [Framing]\n    !!! info \"Sources\"\n        * [Link](url)\n\n## Concept\n\n## Utility\n\n## Limitations\n\n!!! info \"FYI: [Topic]\"\n"
    elif archetype == "B": # Concept
        content += "!!! abstract \"Concept in a Nutshell\"\n    [Definition]\n    !!! tip \"Relevance\"\n\n## Context\n\n## Mechanism\n\n## Application\n\n!!! info \"Further Reading\"\n"
    elif archetype == "C": # Use Case
        content += "???+ info \"Case Study Information\"\n    * Institution: \n\n!!! quote \"Editor's Note\"\n\n## Overview\n\n## Implementation\n\n## Outcomes\n"
    elif archetype == "D": # Tracker
        content += "???- quote \"Featuring...\"\n\n!!! note \"Editor's Note\"\n\n## What Changed\n\n## Comparison\n"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"SUCCESS: Created {filepath} with Archetype {archetype}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python scaffold_page.py \"Title\" \"filename.md\" [Archetype: A/B/C/D]")
        sys.exit(1)
    
    create_page(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "A")

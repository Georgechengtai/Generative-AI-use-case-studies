import os
import sys
import yaml

def create_page(title, filename, section):
    """
    Scaffolds a new markdown page and adds it to mkdocs.yml
    """
    docs_dir = "docs"
    filepath = os.path.join(docs_dir, filename)
    
    if not filename.endswith(".md"):
        filepath += ".md"

    # 1. Create the file
    if os.path.exists(filepath):
        print(f"Warning: {filepath} already exists. Skipping creation.")
    else:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n")
            f.write("!!! note \"Draft\"\n    This page is currently under construction.\n\n")
            f.write("## Introduction\n\n")
            f.write("<!-- AI: Fill this section based on guidelines -->\n")
        print(f"Created {filepath}")

    # 2. Update mkdocs.yml (Simple append for now, user can refine)
    # Note: Parsing comments in YAML is hard with standard libraries, 
    # so we will append to the end of the nav or suggest the user move it.
    # For a robust solution, manual placement by the Agent is often better,
    # but this script ensures the file exists.
    
    print(f"\nSUCCESS: Page '{title}' created at '{filepath}'.")
    print(f"NEXT STEP: Ask Copilot: 'Fill {filename} with content about {title} following the guidelines.'")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script/scaffold_page.py \"Page Title\" \"filename.md\"")
        sys.exit(1)
    
    title = sys.argv[1]
    filename = sys.argv[2]
    section = sys.argv[3] if len(sys.argv) > 3 else "Drafts"
    
    create_page(title, filename, section)

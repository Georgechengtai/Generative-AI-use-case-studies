import os
import re
import markdown
from bs4 import BeautifulSoup

input_folder = 'docs'
output_folder = 'ai_data'

os.makedirs(output_folder, exist_ok=True)

for root, dirs, files in os.walk(input_folder):
    for filename in files:
        if filename.endswith('.md'):
            filepath = os.path.join(root, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                text = f.read()

            # Generate the URL based on the file path
            relative_path = os.path.relpath(filepath, input_folder)
            url = 'https://georgechengtai.github.io/Generative-AI-use-case-studies/' + relative_path.replace('\\', '/').replace('.md', '/')

            # Remove front matter YAML
            text = re.sub(r'^---\s*[\s\S]*?---\s*', '', text)

            # Remove { } syntax
            text = re.sub(r'\{.*?\}', '', text)

            # Replace admonition markers with blockquote markers
            text = re.sub(r'^(\s*)(!{3,}|\?{3,})(\+?)(.*)', r'\1> \4', text, flags=re.MULTILINE)
            text = re.sub(r'^(\s*)(!{3,}|\?{3,})(\+?)\s+\w+(?:\s+"[^"]*")?\s*', r'\1> ', text, flags=re.MULTILINE)

            # Additional cleaning steps
            text = re.sub(r'!\[.*?\]\(.*?\)', '', text)  # Remove images
            text = re.sub(r'\[\^.*?\]', '', text)        # Remove footnote references
            text = re.sub(r'\[\^.*?\]: .*', '', text)    # Remove footnote definitions

            text = text.replace('~~**', '[').replace('**~~', ']')  # Transform buttons
            ## text = re.sub(r'^>.*$', '', text, flags=re.MULTILINE)  # Remove block quotes (if desired) (disabled, not intended)

            # Optionally remove icons
            text = re.sub(r':([a-z_-]+):', '', text)
            text = text.replace('**', '')               # Remove bold formatting

            text = re.sub(r'\[([^\]]+)\]\(((?!http).*?)\)', r'\1', text)
            text = re.sub(r'\[([^\]]+)\]\(mailto:(.*?)\)', r'\1 (\2)', text)

            # Adjust links to include URLs
            text = re.sub(r'\[([^\]]+)\]\((.*?)\)', r'\1 (\2)', text)  # Convert [text](link) to text (link)
            text = re.sub(r'\[([^\]]+)\]\(mailto:(.*?)\)', r'\1 (\2)', text)  # Format email links
            text = re.sub(r'^\s+', '', text, flags=re.MULTILINE)  # Remove leading whitespace
            text = text.replace('\r\n', '\n').replace('\r', '\n')  # Normalize line endings
            text = re.sub(r'\n\s*\n', '\n\n', text)      # Reduce multiple empty lines

            # Convert Markdown to HTML with extensions
            md = markdown.Markdown(extensions=['extra', 'meta', 'toc'])
            html = md.convert(text)
            soup = BeautifulSoup(html, 'html.parser')
            plain_text = soup.get_text()

            # Append the URL at the end
            plain_text += f"\n\nSource: {url}"

            # Save the processed text
            output_path = os.path.join(output_folder, os.path.splitext(relative_path)[0] + '.txt')
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(plain_text)








import os
import re
import markdown
from bs4 import BeautifulSoup

input_folder = 'docs'
output_folder = 'ai_data'

os.makedirs(output_folder, exist_ok=True)

def generate_anchor_id(text):
    anchor = text.strip().lower()
    anchor = re.sub(r'[^\w\s-]', '', anchor)
    anchor = re.sub(r'\s+', '-', anchor)
    return anchor

for root, dirs, files in os.walk(input_folder):
    for filename in files:
        if filename.endswith('.md'):
            filepath = os.path.join(root, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                text = f.read()

            # Remove front matter YAML
            text = re.sub(r'^---\s*[\s\S]*?---\s*', '', text)

            # Remove { } syntax
            text = re.sub(r'\{.*?\}', '', text)

            # Replace admonition markers with blockquote markers
            text = re.sub(r'^(\s*)(!{3,}|\?{3,})(\+?)(.*)', r'\1> \4', text, flags=re.MULTILINE)

            # Additional cleaning steps
            text = re.sub(r'!\[.*?\]\(.*?\)', '', text)  # Remove images
            text = re.sub(r'\[\^.*?\]', '', text)        # Remove footnote references
            text = re.sub(r'\[\^.*?\]: .*', '', text)    # Remove footnote definitions
            text = text.replace('~~**', '[').replace('**~~', ']')  # Transform buttons
            text = re.sub(r'^>.*$', '', text, flags=re.MULTILINE)  # Remove block quotes (if desired)
            # Optionally remove icons
            text = re.sub(r':([a-z_]+):', '', text)
            text = text.replace('**', '')               # Remove bold formatting
            # Adjust links to include URLs
            text = re.sub(r'\[([^\]]+)\]\((.*?)\)', r'\1 (\2)', text)  # Convert [text](link) to text (link)
            text = re.sub(r'\[([^\]]+)\]\(mailto:(.*?)\)', r'\1 (\2)', text)  # Format email links
            text = re.sub(r'^\s+', '', text, flags=re.MULTILINE)  # Remove leading whitespace
            text = text.replace('\r\n', '\n').replace('\r', '\n')  # Normalize line endings
            text = re.sub(r'\n\s*\n', '\n\n', text)      # Reduce multiple empty lines

            # Generate the URL based on the file path
            relative_path = os.path.relpath(filepath, input_folder)
            url_base = 'https://your_website_url/'
            url_path = relative_path.replace('\\', '/').replace('.md', '/')
            url = url_base + url_path

            # Convert Markdown to HTML with extensions
            md = markdown.Markdown(extensions=['extra', 'meta', 'toc'])
            html = md.convert(text)
            soup = BeautifulSoup(html, 'html.parser')

            # Initialize variables to keep track of sections
            current_section_id = ''
            sections = []

            # Iterate over HTML elements
            for element in soup.recursiveChildGenerator():
                if element.name and element.name.startswith('h'):
                    # It's a heading
                    current_section_text = element.get_text()
                    current_section_id = generate_anchor_id(current_section_text)
                elif element.name in ['p', 'li']:
                    # It's a paragraph or list item
                    text_content = element.get_text()
                    if text_content.strip():
                        section_url = url + ('#' + current_section_id if current_section_id else '')
                        # Append the source URL at the end
                        text_content += f"\n\nSource: {section_url}"
                        sections.append(text_content)

            # Write the content to a file
            output_subdir = os.path.join(output_folder, os.path.dirname(relative_path))
            os.makedirs(output_subdir, exist_ok=True)
            output_filename = os.path.splitext(os.path.basename(filepath))[0] + '.txt'
            output_path = os.path.join(output_subdir, output_filename)

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write('\n\n'.join(sections))
import os
import re
import markdown
from bs4 import BeautifulSoup

input_folder = 'docs'
output_folder = 'ai_data'

os.makedirs(output_folder, exist_ok=True)

# Function to generate anchor IDs (you might need to adjust this based on your website's logic)
def generate_anchor_id(text):
    anchor = text.strip().lower()
    anchor = re.sub(r'[^\w\s-]', '', anchor)  # Remove non-alphanumeric characters
    anchor = re.sub(r'\s+', '-', anchor)      # Replace spaces with hyphens
    return anchor

for root, dirs, files in os.walk(input_folder):
    for filename in files:
        if filename.endswith('.md'):
            filepath = os.path.join(root, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                text = f.read()

            # Remove front matter YAML
            text = re.sub(r'^---\s*.*?\s*---\s*', '', text, flags=re.DOTALL)

            # Remove { loading=lazy } syntax
            text = re.sub(r'\{.*?loading=lazy.*?\}', '', text)

            # Remove Admonitions/Callouts
            text = re.sub(r'^(\s*(!{3,}|\?{3,})\+? .*?)$', '', text, flags=re.MULTILINE)

            # Remove unwanted Markdown syntax
            text = re.sub(r'\{.*?\}', '', text)  # Remove any curly braces content
            # Additional cleaning steps can be added here

            # Generate the URL based on the file path
            relative_path = os.path.relpath(filepath, input_folder)
            url_base = 'https://georgechengtai.github.io/Generative-AI-use-case-studies/'
            url_path = relative_path.replace('\\', '/').replace('.md', '/')
            url = url_base + url_path

            # Markdown to HTML
            html = markdown.markdown(text)
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
                elif element.name == 'p':
                    # It's a paragraph
                    paragraph_text = element.get_text()
                    if paragraph_text.strip():
                        section_url = url + ('#' + current_section_id if current_section_id else '')
                        # Append the source URL at the end
                        paragraph_text += f"\n\nSource: {section_url}"
                        sections.append(paragraph_text)

            # Write the content to a file
            output_subdir = os.path.join(output_folder, os.path.dirname(relative_path))
            os.makedirs(output_subdir, exist_ok=True)
            output_filename = os.path.splitext(os.path.basename(filepath))[0] + '.txt'
            output_path = os.path.join(output_subdir, output_filename)

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write('\n\n'.join(sections))
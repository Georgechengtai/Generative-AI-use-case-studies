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

            # Cleaning steps
            text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
            text = re.sub(r'\[\^.*?\]', '', text)
            text = re.sub(r'\[\^.*?\]:.*', '', text)
            text = text.replace('~~**', '[').replace('**~~', ']')
            text = re.sub(r'^>.*$', '', text, flags=re.MULTILINE)
            text = re.sub(r':[a-z_]+:', '', text)
            text = text.replace('**', '')
            text = re.sub(r'\[([^\]]+)\]\(((?!http).*?)\)', r'\1', text)
            text = re.sub(r'\[([^\]]+)\]\(mailto:(.*?)\)', r'\1 (\2)', text)
            text = re.sub(r'^\s+', '', text, flags=re.MULTILINE)
            text = text.replace('\r\n', '\n').replace('\r', '\n')
            text = re.sub(r'\n\s*\n', '\n\n', text)

            # Convert Markdown to Plain Text
            html = markdown.markdown(text)
            soup = BeautifulSoup(html, 'html.parser')
            plain_text = soup.get_text()

            # Append the URL at the end
            plain_text += f"\n\nSource: {url}"

            # Save the processed text
            output_path = os.path.join(output_folder, os.path.splitext(relative_path)[0] + '.txt')
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(plain_text)
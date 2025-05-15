import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load your documents from current directory
documents = []

print("Loading documents...")
# Loop through files in current directory
for filename in os.listdir('.'):  # '.' represents current directory
    if filename.endswith('.txt'):
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
            documents.append(text)

print(f"Loaded {len(documents)} documents.")

# Rest of your code remains the same
print("Splitting documents into chunks...")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs = []

for doc in documents:
    splits = text_splitter.split_text(doc)
    docs.extend(splits)

print(f"Total chunks created: {len(docs)}")

print("Generating embeddings...")
embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L12-v2')
vectorstore = FAISS.from_texts(docs, embeddings)

print("Saving vectorstore...")
vectorstore.save_local('faiss_index')
print("Vectorstore saved successfully.")
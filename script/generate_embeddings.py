import os
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS

# ModuleNotFoundError: Module langchain_community.embeddings not found. Please install langchain-community to access this module. You can install it using `pip install -U langchain-community`
# Why below code require langchain-community?

# Load your documents
docs_folder = 'ai_data'
documents = []

print("Loading documents...")
for root, dirs, files in os.walk(docs_folder):
    for filename in files:
        if filename.endswith('.txt'):
            filepath = os.path.join(root, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                text = f.read()
                documents.append(text)

print(f"Loaded {len(documents)} documents.")

# Split documents into chunks
print("Splitting documents into chunks...")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs = []

for doc in documents:
    splits = text_splitter.split_text(doc)
    docs.extend(splits)

print(f"Total chunks created: {len(docs)}")

# Embed and store the texts
print("Generating embeddings...")
embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L12-v2')
vectorstore = FAISS.from_texts(docs, embeddings)

# Save the vectorstore to disk
print("Saving vectorstore...")
vectorstore.save_local('faiss_index')
print("Vectorstore saved successfully.")
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain_huggingface import HuggingFacePipeline  # Updated import
from langchain_huggingface import HuggingFaceEmbeddings  # Updated import
from langchain_community.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
import gradio as gr

# [Model loading code remains the same]
# Load the Llama-3.2-3B-Instruct model
tokenizer = AutoTokenizer.from_pretrained('meta-llama/Llama-3.2-3B-Instruct')

model = AutoModelForCausalLM.from_pretrained(
    'meta-llama/Llama-3.2-3B-Instruct',
    device_map='auto',
    # load_in_8bit=True,
    low_cpu_mem_usage=True,
)

# Set up the text generation pipeline
pipe = pipeline(
    'text-generation',
    model=model,
    tokenizer=tokenizer,
    max_length=512,
    temperature=0.7,
    top_p=0.9,
    repetition_penalty=1.1,
)

llm = HuggingFacePipeline(pipeline=pipe)

# Load the vectorstore
embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L12-v2')
vectorstore = FAISS.load_local('faiss_index', embeddings, allow_dangerous_deserialization=True)  # Added parameter

# Rest of the code remains the same
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Modified prompt template to include context
prompt_template = """You are a helpful assistant that provides information based on the user's documentation.
Always include the source URL in your answers.

Context: {context}
Question: {question}

Answer:"""
QA_PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template=prompt_template
)

# Modified memory setup
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
    output_key='answer'
)

# Modified chain setup
qa = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vectorstore.as_retriever(),
    memory=memory,
    verbose=True,
    return_source_documents=True,
    combine_docs_chain_kwargs={'prompt': QA_PROMPT},
    chain_type="stuff"
)

# Modified chat function
def chat(user_input, history=[]):
    # Create a proper chat history format if needed
    formatted_history = [(h[0], h[1]) for h in history] if history else []
    
    # Get the response
    response = qa({
        "question": user_input,
        "chat_history": formatted_history
    })
    
    # Extract source documents if needed
    sources = [doc.metadata.get('source', 'No source') for doc in response.get('source_documents', [])]
    
    # Format the answer with sources
    answer = response['answer']
    if sources:
        answer += "\n\nSources:\n" + "\n".join(sources)
    
    history.append((user_input, answer))
    return history, history

# [Gradio interface code remains the same]

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    state = gr.State([])
    with gr.Row():
        txt = gr.Textbox(show_label=False, placeholder="Type your message here...")
        txt.submit(chat, [txt, state], [chatbot, state])

demo.launch(server_name="0.0.0.0", server_port=7860, share=True)

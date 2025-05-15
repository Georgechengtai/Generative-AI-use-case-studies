from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import login
login(token="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")

model_name = "meta-llama/Llama-3.2-3B-Instruct"  # An open access model

# Load the tokenizer
print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Load the model
print("Loading model...")
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map='auto',  # Should use 'cpu' since I am on a CPU-only machine
    torch_dtype='auto',  # Adjust dtype if needed
    # load_in_8bit=True,   # Reduces memory usage, update: but not supported without CUDA, i.e. GPU. I am using VM.Standard.E5.Flex
    low_cpu_mem_usage=True,  # Optimize memory usage
    trust_remote_code=True   # This may be required for some models
)

# Test the model
print("Generating text...")
prompt = "Hello, how are you?"
inputs = tokenizer(prompt, return_tensors='pt')
outputs = model.generate(**inputs, max_new_tokens=50)
print("Generated text:")
print(tokenizer.decode(outputs[0], skip_special_tokens=True))


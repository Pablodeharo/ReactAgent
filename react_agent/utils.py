from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
#from langchain import HuggingFacePipeline
from langchain_community.llms import HuggingFacePipeline

def load_local_chat_model(model_path: str):
    model = AutoModelForCausalLM.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=512)
    return HuggingFacePipeline(pipeline=pipe)
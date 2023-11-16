import os

import llama_cpp

from langchain.llms import LlamaCpp
from langchain.embeddings import LlamaCppEmbeddings, GPT4AllEmbeddings
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

from qualtop_llmapi.models.prompts import llama_stop, mistral_stop, deepseek_stop

def load_model(model_name, 
               temperature=0):
    
    ctx_tokens=4096
    if "codellama-13b" in model_name:
        max_tokens = 1024
        model_path = os.path.join(
                os.path.expanduser("~"),
                ".cache/gpt4all/codellama-13b-instruct.Q5_K_M.gguf")
        stop_conditions = llama_stop
    elif "deepseek" in model_name:
        max_tokens = 1024
        model_path = os.path.join(
                os.path.expanduser("~"),
                ".cache/gpt4all/deepseek-coder-6.7b-instruct.Q5_K_M.gguf")
        stop_conditions = deepseek_stop
    elif "llama-13b" in model_name: # Chat model
        max_tokens = 512
        model_path = os.path.join(
                os.path.expanduser("~"),
                ".cache/gpt4all/llama-2-13b-chat.Q5_K_M.gguf")
        stop_conditions = llama_stop
    elif "llama-7b" in model_name:
        # Test large context
        ctx_tokens *= 7
        max_tokens = 512
        model_path = os.path.join(
                os.path.expanduser("~"),
                ".cache/gpt4all/llama-2-7b-32k-instruct.Q5_K_M.gguf")
        stop_conditions = llama_stop
    else:
        max_tokens = 512
        model_path = os.path.join(
                os.path.expanduser("~"),
                ".cache/gpt4all/mistral-7b-instruct-v0.1.Q4_0.gguf")
        stop_conditions = mistral_stop
    
    if not os.path.exists(model_path):
        print(f"Couldn't find {model_name}, loading alternative model...")
        raise FileNotFoundError("Couldn't find model in filesystem.")
        
    ctx_tokens = ctx_tokens - max_tokens
    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
    
    if llama_cpp.GGML_USE_CUBLAS:
        # create model
        llm = LlamaCpp(
            model_path=model_path,
            n_gpu_layers=80,
            n_batch=1024,
            temperature=temperature,
            max_tokens=max_tokens,
            n_ctx=ctx_tokens,
            f16_kv=True,  # MUST set to True, otherwise you will run into problem after a couple of calls
            stop=stop_conditions,
            top_p=1,
            callback_manager=callback_manager,
            verbose=True,  # Verbose is required to pass to the callback manager
            )
    else:
        llm = LlamaCpp(
            model_path=model_path,
            temperature=temperature,
            max_tokens=max_tokens,
            n_ctx=ctx_tokens,
            stop=stop_conditions,
            top_p=1,
            f16_kv=True,  # MUST set to True, otherwise you will run into problem after a couple of calls
            callback_manager=callback_manager,
            verbose=True,  # Verbose is required to pass to the callback manager
            )
    return llm

def load_embedder(model_name):
    
    ctx_tokens=4096
    # Embed only with low-memory models
    if "llama-7b" in model_name:
        max_tokens = 512
        model_path = os.path.join(
                os.path.expanduser("~"),
                ".cache/gpt4all/llama-2-7b-32k-instruct.Q5_K_M.gguf")
    elif "mistral-7b" in model_name:
        max_tokens = 512
        model_path = os.path.join(
                os.path.expanduser("~"),
                ".cache/gpt4all/mistral-7b-instruct-v0.1.Q4_0.gguf")
    else:
        return GPT4AllEmbeddings()
    if not os.path.exists(model_path):
        print(f"Couldn't find {model_name}, loading alternative model...")
        max_tokens = 512
        model_path = os.path.join(
                os.path.expanduser("~"),
                ".cache/gpt4all/mistral-7b-instruct-v0.1.Q4_0.gguf")
    
    ctx_tokens = ctx_tokens - max_tokens
    # Load embedder in CPU (both model/embedder won't be able to
    # run on the T4)
    embedder = LlamaCppEmbeddings(
            model_path=model_path,
            n_ctx=ctx_tokens,
            f16_kv=True,  # MUST set to True, otherwise you will run into problem after a couple of calls
            )
    return embedder

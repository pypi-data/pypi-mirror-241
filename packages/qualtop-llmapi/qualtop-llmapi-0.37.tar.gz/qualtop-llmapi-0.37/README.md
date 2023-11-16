# Implementation of the OpenAI API for local LLM use

Implementation of the OpenAI API. Currently supports two end points (ChatCompletion and Embeddings) with the following models:

ChatCompletion models:

* 'mistral-7b': 7B Instruct model trained by MistralAI.
* 'llama-13b': 13B Llama 2 model trained by Meta.
* 'llama-7b': 7B Instruct Llama 2 model trained by Together AI (32K context).
* 'codellama-13b': 13B CodeLlama model trained by Meta.

Embeddings models:

* 'mistral-7b' : Encodes documents into 4096-dimension vectors.
* 'bert' : Encodes documents into 386-dimension vectors.

## Getting Started

Can be installed directly with pip (a `setup.py` file is provided, if needed).

Once installed, the FastAPI server (Uvicorn) can be started with:

```
run_server
```

### Prompts

Currently, two kinds of prompts are supported.

* Open ended questions to engage in conversation with the model.
* Instruct prompts for vector-based retrieval over some test collections.

### Some considerations

This project is by no means production ready. The ChatCompletion endpoint in particular has been tailored to communicate with the QOPA-LLM [demo](https://github.com/QOPA-LLM/qualtop_llm_frontend). A lot of work is needed security-wise to avoid data leaking.

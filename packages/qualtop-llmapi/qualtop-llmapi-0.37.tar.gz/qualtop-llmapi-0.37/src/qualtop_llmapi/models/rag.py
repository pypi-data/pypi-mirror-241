# -*- coding:utf-8 -*-
import os

import qualtop_llmapi
from qualtop_llmapi.models.loading import load_embedder
from qualtop_llmapi.models.chatgpt_embeddings import create_message_with_context, num_tokens
from qualtop_llmapi.models.prompts import generate_rag_llama_chat_prompt, generate_rag_mistral_instruct_prompt

from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
from langchain.vectorstores import Chroma
from langchain.embeddings import GPT4AllEmbeddings, LlamaCppEmbeddings


import llama_cpp

import chromadb

def ask(messages, llm, vecdb_id):
    home_dir = os.path.expanduser("~")
    
    if not qualtop_llmapi.embedder:
        # Load mistral embedder
        qualtop_llmapi.embedder = load_embedder("mistral-7b")
    
    embedding_fn = qualtop_llmapi.embedder

    if vecdb_id == "single":
        persistent_client = chromadb.PersistentClient(
                os.path.join(
                    home_dir,
                    ".cache/embeddings",
                    "data/gnp_single")
                )
        #collection = persistent_client.get_collection("context_collection")
        vecdb = Chroma(client=persistent_client,
                       collection_name="contextless_collection",
                       embedding_function=GPT4AllEmbeddings()
                       )
    elif vecdb_id == "collection":
        vecdb = Chroma(persist_directory=os.path.join(home_dir,
                                                      ".cache/embeddings",
                                                      "data/gnp"),
                       embedding_function=GPT4AllEmbeddings(),
                       )
    else:
        raise ValueError(f"Database {vecdb_id} not existent...")
   
    instruction = "Usa las siguientes piezas de contexto para responder la pregunta al final. Si no sabes la respuesta, responde 'No lo sé'."
    system_message = messages[0]['content']
    question = messages[-1]["content"]
    
    # Context
    documents = vecdb.similarity_search(question, k=10, score_threshold=0.5)
    if len(documents) == 0:
        return "No lo sé"
    
    # Fill 4k context
    # TODO: refine
    context = ""
    for i in range(0, len(documents)):
        doc = documents[i]
        total_tokens = num_tokens(context + doc.page_content + "\n", "gpt2")
        if total_tokens < 4096 - 1000:
            context += doc.page_content + "\n"
        else:
            break
    
    # Prompt
    if "mistral-7b" in qualtop_llmapi.selected_model:
        prompt = generate_rag_mistral_instruct_prompt(instruction,
                                                      question,
                                                      context)
    elif "llama" in qualtop_llmapi.selected_model:
        prompt = generate_rag_llama_chat_prompt(system_message,
                                                instruction,
                                                question,
                                                context)

    print(prompt)
    answer = llm(prompt).strip()

    # If answer is empty, ask again ONCE
    if answer == "" :
        context = ""
        for j in range(i, len(documents)):
            doc = documents[j]
            total_tokens = num_tokens(context + doc.page_content + "\n", "gpt2")
            if total_tokens < 4096 - 1000:
                context += doc.page_content + "\n"
            else:
                break
        # Prompt
        if qualtop_llmapi.selected_model == "mistral-7b":
            prompt = generate_rag_mistral_instruct_prompt(instruction,
                                                          question,
                                                          context)
        elif "llama" in qualtop_llmapi.selected_model:
            prompt = generate_rag_llama_chat_prompt(system_message,
                                                    instruction,
                                                    question,
                                                    context)
        print(prompt)
        answer = llm(prompt).strip()
        if answer == "" :
            answer = "No lo sé"

    return answer

def ask_manually(messages, llm, df):
    answer = ""
   
    prompt_template = "[INST]\n"
    prompt_template += "Usa las siguientes piezas de contexto para responder la pregunta del final. Si no sabes la respuesta, responde 'No lo sé'."
    prompt_template += "\n\n{context}\n\n"
    prompt_template += "Pregunta: {question}"
    prompt_template += "\n[\INST]"

    PROMPT = PromptTemplate(template=prompt_template,
                            input_variables=["context", "question"])
    
    prompt = create_message_with_context(
            messages[-1]['content'],
            df,
            "llama-7b",
            4096-500,
            PROMPT)
    answer = llm(prompt)
    return answer

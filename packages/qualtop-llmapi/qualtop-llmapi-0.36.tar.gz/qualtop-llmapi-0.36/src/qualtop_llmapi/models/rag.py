# -*- coding:utf-8 -*-
import os

import qualtop_llmapi
from qualtop_llmapi.models.loading import load_embedder
from qualtop_llmapi.models.chatgpt_embeddings import create_message_with_context

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
    
    # Prompt
    system_message = "You are a helpful assistant. You respond in Spanish."
    instruction = "Usa las siguientes piezas de contexto para responder la pregunta al final. Si no sabes la respuesta, responde 'No lo sé'."
    if qualtop_llmapi.selected_model == "mistral-7b":
        prompt_template = "<s>[INST] " + instruction + "\n\n{context}\n\n"
        prompt_template += "Pregunta: {question} [/INST]"
    elif "llama" in qualtop_llmapi.selected_embedder:
        prompt_template = "<<SYS>>\n" + system_message + "\n<</SYS>>"
        prompt_template += "\n\n[INST]" + instruction + "\n\n{context}\n\n"
        prompt_template += "Pregunta: {question} [/INST]"
    
    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    # Q&A chain
    # TODO: CHECK MODEL NAME TO DECIDE CONTEXT SIZE
    qa_chain = ConversationalRetrievalChain.from_llm(
            llm,
            retriever=vecdb.as_retriever(search_kwargs={'k': 2,
                                         'score_threshold':0.5}),
            return_source_documents=True,
            verbose=True,
            combine_docs_chain_kwargs={"prompt": PROMPT},
    )
    result = qa_chain({"question": messages[-1]['content'], 
                       "chat_history": ""})
    answer = result["answer"].strip()

    # If answer is empty, ask again ONCE
    if answer == "" :
        result = qa_chain({"question": messages[-1]['content'], 
                           "chat_history": ""})
        answer = result["answer"].strip()
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

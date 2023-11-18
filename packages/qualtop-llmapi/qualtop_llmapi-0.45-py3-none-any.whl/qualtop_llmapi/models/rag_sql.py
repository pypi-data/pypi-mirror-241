# -*- coding:utf-8 -*-
import os

import qualtop_llmapi
from qualtop_llmapi.models.loading import load_embedder
from qualtop_llmapi.models.chatgpt_embeddings import create_message_with_context, num_tokens
from qualtop_llmapi.models.prompts import generate_rag_llama_chat_prompt, generate_rag_mistral_instruct_prompt, gentera_employee_table
from qualtop_llmapi.models.prompts import llama_stop, mistral_stop 

from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
from langchain.vectorstores import Chroma
from langchain.embeddings import GPT4AllEmbeddings

from unidecode import unidecode

import llama_cpp

import chromadb

def ask(messages, llm):
    home_dir = os.path.expanduser("~")
    
    # Load vector store
    persistent_client = chromadb.PersistentClient(
            os.path.join(
                home_dir,
                ".cache/embeddings",
                "data/gentera")
            )
    
    vecdb = Chroma(client=persistent_client,
                   collection_name="employee_collection",
                   embedding_function=GPT4AllEmbeddings(),
                   )
    
    # Load information for prompt
    system_message = messages[0]['content']
    question = messages[-1]["content"]
   
    if "numero" in unidecode(question.lower()) or\
            "cuantos" in unidecode(question.lower()) or\
            "total" in unidecode(question.lower()):
        instruction = "La tabla 'gentera' en una base de datos tiene la información mostrada a continuación. Dame la consulta SQL que permita resolver la pregunta al final."
        context = gentera_employee_table
        # Prompt
        if "mistral-7b" in qualtop_llmapi.selected_model:
            prompt = generate_rag_mistral_instruct_prompt(instruction,
                                                          question,
                                                          context)
            stop_conditions = mistral_stop
        elif "llama" in qualtop_llmapi.selected_model:
            prompt = generate_rag_llama_chat_prompt(system_message,
                                                    instruction,
                                                    question,
                                                    context)
            stop_conditions = llama_stop

        print(prompt)
        answer = llm(prompt, stop=stop_conditions+temp_stop_conditions).strip()
        # TODO: Clean returned code and execute
        return answer
    else:
        instruction = 'Usa la información de empleados (colaboradores) siguiente para responder la pregunta. Si la respuesta no se encuentra en el texto, escribe "No lo sé."'
        # Context
        documents = vecdb.similarity_search(question, k=50, score_threshold=0.5)
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
        
        temp_stop_conditions=["Basándome en", "no se menciona", "no se especifica", "no menciona", "no especifíca"]
        # Prompt
        if "mistral-7b" in qualtop_llmapi.selected_model:
            prompt = generate_rag_mistral_instruct_prompt(instruction,
                                                          question,
                                                          context)
            stop_conditions = mistral_stop
        elif "llama" in qualtop_llmapi.selected_model:
            prompt = generate_rag_llama_chat_prompt(system_message,
                                                    instruction,
                                                    question,
                                                    context)
            stop_conditions = llama_stop

        print(prompt)
        answer = llm(prompt, stop=stop_conditions+temp_stop_conditions).strip()
    
    return answer

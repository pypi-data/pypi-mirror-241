# -*- coding:utf-8 -*-
import os

import qualtop_llmapi
from qualtop_llmapi.models.loading import load_embedder
from qualtop_llmapi.models.chatgpt_embeddings import create_message_with_context, num_tokens
from qualtop_llmapi.models.prompts import generate_rag_llama_chat_prompt, generate_rag_mistral_instruct_prompt, gnp_collection_context
from qualtop_llmapi.models.prompts import llama_stop, mistral_stop 

from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
from langchain.vectorstores import Chroma
from langchain.embeddings import GPT4AllEmbeddings

import llama_cpp

import chromadb

def ask(messages, llm, vecdb_id):
    home_dir = os.path.expanduser("~")
    
    persistent_client = chromadb.PersistentClient(
            os.path.join(
                home_dir,
                ".cache/embeddings",
                "data/gnp_collection")
            )

    if vecdb_id == "single":
        vecdb = Chroma(client=persistent_client,
                       collection_name="trasciende_collection",
                       embedding_function=GPT4AllEmbeddings()
                       )
    elif vecdb_id == "collection":
        instruction = "La base de datos de la aseguradora GNP tiene los siguientes Documentos. Usalos para responder la pregunta del final. Si no sabes la respuesta responde 'No lo sé.'"
        system_message = messages[0]['content']
        question = messages[-1]["content"]
        # Prompt
        temp_stop_conditions=["basándome en la información", "no se menciona", "no se especifica"]
        if "mistral-7b" in qualtop_llmapi.selected_model:
            prompt = generate_rag_mistral_instruct_prompt(instruction,
                                                          question,
                                                          gnp_collection_context)
            stop_conditions = mistral_stop
        elif "llama" in qualtop_llmapi.selected_model:
            prompt = generate_rag_llama_chat_prompt(system_message,
                                                    instruction,
                                                    question,
                                                    gnp_collection_context)
            stop_conditions = llama_stop
        print(prompt)
        answer = llm(prompt, stop=stop_conditions+temp_stop_conditions).strip()
        
        # If didn't find answer, then select a collection 
        if answer == "" or "No lo sé." == answer or \
                "basándome en la información" in answer.lower() or \
                "no se menciona" in answer.lower() or \
                "no se especifica" in answer.lower():
            if "dotal" in question.lower():
                collection_name = "dotal_collection"
            elif "platino" in question.lower():
                collection_name = "platino_collection"
            elif "privilegio" in question.lower():
                collection_name = "privilegio_collection"
            elif "profesional" in question.lower():
                collection_name = "profesional_collection"
            elif "trasciende" in question.lower():
                collection_name = "trasciende_collection"
            elif "vision" in question.lower():
                collection_name = "vision_collection"
            else:
                answer = "Lo siento, no lo sé."
                return answer


            vecdb = Chroma(client=persistent_client,
                           collection_name=collection_name,
                           embedding_function=GPT4AllEmbeddings(),
                           )
        else:
            # Did found an answer
            return answer

    else:
        raise ValueError(f"Database {vecdb_id} not existent...")
   
    instruction = "Usa los siguientes documentos para responder la pregunta del final. Si no sabes la respuesta, responde 'No lo sé'."
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
        stop_conditions = mistral_stop
    elif "llama" in qualtop_llmapi.selected_model:
        prompt = generate_rag_llama_chat_prompt(system_message,
                                                instruction,
                                                question,
                                                context)
        stop_conditions = llama_stop

    print(prompt)
    answer = llm(prompt, stop=stop_conditions).strip()

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
        answer = llm(prompt, stop=stop_conditions).strip()
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

import os

import qualtop_llmapi
from qualtop_llmapi.models.prompts import generate_llama_chat_prompt, generate_mistral_instruct_prompt
from qualtop_llmapi.models.prompts import llama_stop, mistral_stop

from langchain.schema.output_parser import StrOutputParser

from langchain.prompts import PromptTemplate

def ask(messages, llm):
    if "llama" in qualtop_llmapi.selected_model:
        stop_conditions = llama_stop
    else:
        stop_conditions = mistral_stop

    chain = messages | llm.bind(stop=stop_conditions) | StrOutputParser()
    output = chain.invoke(input="")
    #output = llm(messages.format())
    output = " ".join(output.split(":")[1:])
    return output.strip()

def ask_code(messages, llm):
    if "llama" in qualtop_llmapi.selected_model:
        stop_conditions = llama_stop
    else:
        stop_conditions = mistral_stop
    # Prompt
    system_message = "You are a helpful code assistant. You respond in Spanish."
    if qualtop_llmapi.selected_model == "mistral-7b":
        prompt_template = "<s>[INST] {question} [/INST]"
    elif "llama" in qualtop_llmapi.selected_model:
        prompt_template = "[INST] <<SYS>>\n"
        prompt_template += system_message
        prompt_template += "\n<</SYS>>\n\n"
        prompt_template += "[INST]{question}[/INST]"
    elif "deepseek" in qualtop_llmapi.selected_model:
        prompt_template = "You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer.\n"
        prompt_template += "### Instruction:\n"
        prompt_template += "{question}\n"
        prompt_template += "### Response:"

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["question"]
    )
    chain = PROMPT | llm.bind(stop=stop_conditions) | StrOutputParser()
    print(messages[-1]['content'])
    output = chain.invoke({'question' : messages[-1]['content']})
    return output.strip()

def ask_manual(messages, llm):

    if qualtop_llmapi.selected_model == "mistral-7b":
        prompt = generate_mistral_instruct_prompt(messages[1:])
        stop_conditions = mistral_stop
    elif "llama" in qualtop_llmapi.selected_model:
        prompt = generate_llama_chat_prompt(messages)
        stop_conditions = llama_stop
    print(prompt)
    output = llm(prompt, stop=llama_stop)
    return output.strip()

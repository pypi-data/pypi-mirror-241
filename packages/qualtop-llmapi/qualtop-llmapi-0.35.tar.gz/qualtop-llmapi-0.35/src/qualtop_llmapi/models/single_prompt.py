import os

import qualtop_llmapi

from langchain.schema.output_parser import StrOutputParser

from langchain.prompts import PromptTemplate

def ask(messages, llm):
    chain = messages | llm | StrOutputParser()
    output = chain.invoke(input="")
    #output = llm(messages.format())
    output = " ".join(output.split(":")[1:])
    return output.strip()

def ask_code(messages, llm):
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
    chain = PROMPT | llm | StrOutputParser()
    print(messages[-1]['content'])
    output = chain.invoke({'question' : messages[-1]['content']})
    return output.strip()

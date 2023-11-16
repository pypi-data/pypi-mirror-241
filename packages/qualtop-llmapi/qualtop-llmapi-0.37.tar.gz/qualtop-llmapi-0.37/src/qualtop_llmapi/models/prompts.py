from string import Template

llama_system = Template("<<SYS>>\n${system}\n<</SYS>>\n\n")
llama_inst = Template("[INST] ${prompt} [/INST]")
llama_inst_response = Template("[INST] ${prompt} [/INST] ${response}")
llama_system_inst = Template("[INST] ${system}${prompt} [/INST]")
llama_system_inst_response = Template("[INST] ${system}${prompt} [/INST] ${response}")
llama_chat_ex = "[INST] <<SYS>>\nYou are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature. If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.\n<</SYS>>\n{prompt}[/INST]"

llama_chat_history_ex = \
'''<s>[INST] <<SYS>>

You are are a helpful assistant

<</SYS>>



Hi there! [/INST] Hello! How can I help you today? </s><s>[INST] What is a neutron star? [/INST] A neutron star is a ... </s><s> [INST] Okay cool, thank you! [/INST] You're welcome! </s><s> [INST] Ah, I have one more question.. [/INST]'''

llama_stop = ["[INST]", 
              "[/INST]",
              "<<SYS>>",
              "<</SYS>>",
              "<s>",
              "</s>",
              "\n\n\n"]

mistral_inst = Template('''[INST] ${prompt} [/INST]''')
mistral_inst_response = Template('''[INST] ${prompt} [/INST] ${response}''')
mistral_stop = ["<s>",
                "</s>",
                "[INST]",
                "[/INST]",
                "\n\n\n"]

deepseek = "You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer.\n### Instruction:\n{prompt}\n### Response:"
deepseek_stop = ["### Instruction:",
                 "### Response:",
                 "\n\n\n"]

rag_template = Template("${instruction}\n\n${context}\n\nPregunta: ${question}")

def generate_llama_chat_prompt(message_list):
    # Message list
    # [{'role':'system', 'content':''}...]
    system_message = message_list.pop(0)
    assert system_message['role'] == 'system'
    assert len(message_list) >= 1
    assert len(message_list) % 2 != 0
    system_message_prompt = llama_system.substitute(system=system_message['content'])
    content_messages = []
    insert_system_message = True
    for i in range(0, len(message_list), 2):
        # First user, then ai
        try:
            user_message = message_list[i]
            ai_message = message_list[i+1]
            if insert_system_message:
               user_message_prompt = llama_system_inst_response.substitute(
                       system=system_message_prompt,
                       prompt=user_message['content'],
                       response=ai_message['content'])
               insert_system_message = False
            else:
                user_message_prompt = llama_inst_response.substitute(
                       prompt=user_message['content'],
                       response=ai_message['content'])
            content_messages.append(user_message_prompt)
        except:
            user_message = message_list[i]
            if insert_system_message:
                user_message_prompt = llama_system_inst.substitute(
                        system=system_message_prompt,
                        prompt=user_message['content'])
                insert_system_message = False
            else:
                user_message_prompt = llama_inst.substitute(prompt=user_message['content'])
            content_messages.append(user_message_prompt)
    
    final_prompt = ""
    for message in content_messages[:len(content_messages)-1]:
        final_prompt += "<s>"
        final_prompt += message
        final_prompt += " </s>"
   
    if len(content_messages) == 1:
        final_prompt += content_messages[-1]
    else:
        final_prompt += "<s>" + content_messages[-1]
    return final_prompt


def generate_mistral_instruct_prompt(message_list):
    # Message list
    # No system message
    assert message_list[0]['role'] != 'system'
    assert len(message_list) >= 1
    assert len(message_list) % 2 != 0
    content_messages = []
    for i in range(0, len(message_list), 2):
        # First user, then ai
        try:
            user_message = message_list[i]
            ai_message = message_list[i+1]
            user_message_prompt = mistral_inst_response.substitute(
                   prompt=user_message['content'],
                   response=ai_message['content'])
            content_messages.append(user_message_prompt)
        except:
            user_message = message_list[i]
            user_message_prompt = mistral_inst.substitute(prompt=user_message['content'])
            content_messages.append(user_message_prompt)
    
    final_prompt = ""
    for message in content_messages[:len(content_messages)-1]:
        final_prompt += "<s>"
        final_prompt += message
        final_prompt += " </s>"
   
    if len(content_messages) == 1:
        final_prompt += content_messages[-1]
    else:
        final_prompt += "<s>" + content_messages[-1]
    return final_prompt

def generate_rag_mistral_instruct_prompt(instruction,
                                         question, 
                                         context):
    prompt_content = rag_template.substitute(instruction=instruction,
                                             question=question,
                                             context=context)
    message = [{"role":"user", "content":prompt_content}]
    return generate_mistral_instruct_prompt(message)

def generate_rag_llama_chat_prompt(system_message,
                                         instruction,
                                         question, 
                                         context):
    prompt_content = rag_template.substitute(instruction=instruction,
                                             question=question,
                                             context=context)
    messages = [
            {"role" : "system", "content" : system_message},
            {"role" : "user", "content" : prompt_content}
            ]
    return generate_llama_chat_prompt(messages)

if __name__ == "__main__":
    messages = [{'role' :'system', 'content':'You are an assistant'},
                {'role' : 'user', 'content':'Hi'},
                {'role' : 'assistant', 'content':'Hello, how are you'},
                {'role' : 'user', 'content':'Fine, thanks, and you?'},
                {'role' : 'assistant', 'content':'Fine, how can I help you?'},
                {'role' : 'user', 'content':'Please, give me something.'},
            ]
    print("\n\nLlama 2\n\n")
    print("\n", messages[:2], "\n")
    print(generate_llama_chat_prompt(messages[:2]))
    print("\n", messages[:4], "\n")
    print(generate_llama_chat_prompt(messages[:4]))
    print("\n", messages[:6], "\n")
    print(generate_llama_chat_prompt(messages[:6]))
    
    print("\n\nMistral\n\n")
    print("\n", messages[1:2], "\n")
    print(generate_mistral_instruct_prompt(messages[1:2]))
    print("\n", messages[1:4], "\n")
    print(generate_mistral_instruct_prompt(messages[1:4]))
    print("\n", messages[1:6], "\n")
    print(generate_mistral_instruct_prompt(messages[1:6]))



llama = "<<SYS>>\n{system}\n<</SYS>>\n\n[INST]{prompt}[/INST]"
llama_chat = "[INST] <<SYS>>\nYou are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature. If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.\n<</SYS>>\n{prompt}[/INST]"

llama_chat_ex = \
'''<s>[INST] <<SYS>>

You are are a helpful assistant

<</SYS>>



Hi there! [/INST] Hello! How can I help you today? </s><s>[INST] What is a neutron star? [/INST] A neutron star is a ... </s><s> [INST] Okay cool, thank you! [/INST] You're welcome! </s><s> [INST] Ah, I have one more question.. [/INST]'''

llama_stop = ["[INST]", 
              "[/INST]",
              "<<SYS>>",
              "<</SYS>>",
              "\n\n\n"]

mistral = '''<s>[INST] {prompt} [/INST]'''
mistral_stop = ["<s>",
                "</s>",
                "[INST]",
                "[/INST]",
                "\n\n\n"]

deepseek = "You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer.\n### Instruction:\n{prompt}\n### Response:"
deepseek_stop = ["### Instruction:",
                 "### Response:",
                 "\n\n\n"]

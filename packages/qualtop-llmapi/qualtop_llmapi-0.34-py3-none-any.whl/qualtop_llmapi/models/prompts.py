

llama = "<<SYS>>\n{system}\n<</SYS>>\n\n[INST]{prompt}[/INST]"
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

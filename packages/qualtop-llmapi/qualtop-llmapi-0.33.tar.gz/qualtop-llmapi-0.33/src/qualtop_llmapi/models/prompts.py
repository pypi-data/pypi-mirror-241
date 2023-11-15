

llama = "<<SYS>>\n{system}\n<</SYS>>\n\n[INST]{prompt}[/INST]"
llama_stop = ["[INST]", 
              "[/INST]",
              "<<SYS>>",
              "<</SYS>>"]

mistral = '''<s>[INST] {prompt} [/INST]'''
mistral_stop = ["<s>",
                "</s>",
                "[INST]",
                "[/INST]"]

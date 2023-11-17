import openai

def mistral():
    openai.api_base = "http://localhost:8070/v1"
    openai.api_key = ""
    temperature = 0
    max_tokens = 500
    request_timeout=60
    messages = [
        {"role": "system", "content": "Eres un asistente inteligente."},
        {"role": "user", "content": "Cual es el significado de la vida?"}
        ]
    response = openai.ChatCompletion.create(
                model="mistral-7b",
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                request_timeout=request_timeout
            )
    print(response["choices"][0]["message"]["content"])

def llama():
    openai.api_base = "http://localhost:8070/v1"
    openai.api_key = ""
    temperature = 0
    max_tokens = 500
    request_timeout=60
    messages = [
        {"role": "system", "content": "Eres un asistente inteligente."},
        {"role": "user", "content": "Cómo funciona la IA Generativa?"}
        ]
    response = openai.ChatCompletion.create(
                model="llama-13b",
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                request_timeout=request_timeout
            )
    print(response["choices"][0]["message"]["content"])

def code():
    openai.api_base = "http://localhost:8070/v1"
    openai.api_key = ""
    temperature = 0
    max_tokens = 500
    request_timeout=60
    messages = [
        {"role": "system", "content": "Eres un asistente inteligente."},
        {"role": "user", "content": "Dame el código para resolver el problema de la cena de los filósofos."}
        ]
    response = openai.ChatCompletion.create(
                model="codellama-13b",
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                request_timeout=request_timeout
            )
    print(response["choices"][0]["message"]["content"])

if __name__ == "__main__":
    mistral()

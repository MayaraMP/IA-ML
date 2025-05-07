from gpt4all import GPT4ALL
from pathlib import Path

modelo = Path("models/mistral-7b-instruct-v0.1.q4_0.gguf").resolve()

llm = GPT4ALL(model_name=modelo.name, model_path=str(modelo.parent), allow_download=False)

prompt_base = (
    "Você é um assistente útil e educado. Sempre responda em alemão, de forma"
)
              
print("ChatBot em portugues iniciado! Digite sair para encerrar.\n")
while True:
    pergunta = input ("Você:")
    if pergunta.strip().lower() == "sair":
        print("Chat encerrado.")
        break
    
    prompt = f"{prompt_base}Usuário: {pergunta}\nBot:"
    resposta = llm.generate(prompt=prompt)
    print ("Bot:", resposta)

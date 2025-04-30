from deep_translator import GoogleTranslator

def chatbot():
    print("Olá! Sou um chatbot de tradução. Digite 'sair' para encerrar.")
    while True:
        texto = input("\nDigite o texto para traduzir:")
        if texto.lower() == "sair":
                print("Até logo!")
                break
        idioma_destino = input("Para qual idioma você quer traduzir (exemplo:en, es, fr, de):")
        try:
            traducao = GoogleTranslator(source="auto", targed=idioma_destino).translate(texto)
            print(f"Tradução: {traducao}")
        except Exception as e:
            print(f"Erro na tradução: {e}")
chatbot()

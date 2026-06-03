from src.engine import MissionEngine
from src.ui import mostrar_boas_vindas, mostrar_resposta

engine = MissionEngine()

mostrar_boas_vindas()

while True:

    pergunta = input("\nDigite sua pergunta (ou sair): ")

    if pergunta.lower() == "sair":
        break

    resposta = engine.analyze(pergunta)

    mostrar_resposta(resposta)

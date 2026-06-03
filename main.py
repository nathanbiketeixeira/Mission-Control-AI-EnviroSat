from src.engine import MissionEngine

engine = MissionEngine()

print("MISSION CONTROL AI - ENVIROSAT")

while True:

    pergunta = input("\nDigite uma pergunta: ")

    if pergunta.lower() == "sair":
        break

    print(engine.analyze(pergunta))

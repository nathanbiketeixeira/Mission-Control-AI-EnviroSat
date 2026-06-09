from pathlib import Path
from ollama import chat
from src.telemetria import coletar
from src.alertas import avaliar


class MissionEngine:

    def __init__(self):
        self.system_prompt = Path(
            "prompts/system_prompt.md"
        ).read_text(
            encoding="utf-8"
        )

    def is_ready(self):
        return True

    def status_snapshot(self):

        dados = coletar()

        return f"""
 STATUS ATUAL DA MISSÃO ENVIROSAT

Temperatura: {dados['temperatura']}°C
Energia: {dados['energia']}%
Precisão GPS: {dados['geolocalizacao']}%
Buffer: {dados['buffer_imagens']}%
Sensor Óptico: {dados['sensor_optico']}
"""

    def analyze(self, pergunta_usuario):

        dados = coletar()

        alertas = avaliar(dados)

        prompt_dinamico = f"""
Pergunta do operador:

{pergunta_usuario}

Dados atuais da missão:

Temperatura: {dados['temperatura']}°C
Energia: {dados['energia']}%
Precisão GPS: {dados['geolocalizacao']}%
Buffer: {dados['buffer_imagens']}%
Sensor Óptico: {dados['sensor_optico']}

Alertas:

{chr(10).join(alertas) if alertas else "Nenhum alerta encontrado."}
"""

        try:

            resposta = chat(
                model="llama3.2",
                messages=[
                    {
                        "role": "system",
                        "content": self.system_prompt
                    },
                    {
                        "role": "user",
                        "content": prompt_dinamico
                    }
                ]
            )

            return resposta["message"]["content"]

        except Exception as erro:

            return f"""
⚠️ ERRO AO ACESSAR A IA

{erro}

Prompt que seria enviado:

{prompt_dinamico}
"""

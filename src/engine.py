from src.telemetria import coletar
from src.alertas import avaliar

class MissionEngine:

    def __init__(self):
        pass

    def is_ready(self):
        return True

    def status_snapshot(self):

        dados = coletar()

        return f"""
Temperatura: {dados['temperatura']}°C
Energia: {dados['energia']}%
Precisão GPS: {dados['geolocalizacao']}%
Buffer: {dados['buffer_imagens']}%
Sensor Óptico: {dados['sensor_optico']}
"""

    def analyze(self, pergunta_usuario):

        dados = coletar()

        alertas = avaliar(dados)

        resposta = f"""
=== TELEMETRIA ===

Temperatura: {dados['temperatura']}°C
Energia: {dados['energia']}%
Precisão GPS: {dados['geolocalizacao']}%
Buffer: {dados['buffer_imagens']}%
Sensor Óptico: {dados['sensor_optico']}

=== ALERTAS ===

"""

        if alertas:

            for alerta in alertas:
                resposta += f"\n• {alerta}"

        else:
            resposta += "\nNenhum alerta encontrado."

        return resposta

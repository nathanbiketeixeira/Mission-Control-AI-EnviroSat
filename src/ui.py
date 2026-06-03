from rich.console import Console
from rich.panel import Panel

console = Console()

def mostrar_boas_vindas():
    console.print(
        Panel(
            "[bold cyan]MISSION CONTROL AI - ENVIROSAT[/bold cyan]\n\n"
            "Sistema de monitoramento ambiental por IA",
            title="Bem-vindo"
        )
    )

def mostrar_resposta(texto):
    console.print(
        Panel(
            texto,
            title="Análise da Missão"
        )
    )

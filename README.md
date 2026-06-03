# Mission-Control-AI-EnviroSat

## Integrante

* Nathan de Mello Teixeira — RM567429
* Victor Puglia Neves RM567854

---

# Sobre o Projeto

O EnviroSat é um sistema inteligente de monitoramento ambiental inspirado em satélites de observação terrestre como Amazônia-1 e Landsat.

A plataforma coleta dados simulados de telemetria, identifica situações críticas através de regras implementadas em Python e utiliza Inteligência Artificial Generativa para transformar informações técnicas em análises compreensíveis para operadores ambientais.

---

# Persona Atendida

Operador de Centro de Controle Ambiental.

Esse profissional acompanha queimadas, desmatamento e áreas protegidas utilizando informações provenientes de satélites de observação da Terra.

---

# Dados Monitorados

* Temperatura do sensor térmico
* Energia disponível
* Precisão de geolocalização
* Buffer de imagens não transmitidas
* Integridade do sensor óptico

---

# Tecnologias Utilizadas

* Python 3.10+
* Ollama Cloud
* GPT-OSS 120B
* Python-dotenv
* Rich
* PyFiglet

---

# Como Executar

1. Clone o repositório

```bash
git clone https://github.com/seuusuario/mission-control-ai.git
```

2. Crie o ambiente virtual

```bash
python -m venv .venv
```

3. Ative o ambiente

```bash
source .venv/bin/activate
```

4. Instale dependências

```bash
pip install -r requirements.txt
```

5. Configure o arquivo .env

```env
OLLAMA_API_KEY=sua_chave
```

6. Execute

```bash
python main.py
```

---

# Cenários Testados

## Cenário 1

Operação Normal

Todos os sensores funcionando.

## Cenário 2

Temperatura Crítica

Sensor térmico acima do limite operacional.

## Cenário 3

Energia Crítica

Bateria abaixo de 20%.

## Cenário 4

Falha de Geolocalização

Erro na precisão de posicionamento.

---

# Proposta de Valor

## Qual problema resolve?

Permite detectar queimadas e desmatamentos com maior rapidez.

## Quem paga?

Órgãos ambientais, governos estaduais, IBAMA e empresas privadas de monitoramento ambiental.

## Métrica de Impacto

Monitoramento de até 500 mil hectares por ano, reduzindo o tempo de resposta a focos de incêndio.

## Modelo de Negócio

Data as a Service (DaaS) por assinatura.

---

# Limitações

* Dados simulados
* Não utiliza sensores reais
* Dependência de conexão com internet para uso da IA

---

# Vídeo de Demonstração

Inserir link do YouTube após gravação.

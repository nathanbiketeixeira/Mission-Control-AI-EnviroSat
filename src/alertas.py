def avaliar(dados):

    alertas = []

    if dados["temperatura"] > 70:
        alertas.append(
            "ALERTA CRÍTICO: Temperatura elevada."
        )

    if dados["energia"] < 20:
        alertas.append(
            "ALERTA CRÍTICO: Energia abaixo de 20%."
        )

    if dados["geolocalizacao"] < 70:
        alertas.append(
            "ALERTA: Precisão de geolocalização comprometida."
        )

    if dados["buffer_imagens"] > 80:
        alertas.append(
            "ALERTA: Buffer de imagens próximo do limite."
        )

    return alertas

import random

def coletar():

    return {
        "temperatura": round(random.uniform(20, 90), 2),
        "energia": round(random.uniform(10, 100), 2),
        "geolocalizacao": round(random.uniform(50, 100), 2),
        "buffer_imagens": random.randint(0, 100),
        "sensor_optico": random.choice(
            ["OK", "ATENÇÃO", "CRÍTICO"]
        )
    }

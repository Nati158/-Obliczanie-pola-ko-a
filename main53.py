import math

def oblicz_pole_kola(promien):
    pole = math.pi * promien ** 2
    return pole

promien = 5
pole_kola = oblicz_pole_kola(promien)
print("Pole koła o promieniu", promien, "to:", pole_kola)

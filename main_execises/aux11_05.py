import random


def celsius_para_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


celsius = random.randrange(11, 18)
fahrenheit = celsius_para_fahrenheit(celsius)
print(f"{celsius}ºC é igual a {fahrenheit}ºF.")


def intervalo_aleatorio():
    max = random.randrange(-10, 35)
    min = random.randrange(-10, max)
    return {"min": min, "max": max}


def imprimir_intervalo():
    intervalo = intervalo_aleatorio()
    print(f"""
          As temperaturas para hoje são: 
            {intervalo["min"]} - {intervalo["max"]}ºC
            {celsius_para_fahrenheit(intervalo["min"])} - {celsius_para_fahrenheit(intervalo["max"])}ºF
          """)

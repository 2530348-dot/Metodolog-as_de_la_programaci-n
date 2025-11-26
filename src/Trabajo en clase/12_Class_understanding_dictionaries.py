# Diccionarios básicos
homer_0 = {
    "color": "yellow",
    "bag": "homer-donut",
    "hair": "black",
    "dress": "casual",
}
print(homer_0)
print(type(homer_0))

marge_0 = {
    "color": "yellow",
    "bag": "green-purse",
    "hair": "blue",
    "dress": "casual",
}

scar_0 = {
    "color": "yellow",
    "headshot": 1.5,
}

print(marge_0["bag"])
print(marge_0["color"])

# Agregar elementos a un diccionario
homer_0["x-position"] = 15
homer_0["y-position"] = 20
homer_0["z-position"] = 10
print(homer_0)

# Diccionario correcto (antes lo tenías como lista)
alien_2 = {
    "color": "blue"
}
alien_2["x-position"] = 0
alien_2["y-position"] = 25
print(alien_2)

# Iterar claves y valores
for key, value in alien_2.items():
    print(f"The key '{key}' has value '{value}'")

# Iterar solo claves
for key in alien_2.keys():
    print(key)

# Iterar items completos
for item in alien_2.items():
    print(item)

# Listas de diccionarios
convenants = [
    {"type": "covenant_grunt"},
    {"type": "covenant_elite"},
    {"type": "covenant_jackal"},
]

for enemy in convenants:
    print("\n", enemy)

# Diccionarios dentro de diccionarios
sensor = {
    "temperature": {
        "id": "temp_1",
        "location": "aula 105",
        "value": 25,
        "unit": "°C"
    },
    "humidity": {
        "id": "hum_1",
        "location": "aula 105",
        "value": 39,
        "unit": "%"
    }
}

selected = input("Escribe 'temperature' o 'humidity': ")
print(sensor.get(selected, "Sensor no encontrado"))

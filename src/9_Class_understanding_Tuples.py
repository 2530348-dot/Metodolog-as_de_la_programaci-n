"""
Las tuplas son elementos que no cambian de tamaño.
Las tuplas son INMUTABLES.

Se utilizan los paréntesis () para definir una tupla.
"""

Rectangle_measurements = (200, 50)  # (largo, ancho)

print(Rectangle_measurements[0])
print(Rectangle_measurements[1])

for measure in Rectangle_measurements:
    print(measure)

print(dir(Rectangle_measurements))

# Regresando un poco a listas
cars = ["bwm", "toyotara", "masda"]
print(cars)

cars[0] = "BMW"
cars[1] = "TOYOTA"
cars[2] = "MAZDA"
print(cars)

# No podemos modificar una tupla directamente, pero sí podemos cambiar
# la asignación de la variable que almacena una tupla.

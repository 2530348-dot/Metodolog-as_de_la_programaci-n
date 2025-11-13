"""
Las tuplas son elementos que no cambian de tamamño
Las tuplas son INMUTABLES.

Se utiliza los () parentesis para definir una tupla 

"""
Rectangle_measurements = (200,50) # (largo , ancho)
print(Rectangle[0])
print(Rectangle[1])

for measure in Rectangle_measurements:
print(dir(Rectangle_measurements))


#Regresando un poco a listas

cars=["bwm","toyotara","masda"]
print(cars)
cars[0]="BMW"
cars[1]="TOYOTA"
cars[2]="MAZDA"
print(cars)

# No podemos modificar una tupla directamente, lo que si podemos hacer es cambiar la asignacion de una variable que almacena una tupla

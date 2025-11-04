# List
"""
    
    Las listas son elementos "MUTABLES"
    
    Las listas nos permiten almacenar informacion en algun lugar la cantidad que tengan
    ya sean pocos elementos o millones de elementos.

    Se recomienda nombrar una variable del tipo lista en plural.

    En python los corchetes [] definen una lista, los elementos van separados por comas.

"""

bicycles=["trek","canondale","redline","specialized","giant"]
print(bicycles)
print(bicycles[0].title())

# Los indices comienzan en 0 y terminan en n-1 donde n es el numero de espacios entre comas o variables independientes
print(bicycles[4].title())

# Accediendo al ultimo elemento

print(bicycles[-1].title())
print(bicycles[-2].title())
print(bicycles[-3].title())
print(bicycles[-4].title())
print(bicycles[-5].title())

"""

Métodos de las listas en Python

append(x) → Agrega un elemento al final de la lista.

insert(i, x) → Inserta un elemento en la posición indicada.

extend(iterable) → Agrega varios elementos al final (otra lista, tupla, etc.).

remove(x) → Elimina la primera aparición del elemento indicado.

pop([i]) → Elimina y devuelve el elemento en la posición dada (por defecto el último).

clear() → Elimina todos los elementos de la lista.

index(x) → Devuelve el índice del primer elemento igual a x.

count(x) → Devuelve cuántas veces aparece x en la lista.

sort() → Ordena los elementos de la lista (por defecto, de menor a mayor).

reverse() → Invierte el orden de los elementos en la lista.

copy() → Devuelve una copia superficial de la lista.

"""

# Utilizando valores de la lista

message="Mi primer bicicleta fue una " + bicycles [4].upper() + "."
print(message)

message_f = f"Mi primer bicicleta fue una {bicycles [4] .title()}."
print(message_f)

print(bicycles)

#Agregar elementos a una lista

print("\n")
print("Agregar elementos a una lista")
print(bicycles)

print("Metodo de las listas para agregar elementos a una lista")
bicycles.append("ducatti")
print(bicycles)
# List
"""
    Las listas son elementos "MUTABLES".

    Las listas nos permiten almacenar información en un solo lugar,
    sin importar la cantidad de elementos que tengan, ya sean pocos o millones.

    Se recomienda nombrar una variable del tipo lista en plural.

    En Python los corchetes [] definen una lista, y los elementos van separados por comas.
"""

# Creación de una lista
bicycles = ["trek", "canondale", "redline", "specialized", "giant"]
print(bicycles)
print(bicycles[0].title())

# Los índices comienzan en 0 y terminan en n-1 donde n es el número de elementos.
print(bicycles[4].title())

# Accediendo al último elemento
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
message = "Mi primer bicicleta fue una " + bicycles[4].upper() + "."
print(message)

message_f = f"Mi primer bicicleta fue una {bicycles[4].title()}."
print(message_f)

print(bicycles)

# Agregar elementos a una lista
print("\n")
print("Agregar elementos a una lista")
print(bicycles)

print("Método .append() para agregar elementos a una lista")
bicycles.append("ducatti")
print(bicycles)

"""
   Agrega elementos al final de una lista.
   El método append agrega un elemento a la lista.
"""

print("\n ---Método .append()---")
motorcycles = ["honda", "yamaha", "susuki"]
print(motorcycles)  # Salida: ["honda", "yamaha", "susuki"]
motorcycles.append("ducatti")
print(motorcycles)  # Salida: ["honda", "yamaha", "susuki", "ducatti"]

"""
   Agregar elementos en una lista en un punto determinado.
"""
print("\n ---Método .insert()---")
print(motorcycles)
motorcycles.insert(0, "bmw")
print(motorcycles)

"""
   Eliminar elementos con la instrucción del.
   La instrucción del elimina un elemento por su índice.
"""
print("\n ---Instrucción del---")
del motorcycles[0]
print(motorcycles)

"""
   Método de lista .pop()
   Elimina y devuelve un elemento según su posición.
"""
print("\n ---Método .pop()---")
last_motorcycle = motorcycles.pop(1)
print(motorcycles)
print(f"La motocicleta eliminada con pop fue: {last_motorcycle}")

"""
   Método de lista .remove()
   Elimina la primera aparición de un elemento indicado por su valor.
"""
print("\n ---Método .remove()---")
print("Lista antes de remove():", motorcycles)
motorcycles.remove("susuki")
print("Lista después de remove():", motorcycles)

"""
   Método .extend()
   Permite agregar múltiples elementos al final de la lista desde otra lista o iterable.
"""
print("\n ---Método .extend()---")
motorcycles.extend(["triumph", "aprilia"])
print(motorcycles)

"""
   Método .clear()
   Elimina todos los elementos de la lista.
"""
print("\n ---Método .clear()---")
temporal = ["uno", "dos", "tres"]
print("Antes de clear():", temporal)
temporal.clear()
print("Después de clear():", temporal)

"""
   Método .index()
   Devuelve el índice de la primera aparición de un valor.
"""
print("\n ---Método .index()---")
frutas = ["manzana", "pera", "uva", "pera"]
print(frutas)
posicion = frutas.index("pera")
print("La primera aparición de 'pera' está en la posición:", posicion)

"""
   Método .count()
   Devuelve cuántas veces aparece un valor en la lista.
"""
print("\n ---Método .count()---")
print("La palabra 'pera' aparece:", frutas.count("pera"), "veces.")

"""
   Método .sort()
   Ordena los elementos de la lista de menor a mayor (por defecto).
   Si se pasa reverse=True, los ordena de mayor a menor.
"""
print("\n ---Método .sort()---")
numeros = [5, 2, 9, 1, 7]
print("Antes de sort:", numeros)
numeros.sort()
print("Orden ascendente:", numeros)
numeros.sort(reverse=True)
print("Orden descendente:", numeros)

"""
   Método .reverse()
   Invierte el orden actual de los elementos de la lista.
"""
print("\n ---Método .reverse()---")
colores = ["rojo", "verde", "azul"]
print("Antes de reverse:", colores)
colores.reverse()
print("Después de reverse:", colores)

"""
   Método .copy()
   Devuelve una copia superficial de la lista.
"""
print("\n ---Método .copy()---")
original = ["A", "B", "C"]
copia = original.copy()
print("Original:", original)
print("Copia:", copia)
copia.append("D")
print("Después de modificar copia:")
print("Original:", original)
print("Copia:", copia)

"""
   Funciones comunes que se pueden usar con listas:
   len() → Devuelve el número de elementos.
   sum() → Devuelve la suma de los valores numéricos.
   min() → Devuelve el valor mínimo.
   max() → Devuelve el valor máximo.
"""
print("\n ---Funciones comunes---")
nums = [10, 20, 5, 40]
print("Lista:", nums)
print("Cantidad de elementos:", len(nums))
print("Suma total:", sum(nums))
print("Valor mínimo:", min(nums))
print("Valor máximo:", max(nums))

"""
   Ejemplo combinado de métodos de lista.
"""
print("\n ---Ejemplo combinado---")
autos = ["bmw", "audi", "toyota", "honda"]
print("Lista original:", autos)

autos.append("nissan")
autos.insert(1, "ford")
autos.remove("audi")
ultimo = autos.pop()
autos.sort()
autos.reverse()
print("Lista final:", autos)

print(f"El último auto eliminado fue: {ultimo}")
print(f"El último auto eliminado fue: {ultimo}")
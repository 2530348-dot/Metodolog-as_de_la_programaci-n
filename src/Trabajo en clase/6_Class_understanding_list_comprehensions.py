"""
   squeres=[]
   For value in range (0,11)
   squere = value**2
   squeres.append(squere)
   print(squeres)
"""

"""

Una list Comprehension combina el ciclo for
y la creaccion de nuevos elementos en una sola
linea y automaticamente agrega cada nuevo elemento
a la lista sin usar el metodo append.

"""

squeres=[value**2 for value in range (0,11)]
print(squeres)

pares = [n for n in range(1, 101) if n % 2 == 0]
print(pares)


inpares = [n for n in range(1, 101) if n % 2 == 1]
print(inpares)
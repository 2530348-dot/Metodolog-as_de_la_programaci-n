
 # Trabajando con listas
"""
Recorrer una lista sin importar la cantidad de elementos que tenga.
"""

magicans =  ["ron", "hermion", "harry", "hadrig", "cedrik"]
 
print(magicans[0], magicans[1], magicans[2])

for magican in magicans: 
    print(magican)
    print(magican.upper())
    print(f"{magican.title()} ese fue un gran hechizo")
    print(f"{magican.lower()} No podemos esperar al siguiente hechizo")

print("Gracias a todos, fue un gran espectaculo")

"""
Identacion:
    Python utiliza la identacion para determinar couando una linea de
    codigo esta conectada a la linea de codigo anterior,

    Basicamente, se utilizan 4 espacios en blanco para obligatnos a  
    escribir un codigo ordenado y legible.
"""
# No olvidemos identar nuestro codigo correctamente

alumnos = ["Andrik", "Medio", "Alexis"]
for alumno in alumnos:
    print(alumno)
print("I can't unit to see your next trick", {alumno.title()})

# Identacion inecesaria
message =  "Hello Python world!"
print(message)
# Esto causara un error de identacion
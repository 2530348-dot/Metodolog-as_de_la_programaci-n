try:
    age = int(input("Escribe tu edad: "))
except:
    age = -1
    print("tuviste un error, ingresaste un caracter no valido")

if age >= 100:
   print("Tines mas de un siglo de vida,Que haces programando???? vete a descansar")
elif age >= 18 and age < 100:
    print("Eres mayor de edad")
elif age >= 0 and age < 18:
    print("Eres menor de edad")
else:
    print("Tuviste un error de valor")

print("Hola Charly")

"""
   Hacer un programa que pregunte la edad de una
   persona y responda lo siguiente:
     -Si la edad es menor o igual a 4, entonces la entrada
    es gratuita
     -Si la edad es manor a 18, pero mayor que 4
     entonces la entrada cuesta $200
     -Si la entrada es mayor o igual que 18, entonces la 
     entrada cuesta $400

"""

age = 0

try:
    age = int(input("Escribe tu edad: "))
except:
    age = -1
    print("tuviste un error, ingresaste un caracter invalido")

if age >= 100:
   print("Tines mas de un siglo de vida,Que haces programando???? vete a descansar")
elif age >= 18 and age < 100:
    print("Tu entrada cuesta 400")
elif age > 4 and age < 18:
    print("tu entrada cuesta 200")
elif age >= 0 and age <= 4:
    print("Tu entrada es Gratuita")
else:
    print("Tuviste un error de valor")

print("Ohhh maaa goood!")

#Multiple If

guisos = ["desebrada","salsa verde","asado","pozole"]
if "asado" in guisos:
    print("Si hay asado")
else:
    print("No hay asado")
if "salsa verde" in guisos:
    print("Si hay salsa verde")
else:
    print("No hay salsa verde")
if "tamales" in guisos:
    print("Si hay salsa tamales")
else:
    print("No hay tamales")

# Utilizando varias listas

guisos_disponibles = ["salsa verde","mole","deshebrada",]
guisos_a_ordenar = ["deshebrada","caldo de iguana"]

print("Que guiso desea ordenar")
for guiso in guisos_a_ordenar:
    print(f"Deseo {guiso}")
    if guiso in guisos_disponibles:
        print (f"Si tenemos {guiso}")
else:
    print("no tenemos de ese guiso")
print("Realizado el pedido")

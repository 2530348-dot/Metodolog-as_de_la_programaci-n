"""
Un string es de manera sencilla una serie de caracteres. en python, todo lo que se encuentre dentro de las comillas simples ( ) o dobles (" ")sera considerado un string

ejemplo:
  "Esto es un string"
  'Esto tambien es un string'

  'le dije a un amigo que python es el lenguaje mas versatil'
  "es lenguaje phyton lleva el nombre python, no por la serpiente"




"""

name = "clase de programacion"
print (name)

# title 
print(name.title())

"""
Un metodo es una accion que python
puede realizar en un fragmento de datos
o sobre la variable.

    El punto . despues de una variable 
seguido del metodo title() dice que 
se tiene que ejecutar el metodo title()
de la variable name.

    Todos los metodos van seguidos del parentesis 
    por que en ocaciones neccesita informacion adicional
    para funcionar, la cual iria dentro de los parentesis.
    En esta ocacion, el metodo .title() no requiere informacion 
    adicional para funcionar.


"""
print ("metodo upper: ", name.upper())
print ("metodo upper: ", name.lower())

# Concatenacion de STRING

first_name = "charly"
last_name = "mercury"
full_name = first_name + "" + last_name

print(full_name)
print(full_name.title())

#Whitespaces
"""
Se refiere a cualquier caracter que no se imprime,
es decir, un espacio, tabuladores y saltos de linea
los Whitespaces se utilizan comunmente para organizar
las salidas de tal manera que sea mas amigable de leer
o ver para el usuario

Ejemplo:
+ Tabuladore: \t
+ Salto de linea: \n

"""

print("Whitespaces Tabuladores")
print("tabulador")
print("\tPython")
print("\t\tPython")

print("Whitespace Salto de linea")
print("lenguaje: Python\n\tC++\n\tJava_script\n")


#Eliminacion de espacios en blanco


Programing_lenguages = " Python" 
print(Programing_lenguages)
print(Programing_lenguages.rstrip())
print(Programing_lenguages.lstrip())
print(Programing_lenguages.rstrip())

#Error de sintaxis en Strings

message = "Una fortaleza de python es su comunidad"
print(message)
message = "Una fortaleza de python es su comunidad"
print(message)
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
    adicional para funcionar.


"""
print ("metodo upper: ", name.upper())
print ("metodo upper: ", name.lower())

# Concatenacion de STRING

first_name = "charly"
last_name = "mercury"
full_name = first_name + "" + last_name

print(full_name)
print(full_name.title())


"""
Docstring for Trabajo en clase.14_Class_understanding_While_loop_centinel

 Un programa que:
    -Cunte cuantos numeros ha ingresado el usuario
    -Relice la suma de estos numeros
    -Me diga cual es el minimo de los numeros ingresados
    -Me diga cual es el maximo de los numeros ingresados 
    -Me diga el promedio de los numeros ingresados 
    -

"""
counter = 0
sum_numbers = 0.0
minimum = None
maximum = None

while True:

    user_input = input("Ingresa un número (o Exit para salir): ")
    print("Escribe -Exit- para salir")

    if user_input == "Exit":
        break

    try:
        value = float(user_input)
    except ValueError:
        print("Caracter inválido: por favor ingresa un valor numérico")
        continue
    except KeyboardInterrupt:
        print("Salida manual")
        break

    counter += 1
    sum_numbers += value

    if minimum is None or value < minimum:
        minimum = value

    if maximum is None or value > maximum:
        maximum = value


print("Cantidad de valores ingresados: ",counter)
print("La suma de todos los valores: ",sum_numbers)
print("El numero de mayor valor: ",maximum)
print("El numero de menor valor: ",minimum)


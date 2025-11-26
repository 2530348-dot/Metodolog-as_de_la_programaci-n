# While
"""
    El while es un ciclo controlado/comando
    por condicion.

    La estructura basica de un while es:

        while conditional
            actions
"""
# While infinito
"""
    programa si el usuario escribe un numero
    entre 25 y 50, entonces estar dentro del rango
    y salirme del while.
    de otro modo pedirle otro numero.
"""
while True:
    try:
        number = int(input("Ingresa un numero")) 

        if 25 <=  number <= 50:
            print("Estas en el rango, lo hiciste bien")
            break
        else:
            print("Estas fuera del rango, intentalo otra vez")

    except ValueError:
        print("Se ha introducido una variable no valida")
    except KeyboardInterrupt:
        print("\nEl usuario salio del while por voluntad propia")
        break
print("Saliste del while =)")








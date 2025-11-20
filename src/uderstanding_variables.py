#Uso de variables
message = "This is a profesional proyect of python"
print(message)

# Cambiamos el valor de la misma variable
message = "Suker for pine"
print(message)

"""
 Traceback: Es un registro de donde el interprete tuvo problemas
 al intentar ejecutar su codigo.
 
 (ejemplo)
 Traceback (most recent call last)
   file "C:\Users\omega\python_projects\casa_domotica"
    print(mesage)

 NameError: name "mesage" is not defined. Did you mean: 'mesage

 NameError: Significa que olvidamos establecer el valor
"""

"""
 1.-Ejercicio:Almacena un mensaje en una variable e imprimelo.
 2.-Ejercicio:Almacena un mensaje en una variable e imprimelo. luego cambia el valor de esa variale y luego imprime el nuevo mensaje 
"""












def convertir_temperaturas(celsius):
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin

def estado_del_agua(celsius):
    if celsius <= 0:
        return "Sólido (hielo)"
    elif 0 < celsius < 100:
        return "Líquido (agua)"
    else:
        return "Gaseoso (vapor de agua)"

def main():
    celsius = float(input("Ingrese la temperatura en °C: "))
    fahrenheit, kelvin = convertir_temperaturas(celsius)
    estado = estado_del_agua(celsius)
    print(f"\nTemperatura en Celsius: {celsius:.2f} °C")
    print(f"Temperatura en Fahrenheit: {fahrenheit:.2f} °F")
    print(f"Temperatura en Kelvin: {kelvin:.2f} °K")
    print(f"Estado del agua: {estado}")

if __name__ == "__main__":
    main()

"""
Universidad Politécnica de Victoria
Materia: Metodología de la Programación
Grupo: IM-03
Alumno: David Emiliano Vázquez Enríquez
Matrícula: 2530348
Proyecto: Fibonacci series generator
Profesor: Carlos Antonio Tovar García
Fecha: 22/11/2025
"""

"""
Resumen Ejecutivo

El presente proyecto implementa un generador de la serie de Fibonacci en Python. 
El programa permite al usuario ingresar un número entero n y, mediante validación de 
entrada, genera los primeros n términos de la secuencia comenzando desde 0 y 1. 
Se destacan aspectos importantes de la programación estructurada, como el uso de 
bucles para la iteración, la verificación de datos de entrada y la correcta presentación 
de resultados en pantalla. Esta solución ilustra cómo una lógica clara y organizada 
facilita la reutilización del código y asegura la precisión de los resultados incluso 
para casos límite. Además, se enfatiza la importancia de manejar entradas inválidas 
para evitar errores durante la ejecución.
"""
"""
Diagram / Flow description:

1) Start
2) Prompt user for number of terms (n)
3) Validate n:
    - Must be integer
    - Must be >= 1
    - Optional: must be <= 50
   If invalid -> print "Error: invalid input" and exit
4) Initialize first two terms: a=0, b=1
5) Loop from 0 to n-1:
    - Append current term (a) to series
    - Update a, b = b, a+b
6) Print "Number of terms:" n
7) Print "Fibonacci series:" followed by terms
8) End
"""

"""
Problem: Fibonacci series generator
Description: Program that reads an integer n and prints the first n terms of the Fibonacci series starting at 0 and 1.

Inputs:
- n (int; number of terms to generate)

Outputs:
- "Number of terms:" n
- "Fibonacci series:" followed by the n terms separated by spaces

Validations:
- n must be an integer
- n >= 1
- n <= 50 (to avoid very large sequences)

Test cases:
1) Normal: n = 5 → expected series: 0 1 1 2 3
2) Border: n = 1 → expected series: 0
3) Error: n = 0 → expected message: "Error: invalid input"
"""

# Fibonacci series generator
try:
    n_input = input("Enter the number of terms: ")
    n = int(n_input)

    if n < 1 or n > 50:
        raise ValueError

    fibonacci_series = []
    a, b = 0, 1

    for _ in range(n):
        fibonacci_series.append(a)
        a, b = b, a + b

    print("Number of terms:", n)
    print("Fibonacci series:", " ".join(str(x) for x in fibonacci_series))

except ValueError:
    print("Error: invalid input")

"""
Conclusiones

El desarrollo de este programa permitió comprender la importancia de los bucles para generar 
series numéricas de manera eficiente y repetitiva, evitando cálculos manuales y garantizando 
precisión. La implementación de validaciones de entrada asegura que el programa sea robusto, 
previniendo errores cuando el usuario proporciona valores no válidos o fuera de rango. 
El manejo correcto de los casos especiales, como n = 1 o n = 2, garantiza la exactitud 
de la serie incluso con los valores más pequeños. La lógica desarrollada puede aplicarse 
en otros contextos donde se requieran cálculos secuenciales o generación de patrones numéricos. 
Asimismo, este proyecto enfatiza buenas prácticas de programación, como la documentación clara, 
la estructuración del código y la presentación ordenada de los resultados, contribuyendo a 
la profesionalización del desarrollo de software.
"""

"""
Referencias

[1] Python Software Foundation, “Python Documentation – Control Flow Tools,” [Online]. Available: https://docs.python.org/3/tutorial/controlflow.html
[2] Real Python, “Fibonacci Series in Python,” [Online]. Available: https://realpython.com/fibonacci-python/
[3] M. Lutz, Learning Python, 5th ed., O'Reilly Media, 2013.
[4] D. Beazley and B. K. Jones, Python Cookbook, 3rd ed., O’Reilly Media, 2013.
[5] A. Sweigart, Automate the Boring Stuff with Python, 2nd ed., No Starch Press, 2019.
"""

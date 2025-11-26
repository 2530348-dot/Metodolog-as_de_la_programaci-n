"""
Universidad Politécnica de Victoria
Materia: Metodología de la Programación
Grupo: IM-03
Alumno: David Emiliano Vázquez Enríquez
Matrícula: 2530348
Proyecto: Loop Handling in Python
Profesor: Carlos Antonio Tovar García
Fecha: 22/11/2025
"""
"""
RESUMEN EJECUTIVO

Este proyecto trata sobre el uso de los bucles for y while
en Python y cómo ayudan a repetir tareas sin escribir muchas
líneas de código. A través de varios ejercicios, se muestra
cómo usar los bucles para sumar números, crear tablas, calcular
promedios, validar contraseñas, hacer menús y generar patrones
con asteriscos. El trabajo permite comprender mejor cómo funcionan
las estructuras de repetición y cómo aplicarlas correctamente en 
distintos problemas básicos de programación.

"""

# 7.1 Problem 1: Sum of range with for
"""
Descripción:
Calcula la suma de todos los enteros desde 1 hasta n (incluyendo n). 
Además, calcula la suma únicamente de los números pares dentro del mismo rango usando un ciclo for.

Entries:
- n (int): upper limit of the range.

Outputs:
- "Sum 1..n:" <total_sum>
- "Even sum 1..n:" <even_sum>

Validations:
- n must be convertible to int.
- n >= 1; otherwise print "Error: invalid input".

Test cases:
1) n = 5 → Sum = 15, Even sum = 6
2) n = 1 → Sum = 1, Even sum = 0
3) n = 10 → Sum = 55, Even sum = 30
4) n = -2 → Error
5) n = "hola" → Error
"""

n_input = input("Enter n: ")

try:
    n = int(n_input)
    if n < 1:
        print("Error: invalid input")
    else:
        total_sum = 0
        even_sum = 0
        for i in range(1, n + 1):
            total_sum += i
            if i % 2 == 0:
                even_sum += i
        print("Sum 1..n:", total_sum)
        print("Even sum 1..n:", even_sum)
except:
    print("Error: invalid input")


# 7.2 Problem 2: Multiplication table with for
"""
Descripción:
Genera la tabla de multiplicar de un número base, desde 1 hasta m, usando un ciclo for.

Entries:
- base (int)
- m (int): table limit.

Outputs:
- One line per multiplication: "<base> x <i> = <result>"

Validations:
- base and m must be convertible to int.
- m >= 1; otherwise print "Error: invalid input".

Test cases:
1) base=5, m=4 → prints 4 lines
2) base=3, m=1 → prints "3 x 1 = 3"
3) base=9, m=10 → prints 10 lines
4) m=0 → Error
5) base="aaa" → Error
"""

base_input = input("Enter base: ")
m_input = input("Enter m: ")

try:
    base = int(base_input)
    m = int(m_input)
    if m < 1:
        print("Error: invalid input")
    else:
        for i in range(1, m + 1):
            print(f"{base} x {i} = {base * i}")
except:
    print("Error: invalid input")


# 7.3 Problem 3: Average with while and sentinel
"""
Descripción:
Lee números uno por uno hasta que el usuario ingrese el valor centinela (-1). 
Calcula el promedio y la cantidad de números ingresados. Si no se ingresa ningún valor válido, muestra error.

Entries:
- number (float) repeatedly
- sentinel = -1

Outputs:
- "Count:" <count>
- "Average:" <average>
- "Error: no data" if no valid input.

Validations:
- Each number must be convertible to float.
- Sentinel must not be included in calculations.

Test cases:
1) 3, 6, 9, -1 → Count=3, Avg=6
2) 10, -1 → Count=1, Avg=10
3) -1 → Error
4) abc → ignored
5) 2.5, 2.5, 2.5, -1 → Avg=2.5
"""

sentinel = -1
count = 0
total = 0.0

while True:
    value = input("Enter number (-1 to stop): ")
    try:
        num = float(value)
        if num == sentinel:
            break
        total += num
        count += 1
    except:
        print("Invalid number, ignored.")

if count == 0:
    print("Error: no data")
else:
    print("Count:", count)
    print("Average:", total / count)


# 7.4 Problem 4: Password attempts with while
"""
Descripción:
Sistema de verificación de contraseña con un número máximo de intentos. 
Si la contraseña ingresada es correcta antes de agotar los intentos, se muestra éxito. 
Si se agotan los intentos, se bloquea la cuenta.

Entries:
- user_password (string)

Outputs:
- "Login success" if correct
- "Account locked" if attempts exhausted

Validations:
- MAX_ATTEMPTS > 0
- Count attempts correctly

Test cases:
1) Correct on first try → success
2) Wrong, wrong, correct → success
3) Wrong all attempts → locked
4) Empty input → attempts consumed
5) Password with spaces → valid if matches
"""

CORRECT_PASSWORD = "admin123"
MAX_ATTEMPTS = 3
attempts = 0

while attempts < MAX_ATTEMPTS:
    pwd = input("Enter password: ")
    if pwd == CORRECT_PASSWORD:
        print("Login success")
        break
    else:
        attempts += 1

if attempts == MAX_ATTEMPTS:
    print("Account locked")


# 7.5 Problem 5: Simple menu with while
"""
Descripción:
Crea un menú interactivo que se repite hasta que el usuario elija 0 (salir). 
Incluye un contador que puede visualizarse o incrementarse.

Entries:
- option (int)

Outputs:
- "Hello!"
- "Counter:" <value>
- "Counter incremented"
- "Bye!"
- "Error: invalid option"

Validations:
- option must be convertible to int
- Only 0,1,2,3 valid

Test cases:
1) 1 → Hello!
2) 2 → shows counter
3) 3 → increments counter
4) 9 → error
5) Sequence 1,2,3,0 → all features
"""

counter = 0

while True:
    print("1) Show greeting")
    print("2) Show current counter value")
    print("3) Increment counter")
    print("0) Exit")

    opt = input("Select option: ")

    try:
        opt = int(opt)
    except:
        print("Error: invalid option")
        continue

    if opt == 0:
        print("Bye!")
        break
    elif opt == 1:
        print("Hello!")
    elif opt == 2:
        print("Counter:", counter)
    elif opt == 3:
        counter += 1
        print("Counter incremented")
    else:
        print("Error: invalid option")


# 7.6 Problem 6: Pattern printing with nested loops
"""
Descripción:
Imprime un patrón de asteriscos en forma de triángulo rectángulo usando ciclos for anidados.
Opcionalmente, puede imprimirse también un triángulo invertido.

Entries:
- n (int): number of rows for the pattern.

Outputs:
- Pattern printed line by line:
  *
  **
  ***
  ****

Validations:
- n must be convertible to int
- n >= 1

Test cases:
1) n=1 → "*"
2) n=3 → "*", "**", "***"
3) n=5 → prints 5 lines
4) n=0 → error
5) n="hola" → error
"""

n_input = input("Enter n: ")

try:
    n = int(n_input)
    if n < 1:
        print("Error: invalid input")
    else:
        for i in range(1, n + 1):
            print("*" * i)
except:
    print("Error: invalid input")


"""
#Conclusion
Este proyecto permitió entender mejor cómo funcionan los bucles for 
y while en Python. Gracias a los ejercicios, fue posible practicar 
tareas repetitivas, validación de datos y control del flujo del programa. 
También se reforzó la importancia de evitar errores como ciclos infinitos 
y de usar contadores y acumuladores cuando son necesarios. En general, 
el proyecto ayudó a mejorar las habilidades básicas de programación y a 
usar correctamente las estructuras de repetición.
"""
"""
REFERENCIAS

[1] M. Lutz, Learning Python, 5th ed. Sebastopol, CA, USA: O’Reilly Media, 2013.

[2] E. Matthes, Python Crash Course: A Hands-On, Project-Based Introduction to Programming,
2nd ed. San Francisco, CA, USA: No Starch Press, 2019.

[3] Python Software Foundation, "Python 3 Documentation". Disponible en:
https://docs.python.org/3/

[4] J. Zelle, Python Programming: An Introduction to Computer Science, 
3rd ed. Franklin, Beedle & Associates, 2016.

[5] D. Beazley and B. Jones, Python Cookbook, 3rd ed. Sebastopol, CA, USA:
O’Reilly Media, 2013.
"""

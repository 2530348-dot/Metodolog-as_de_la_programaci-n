"""
Universidad Politécnica de Victoria
Materia: Metodología de la Programación
Grupo: IM-03
Alumno: David Emiliano Vázquez Enríquez
Matrícula: 2530348
Proyecto: Python numeric, boolean and string handling
Profesor: Carlos Antonio Tovar García
Fecha: 22/11/2025
"""

"""
Este proyecto reúne siete programas en Python que trabajan con números, valores booleanos y cadenas de texto. 
En cada ejercicio utilicé validaciones básicas, condiciones, manejo sencillo de errores y formatos de salida 
para que los resultados fueran fáciles de interpretar.

En los programas practiqué el uso de enteros y flotantes en operaciones comunes, la modificación de textos 
con métodos de cadena y la aplicación de valores booleanos para tomar decisiones dentro del código. 
Estas técnicas se aplican en casos prácticos como conversiones, revisión de datos, comparaciones y 
organización de la información que introduce el usuario.

Además, reforcé habilidades clave de programación: planear algoritmos, documentar entradas y salidas, 
crear casos de prueba y prevenir fallos mediante validaciones simples. En conjunto, este trabajo me ayudó 
a comprender mejor cómo Python maneja datos, realiza cálculos y ejecuta decisiones lógicas en programas 
que funcionan correctamente.

"""


# Problem 1: Temperature Converter
"""
Descripción:
Convierte una temperatura dada en grados Celsius 
a su valor equivalente en grados Fahrenheit.

Inputs:
- temp_c: number

Outputs:
- Fahrenheit temperature

Validations:
- Input must be numeric.

Test cases:
1) 0 -> 32
2) 25 -> 77
3) "abc" -> Error
"""

def convertir_celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def es_numero(valor):
    return valor.replace(".", "", 1).isdigit() or \
           (valor.startswith("-") and valor[1:].replace(".", "", 1).isdigit())

def main():
    temp_c = input("Ingresa grados Celsius: ").strip()

    if es_numero(temp_c):
        c = float(temp_c)
        f = convertir_celsius_a_fahrenheit(c)
        print(f"Fahrenheit: {f}")
    else:
        print("Error: ingresa un número válido.")


# Problem 2: Extra Hours Salary Calculator
"""
Descripción:
Calcula el pago según las horas trabajadas y la tarifa por hora. 
Las horas extra (más de 40) se pagan a 1.5 veces la tarifa normal.

Inputs:
- hours: number
- rate: number

Outputs:
- Total salary

Validations:
- Both inputs must be numeric and positive.

Test cases:
1) hours=40, rate=10 -> 400
2) hours=45, rate=10 -> 475
3) hours="abc" -> Error
"""

def es_numero(valor):
    return valor.replace(".", "", 1).isdigit() or \
           (valor.startswith("-") and valor[1:].replace(".", "", 1).isdigit())

def calcular_pago(horas, tarifa):
    if horas > 40:
        return (40 * tarifa) + ((horas - 40) * (tarifa * 1.5))
    else:
        return horas * tarifa

def main():
    hours = input("Hours worked: ").strip()
    rate = input("Hourly rate: ").strip()

    if es_numero(hours) and es_numero(rate):
        h = float(hours)
        r = float(rate)

        if h < 0 or r < 0:
            print("Error")
        else:
            total = calcular_pago(h, r)
            print(total)
    else:
        print("Error")

main()



# Problem 3: Discount Evaluator
"""
Descripción:
Calcula el precio final aplicando un descuento dependiendo del monto. 
Si el monto es mayor o igual a 500, se aplica un descuento del 10%.

Inputs:
- amount: number

Outputs:
- Final price with discount

Validations:
- Amount must be numeric and >= 0.

Test cases:
1) 100 -> no discount
2) 600 -> 10% discount
3) "abc" -> Error
"""

def es_numero(valor):
    return valor.replace(".", "", 1).isdigit() or \
           (valor.startswith("-") and valor[1:].replace(".", "", 1).isdigit())

def calcular_precio_final(monto):
    if monto >= 500:
        return monto * 0.90
    return monto

def main():
    amount = input("Amount: ").strip()

    if es_numero(amount):
        a = float(amount)

        if a < 0:
            print("Error")
        else:
            final_price = calcular_precio_final(a)
            print(final_price)
    else:
        print("Error")

main()



# Problem 4: Integer Stats
"""
Descripción:
Lee tres números enteros y muestra el menor, el mayor y el promedio.

Inputs:
- n1, n2, n3: integers

Outputs:
- Minimum, maximum, average

Validations:
- All inputs must be integers.

Test cases:
1) 1, 5, 10 -> min=1, max=10, avg=5.33
2) -3, 0, 3 -> min=-3, max=3, avg=0
3) "a", 5, 9 -> Error
"""

def es_entero(valor):
    return valor.lstrip("-").isdigit()

def main():
    n1 = input("Enter integer 1: ").strip()
    n2 = input("Enter integer 2: ").strip()
    n3 = input("Enter integer 3: ").strip()

    if es_entero(n1) and es_entero(n2) and es_entero(n3):
        i1 = int(n1)
        i2 = int(n2)
        i3 = int(n3)

        mn = min(i1, i2, i3)
        mx = max(i1, i2, i3)
        avg = (i1 + i2 + i3) / 3

        print(mn, mx, avg)
    else:
        print("Error")

main()



# Problem 5: Loan Eligibility Checker
"""
Descripción:
Determina si una persona es elegible basándose en su edad y sus ingresos.

Inputs:
- age: number
- income: number

Outputs:
- eligible / not eligible

Validations:
- Age and income must be numeric and >= 0.

Test cases:
1) age=25, income=15000 -> eligible
2) age=17, income=20000 -> not eligible
3) "abc", 20000 -> Error
"""

def es_numero(valor):
    return valor.replace(".", "", 1).isdigit() or \
           (valor.startswith("-") and valor[1:].replace(".", "", 1).isdigit())

def main():
    age = input("Enter age: ").strip()
    income = input("Enter income: ").strip()

    if es_numero(age) and es_numero(income):
        ag = float(age)
        inc = float(income)

        if ag < 0 or inc < 0:
            print("Error")
        else:
            if ag >= 18 and inc >= 10000:
                print("eligible")
            else:
                print("not eligible")
    else:
        print("Error")

main()


# Problem 6: Product Label Formatter
"""
Descripción:
Crea una etiqueta de producto con exactamente 30 caracteres, 
combinando el nombre y el precio.


Inputs:
- product_name: string
- price_value: number/string

Outputs:
- 30-character label

Validations:
- Name must not be empty.
- Price must be numeric and positive.

Test cases:
1) "Apple", 10 -> label (30 chars)
2) long name -> trimmed
3) price="abc" -> Error
"""

def es_numero(valor):
    return valor.replace(".", "", 1).isdigit() or \
           (valor.startswith("-") and valor[1:].replace(".", "", 1).isdigit())

def main():
    product_name = input("Enter product name: ").strip()
    price_value = input("Enter price: ").strip()

    if product_name == "" or price_value == "":
        print("Error")
        return

    if es_numero(price_value):
        price_num = float(price_value)
        label = f"Product: {product_name} | Price: ${price_num}"

        if len(label) < 30:
            label = label + (" " * (30 - len(label)))
        else:
            label = label[:30]

        print(f"Label: \"{label}\"")
    else:
        print("Error")

main()


# Problem 7: Password Strength Classifier
"""
Descripción:
Clasifica una contraseña como débil, media o fuerte según
su longitud y variedad de caracteres.

Inputs:
- password_input: string

Outputs:
- weak / medium / strong

Validations:
- Must not be empty.

Test cases:
1) "Abc123!!" -> strong
2) "password" -> weak
3) "" -> Error
"""

password_input = input("Enter password: ").strip()

if password_input == "":
    print("Error")
else:
    length = len(password_input)
    has_upper = any(c.isupper() for c in password_input)
    has_lower = any(c.islower() for c in password_input)
    has_digit = any(c.isdigit() for c in password_input)
    has_special = any(not c.isalnum() for c in password_input)

    score = 0
    if length >= 8:
        score += 1
    if has_upper and has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    if score >= 3:
        print("strong")
    elif score == 2:
        print("medium")
    else:
        print("weak")


# Conclusiones
"""
Los siete programas permiten practicar de forma directa el uso de números,
valores booleanos y manipulación de cadenas en Python. La validación de
entradas fue importante para evitar errores y asegurar que cada programa
funcionara correctamente. 

En cada ejercicio se aplicaron condiciones, comparaciones, operaciones
aritméticas y lógica de clasificación, lo que ayudó a comprender mejor
cómo se toman decisiones dentro del código. En conjunto, estos programas
refuerzan habilidades básicas de programación que serán útiles al trabajar
con proyectos más avanzados.
"""

# Referencias
"""
1) Python Documentation – Built-in Types.
2) Python String Methods – Official Docs.
3) Real Python – Boolean Logic in Python.
4) W3Schools – Python Input and Data Types.
5) Automate the Boring Stuff with Python – Chapters on strings & logic.
"""


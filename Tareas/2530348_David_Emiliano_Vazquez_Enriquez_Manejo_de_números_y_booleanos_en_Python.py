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
Este proyecto integra siete programas en Python enfocados en el manejo de tipos 
numéricos, valores booleanos y procesamiento de cadenas. Cada problema incluye 
validación de entradas, uso de condiciones lógicas, manejo de errores y formateo 
controlado de la salida para asegurar resultados claros y consistentes.

Los programas muestran aplicaciones prácticas del uso de enteros y flotantes en 
operaciones matemáticas, manipulación de textos mediante métodos de cadena, y 
evaluación booleana en la toma de decisiones. Estos conceptos se aplican en 
escenarios reales como conversiones de unidades, análisis de datos, comparaciones, 
clasificación de información y procesamiento estructurado de entradas del usuario.

Además, el proyecto refuerza habilidades esenciales en programación, tales como el 
diseño de algoritmos, la correcta documentación de entradas y salidas, la creación 
de casos de prueba y la implementación de validaciones para evitar fallos en la 
ejecución. En conjunto, este trabajo ofrece una base sólida para comprender cómo 
Python gestiona datos, realiza cálculos y ejecuta decisiones lógicas dentro de 
programas confiables y bien estructurados.
"""


# Problem 1: Temperature Converter
"""
Description:
Converts Celsius input into Fahrenheit.

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

temp_c = input("Enter Celsius: ").strip()
try:
    c = float(temp_c)
    f = (c * 9/5) + 32
    print(f"Fahrenheit: {f}")
except:
    print("Error")


# Problem 2: Extra Hours Salary Calculator
"""
Description:
Calculates payment based on hours worked and hourly rate. Extra hours (>40) pay 1.5x.

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

hours = input("Hours worked: ").strip()
rate = input("Hourly rate: ").strip()
try:
    h = float(hours)
    r = float(rate)
    if h < 0 or r < 0:
        print("Error")
    else:
        if h > 40:
            total = (40*r) + ((h-40)*(1.5*r))
        else:
            total = h*r
        print(total)
except:
    print("Error")


# Problem 3: Discount Evaluator
"""
Description:
Evaluates final price after discount based on amount.

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

amount = input("Amount: ").strip()
try:
    a = float(amount)
    if a < 0:
        print("Error")
    else:
        if a >= 500:
            final_price = a * 0.90
        else:
            final_price = a
        print(final_price)
except:
    print("Error")


# Problem 4: Integer Stats
"""
Description:
Reads three integers and prints min, max, and average.

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

n1 = input("Enter integer 1: ").strip()
n2 = input("Enter integer 2: ").strip()
n3 = input("Enter integer 3: ").strip()
try:
    i1 = int(n1)
    i2 = int(n2)
    i3 = int(n3)
    mn = min(i1, i2, i3)
    mx = max(i1, i2, i3)
    avg = (i1 + i2 + i3) / 3
    print(mn, mx, avg)
except:
    print("Error")


# Problem 5: Loan Eligibility Checker
"""
Description:
Determines eligibility based on age and income.

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

age = input("Enter age: ").strip()
income = input("Enter income: ").strip()
try:
    ag = float(age)
    inc = float(income)
    if ag < 0 or inc < 0:
        print("Error")
    else:
        if ag >= 18 and inc >= 10000:
            print("eligible")
        else:
            print("not eligible")
except:
    print("Error")


# Problem 6: Product Label Formatter
"""
Description:
Creates a product label of exactly 30 characters.

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

product_name = input("Enter product name: ").strip()
price_value = input("Enter price: ").strip()

if product_name == "" or price_value == "":
    print("Error")
else:
    try:
        price_num = float(price_value)
        label = f"Product: {product_name} | Price: ${price_num}"
        if len(label) < 30:
            label = label + (" " * (30 - len(label)))
        else:
            label = label[:30]
        print(f"Label: \"{label}\"")
    except:
        print("Error")


# Problem 7: Password Strength Classifier
"""
Description:
Classifies a password as weak, medium, or strong based on length and variety.

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


# Conclusions
"""
All seven programs demonstrate practical use of numeric processing,
boolean logic and string manipulation in Python. Input validation
proved essential to avoid runtime errors and ensure correct behavior.
Each problem required applying conditions, comparisons, arithmetic
operations and classification logic. These exercises strengthen the
foundational programming skills needed for more complex applications.
"""

# References
"""
1) Python Documentation – Built-in Types.
2) Python String Methods – Official Docs.
3) Real Python – Boolean Logic in Python.
4) W3Schools – Python Input and Data Types.
5) Automate the Boring Stuff with Python – Chapters on strings & logic.
"""

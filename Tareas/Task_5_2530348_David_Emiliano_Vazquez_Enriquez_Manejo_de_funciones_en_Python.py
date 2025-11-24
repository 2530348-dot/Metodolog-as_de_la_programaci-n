"""
Portada

Universidad Politécnica de Victoria
Materia: Metodología de la Programación
Grupo: IM-03
Alumno: David Emiliano Vázquez Enríquez
Matrícula: 2530348
Proyecto: Manejo de funciones en Python
Profesor: Carlos Antonio Tovar García
Fecha: 22/11/2025
"""
# Resumen Ejecutivo
"""
El presente proyecto aborda el manejo de funciones en Python, destacando su importancia 
para organizar y estructurar el código de manera clara y eficiente. Se explican conceptos 
como la definición de funciones, el uso de parámetros y valores por defecto, la devolución 
de resultados, las funciones anónimas y la recursión. El trabajo muestra cómo las funciones 
permiten automatizar tareas, mejorar la reutilización de código y facilitar el mantenimiento 
de programas complejos, contribuyendo a una programación más profesional y organizada.
"""
""" 
Problema 1: Área y perímetro de un rectángulo
Descripción: Define dos funciones para calcular el área y el perímetro de un rectángulo. 
El código principal debe leer o definir el ancho y el alto, llamar a las funciones y mostrar los resultados.

Entradas:
- ancho (float)
- alto (float)

Salidas:
- "Área:" <valor_area>
- "Perímetro:" <valor_perimetro>

Validaciones:
- ancho > 0
- alto > 0
- Si alguna condición no se cumple, mostrar "Error: entrada inválida" y no llamar a las funciones.

Casos de prueba:
1) Normal: ancho=5, alto=10
2) Límite: ancho=0, alto=10
3) Error: ancho=-5, alto=-10
"""
def calculate_area(ancho, alto):
    return ancho * alto

def calculate_perimeter(ancho, alto):
    return 2 * (ancho + alto)

ancho = 5
alto = 10

if ancho > 0 and alto > 0:
    print("Área:", calculate_area(ancho, alto))
    print("Perímetro:", calculate_perimeter(ancho, alto))
else:
    print("Error: entrada inválida")


""" 
Problema 2: Clasificador de calificaciones
Descripción: Define una función classify_grade(calificacion) que devuelva una letra según la calificación numérica. 
El código principal debe llamar a la función y mostrar el resultado.

Entradas:
- calificacion (float o int)

Salidas:
- "Calificación:" <calificacion>
- "Categoría:" <letra_grade>

Validaciones:
- 0 <= calificacion <= 100
- Si no se cumple, mostrar "Error: entrada inválida" y no clasificar.

Casos de prueba:
1) Normal: calificacion=85
2) Límite: calificacion=90
3) Error: calificacion=105
"""
def classify_grade(calificacion):
    if calificacion >= 90:
        return "A"
    elif calificacion >= 80:
        return "B"
    elif calificacion >= 70:
        return "C"
    elif calificacion >= 60:
        return "D"
    else:
        return "F"

calificacion = 85
if 0 <= calificacion <= 100:
    print("Calificación:", calificacion)
    print("Categoría:", classify_grade(calificacion))
else:
    print("Error: entrada inválida")


""" 
Problema 3: Función de estadísticas de lista
Descripción: Define summarize_numbers(lista_numeros) que devuelva un diccionario con mínimo, máximo y promedio.
El código principal construye la lista a partir de texto, llama a la función y muestra los resultados.

Entradas:
- texto_numeros (string, ejemplo: "10,20,30")

Salidas:
- "Mínimo:" <valor_min>
- "Máximo:" <valor_max>
- "Promedio:" <valor_promedio>

Validaciones:
- texto_numeros no vacío
- Todos los elementos convertibles a números
- Si no se cumple, mostrar "Error: entrada inválida"

Casos de prueba:
1) Normal: "10,20,30,40"
2) Límite: "5"
3) Error: "10,abc,30"
"""
def summarize_numbers(lista_numeros):
    numeros = [float(x) for x in lista_numeros]
    return {
        "min": min(numeros),
        "max": max(numeros),
        "average": sum(numeros) / len(numeros)
    }

texto_numeros = "10,20,30,40"
try:
    if texto_numeros.strip() == "":
        raise ValueError
    lista = [x.strip() for x in texto_numeros.split(",") if x.strip() != ""]
    if not lista:
        raise ValueError
    resultados = summarize_numbers(lista)
    print("Mínimo:", resultados["min"])
    print("Máximo:", resultados["max"])
    print("Promedio:", resultados["average"])
except:
    print("Error: entrada inválida")


""" 
Problema 4: Aplicar descuento a lista
Descripción: Define apply_discount(lista_precios, tasa_descuento) que devuelva una nueva lista con precios descontados.
El código principal crea una lista de precios, llama a la función y muestra ambas listas.

Entradas:
- texto_precios (string, ejemplo: "100,200,300")
- tasa_descuento (float, 0 <= tasa <= 1)

Salidas:
- "Precios originales:" <lista_original>
- "Precios con descuento:" <lista_descuento>

Validaciones:
- texto_precios no vacío y todos los precios > 0
- 0 <= tasa_descuento <= 1
- Si no se cumple, mostrar "Error: entrada inválida"

Casos de prueba:
1) Normal: "100,200,300", tasa_descuento=0.1
2) Límite: "50", tasa_descuento=0
3) Error: "100,-200,300", tasa_descuento=1.2
"""
def apply_discount(lista_precios, tasa_descuento):
    return [precio * (1 - tasa_descuento) for precio in lista_precios]

texto_precios = "100,200,300"
tasa_descuento = 0.1
try:
    lista = [float(x) for x in texto_precios.split(",")]
    if any(p <= 0 for p in lista) or not (0 <= tasa_descuento <= 1):
        raise ValueError
    lista_descuento = apply_discount(lista, tasa_descuento)
    print("Precios originales:", lista)
    print("Precios con descuento:", lista_descuento)
except:
    print("Error: entrada inválida")


""" 
Problema 5: Función de saludo con parámetros por defecto
Descripción: Define greet(nombre, titulo="") que devuelva "Hola, <nombre_completo>!".
El código principal debe llamar a la función usando argumentos posicionales y nombrados.

Entradas:
- nombre (string)
- titulo (string, opcional)

Salidas:
- "Saludo:" <mensaje_saludo>

Validaciones:
- nombre no vacío
- titulo puede estar vacío, pero se normaliza si se proporciona

Casos de prueba:
1) Normal: nombre="Alice", titulo="Dra."
2) Límite: nombre="Bob", titulo=""
3) Error: nombre="", titulo="Sr."
"""
def greet(nombre, titulo=""):
    nombre = nombre.strip()
    titulo = titulo.strip()
    if titulo:
        full_name = f"{titulo} {nombre}"
    else:
        full_name = nombre
    return f"Hola, {full_name}!"

nombre = "Alice"
titulo = "Dra."
if nombre.strip():
    print("Saludo:", greet(nombre, titulo))
else:
    print("Error: entrada inválida")


""" 
Problema 6: Función factorial
Descripción: Define factorial(n) que devuelva n!. Puede implementarse de forma iterativa o recursiva.
El código principal debe leer/definir n, validar, llamar a factorial(n) y mostrar el resultado.

Entradas:
- n (int)

Salidas:
- "n:" <n>
- "Factorial:" <valor_factorial>

Validaciones:
- n entero >= 0, opcionalmente n <= 20
- Si no se cumple, mostrar "Error: entrada inválida"

Casos de prueba:
1) Normal: n=5
2) Límite: n=0
3) Error: n=-3
"""
def factorial(n):
    # Implementación iterativa
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = 5
if isinstance(n, int) and n >= 0 and n <= 20:
    print("n:", n)
    print("Factorial:", factorial(n))
else:
    print("Error: entrada inválida")


# Conclusion 
"""
El manejo de funciones en Python es fundamental para desarrollar programas claros, 
reutilizables y fáciles de mantener. Su uso adecuado simplifica la resolución de problemas, 
mejora la productividad y constituye la base para avanzar hacia técnicas de programación 
más avanzadas, garantizando la eficiencia y calidad del software.
"""
# Referencias
"""
[1] M. Lutz, Programming Python, 4th ed., O’Reilly Media, 2011.
[2] A. Sweigart, Automate the Boring Stuff with Python, 2nd ed., No Starch Press, 2019.
[3] D. Beazley and B. K. Jones, Python Cookbook, 3rd ed., O’Reilly Media, 2013.
[4] Python Software Foundation, “Python Documentation – Functions,” [Online]. 
Available: https://docs.python.org/3/tutorial/functions.html.
[5] J. Grus, Data Science from Scratch, 2nd ed., O’Reilly Media, 2019.
"""
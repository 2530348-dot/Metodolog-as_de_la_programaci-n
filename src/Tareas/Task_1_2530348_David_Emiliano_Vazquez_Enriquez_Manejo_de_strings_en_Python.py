"""
Universidad Politécnica de Victoria
Materia: Metodología de la Programación
Grupo: IM-03
Alumno: David Emiliano Vázquez Enríquez
Matrícula: 2530348
Proyecto: String Handling in Python
Profesor: Carlos Antonio Tovar García
Fecha: 22/11/2025
"""
"""
El proyecto de Manejo de Strings en Python reúne seis ejercicios diseñados para aplicar
las operaciones fundamentales sobre cadenas dentro del lenguaje. Cada problema aborda un
caso realista donde el usuario ingresa texto que debe ser limpiado, validado y procesado.

Los programas incluyen: formateo de nombre completo con iniciales, validación básica de
correo electrónico, detección de palíndromos ignorando espacios, análisis de palabras en
una oración, clasificación de contraseñas según su fortaleza y creación de etiquetas de
producto con longitud fija. En todos los casos se aplican técnicas como strip(), lower(),
split(), replace(), slicing, conteo de caracteres y verificación de patrones simples.

Este conjunto de soluciones demuestra la importancia de normalizar texto antes de
procesarlo, validar entradas para evitar errores y aprovechar la inmutabilidad de los
strings para generar nuevas versiones limpias y seguras. El documento también integra
casos de prueba y conclusiones que reflejan la lógica aplicada en cada ejercicio.
"""

#Problem 1: Full name formatter

"""

Descripción:
Da formato a un nombre completo en 
Title Case y genera sus iniciales usando la entrada limpiada.
Inputs:
- full_name: string

Outputs:
- Formatted name: <...>
- Initials: <...>

Validations:
- Input cannot be empty.
- Must contain at least two words.

Test cases:
1) Normal: "juan carlos tovar" -> Formatted name: Juan Carlos Tovar | Initials: J.C.T.
2) Border: "  ana   perez  " -> Ana Perez | A.P.
3) Error: "   " -> Error: invalid input
"""

full_name = input("Enter full name: ").strip()

if full_name == "" or len(full_name.split()) < 2:
    print("Error: invalid input")
else:
    parts = full_name.lower().split()
    formatted = " ".join([p.title() for p in parts])
    initials = ".".join([p[0].upper() for p in parts]) + "."
    print(f"Formatted name: {formatted}")
    print(f"Initials: {initials}")


#Problem 2: Simple email validator


"""
Descripción:
Verifica si un correo electrónico contiene exactamente un '@', 
no tiene espacios y cuenta con al menos un '.' después del '@'.

Inputs:
- email_text: string

Outputs:
- Valid email: true/false
- Domain: <...> (if valid)

Validations:
- Email cannot be empty.
- Must have exactly one '@'.
- No spaces allowed.

Test cases:
1) Normal: "user@mail.com" -> Valid email: true | Domain: mail.com
2) Border: "test@domain" -> Valid email: false
3) Error: "user@@mail.com" -> Valid email: false
"""

email_text = input("Enter email: ").strip()

if email_text == "" or " " in email_text or email_text.count("@") != 1:
    print("Valid email: false")
else:
    at_index = email_text.find("@")
    domain = email_text[at_index + 1:]
    if "." in domain:
        print("Valid email: true")
        print(f"Domain: {domain}")
    else:
        print("Valid email: false")

#Problem 3: Palindrome checker

"""
Descripción:
Determina si una frase es un palíndromo,
 ignorando espacios y mayúsculas/minúsculas.

Inputs:
- phrase: string

Outputs:
- Is palindrome: true/false

Validations:
- Input cannot be empty.
- Minimum length after cleaning: 3 characters.

Test cases:
1) Normal: "Anita lava la tina" -> true
2) Border: "ala" -> true
3) Error: "a" -> Error: too short
"""

phrase = input("Enter phrase: ").strip()

if phrase == "":
    print("Error: invalid input")
else:
    cleaned = phrase.replace(" ", "").lower()
    if len(cleaned) < 3:
        print("Error: too short")
    else:
        is_pal = cleaned == cleaned[::-1]
        print(f"Is palindrome: {str(is_pal).lower()}")


#Problem 4: Sentence word stats

"""

Descripción:
Analiza una oración y muestra el total de palabras, la primera,
 la última, así como la palabra más corta y la más larga.

Inputs:
- sentence: string

Outputs:
- Word count
- First word
- Last word
- Shortest and longest words

Validations:
- Cannot be empty.
- Must contain at least one valid word.

Test cases:
1) Normal: "hello world from python" -> count=4, first=hello, last=python
2) Border: "   hi   " -> count=1
3) Error: "    " -> Error: invalid input
"""

sentence = input("Enter sentence: ").strip()

if sentence == "":
    print("Error: invalid input")
else:
    words = sentence.split()
    if len(words) == 0:
        print("Error: invalid input")
    else:
        shortest = min(words, key=len)
        longest = max(words, key=len)
        print(f"Word count: {len(words)}")
        print(f"First word: {words[0]}")
        print(f"Last word: {words[-1]}")
        print(f"Shortest word: {shortest}")
        print(f"Longest word: {longest}")


#Problem 5: Password strength classifier

"""
Descripción:
Clasifica una contraseña como débil, 
media o fuerte según la variedad de caracteres y su longitud.

Inputs:
- password_input: string

Outputs:
- Password strength: weak/medium/strong

Validations:
- Cannot be empty.
- Length must be checked.

Test cases:
1) Normal: "Abc123!!" -> strong
2) Border: "password" -> weak
3) Error: "" -> Error: invalid input
"""

password_input = input("Enter password: ")

if password_input.strip() == "":
    print("Error: invalid input")
else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for c in password_input:
        if c.isupper():
            has_upper = True
        elif c.islower():
            has_lower = True
        elif c.isdigit():
            has_digit = True
        elif not c.isalnum():
            has_symbol = True

    length = len(password_input)

    if length < 8 or (has_lower and not has_upper and not has_digit and not has_symbol):
        print("Password strength: weak")
    elif length >= 8 and ((has_upper and has_lower) or has_digit):
        if has_upper and has_lower and has_digit and has_symbol:
            print("Password strength: strong")
        else:
            print("Password strength: medium")
    else:
        print("Password strength: weak")

#Problem 6: Product label formatter

"""
Descripción:
Crea una etiqueta de producto con exactamente 30 caracteres,
 añadiendo relleno o recortando según sea necesario.

Inputs:
- product_name: string
- price_value: string/number

Outputs:
- Label: "<30 char string>"

Validations:
- product_name cannot be empty.
- price_value must be numeric and positive.

Test cases:
1) Normal: product="Apple", price="10" -> valid label 30 chars
2) Border: long product name -> trimmed
3) Error: price="abc" -> invalid price
"""

product_name = input("Enter product name: ").strip()
price_value = input("Enter price: ").strip()

if product_name == "" or price_value == "":
    print("Error: invalid input")
else:
    try:
        price_num = float(price_value)
        label = f"Product: {product_name} | Price: ${price_num}"
        if len(label) < 30:
            label = label + " " * (30 - len(label))
        else:
            label = label[:30]
        print(f"Label: \"{label}\"")
    except:
        print("Error: invalid price")


"""
Las actividades realizadas permitieron comprobar que el manejo de strings en Python es
fundamental para validar, limpiar y transformar datos ingresados por el usuario. Mediante
el uso de operaciones como strip(), lower(), split(), join(), replace() y slicing, es
posible garantizar que la información se procese de forma correcta y segura.

Durante el desarrollo de los seis problemas, se reforzó la importancia de normalizar
entradas antes de compararlas, pues pequeñas variaciones como mayúsculas, espacios o
caracteres no deseados pueden alterar los resultados. También se observó cómo la
inmutabilidad de los strings permite trabajar de forma predecible, generando nuevas
cadenas en cada transformación.

La creación de validaciones claras evita errores lógicos y ayuda a construir programas
robustos orientados al usuario. Finalmente, se demostró que la manipulación adecuada de
texto es una habilidad indispensable en prácticamente cualquier aplicación real.
"""
"""
References:
1) Python Documentation  Built-in Types: Text Sequence Type — str.
2) Python Official Tutorial  String Methods and Operations.
3) “Automate the Boring Stuff with Python”  Al Sweigart, Chapter on Strings.
4) Real Python  “Essential String Manipulation Techniques”.
5) W3Schools  Python String Methods Reference.
"""
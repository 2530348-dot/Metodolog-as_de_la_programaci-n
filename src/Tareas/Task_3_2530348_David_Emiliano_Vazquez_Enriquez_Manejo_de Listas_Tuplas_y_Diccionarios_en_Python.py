"""
Universidad Politécnica de Victoria
Materia: Metodología de la Programación
Grupo: IM-03
Alumno: David Emiliano Vázquez Enríquez
Matrícula: 2530348
Proyecto: Python Collections Lists, Tuples and Dictionaries
Profesor: Carlos Antonio Tovar García
Fecha: 22/11/2025
"""
"""
RESUMEN EJECUTIVO

Las Listas en Python ayudan a organizar datos de manera sencilla y práctica. 
Las listas permiten guardar varios valores y modificarlos cuando sea necesario.  
Las tuplas funcionan de forma similar, pero sus datos no se pueden cambiar, por 
lo que son útiles para información que debe mantenerse fija, como coordenadas.  

Los diccionarios guardan datos usando una clave y un valor, lo que facilita buscar 
información rápida­mente, por ejemplo en catálogos, contactos o registros.

En este documento se presentan seis ejercicios donde se usan listas, tuplas y 
diccionarios en situaciones reales. Cada problema incluye su descripción y casos 
de prueba, mostrando cómo agregar, buscar, actualizar y organizar datos. Estos 
ejercicios ayudan a entender mejor cómo funcionan estas estructuras y cómo 
aplicarlas en programas simples y útiles.

"""
# Problem 1 – Shopping List Basics
"""
Descripción:
Este programa trabaja con una lista de elementos. Crea una lista inicial, agrega
un nuevo artículo, cuenta el total de elementos y revisa si un producto específico
está dentro de la lista.

INPUTS:
- initial_items_text (string)
- new_item (string)
- search_item (string)

OUTPUTS:
- Items list
- Total items count
- Boolean value showing if item was found

VALIDATIONS:
- initial_items_text must not be empty
- All items must be cleaned using strip()
- new_item and search_item must not be empty

TEST CASES:
1) Normal: "apple,banana", "orange", "banana"
2) Normal: "milk,bread,eggs", "coffee", "eggs"
3) Border: "", "apple", "apple"
4) Border: "apple", "", "apple"
5) Error: "apple,banana", "orange", ""
"""

initial_items_text = "apple,banana,orange"
new_item = "grape"
search_item = "banana"

if initial_items_text.strip() == "":
    items_list = []
else:
    items_list = [i.strip() for i in initial_items_text.split(",")]

if new_item.strip() != "":
    items_list.append(new_item.strip())

is_in_list = search_item.strip() in items_list if search_item.strip() else False

print("Items list:", items_list)
print("Total items:", len(items_list))
print("Found item:", is_in_list)

# Problem 2 – Points and Distances with Tuples
"""
Descripción:
Este programa usa tuplas para guardar las coordenadas de dos puntos y calcula
la distancia euclidiana entre ellos, así como el punto medio.

INPUTS:
- x1, y1, x2, y2 (float)

OUTPUTS:
- Point A, Point B
- Distance between points
- Midpoint tuple

VALIDATIONS:
- Inputs must be convertible to float

TEST CASES:
1) Normal: (0,0) and (3,4)
2) Normal: (1,2) and (5,9)
3) Border: (0,0) and (0,0)
4) Border: (-5,-5) and (5,5)
5) Error: x1 = "abc"
"""

x1 = 0.0
y1 = 0.0
x2 = 3.0
y2 = 4.0

point_a = (x1, y1)
point_b = (x2, y2)

distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
midpoint = ((x1 + x2)/2, (y1 + y2)/2)

print("Point A:", point_a)
print("Point B:", point_b)
print("Distance:", distance)
print("Midpoint:", midpoint)

# Problem 3 – Product Catalog Dictionary
"""
Descripción:
Gestiona un diccionario de productos con sus precios y calcula el total a pagar
según la cantidad solicitada por el usuario.

INPUTS:
- product_name (string)
- quantity (int)

OUTPUTS:
- Unit price
- Quantity
- Total price
- Error if product does not exist

VALIDATIONS:
- quantity > 0
- product_name must not be empty
- product must exist in dictionary

TEST CASES:
1) Normal: "apple", 2
2) Normal: "banana", 5
3) Border: product in dict but quantity = 1
4) Error: product does not exist
5) Error: quantity = 0
"""

product_prices = {"apple": 10.0, "banana": 7.5, "milk": 22.0}

product_name = "apple"
quantity = 3

if product_name.strip() == "" or quantity <= 0:
    print("Error: invalid input")
elif product_name not in product_prices:
    print("Error: product not found")
else:
    unit_price = product_prices[product_name]
    total_price = unit_price * quantity
    print("Unit price:", unit_price)
    print("Quantity:", quantity)
    print("Total:", total_price)


# Problem 4 – Student Grades
"""
Descripción:
Utiliza un diccionario donde cada estudiante tiene una lista de calificaciones.
Calcula el promedio y determina si el estudiante aprobó o no.

INPUTS:
- student_name (string)

OUTPUTS:
- Grades list
- Average
- Passed boolean
- Error if student does not exist

VALIDATIONS:
- student_name must not be empty
- student must exist
- grades list must not be empty

TEST CASES:
1) Normal: "Alice"
2) Normal: "Bob"
3) Border: student has exactly 1 grade
4) Error: student does not exist
5) Error: student_name = ""
"""

grades = {
    "Alice": [90, 85, 88],
    "Bob": [70, 75, 72],
    "Carol": [60, 65, 55]
}

student_name = "Alice"

if student_name.strip() == "":
    print("Error: invalid input")
elif student_name not in grades:
    print("Error: student not found")
else:
    student_grades = grades[student_name]
    average = sum(student_grades) / len(student_grades)
    is_passed = average >= 70.0
    print("Grades:", student_grades)
    print("Average:", average)
    print("Passed:", is_passed)


# Problem 5 – Word Frequency Counter
"""
Descripción:
Cuenta la frecuencia de cada palabra en una oración usando listas y diccionarios.
También identifica cuál es la palabra que más se repite.

INPUTS:
- sentence (string)

OUTPUTS:
- Words list
- Frequency dictionary
- Most common word

VALIDATIONS:
- sentence must not be empty
- words list must not be empty

TEST CASES:
1) Normal: "apple banana apple orange"
2) Normal: "hello world hello"
3) Border: "apple"
4) Border: "A A A a"
5) Error: ""
"""

sentence = "apple banana apple orange"

if sentence.strip() == "":
    print("Error: invalid input")
else:
    words_list = sentence.lower().split()
    freq = {}
    for w in words_list:
        freq[w] = freq.get(w, 0) + 1
    most_common = max(freq, key=freq.get)

    print("Words list:", words_list)
    print("Frequencies:", freq)
    print("Most common word:", most_common)

# Problem 6 – Contact Book CRUD
"""
Descripción:
Implementa un sistema de contactos tipo CRUD con un diccionario, permitiendo
agregar, buscar o eliminar contactos según la acción indicada.


INPUTS:
- action_text
- name
- phone (only for ADD)

OUTPUTS:
- Contact saved
- Phone found
- Contact deleted
- Error if not found

VALIDATIONS:
- action must be ADD, SEARCH or DELETE
- name must not be empty
- phone must not be empty when adding

TEST CASES:
1) ADD: ("ADD", "Alice", "12345")
2) SEARCH: ("SEARCH", "Alice")
3) DELETE: ("DELETE", "Alice")
4) Error: search non-existing name
5) Error: ADD with empty phone
"""

contacts = {"Bob": "777888999"}

action_text = "ADD".upper()
name = "Alice"
phone = "555222111"

if action_text not in ["ADD", "SEARCH", "DELETE"]:
    print("Error: invalid action")
else:
    if action_text == "ADD":
        if name.strip() == "" or phone.strip() == "":
            print("Error: invalid input")
        else:
            contacts[name] = phone
            print("Contact saved:", name, phone)

    elif action_text == "SEARCH":
        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Error: contact not found")

    elif action_text == "DELETE":
        if name in contacts:
            contacts.pop(name)
            print("Contact deleted:", name)
        else:
            print("Error: contact not found")


"""
Conclusión:
A lo largo de estos ejercicios se reforzaron las bases de Python mediante el uso
de listas, tuplas, diccionarios y cadenas de texto. También se practicó la validación
de entradas, el manejo de condiciones y la organización de datos. Cada programa
permitió aplicar lógica y razonamiento para resolver problemas comunes, lo que
ayuda a desarrollar pensamiento computacional y una mejor comprensión del flujo
de un programa. En general, estos ejercicios fortalecen las habilidades necesarias
para crear aplicaciones más avanzadas, confiables y bien estructuradas.
"""

"""
REFERENCES

[1] M. Lutz, *Learning Python*, 5th ed. Sebastopol, CA, USA: O_Reilly Media, 2013.

[2] E. Matthes, *Python Crash Course: A Hands-On, Project-Based Introduction to Programming*,
2nd ed. San Francisco, CA, USA: No Starch Press, 2019.

[3] Python Software Foundation, “Python 3 Documentation,” python.org. 
Available: https://docs.python.org/3/

[4] J. Zelle, *Python Programming: An Introduction to Computer Science*, 
3rd ed. Franklin, Beedle & Associates, 2016.

[5] D. Beazley and B. Jones, *Python Cookbook*, 3rd ed. Sebastopol, CA, USA: O’Reilly Media, 2013.
"""


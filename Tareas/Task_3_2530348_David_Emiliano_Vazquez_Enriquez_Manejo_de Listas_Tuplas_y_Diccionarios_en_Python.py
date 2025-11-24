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

Las colecciones en Python permiten organizar y manipular datos de forma eficiente. 
Las listas (list) son estructuras ordenadas y mutables, lo que permite agregar, 
eliminar y modificar elementos durante la ejecución del programa. Las tuplas (tuple) 
son estructuras ordenadas pero inmutables, ideales para representar datos fijos como 
coordenadas o registros que no deben cambiar.

Los diccionarios (dict) almacenan información mediante pares clave-valor, 
permitiendo búsquedas rápidas y gestión de datos relacionados como catálogos, 
contactos o calificaciones.

Este documento contiene seis problemas prácticos que demuestran el uso real de listas, 
tuplas y diccionarios. Cada problema incluye descripción, entradas, salidas, 
validaciones y casos de prueba (normal, borde y error). A través de estos ejercicios 
se aplican operaciones esenciales como búsqueda, actualización, agregación y 
procesamiento de datos, reforzando el dominio de estas estructuras en contextos 
prácticos de programación.
"""
# Problem 1 – Shopping List Basics
"""
DESCRIPTION:
This program works with a list of items. It creates an initial list, adds a new item,
counts the total items, and checks if a specific product exists.

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
DESCRIPTION:
This program uses tuples to store coordinates for two points and calculates
the Euclidean distance and midpoint.

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
DESCRIPTION:
Manages a dictionary of products and calculates total price based on quantity.

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
DESCRIPTION:
Uses a dictionary where each key is a student name and value is a list of grades.
Computes average and determines if passed.

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
DESCRIPTION:
Counts the frequency of each word in a sentence using list + dictionary.

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
DESCRIPTION:
Implements a contact book using a dictionary with ADD, SEARCH, and DELETE actions.

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
CONCLUSIONS

Throughout the development of the programs, the practical use of Python’s fundamental
data types—integers, floats, booleans, and strings—was reinforced through real
applications. Each exercise demonstrated how proper input validation, conditional
logic, and structured output contribute to reliable and predictable program behavior.

The problems allowed the integration of numerical operations, string manipulation,
and logical evaluations to solve tasks such as comparisons, classifications,
unit conversions, and data processing. By implementing structured algorithms and
testing them with multiple scenarios, the projects strengthened analytical thinking
and problem-solving skills.

Additionally, the emphasis on documenting inputs, outputs, and test cases improved
clarity and maintainability, highlighting the importance of clean, organized, and
well-designed code. Overall, this set of programs helps build a solid foundation
for more advanced programming concepts and the development of efficient and
professional Python applications.
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


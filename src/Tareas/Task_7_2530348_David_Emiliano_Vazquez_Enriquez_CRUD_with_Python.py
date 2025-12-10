"""
Portada

Universidad Politécnica de Victoria
Materia: Metodología de la Programación
Grupo: IM-03
Alumno: David Emiliano Vázquez Enríquez
Matrícula: 2530348
Proyecto: CRUD with Python
Profesor: Carlos Antonio Tovar García
Fecha: 22/11/2025
"""

"""
Resumen Ejecutivo

El presente proyecto implementa un gestor CRUD (Create, Read, Update, Delete) en Python 
usando una lista de diccionarios para almacenar elementos en memoria. Cada operación está 
encapsulada en funciones separadas, permitiendo organizar y estructurar la lógica del programa 
de manera clara y reutilizable. El usuario puede crear nuevos ítems, consultar información, 
actualizar datos existentes y eliminar elementos según su identificador único. 
El programa valida entradas, maneja errores y muestra mensajes claros en inglés. 
Se destaca la importancia de separar responsabilidades, usar funciones para modularidad 
y garantizar que las operaciones de datos sean robustas y comprensibles.
"""

"""
Problem: In-memory CRUD manager with functions
Programa que implementa un CRUD simple (Crear, Leer, Actualizar y Eliminar)
para elementos almacenados en una lista de diccionarios, usando funciones separadas
 y un menú basado en texto.
 
Inputs:
- Menu options (int)
- For CREATE/UPDATE: item_id (string), name (string), price (float), quantity (int)
- For READ/DELETE: item_id (string)

Outputs:
- Messages indicating the result of each operation:
  - "Item created", "Item updated", "Item deleted", "Item not found", "Items list:"

Validations:
- Menu option must be valid
- item_id must not be empty
- price >= 0.0, quantity >= 0
- CREATE: id must not already exist
- READ/UPDATE/DELETE: id must exist

Test cases:
1) Normal: create item, read it, update it, delete it → expected messages and final state
2) Border: create item with minimal data (quantity=0) → valid operation
3) Error: invalid menu option or invalid id → expected error messages
"""


items = []

def find_item_index_by_id(item_id):
    for index, item in enumerate(items):
        if item["id"] == item_id:
            return index
    return None

def create_item(item_id, name, price, quantity):
    if find_item_index_by_id(item_id) is not None:
        print("Error: item id already exists")
        return
    items.append({"id": item_id, "name": name, "price": price, "quantity": quantity})
    print("Item created")

def read_item(item_id):
    index = find_item_index_by_id(item_id)
    if index is None:
        print("Item not found")
    else:
        item = items[index]
        print("Item found:", item)

def update_item(item_id, new_name, new_price, new_quantity):
    index = find_item_index_by_id(item_id)
    if index is None:
        print("Item not found")
    else:
        items[index]["name"] = new_name
        items[index]["price"] = new_price
        items[index]["quantity"] = new_quantity
        print("Item updated")

def delete_item(item_id):
    index = find_item_index_by_id(item_id)
    if index is None:
        print("Item not found")
    else:
        items.pop(index)
        print("Item deleted")

def list_items():
    if not items:
        print("No items in the list")
    else:
        print("Items list:")
        for item in items:
            print(item)

def input_float(prompt):
    try:
        value = float(input(prompt))
        if value < 0:
            raise ValueError
        return value
    except ValueError:
        print("Error: invalid input")
        return None

def input_int(prompt):
    try:
        value = int(input(prompt))
        if value < 0:
            raise ValueError
        return value
    except ValueError:
        print("Error: invalid input")
        return None

def main():
    while True:
        print("\nMenu:")
        print("1) Create item")
        print("2) Read item by id")
        print("3) Update item by id")
        print("4) Delete item by id")
        print("5) List all items")
        print("0) Exit")
        option = input("Select an option: ").strip()
        
        if option == "1":
            item_id = input("Enter item id: ").strip()
            name = input("Enter item name: ").strip()
            price = input_float("Enter price: ")
            quantity = input_int("Enter quantity: ")
            if item_id and name and price is not None and quantity is not None:
                create_item(item_id, name, price, quantity)
            else:
                print("Error: invalid input")
        elif option == "2":
            item_id = input("Enter item id to read: ").strip()
            if item_id:
                read_item(item_id)
            else:
                print("Error: invalid input")
        elif option == "3":
            item_id = input("Enter item id to update: ").strip()
            if not item_id:
                print("Error: invalid input")
                continue
            name = input("Enter new name: ").strip()
            price = input_float("Enter new price: ")
            quantity = input_int("Enter new quantity: ")
            if name and price is not None and quantity is not None:
                update_item(item_id, name, price, quantity)
            else:
                print("Error: invalid input")
        elif option == "4":
            item_id = input("Enter item id to delete: ").strip()
            if item_id:
                delete_item(item_id)
            else:
                print("Error: invalid input")
        elif option == "5":
            list_items()
        elif option == "0":
            print("Exiting program")
            break
        else:
            print("Error: invalid input")

if __name__ == "__main__":
    main()

"""
Conclusiones

El uso de funciones para cada operación CRUD simplificó la estructura del programa y 
facilitó la reutilización del código. La elección de una lista de diccionarios permitió 
almacenar y gestionar los datos de manera eficiente, manteniendo la claridad y accesibilidad 
de cada ítem mediante su identificador único. Las validaciones implementadas previenen 
errores de entrada y aseguran que las operaciones se realicen correctamente. 
El menú interactivo permite al usuario realizar todas las operaciones de manera intuitiva. 
Este CRUD en memoria puede extenderse fácilmente para guardar datos en archivos o bases de datos 
más complejas, demostrando la flexibilidad de la programación modular en Python.
"""

"""
Referencias

[1] Python Software Foundation, “Python Documentation  Data structures,” [Online]. Available: https://docs.python.org/3/tutorial/datastructures.html
[2] Python Software Foundation, “Python Documentation  Defining functions,” [Online]. Available: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
[3] Real Python, “Python CRUD Example,” [Online]. Available: https://realpython.com/python-crud/
[4] M. Lutz, Learning Python, 5th ed., O'Reilly Media, 2013.
[5] A. Sweigart, Automate the Boring Stuff with Python, 2nd ed., No Starch Press, 2019.
"""

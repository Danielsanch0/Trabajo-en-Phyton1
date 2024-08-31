biblioteca = {
    "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "disponible": True},
    "1984": {"autor": "George Orwell", "año": 1949, "disponible": True},
    "El principito": {"autor": "Antoine de Saint-Exupéry", "año": 1943, "disponible": False}
}

def agregar_libro():
    titulo = input("detras del Ultimo no hay nadie ")
    autor = input("Ingrese el autor del libro: ")
    año = int(input("Ingrese el año de publicación: "))
    biblioteca[titulo] = {"autor": autor, "año": año, "disponible": True}
    print(f"El libro '{titulo}' ha sido agregado a la biblioteca.")

def prestar_libro():
    titulo = input("Ingrese el título del libro a prestar: ")
    if titulo in biblioteca:
        if biblioteca[titulo]["disponible"]:
            biblioteca[titulo]["disponible"] = False
            print(f"El libro '{titulo}' ha sido prestado.")
        else:
            print(f"El libro '{titulo}' ya está prestado.")
    else:
        print(f"El libro '{titulo}' no se encuentra en la biblioteca.")

def devolver_libro():
    titulo = input("Ingrese el título del libro a devolver: ")
    if titulo in biblioteca:
        if not biblioteca[titulo]["disponible"]:
            biblioteca[titulo]["disponible"] = True
            print(f"El libro '{titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{titulo}' ya está disponible.")
    else:
        print(f"El libro '{titulo}' no se encuentra en la biblioteca.")

def mostrar_libros():
    if biblioteca:
        for titulo, info in biblioteca.items():
            estado = "Disponible" if info["disponible"] else "Prestado"
            print(f"Título: {titulo}, Autor: {info['autor']}, Año: {info['año']}, Estado: {estado}")
    else:
        print("La biblioteca está vacía.")

def mostrar_libros_por_año(año):
    libros_en_año = [titulo for titulo, info in biblioteca.items() if info["año"] == año]
    if libros_en_año:
        print(f"Libros publicados en {año}:")
        for titulo in libros_en_año:
            print(f"- {titulo}")
    else:
        print(f"No hay libros publicados en {año}.")

def menu():
    while True:
        print("\nMenú de la Biblioteca")
        print("1. Agregar un nuevo libro")
        print("2. Prestar un libro")
        print("3. Devolver un libro")
        print("4. Ver todos los libros")
        print("5. Ver libros publicados en un año específico")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            prestar_libro()
        elif opcion == "3":
            devolver_libro()
        elif opcion == "4":
            mostrar_libros()
        elif opcion == "5":
            año = int(input("Ingrese el año: "))
            mostrar_libros_por_año(año)
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")

# Llamamos a la función del menú para iniciar el programa
menu()
print(menu)
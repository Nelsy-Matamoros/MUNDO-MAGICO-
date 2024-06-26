"""
Este programa gestiona un registro básico de estudiantes. Permite agregar estudiantes con su nombre, edad y si están inscritos (booleano).
También permite ver todos los estudiantes y eliminar estudiantes del registro.
"""

# Lista para almacenar los registros de los estudiantes
students = []


def add_student(name, age, enrolled):
    """
    Función para agregar un estudiante al registro.
    :param name: str - Nombre del estudiante
    :param age: int - Edad del estudiante
    :param enrolled: bool - Si el estudiante está inscrito o no
    """
    student = {
        "name": name,
        "age": age,
        "enrolled": enrolled
    }
    students.append(student)


def view_students():
    """
    Función para mostrar todos los estudiantes en el registro.
    """
    for student in students:
        enrolled_status = "Inscrito" if student["enrolled"] else "No inscrito"
        print(f"Nombre: {student['name']}, Edad: {student['age']}, Estado: {enrolled_status}")


def delete_student(name):
    """
    Función para eliminar un estudiante del registro por su nombre.
    :param name: str - Nombre del estudiante a eliminar
    """
    global students
    students = [student for student in students if student["name"] != name]


def main():
    """
    Función principal que gestiona la interacción con el usuario.
    """
    while True:
        print("\nOpciones:")
        print("1. Agregar estudiante")
        print("2. Ver estudiantes")
        print("3. Eliminar estudiante")
        print("4. Salir")

        choice = input("Elige una opción: ")

        if choice == '1':
            name = input("Nombre del estudiante: ")
            age = int(input("Edad del estudiante: "))
            enrolled = input("¿Está inscrito? (sí/no): ").strip().lower() == 'sí'
            add_student(name, age, enrolled)
        elif choice == '2':
            view_students()
        elif choice == '3':
            name = input("Nombre del estudiante a eliminar: ")
            delete_student(name)
        elif choice == '4':
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")


if __name__ == "__main__":
    main()

from task_repository import get_data
from task_service import add_task, update_list_in_db, delete_task

def show_menu():
    return """\n
          Gestor de Tareas 
    1. Agregar una tarea (Pedir una descripción y agregarla a la lista).
    2. Ver tareas (Mostrar todas las tareas con su estado).
    3. Marcar una tarea como completada (Actualizar el estado de una tarea por su ID).
    4. Eliminar una tarea (Eliminar una tarea por su ID).
    5. Salir (Terminar el programa).
    """

def show_tasks():
    tasks = get_data()
    if not tasks:
        print("No hay tareas registradas.")
    else:
        for task in tasks:
            print(f"ID: {task['id']} | Descripción: {task['description']} | Estado: {task['status']}")

def get_valid_id(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Ingrese un número válido.")

def task_manager():
    while True:
        print(show_menu())
        option = input("Seleccione una opción (1, 2, 3, 4 o 5): ").strip()

        if option not in {"1", "2", "3", "4", "5"}:
            print("Opción no válida. Intente de nuevo.")
            continue

        option = int(option)

        if option == 1:
            while True:
                description = input("Ingrese la descripción de la tarea: ").strip()
                if description:
                    tasks = get_data()
                    task_id = len(tasks) + 1
                    new_task = {"id": task_id, "description": description, "status": "pendiente"}
                    add_task(new_task)
                    print("Tarea agregada con éxito. :)")
                else:
                    print("La descripción no puede estar vacía.")
                
                if input("¿Desea agregar otra tarea? (s/n): ").strip().lower() != "s":
                    break

        elif option == 2:
            show_tasks()

        elif option == 3:
            while True:
                show_tasks()
                task_id = get_valid_id("Ingrese el ID de la tarea a completar: ")
                update_list_in_db(task_id)
                print("Tarea marcada como completada.")
                
                if input("¿Desea completar otra tarea? (s/n): ").strip().lower() != "s":
                    break

        elif option == 4:
            while True:
                show_tasks()
                task_id = get_valid_id("Ingrese el ID de la tarea a eliminar: ")
                delete_task(task_id)
                print("Tarea eliminada con éxito.")
                
                if input("¿Desea eliminar otra tarea? (s/n): ").strip().lower() != "s":
                    break

        elif option == 5:
            print("Saliendo del gestor de tareas. ¡Hasta pronto!")
            break

if __name__ == "__main__":
    task_manager()

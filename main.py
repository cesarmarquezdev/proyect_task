from task_repository import get_data, get_id
from task_service import add_task, update_list_in_db , delete_task
data = get_data()

final_check ="s"
while final_check == "s":
    print("""
          Gestor de Tareas 
    1. **Agregar una tarea** (Pedir una descripción y agregarla a la lista).
    2. **Ver tareas** (Mostrar todas las tareas con su estado).
    3. **Marcar una tarea como completada** (Actualizar el estado de una tarea por su ID).
    4. **Eliminar una tarea** (Eliminar una tarea por su ID).
    5. **Salir** (Terminar el programa).

    """)

            
    loop_check = "s"

    while loop_check == "s":
        option = input("Seleccione una opción 1, 2, 3 , 4 o 5 ): ").strip()
        if not option.isdigit() or option not in {"1", "2", "3", "4", "5"}:
            print("Opcion no valida. Intente de nuevo: ")
            continue
        option = int(option)

        if option == 1:
            check_option = "s"
            while check_option == "s":
                id = 0
                desciption = str(input("Ingrese la descripción de la tarea: "))
                if not desciption:
                    print("Descripcion de la tarea no validad, porfavor ingrese una valida")
                    
                for i in data:
                    id += 1
                id += 1
                new_task = {"id": id, "description": desciption, "status": "pendiente"}
                add_task(new_task)
                print("Tarea agregada con éxito. :) ")
                
                check_option = str(input("Desea agregar otra tarea s/n: "))
            
            
        if option == 2:
            data = get_data()
            if not data:
                print("No hay tareas registradas.")
            for task in data: 
                id_task = task["id"]
                task_task = task["description"]
                status_task =task["status"]
                print(f"ID: {id_task} | Descripcion: {task_task} | Estado: { status_task}")
                
          
        if option == 3:
            check_option = "s"
            while check_option == "s":
                data = get_data()
                try:
                    id =int(input("Ingrese el ID de la tarea a completar: ")) 
                    update_list_in_db(id)
                except ValueError:
                    print("Ingrese un digito valido")
                
                check_option = str(input("Desea completar otra tarea s/n: "))
                
        if option == 4:
            check_option = "s"
            
            while check_option == "s":
                
                data = get_data()
                try:
                    id = int(input("Ingrese el ID de la tarea a eliminar: "))
                    delete_task(id)
                except ValueError:
                    print("Ingrese un digito valido")
                check_option = str(input("Desea eliminar otra tarea s/n: "))
        if option == 5:
            loop_check = "n" 
            final_check = "n"

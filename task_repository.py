import json
import os

# 📂 Ruta del archivo JSON
FILE_PATH = r'C:\Users\cesar\OneDrive\Python\Proyect_taks_manager\task_data_base.json'

def get_data() -> list:
    if not os.path.exists(FILE_PATH):
        print("El archivo no existe. Se creará uno nuevo con una tarea inicial.")
        new_task = input("Ingrese la descripción de la tarea: ")
        new_data = [{"id": 1, "descripcion": new_task, "estado": "pendiente"}]
        
        with open(FILE_PATH, 'w', encoding='utf-8') as file:
            json.dump(new_data, file, indent=4)
        
        return new_data
    
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error al leer el archivo JSON. Se creará una nueva lista.")
        new_task = input("Ingrese la descripción de la tarea: ")
        new_data = [{"id": 1, "descripcion": new_task, "estado": "pendiente"}]
        
        with open(FILE_PATH, 'w', encoding='utf-8') as file:
            json.dump(new_data, file, indent=4)
        
        return new_data

def mark_task_completed(task_id: int):
    data = get_data()
    
    for task in data:
        if task_id == task["id"]:
            task["estado"] = "completada"
            print("Tarea marcada como completada.")
            
            with open(FILE_PATH, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
            
            return task
    
    print("Tarea no encontrada.")
    return None

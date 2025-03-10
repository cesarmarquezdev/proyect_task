import json
from task_repository import get_data

# 📂 Ruta del archivo JSON
FILE_PATH = r'C:\Users\cesar\OneDrive\Python\Proyect_taks_manager\task_data_base.json'

def add_task(new_task: dict) -> bool:
    if not new_task:
        print("Descripción de la tarea no válida, por favor ingrese una válida.")
        return False
    
    data = get_data()
    data.append(new_task)
    
    try:
        with open(FILE_PATH, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        return True
    except Exception as e:
        print(f"❌ Error al guardar datos: {e}")
        return False

def update_list_in_db(task_id: int) -> bool:
    data = get_data()
    
    for task in data:
        if task["id"] == task_id:
            task["estado"] = "completada"
            print("Tarea marcada como completada.")
            break
    else:
        print("Tarea no encontrada.")
        return False
    
    try:
        with open(FILE_PATH, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        return True
    except Exception as e:
        print(f"❌ Error al guardar datos: {e}")
        return False

def delete_task(task_id: int) -> bool:
    data = get_data()
    
    for task in data:
        if task["id"] == task_id:
            data.remove(task)
            print("Tarea eliminada con éxito.")
            break
    else:
        print("Tarea no encontrada.")
        return False
    
    try:
        with open(FILE_PATH, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        return True
    except Exception as e:
        print(f"❌ Error al guardar datos: {e}")
        return False

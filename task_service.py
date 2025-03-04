import json
from task_repository import get_data

# 📂 Ruta del archivo JSON
FILE_PATH = r'C:\Users\cesar\OneDrive\Python\Proyect_taks_manager\task_data_base.json'

def add_task(new_task) -> bool:
    
    if not new_task:
        print("Descripcion de la tarea no validad, porfavor ingrese una valida")
        return
    data=get_data()
    

    data.append(new_task)
    data_str = json.dumps(data,indent=4)
            
    with open(FILE_PATH, 'w') as file:
        file.write(data_str)

def update_list_in_db(id):
   
    data = get_data()
    

    for i in range(len(data)):
        if data[i]["id"] == id:
            data[i]["status"] = "completada"
            print("Tarea marcada como completada.")
            break
    else:
        print("Tarea no encontrada.")
    

    try:
        with open(FILE_PATH, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
            
        return True
    except Exception as e:
        
        print(f"❌ Error al guardar datos: {e}")
        return False

def delete_task(id):
    data = get_data()
    for task in data:
        if id == task["id"]:
            data.remove(task)
            print("Tarea eliminada con éxito.")
            break
    else:
        print("Tarea no encontrada.")
        
    try:
        with open(FILE_PATH, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
            
        return True
    except Exception as e:
        
        print(f"❌ Error al guardar datos: {e}")
        return False        
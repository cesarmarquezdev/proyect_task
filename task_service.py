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
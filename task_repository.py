import json

# 📂 Ruta del archivo JSON
FILE_PATH = r'C:\Users\cesar\OneDrive\Python\Proyect_taks_manager\task_data_base.json'

def get_data() -> dict:
    """Lee y devuelve los datos del archivo JSON."""
    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)

def get_id( id= int) : 
   
    data = get_data()
  
    for task in data:
        if id == task["id"]:
            task["status"] = "completada"
            result = task["id"]
            print("Tarea marcada como completada.")
            break
    else: 
        print("Tarea no encontrada.")
    return result
            
      
    
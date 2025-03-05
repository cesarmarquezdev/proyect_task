import json
import os

# 📂 Ruta del archivo JSON
FILE_PATH = r'C:\Users\cesar\OneDrive\Python\Proyect_taks_manager\task_data_base.json'


def get_data() -> dict:
    
    if not os.path.exists(FILE_PATH):
        print("El archivo no existe. Se creará uno nuevo con una tarea inicial.")
        new_task = str(input("Imgrese la descripcion a agregar: "))
        new_data = [{"id": 1, "descripcion": "Ejemplo de tarea", "estado": "pendiente"}]
        
        with open(FILE_PATH, 'w', encoding='utf-8') as file:
            file.write(new_data)
        
        return new_data
        
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            return json.load(file)
    except:  # Capturar solo si el archivo no existe
        print("La lista está vacía.")
        print("Agregue una tarea para crear la lista: ")
        
        new_task = str(input("Ingrese la descripción de la tarea: "))
        new_data = [{"id": 1, "descripcion": new_task, "estado": "pendiente"}]
    
        data_str = json.dumps(new_data, indent=4)
                
        with open(FILE_PATH, 'w', encoding='utf-8') as file:
            file.write(data_str)
        
        return new_data 

    


def get_id( id) : 
   
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
            
      
    
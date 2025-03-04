data = [
    {"id": 1, "description": "Hacer la compra", "status": "pendiente"},
    {"id": 2, "description": "Llamar al banco", "status": "completada"},
]
id = 1 
for task in data:
    if id == task["id"]:
        task["status"] = "completada"
        result = id
        break
    else:
        print("Tarea no encontrada.")
print(result) 
print(data)
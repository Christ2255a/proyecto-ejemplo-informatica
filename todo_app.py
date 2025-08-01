# todo_app.py
# Gestor de tareas simple para una lista de tareas.
# Permite agregar tareas, listar tareas y marcar tareas como completadas.
# Las tareas se guardan en un archivo JSON para persistencia.

import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)

def list_tasks(tasks):
    if not tasks:
        print("No hay tareas.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "\u2714" if task.get("completed") else "\u2718"
            print(f"{i}. {task['title']} - {status}")
            print(f"   {task['description']}")

def add_task(tasks):
    title = input("Título de la tarea: ")
    description = input("Descripción de la tarea: ")
    tasks.append({"title": title, "description": description, "completed": False})
    print("Tarea agregada.")

def complete_task(tasks):
    list_tasks(tasks)
    try:
        idx = int(input("Número de tarea a marcar como completada: "))
        if 1 <= idx <= len(tasks):
            tasks[idx - 1]["completed"] = True
            print("Tarea marcada como completada.")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Entrada no válida.")

def main():
    tasks = load_tasks()
    while True:
        print("\nGestor de Tareas")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Marcar tarea como completada")
        print("4. Guardar y salir")
        choice = input("Elige una opción: ")

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Tareas guardadas. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()

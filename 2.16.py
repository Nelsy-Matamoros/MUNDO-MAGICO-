import tkinter as tk
from tkinter import messagebox

# Funciones para la gestión de tareas
def agregar_tarea(event=None):
    tarea = entrada.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada.delete(0, tk.END)

def marcar_completada(event=None):
    try:
        indice = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(indice)
        if not tarea.startswith("✔ "):
            lista_tareas.delete(indice)
            lista_tareas.insert(indice, "✔ " + tarea)
    except IndexError:
        messagebox.showwarning("Error", "Por favor, selecciona una tarea.")

def eliminar_tarea(event=None):
    try:
        indice = lista_tareas.curselection()[0]
        lista_tareas.delete(indice)
    except IndexError:
        messagebox.showwarning("Error", "Por favor, selecciona una tarea.")

def cerrar_aplicacion(event=None):
    ventana.quit()

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Tareas")

# Crear campo de entrada
entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=10)

# Crear lista de tareas
lista_tareas = tk.Listbox(ventana, width=40, height=10)
lista_tareas.pack(pady=10)

# Crear botones
boton_agregar = tk.Button(ventana, text="Agregar Tarea", command=agregar_tarea)
boton_agregar.pack(pady=5)

boton_completar = tk.Button(ventana, text="Marcar Completada", command=marcar_completada)
boton_completar.pack(pady=5)

boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
boton_eliminar.pack(pady=5)

# Asignar atajos de teclado
ventana.bind('<Return>', agregar_tarea)  # Presionar Enter para añadir tarea
ventana.bind('<c>', marcar_completada)   # Presionar 'C' para marcar como completada
ventana.bind('<d>', eliminar_tarea)      # Presionar 'D' para eliminar tarea
ventana.bind('<Delete>', eliminar_tarea) # Presionar tecla Delete para eliminar tarea
ventana.bind('<Escape>', cerrar_aplicacion)  # Presionar Escape para cerrar

# Iniciar la aplicación
ventana.mainloop()

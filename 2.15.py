import tkinter as tk
from tkinter import messagebox


class TaskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # Lista de tareas (Listbox)
        self.task_list = tk.Listbox(root, height=10, width=50, selectmode=tk.SINGLE)
        self.task_list.pack(pady=10)

        # Campo de entrada (Entry)
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)
        self.task_entry.bind("<Return>", self.add_task_event)  # Añadir con Enter

        # Botones
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

    def add_task_event(self, event):
        """Añadir tarea cuando se presiona Enter."""
        self.add_task()

    def add_task(self):
        """Añadir nueva tarea a la lista."""
        task = self.task_entry.get()
        if task != "":
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)  # Limpiar campo de entrada
        else:
            messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")

    def complete_task(self):
        """Marcar tarea seleccionada como completada."""
        try:
            selected_task_index = self.task_list.curselection()[0]
            task = self.task_list.get(selected_task_index)
            self.task_list.delete(selected_task_index)
            self.task_list.insert(selected_task_index, task + " (Completada)")
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para completar.")

    def delete_task(self):
        """Eliminar tarea seleccionada."""
        try:
            selected_task_index = self.task_list.curselection()[0]
            self.task_list.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()

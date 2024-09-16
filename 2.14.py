import tkinter as tk
from tkinter import ttk, messagebox

# Clase para la aplicación de la agenda
class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("500x400")

        # Frame para la visualización de eventos
        self.event_frame = tk.Frame(self.root)
        self.event_frame.pack(pady=10)

        # Lista (TreeView) para mostrar eventos
        self.tree = ttk.Treeview(self.event_frame, columns=("Fecha", "Hora", "Descripción"), show='headings', height=8)
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.column("Fecha", width=100)
        self.tree.column("Hora", width=100)
        self.tree.column("Descripción", width=250)
        self.tree.pack()

        # Barra de desplazamiento para la TreeView
        self.scrollbar = ttk.Scrollbar(self.event_frame, orient="vertical", command=self.tree.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        # Frame para la entrada de datos
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=10)

        # Etiquetas y campos de entrada
        tk.Label(self.input_frame, text="Fecha (DD/MM/YYYY)").grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = tk.Entry(self.input_frame)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.input_frame, text="Hora (HH:MM)").grid(row=1, column=0, padx=5, pady=5)
        self.time_entry = tk.Entry(self.input_frame)
        self.time_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.input_frame, text="Descripción").grid(row=2, column=0, padx=5, pady=5)
        self.desc_entry = tk.Entry(self.input_frame)
        self.desc_entry.grid(row=2, column=1, padx=5, pady=5)

        # Frame para los botones de acción
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        # Botón para agregar evento
        self.add_button = tk.Button(self.button_frame, text="Agregar Evento", command=self.add_event)
        self.add_button.grid(row=0, column=0, padx=10)

        # Botón para eliminar evento seleccionado
        self.del_button = tk.Button(self.button_frame, text="Eliminar Evento Seleccionado", command=self.delete_event)
        self.del_button.grid(row=0, column=1, padx=10)

        # Botón para salir de la aplicación
        self.exit_button = tk.Button(self.button_frame, text="Salir", command=self.root.quit)
        self.exit_button.grid(row=0, column=2, padx=10)

    # Función para agregar un evento
    def add_event(self):
        date = self.date_entry.get()
        time = self.time_entry.get()
        desc = self.desc_entry.get()

        # Validar que los campos no estén vacíos
        if date and time and desc:
            # Validar formato de hora
            try:
                valid_time = time.split(":")
                if len(valid_time) != 2 or not (0 <= int(valid_time[0]) < 24) or not (0 <= int(valid_time[1]) < 60):
                    raise ValueError

                # Insertar el evento en el Treeview
                self.tree.insert('', 'end', values=(date, time, desc))
                self.clear_entries()
            except ValueError:
                messagebox.showerror("Error", "Formato de hora no válido. Usa HH:MM.")
        else:
            messagebox.showwarning("Advertencia", "Todos los campos deben estar llenos")

    # Función para eliminar el evento seleccionado
    def delete_event(self):
        selected_item = self.tree.selection()
        if selected_item:
            confirm = messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar el evento seleccionado?")
            if confirm:
                self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Advertencia", "Selecciona un evento para eliminar")

    # Función para limpiar las entradas
    def clear_entries(self):
        self.date_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

# Inicializar la ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()

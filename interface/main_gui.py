import tkinter as tk
from tkinter import messagebox
from core.persistence import save_data, load_data

class EventPlannerApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x250")
        self.root.resizable(False, False)
        self.root.title("Planificador de Eventos Universitario")
        self.events = []
        self.resources = []
        self.constraints = []
        self.load_data()
        self.create_main_menu()

    def load_data(self):
        self.events, self.resources, self.constraints = load_data()

    def save_data(self):
        save_data(self.events, self.resources, self.constraints)

    def create_main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text="Planificador de Eventos Universitario", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.root, text="Listar Eventos", command=lambda: self.show_list_events()).pack(pady=5)
        tk.Button(self.root, text="Agregar Evento", command=lambda: self.show_add_event_window()).pack(pady=5)
        tk.Button(self.root, text="Eliminar Evento", command=lambda: self.show_delete_event_window()).pack(pady=5)
        tk.Button(self.root, text="Ver Horario de Recurso", command=lambda: self.show_view_resource_schedule()).pack(pady=5)
        tk.Button(self.root, text="Guardar Datos", command=self.save_data).pack(pady=5)

    def show_list_events(self):
        from .list_events import show_list_events_window
        show_list_events_window(self)

    def show_add_event_window(self):
        from .add_event import show_add_event_window
        show_add_event_window(self)

    def show_delete_event_window(self):
        from .delete_event import show_delete_event_window
        show_delete_event_window(self)

    def show_view_resource_schedule(self):
        from .view_schedule import show_view_resource_schedule_window
        show_view_resource_schedule_window(self)

    def show_edit_event_window(self, index):
        from .edit_event import show_edit_event_window
        show_edit_event_window(self, index)
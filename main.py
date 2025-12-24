"""
Planificador de Eventos Universitario - Punto de Entrada Principal

Este script lanza la interfaz gráfica de usuario para la aplicación de planificación de eventos.
"""

import tkinter as tk
from interface.main_gui import EventPlannerApp

if __name__ == "__main__":
    root = tk.Tk()
    app = EventPlannerApp(root)
    root.mainloop()
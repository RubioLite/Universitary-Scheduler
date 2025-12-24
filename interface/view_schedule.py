import tkinter as tk
from tkinter import simpledialog, messagebox

def show_view_resource_schedule_window(app):
    resource_id = simpledialog.askstring("Horarios", "Ingrese ID del recurso:")
    if resource_id:
        res = next((r for r in app.resources if r.id == resource_id), None)
        if not res:
            messagebox.showerror("Error", f"Recurso '{resource_id}' no encontrado.")
            return
        window = tk.Toplevel(app.root)
        window.title(f"Horario para {res.name} ({resource_id})")
        window.resizable(False, False)
        listbox = tk.Listbox(window, width=80, height=20)
        listbox.pack()
        events_for_res = [e for e in app.events if resource_id in e.resources]
        if not events_for_res:
            listbox.insert(tk.END, "No hay eventos programados para este recurso.")
        else:
            for event in sorted(events_for_res, key=lambda e: e.start_time):
                listbox.insert(tk.END, f"{event.name}: {event.start_time.strftime('%Y-%m-%d %H:%M')} - {event.end_time.strftime('%Y-%m-%d %H:%M')}")

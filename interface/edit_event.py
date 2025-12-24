import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import timedelta
from core.scheduler import plan_event, find_next_slot
from core.utils import parse_datetime

def show_edit_event_window(app, index):
    event = app.events[index]
    window = tk.Toplevel(app.root)
    window.resizable(False, False)
    window.title("Editar Evento")
    window.geometry("520x330")
    tk.Label(window, text="Nombre del Evento:").grid(row=0, column=0, padx=5, pady=5)
    name_entry = tk.Entry(window, width=35)
    name_entry.insert(0, event.name)
    name_entry.grid(row=0, column=1, padx=5, pady=5)
    tk.Label(window, text="Hora de Inicio (AAAA-MM-DDTHH:MM):").grid(row=1, column=0, padx=5, pady=5)
    start_entry = tk.Entry(window, width=35)
    start_entry.insert(0, event.start_time.strftime('%Y-%m-%dT%H:%M'))
    start_entry.grid(row=1, column=1, padx=5, pady=5)
    tk.Label(window, text="Hora de Fin (AAAA-MM-DDTHH:MM):").grid(row=2, column=0, padx=5, pady=5)
    end_entry = tk.Entry(window, width=35)
    end_entry.insert(0, event.end_time.strftime('%Y-%m-%dT%H:%M'))
    end_entry.grid(row=2, column=1, padx=5, pady=5)
    tk.Label(window, text="Seleccionar Recursos:").grid(row=3, column=0, padx=5, pady=5)
    resource_listbox = tk.Listbox(window, selectmode=tk.MULTIPLE, height=10, width=35)
    for i, res in enumerate(app.resources):
        resource_listbox.insert(tk.END, f"{res.id}: {res.name}")
        if res.id in event.resources:
            resource_listbox.selection_set(i)
    resource_listbox.grid(row=3, column=1, padx=5, pady=5)

    def edit_event():
        name = name_entry.get().strip()
        if not name:
            messagebox.showerror("Error", "El nombre del evento es requerido.")
            return
        try:
            start = parse_datetime(start_entry.get())
            end = parse_datetime(end_entry.get())
            if start >= end:
                raise ValueError("La hora de inicio debe ser anterior a la hora de fin.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return
        selected = resource_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "Seleccione al menos un recurso.")
            return
        resources = [app.resources[i].id for i in selected]
        # Elimina el evento viejo temporalmente
        old_event = app.events.pop(index)
        success, msg = plan_event(name, start, end, resources, app.events, app.constraints)
        if success:
            app.save_data()
            messagebox.showinfo("Éxito", "Evento editado exitosamente.")
            window.destroy()
            app.create_main_menu()
        else:
            # Regresa el evento a su estado viejo
            app.events.insert(index, old_event)
            messagebox.showerror("Error", msg)

    tk.Button(window, text="Editar Evento", command=edit_event).grid(row=4, column=0, padx=5, pady=5)

    def find_slot():
        duration_str = simpledialog.askstring("Duración", "Ingrese duración en horas (ej. 2.5):")
        if duration_str:
            try:
                hours = float(duration_str)
                if hours <= 0:
                    raise ValueError("La duración debe ser positiva.")
                duration = timedelta(hours=hours)
                selected = resource_listbox.curselection()
                if not selected:
                    messagebox.showerror("Error", "Seleccione recursos primero.")
                    return
                resources = [app.resources[i].id for i in selected]
                # Elimina el evento temporalmente para encontrar un espacio
                temp_event = app.events.pop(index)
                start, end = find_next_slot(duration, resources, app.events, app.constraints)
                app.events.insert(index, temp_event)  # Lo devuelve a su estado anterior
                if start:
                    start_entry.delete(0, tk.END)
                    start_entry.insert(0, start.strftime('%Y-%m-%dT%H:%M'))
                    end_entry.delete(0, tk.END)
                    end_entry.insert(0, end.strftime('%Y-%m-%dT%H:%M'))
                    messagebox.showinfo("Espacio Encontrado", f"Sugerido: {start.strftime('%Y-%m-%d %H:%M')} - {end.strftime('%Y-%m-%d %H:%M')}")
                else:
                    messagebox.showerror("Sin Espacio", "No se encontró espacio disponible dentro de 30 días.")
            except ValueError as e:
                messagebox.showerror("Error", f"Entrada inválida: {e}")

    tk.Button(window, text="Encontrar Próximo Espacio", command=find_slot).grid(row=4, column=1, padx=5, pady=5)
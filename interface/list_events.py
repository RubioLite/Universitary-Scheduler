import tkinter as tk

def show_list_events_window(app):
    window = tk.Toplevel(app.root)
    window.resizable(False, False)
    window.title("Lista de Eventos")
    listbox = tk.Listbox(window, width=80, height=20)
    listbox.pack()
    for event in app.events:
        resources_str = ', '.join(event.resources)
        listbox.insert(tk.END, f"{event.name}: {event.start_time.strftime('%Y-%m-%d %H:%M')} - {event.end_time.strftime('%Y-%m-%d %H:%M')}, Recursos: {resources_str}")
    # Hacer doble click para editar
    listbox.bind('<Double-1>', lambda e: app.show_edit_event_window(listbox.curselection()[0]) if listbox.curselection() else None)
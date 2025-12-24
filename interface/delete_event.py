import tkinter as tk
from tkinter import messagebox

def show_delete_event_window(app):
    window = tk.Toplevel(app.root)
    window.resizable(False, False)
    window.title("Eliminar Evento")
    listbox = tk.Listbox(window, width=80, height=20)
    listbox.pack(padx=10, pady=10)
    for i, event in enumerate(app.events):
        listbox.insert(tk.END, f"{i+1}: {event.name} ({event.start_time.strftime('%Y-%m-%d %H:%M')} - {event.end_time.strftime('%Y-%m-%d %H:%M')})")

    def delete():
        selected = listbox.curselection()
        if selected:
            idx = selected[0]
            event_name = app.events[idx].name
            del app.events[idx]
            app.save_data()
            messagebox.showinfo("Éxito", f"Evento '{event_name}' eliminado.")
            window.destroy()
            app.create_main_menu()
        else:
            messagebox.showerror("Error", "Seleccione un evento para eliminar.")

    tk.Button(window, text="Eliminar Evento Seleccionado", command=delete).pack(pady=5)
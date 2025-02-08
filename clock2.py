import tkinter as tk
import time

def update_time():
    # Obtiene la hora actual en formato HH:MM:SS
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    # Programa la actualización cada 1000 milisegundos (1 segundo)
    root.after(1000, update_time)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Reloj Digital")

# Crea una etiqueta (label) con estilo para mostrar la hora
label = tk.Label(root, font=("Helvetica", 48), fg="black", bg="white")
label.pack(padx=20, pady=20)

# Inicia la actualización del reloj
update_time()

# Inicia el bucle principal de la GUI
root.mainloop()
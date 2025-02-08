# clock2.py
Programa en Python que muestra la hora actual en una ventana.

# Syntax

1. Importar módulos:

    - `import tkinter as tk:` Importa el módulo `tkinter`, que es la biblioteca estándar de Python para interfaces gráficas, y lo renombra a `tk` para simplificar su uso en el código.
    - `import time:` Igual que en el proyecto [clock1.py](https://github.com/mgdApp/clock1.py), se importa el módulo `time` para trabajar con la hora actual.

2. Definición para mostrar la hora:

```
def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    root.after(1000, update_time)
```

- `current_time = time.strftime("%H:%M:%S")`: Obtiene la hora actual en formato 24 horas.
- `label.config(text=current_time)`: Actualiza la propiedad `text` del widget `label` con el valor de `current_time`. Es decir, actualiza el contenido de la ventana con la hora actual.
- `root.after(1000, update_time)`: Programa la llamada a la función `update_time` después de 1000 milisegundos (1 segundo).

    - La función (o método) `after` de Tkinter recibe 2 parámetros: el primero es el tiempo en milisegundos y el segundo es la función a ejecutar.
    - Esto crea un ciclo que se ejecuta cada segundo sin utilizar `while True`.

3. Crear la ventana:

    - `root = tk.Tk()`: Crea la ventana principal del programa. La variable `root` representa la raíz de la interfaz gráfica.
    - `root.title("Reloj Digital")`: Coloca el título en la barra superior de la ventana.

4. Añadir el contenido:

    - `label = tk.Label(root, font=("Helvetica", 48), fg="black", bg="white")`: Crea un widget de tipo `Label` (etiqueta) que será hijo de la ventana `root`.

        - `font=("Helvetica", 48)`: Se especifica la fuente Helvetica y el tamaño del texto 48.
        - `fg="black"`: Define el color del texto (foreground) en negro.
        - `bg="white"`: Define el color de fondo de la etiqueta en blanco.

    - `label.pack(padx=20, pady=20)`: El método `pack` es un gestor de posicionamiento del widget. En este caso, agregan un relleno (padding) horizontal y vertical de 20 píxeles alrededor del widget para evitar que este completamente pegado al borde de la ventana.

5. Muestra la hora:

    - `update_time()`: Se llama a la función `update_time` para mostrar la hora actualizada.
    - `root.mainloop()`: Inicia el bucle principal de eventos de Tkinter.

        - Este bucle es el que mantiene la ventana abierta y la espera de eventos (como clics, actualizaciones, etc).
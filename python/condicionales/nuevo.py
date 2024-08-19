import tkinter as tk

def crear_gradiente(canvas, ancho, alto, color1, color2):
    # Dividir la altura del canvas en pasos para el gradiente
    pasos = 100
    for i in range(pasos):
        # Calcular la proporción de la mezcla de colores
        proporción = i / pasos
        r = int(color1[0] * (1 - proporción) + color2[0] * proporción)
        g = int(color1[1] * (1 - proporción) + color2[1] * proporción)
        b = int(color1[2] * (1 - proporción) + color2[2] * proporción)
        color = f'#{r:02x}{g:02x}{b:02x}'
        
        # Dibujar una línea horizontal con el color calculado
        canvas.create_line(0, i * (alto / pasos), ancho, i * (alto / pasos), fill=color)

# Convertir colores hexadecimales a tuplas de RGB
def hex_a_rgb(hex):
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

# Crear la ventana principal
root = tk.Tk()
root.title("Ventana con Fondo Gradiente")

# Crear un canvas con el mismo tamaño que la ventana
ancho = 400
alto = 400
canvas = tk.Canvas(root, width=ancho, height=alto)
canvas.pack(fill="both", expand=True)

# Definir los colores del gradiente (en formato hexadecimal)
color1 = hex_a_rgb('ff0000')  # Rojo
color2 = hex_a_rgb('0000ff')  # Azul

# Crear el gradiente en el canvas
crear_gradiente(canvas, ancho, alto, color1, color2)

# Ejecutar el bucle principal de Tkinter
root.mainloop()

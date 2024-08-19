"""Para tributar un determinado impuesto se debe ser mayor de 18 años y tener unos ingresos iguales o superiores
a “1.500.000” mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales
y muestre por pantalla si el usuario tiene que tributar o no."""


import tkinter as tk
from tkinter import messagebox



def solicitar_datos_usuario():
    """Solicita el nombre, la edad y los ingresos mensuales del usuario a través de una interfaz gráfica."""
    
    def on_submit():
        nombre = entry_nombre.get()
        try:
            edad = int(entry_edad.get())
            ingresos = float(entry_ingresos.get())
            if edad < 0 or ingresos < 0:
                raise ValueError("Los valores no pueden ser negativos.")
            debe_tributar = verificar_si_debe_tributar(edad, ingresos)
            mostrar_resultado(nombre, edad, ingresos, debe_tributar)
        except ValueError:
            #usamos messagebox por si hay algun error me genere una ventana que diga lo siguiente
            messagebox.showerror("Error", "Entrada no válida. Por favor, ingrese números correctos.")
    
    #cambiamos el nombre de la biblioteca a (entrada_de_texto)
    entrada_de_texto = tk.Tk()
    #cambiamos el nombre de la ventana que creamos
    entrada_de_texto.title("Verificación de Tributación")
    #le damos un ancho y un alto
    entrada_de_texto.geometry("600x200")
    #entrada_de_texto.iconbitmap("x.ico")
    
    entrada_de_texto.configure(background="lightgray")
    
        
    #creamos la etiqueta que nos permite saber que debo ingresar en cada entrada de texto
    tk.Label(entrada_de_texto, text="Nombre:", background="black", fg="white", font=("Arial",15)).grid(row=0)
    tk.Label(entrada_de_texto, text="Edad:",background="black", fg="white", font=("Arial",15)).grid(row=1)
    tk.Label(entrada_de_texto, text="Ingresos Mensuales (COP):",background="black", fg="white", font=("Arial",15)).grid(row=2)
    
    
    
    #creamos las entradas de texto donde el usuario ingresara sus datos
    entry_nombre = tk.Entry(entrada_de_texto, font="Helvetica 20", background="lightblue")
    entry_edad = tk.Entry(entrada_de_texto, font="Helvetica 20",background="lightblue")
    entry_ingresos = tk.Entry(entrada_de_texto, font="Helvetica 20",background="lightblue")
    
    
    #y con grid la ubicamos en la ventana
    entry_nombre.grid(row=0, column=1)
    entry_edad.grid(row=1, column=1)
    entry_ingresos.grid(row=2, column=1)
    
    
    #creamos el boton enviar que es el que se presiona al terminar de ingresar los datos
    submit_button = tk.Button(entrada_de_texto, text="Enviar",background="black", fg="white", command=on_submit, font=("Arial",20))
    submit_button.grid(row=4, columnspan=2)
    
    entrada_de_texto.mainloop()

def verificar_si_debe_tributar(edad, ingresos):
    """Verifica si el usuario debe tributar basándose en su edad e ingresos."""
    LIMITE_DE_EDAD = 18
    LIMITE_DE_INGRESOS = 1500000
    
    return edad >= LIMITE_DE_EDAD and ingresos >= LIMITE_DE_INGRESOS

def mostrar_resultado(nombre, edad, ingresos, debe_tributar):
    """Muestra el resultado de si el usuario debe tributar o no, incluyendo su nombre, edad e ingresos."""
    if debe_tributar:
        mensaje = f"{nombre}, con {edad} años y ingresos de {ingresos} pesos, debe tributar."
    else:
        mensaje = f"{nombre}, con {edad} años y ingresos de {ingresos} pesos, no debe tributar."
    #usamos de nuevo messagebox para que genere una ventana que muestre el (mensaje) de arriba
    messagebox.showinfo("Resultado", mensaje)

def main():
    """Función principal del programa."""
    solicitar_datos_usuario()

if __name__ == "__main__":
    main()

from tkinter import *
from tkinter import messagebox
from logica import Creador

color = "#00509D"
amarillo = "#FFFF00"


creador = Creador()

def mostrar_contraseña():
    try:
        longitud = int(entry_longitud.get())
        contraseña = creador.contraRandom(longitud)
        label_contraseña.config(text=contraseña)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número válido para la longitud.")

def copiar_contraseña(event):
    texto = label_contraseña.cget("text")  # Obtener el texto del Label
    if texto:  # Verificar que no esté vacío
        raiz.clipboard_clear()  # Limpiar el portapapeles
        raiz.clipboard_append(texto)  # Copiar el texto al portapapeles
        raiz.update()  # Actualizar el portapapeles
        messagebox.showinfo("Copiado", f"Contraseña copiada: {texto}")
    else:
        messagebox.showwarning("Advertencia", "No hay contraseña para copiar.")

# CREACION DE LA VENTANA
raiz = Tk()  # Instancia del objeto
raiz.title("Titulo pagina")  # Titulo de la ventana
raiz.iconbitmap("ola.ico")  # Icono de la ventana
raiz.config(bg=color)  # Color de fondo

# CREACION DEL FRAME
miFrame = Frame(raiz, bg=amarillo, width=650, height=550, pady=10, border=20)
miFrame.pack(fill="y", expand=True)

# CREACION DE UN LABEL
Label(miFrame, text="Generador de contraseñas aleatorio", fg="black", bg=amarillo, font=("Verdana", 20)).place(x=60, y=30)  # TITULO
Label(miFrame, text="Escoja la longitud de su contraseña", fg="black", bg=amarillo, font=("Verdana", 10)).place(x=30, y=120)  # TEXTO PIDIENDO CONTRASEÑA

# Caja de texto para ingresar la longitud
entry_longitud = Entry(miFrame)
entry_longitud.place(x=300, y=120)

# Botón para generar la contraseña
boton = Button(miFrame, text="Generar", command=mostrar_contraseña)
boton.place(x=450, y=120)

# Label para mostrar el resultado de la contraseña
Label(miFrame, text="Aquí está su contraseña", fg="black", bg=amarillo, font=("Verdana", 10)).place(x=30, y=240)
label_contraseña = Label(miFrame, text="", bg=amarillo, font=("Verdana", 10), fg="blue", cursor="hand2")
label_contraseña.place(x=200, y=240)

# Asociar el evento de clic para copiar la contraseña
label_contraseña.bind("<Button-1>", copiar_contraseña)

# Ejecutar la aplicación
raiz.mainloop()

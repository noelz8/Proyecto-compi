import tkinter as tk
from tkinter import scrolledtext
from tkinter import font
from tkinter import filedialog


#Valores fijos
# Crear botones con el mismo tamaño
ancho_boton = 10  # Ancho fijo para los botones
altura_boton = 2  # Altura fija para los botones
boton_estilo = {"relief": "solid", "borderwidth": 2}


# Crear la ventana principal
ventana = tk.Tk()
# Configurar propiedades de la ventana
ventana.title("Visual Studio IDE")
ventana.geometry("800x600")




# Función para cerrar la ventana
def cerrar_ventana():
    ventana.destroy()

# Función para compilar el archivo
def compileCode():
    print("Se compiló correctamente el codigo")

# Función para cargar el archivo
def cargarArchivo():
    archivo = filedialog.askopenfile(filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
    if archivo is not None:
        contenido = archivo.read()
        editor.delete(1.0, tk.END)
        editor.insert(tk.INSERT, contenido)
        archivo.close()



# Crear un widget de texto para el código
editor = scrolledtext.ScrolledText(ventana, width=80, height=25, wrap=tk.WORD)
editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
#Agregar de fuente al texto (editor)
fuente = font.Font(family = "Inconsolata", size =11)
editor.configure(font = fuente)
#Agregar fuente a los botones
fuente_boton = font.Font(family="Segoe UI", size=9, weight="bold")



# Crear boton para cerrar la ventana del IDE
boton_cerrar = tk.Button(ventana, text="Close", command=cerrar_ventana,font = fuente_boton,width=ancho_boton,height=altura_boton,**boton_estilo)
boton_cerrar.pack()
#Crear boton para compilar archivo
boton_compilar = tk.Button(ventana, text="Compile", command=compileCode,font = fuente_boton,width=ancho_boton,height=altura_boton,**boton_estilo)
boton_compilar.pack()
#Crear boton para cargar archivo
boton_compilar = tk.Button(ventana, text="Load File", command=cargarArchivo,font = fuente_boton,width=ancho_boton,height=altura_boton,**boton_estilo)
boton_compilar.pack()



# Bucle principal
ventana.mainloop()

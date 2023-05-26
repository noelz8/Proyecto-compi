import tkinter as tk
from tkinter import scrolledtext
from tkinter import font
from tkinter import filedialog, messagebox
import subprocess
import sys


#Valores fijos
# Crear botones con el mismo tamaño
ancho_boton = 10  # Ancho fijo para los botones
altura_boton = 2  # Altura fija para los botones
boton_estilo = {"relief": "solid", "borderwidth": 1}


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
    codigo = editor.get("1.0", tk.END)
    
    # Crear un widget de texto para mostrar la salida de compilación
    texto_consola = scrolledtext.ScrolledText(contenedor, width=80, height=10, wrap=tk.WORD)
    texto_consola.pack(side = tk.BOTTOM,fill=tk.BOTH, expand=True)
    
    # Redirigir la salida estándar al widget de texto
    sys.stdout = sys.stderr = ConsolaRedireccionada(texto_consola)
    
    # Aquí debes realizar el proceso de compilación adecuado para el lenguaje de programación específico
    # En este ejemplo, usaremos un comando genérico para simular la compilación en Python
    try:
        resultado = subprocess.check_output(["python", "-c", codigo], universal_newlines=True)
        print("El código se compiló correctamente.\n\nResultado:\n" + resultado)
    except subprocess.CalledProcessError as e:
        print("Ocurrió un error al compilar el código:\n" + e.output)

# Clase personalizada para redirigir la salida estándar al widget de texto
class ConsolaRedireccionada:
    def __init__(self, widget):
        self.widget = widget

    def write(self, message):
        self.widget.insert(tk.END, message)

    def flush(self):
        pass

# Crear un contenedor para organizar los elementos
contenedor = tk.Frame(ventana)
contenedor.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

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

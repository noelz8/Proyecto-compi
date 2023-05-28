import tkinter as tk
from tkinter import scrolledtext
from tkinter import font
from tkinter import filedialog
import subprocess
import sys

#Variables Globales
archivo_actual = ""



# Crear la ventana principal
ventana = tk.Tk()
# Configurar propiedades de la ventana
ventana.title("Visual Studio Braille Read")
ventana.geometry("800x500")

# Función para cerrar la ventana
def cerrar_ventana():
    ventana.destroy()


def compilar_codigo():
    codigo = editor.get("1.0", tk.END)
    
    # Clear the existing text in the console widget
    texto_consola.delete('1.0', tk.END)
    
    # Redirigir la salida estándar al widget de texto
    sys.stdout = sys.stderr = ConsolaRedireccionada(texto_consola)
    
    # Aquí debes realizar el proceso de compilación adecuado para el lenguaje de programación específico
    # En este ejemplo, usaremos un comando genérico para simular la compilación en Python
    try:
        resultado = subprocess.check_output(["python", "-c", codigo], universal_newlines=True)
        print("El código se compiló correctamente.\n" + resultado)
    except subprocess.CalledProcessError as e:
        print("Ocurrió un error al compilar el código:")
        print("e.output:", e.output)
        print("e.stderr:", e.stderr)


# Clase personalizada para redirigir la salida estándar al widget de texto
class ConsolaRedireccionada:
    def __init__(self, widget):
        self.widget = widget

    def write(self, message):
        self.widget.insert(tk.END, message)

    def flush(self):
        pass

# Crear un contenedor para organizar los elementos del resultado de la compilacion
contenedor = tk.Frame(ventana)
contenedor.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

# Crear un widget para que muestre resultados de la compilación
texto_consola = scrolledtext.ScrolledText(contenedor, width=80, height=10, wrap=tk.WORD)
texto_consola.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
fuenteTerminal = font.Font(family = "Inconsolata", size =10,weight="bold")
texto_consola.config(background="#535353",font=fuenteTerminal,foreground="#ffffff")



# Funciones realacionadas con el manejo de archivos

# Función para cargar el archivo
def cargarArchivo():
    archivo = filedialog.askopenfile(filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
    if archivo is not None:
        contenido = archivo.read()
        editor.delete(1.0, tk.END)
        editor.insert(tk.INSERT, contenido)
        archivo.close()

# Funcion para guardar cambios en un archivo ya existente
def guardar():
    global archivo_actual
    contenido = editor.get("1.0", tk.END)
    if archivo_actual:
        with open(archivo_actual, "w") as archivo:
            archivo.write(contenido)
        print("Archivo guardado correctamente.")
    else:
        guardar_como()


# Función para guardar el contenido en un archivo seleccionado por el usuario
def guardar_como():
    global archivo_actual
    contenido = editor.get("1.0", tk.END)
    archivo = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if archivo:
        archivo.write(contenido)
        archivo_actual = archivo.name
        archivo.close()
        print("Archivo guardado correctamente.")





# Crear un widget de texto para el código (editor)
editor = scrolledtext.ScrolledText(ventana, width=80, height=25, wrap=tk.WORD)
editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
fuente = font.Font(family = "Inconsolata", size =11)
#Agregar de fuente al texto (editor)
editor.configure(font = fuente)




# Crear una barra de menú principal
menuBar = tk.Menu(ventana)

# Crear barra de menú para archivo
menu_archivo = tk.Menu(menuBar,tearoff=0)
menu_archivo.add_command(label="Abrir", command=cargarArchivo)
menu_archivo.add_command(label="Guardar", command=guardar)
menu_archivo.add_command(label="Guardar como", command=guardar_como)
menu_archivo.add_command(label="Salir", command=cerrar_ventana)
menuBar.add_cascade(label = "Archivo",menu=menu_archivo)

# Crear una barra menú para compilar 
menu_run = tk.Menu(menuBar,tearoff=0)
menu_run.add_command(label="Compilar")
menu_run.add_command(label="Ejecutar", command=compilar_codigo)
menuBar.add_cascade(label = "Run",menu=menu_run)

# Añade el menuBar a la ventana
ventana.config(menu=menuBar)

# Bucle principal
ventana.mainloop()

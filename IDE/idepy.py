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
    
    # Elimina elementos en la consola widget
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
texto_consola = scrolledtext.ScrolledText(contenedor, width=80, height=10, wrap=tk.WORD,relief=tk.FLAT)
texto_consola.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
# Fuente de la terminal y colores de la terminal
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

# Función para agregar líneas de código
def agregar_linea_codigo(event):
    contenido = editor.get("1.0", tk.END)
    lineas_codigo = contenido.count('\n')
    lineasCodigoTexto.delete(1.0, tk.END)
    for i in range(1, lineas_codigo + 1):
        lineasCodigoTexto.insert(tk.END, str(i) + "\n")
    editor.yview_moveto(1.0)
    lineasCodigoTexto.yview_moveto(1.0)

# Funcion para mover dos elementos al mismo tiempo (tk.Text) en el frame Codigo Contenedor
def movimientoSincronizadoScrollText(*args):
    editor.yview(*args)
    lineasCodigoTexto.yview(*args)
    


# Crear un contenedor para las líneas de código
CodigoContenedor = tk.Frame(ventana)
CodigoContenedor.pack(side=tk.LEFT, fill=tk.Y)

# Crear un barra de navegacion
texto_scroll = tk.Scrollbar(CodigoContenedor)
texto_scroll.pack(side=tk.RIGHT,fill=tk.Y)

# Crear un widget de texto para el código (editor)
editor = tk.Text(CodigoContenedor, width=92, height=25, wrap=tk.WORD,relief=tk.FLAT,yscrollcommand=texto_scroll.set)
editor.pack(side=tk.RIGHT, fill=tk.Y)
fuente = font.Font(family = "Inconsolata", size =11)
#Agregar de fuente al texto (editor)
editor.configure(font = fuente)

# Crear un widget de texto para las líneas de código
lineasCodigoTexto = tk.Text(CodigoContenedor, width=4, height=25, bg="lightgray", relief=tk.FLAT,yscrollcommand=texto_scroll.set)
lineasCodigoTexto.pack(side=tk.LEFT, fill=tk.Y)
#Agregar de fuente al texto (lineasCodigoTexto)
lineasCodigoTexto.configure(font= fuente)
texto_scroll.config(command=movimientoSincronizadoScrollText)


# Al presionar una tecla añade las lineas de codigo
editor.bind("<KeyPress>", agregar_linea_codigo)


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

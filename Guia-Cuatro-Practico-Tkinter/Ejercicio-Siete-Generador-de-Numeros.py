"""""
Ejercicio 7 - Generador de números

Escribir una aplicación GUI (llamada Generador de números). Su
función será: al pulsar el botón Generar, generará un número
aleatorio en el rango de los dos Spin Box.
La aplicación lleva:
1 - 3 Etiquetas (Número 1, Número 2 y Número Generado)
2 - 2 Spin Box
3 - 1 lineEdit que no pueda ser modificado
4 - 1 Botón "Generar"
"""""

import tkinter as tk
from tkinter import Spinbox
import random

class GeneradorNumerosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de números")
        self.root.configure(bg='#69002C') 
        
        self.label1 = tk.Label(root, text="Número 1", bg='#69002C', fg='white')
        self.label1.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        
        self.spinbox1 = Spinbox(root, from_=0, to=100)
        self.spinbox1.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
        
        self.label2 = tk.Label(root, text="Número 2", bg='#69002C', fg='white')
        self.label2.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        
        self.spinbox2 = Spinbox(root, from_=0, to=100)
        self.spinbox2.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
        
        self.label3 = tk.Label(root, text="Número Generado", bg='#69002C', fg='white')
        self.label3.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        
        self.numero_generado = tk.Entry(root, justify='center', state='readonly')
        self.numero_generado.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)
        
        self.generar_button = tk.Button(root, text="Generar", command=self.generar_numero)
        self.generar_button.grid(row=3, column=0, columnspan=2, pady=10)
    
    def generar_numero(self):
        numero1 = int(self.spinbox1.get())
        numero2 = int(self.spinbox2.get())
        if numero1 > numero2:
            numero1, numero2 = numero2, numero1
        numero_generado = random.randint(numero1, numero2)
        self.mostrar_numero_generado(numero_generado)
    
    def mostrar_numero_generado(self, numero):
        self.numero_generado.config(state='normal')
        self.numero_generado.delete(0, tk.END)
        self.numero_generado.insert(0, str(numero))
        self.numero_generado.config(state='readonly')

root = tk.Tk()
app = GeneradorNumerosApp(root)
root.mainloop()


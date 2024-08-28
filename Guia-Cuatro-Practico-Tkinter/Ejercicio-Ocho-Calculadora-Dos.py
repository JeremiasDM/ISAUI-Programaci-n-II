"""""
Ejercicio 8 - Calculadora 2.

Escribir una aplicación GUI (llamada Calculadora 2) como la que se ve
en la figura y que funcione como una calculadora.

La aplicación lleva:
1 - 4 Etiquetas (Valor 1, Valor 2, Resultado y Operaciones)
2 - 4 radioButton (Sumar, Restar, Multiplicar y Dividir)
3 - 3 lineEdit (el lineEdit Resultado no puede ser modificado)
4 - 1 botón Calcular, que al ser presionado realice la operación
correspondiente.
"""""

import tkinter as tk
from tkinter import messagebox

class Calculadora2App:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora 2")
        self.root.configure(bg='#69002C') 
        
        self.label1 = tk.Label(root, text="Valor 1", bg='#69002C', fg='white')
        self.label1.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        
        self.valor1_entry = tk.Entry(root)
        self.valor1_entry.grid(row=0, column=1, padx=10, pady=5)
        
        self.label2 = tk.Label(root, text="Valor 2", bg='#69002C', fg='white')
        self.label2.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        
        self.valor2_entry = tk.Entry(root)
        self.valor2_entry.grid(row=1, column=1, padx=10, pady=5)
        
        self.label3 = tk.Label(root, text="Operaciones", bg='#69002C', fg='white')
        self.label3.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        
        self.operacion = tk.StringVar(value="Sumar")
        
        self.sumar_rb = tk.Radiobutton(root, text="Sumar", variable=self.operacion, value="Sumar", bg='#69002C', fg='white', selectcolor='#69002C')
        self.sumar_rb.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        
        self.restar_rb = tk.Radiobutton(root, text="Restar", variable=self.operacion, value="Restar", bg='#69002C', fg='white', selectcolor='#69002C')
        self.restar_rb.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
        
        self.multiplicar_rb = tk.Radiobutton(root, text="Multiplicar", variable=self.operacion, value="Multiplicar", bg='#69002C', fg='white', selectcolor='#69002C')
        self.multiplicar_rb.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
        
        self.dividir_rb = tk.Radiobutton(root, text="Dividir", variable=self.operacion, value="Dividir", bg='#69002C', fg='white', selectcolor='#69002C')
        self.dividir_rb.grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)
        
        self.label4 = tk.Label(root, text="Resultado", bg='#69002C', fg='white')
        self.label4.grid(row=7, column=0, padx=10, pady=5, sticky=tk.W)
        
        self.resultado_entry = tk.Entry(root, state='readonly')
        self.resultado_entry.grid(row=7, column=1, padx=10, pady=5)
        
        self.calcular_button = tk.Button(root, text="Calcular", command=self.calcular)
        self.calcular_button.grid(row=8, column=0, columnspan=2, pady=10)
    
    def calcular(self):
        try:
            valor1 = float(self.valor1_entry.get())
            valor2 = float(self.valor2_entry.get())
            operacion = self.operacion.get()

            if operacion == "Sumar":
                resultado = valor1 + valor2
            elif operacion == "Restar":
                resultado = valor1 - valor2
            elif operacion == "Multiplicar":
                resultado = valor1 * valor2
            elif operacion == "Dividir":
                if valor2 != 0:
                    resultado = valor1 / valor2
                else:
                    messagebox.showerror("Error", "No se puede dividir por cero.")
                    return
            self.mostrar_resultado(resultado)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa números válidos.")
    
    def mostrar_resultado(self, resultado):
        self.resultado_entry.config(state='normal')
        self.resultado_entry.delete(0, tk.END)
        self.resultado_entry.insert(0, str(resultado))
        self.resultado_entry.config(state='readonly')

root = tk.Tk()
app = Calculadora2App(root)
root.mainloop()


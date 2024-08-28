"""""
Ejercicio 5 - Calculadora

Escribir una aplicación GUI (llamada Calculadora) que funcione como
una simple calculadora.

La aplicación lleva:
1 - Tres etiquetas (Primer número, Segundo número y Resultado)
2 - 3 lineEdit (el lineEdit de Resultado no se puede modificar)
3 - 6 Botones (+, -, *, /, % y RESET). El botón CLEAR debe borrar los
3 lineEdit. Al presionar (+, -, *, / o %) el único campo que se modifica
es Resultado.
"""""

import tkinter as tk
from tkinter import messagebox

class CalculadoraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.configure(bg='#69002C') 
        
        self.label1 = tk.Label(root, text="Primer número", bg='#69002C', fg='white')
        self.label1.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.primer_numero = tk.Entry(root)
        self.primer_numero.grid(row=0, column=1, padx=10, pady=5)

        self.label2 = tk.Label(root, text="Segundo número", bg='#69002C', fg='white')
        self.label2.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.segundo_numero = tk.Entry(root)
        self.segundo_numero.grid(row=1, column=1, padx=10, pady=5)

        self.label3 = tk.Label(root, text="Resultado", bg='#69002C', fg='white')
        self.label3.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.resultado = tk.Entry(root, state='readonly')
        self.resultado.grid(row=2, column=1, padx=10, pady=5)

        self.boton_frame = tk.Frame(root, bg='#69002C')
        self.boton_frame.grid(row=3, column=0, columnspan=2, pady=10, padx=10)

        self.boton_sumar = tk.Button(self.boton_frame, text="+", command=self.sumar)
        self.boton_sumar.grid(row=0, column=0, padx=5, pady=5)

        self.boton_restar = tk.Button(self.boton_frame, text="-", command=self.restar)
        self.boton_restar.grid(row=0, column=1, padx=5, pady=5)

        self.boton_multiplicar = tk.Button(self.boton_frame, text="*", command=self.multiplicar)
        self.boton_multiplicar.grid(row=0, column=2, padx=5, pady=5)

        self.boton_dividir = tk.Button(self.boton_frame, text="/", command=self.dividir)
        self.boton_dividir.grid(row=0, column=3, padx=5, pady=5)

        self.boton_modulo = tk.Button(self.boton_frame, text="%", command=self.modulo)
        self.boton_modulo.grid(row=0, column=4, padx=5, pady=5)

        self.boton_reset = tk.Button(self.boton_frame, text="RESET", command=self.resetear)
        self.boton_reset.grid(row=0, column=5, padx=5, pady=5)

    def obtener_numeros(self):
        try:
            numero1 = float(self.primer_numero.get())
            numero2 = float(self.segundo_numero.get())
            return numero1, numero2
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa números válidos.")
            return None, None
    
    def sumar(self):
        numero1, numero2 = self.obtener_numeros()
        if numero1 is not None and numero2 is not None:
            resultado = numero1 + numero2
            self.mostrar_resultado(resultado)

    def restar(self):
        numero1, numero2 = self.obtener_numeros()
        if numero1 is not None and numero2 is not None:
            resultado = numero1 - numero2
            self.mostrar_resultado(resultado)

    def multiplicar(self):
        numero1, numero2 = self.obtener_numeros()
        if numero1 is not None and numero2 is not None:
            resultado = numero1 * numero2
            self.mostrar_resultado(resultado)

    def dividir(self):
        numero1, numero2 = self.obtener_numeros()
        if numero1 is not None and numero2 is not None:
            if numero2 != 0:
                resultado = numero1 / numero2
                self.mostrar_resultado(resultado)
            else:
                messagebox.showerror("Error", "No se puede dividir por cero.")
    
    def modulo(self):
        numero1, numero2 = self.obtener_numeros()
        if numero1 is not None and numero2 is not None:
            if numero2 != 0:
                resultado = numero1 % numero2
                self.mostrar_resultado(resultado)
            else:
                messagebox.showerror("Error", "No se puede dividir por cero.")
    
    def mostrar_resultado(self, resultado):
        self.resultado.config(state='normal')
        self.resultado.delete(0, tk.END)
        self.resultado.insert(0, str(resultado))
        self.resultado.config(state='readonly')
    
    def resetear(self):
        self.primer_numero.delete(0, tk.END)
        self.segundo_numero.delete(0, tk.END)
        self.resultado.config(state='normal')
        self.resultado.delete(0, tk.END)
        self.resultado.config(state='readonly')

root = tk.Tk()
app = CalculadoraApp(root)
root.mainloop()



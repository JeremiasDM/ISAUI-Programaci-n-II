"""""
 Ejercicio 1.3 – Factorial.

Escribir una aplicación GUI (llamada Factorial) como la que se ve en
la figura. Cada ves que se haga clic en el botón "Siguiente", debe
calcular el factorial del primer lineEdit y mostrarlo en el segundo. Al
dar siguiente (n se incrementa en 1) n = 2 con su factorial
correspondiente.

Formula de factorial .
Factorial de 5 = 1 x 2 x 3 x 4 x 5 = 120
Factorial de 3 = 1 x 2 x 3 = 6
La aplicación lleva:
1 - Dos etiquetas: una para n y otra para Factorial (n)
2 - Dos lineEdit no editables
3 - Un botón siguiente
"""""

import tkinter as tk
from math import factorial

class FactorialApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Factorial")
        self.root.configure(bg='#69002C')
        
        self.n = 1
        
        self.label_n = tk.Label(root, text="n", bg='#69002C', fg='white')
        self.label_n.grid(row=0, column=0, padx=10, pady=10)
        
        self.n_display = tk.Entry(root, justify='center')
        self.n_display.grid(row=0, column=1, padx=10, pady=10)
        self.n_display.insert(0, str(self.n))
        self.n_display.config(state='readonly')
        
        self.label_factorial = tk.Label(root, text="Factorial (n)", bg='#69002C', fg='white')
        self.label_factorial.grid(row=1, column=0, padx=10, pady=10)
        
        self.factorial_display = tk.Entry(root, justify='center')
        self.factorial_display.grid(row=1, column=1, padx=10, pady=10)
        self.factorial_display.insert(0, str(factorial(self.n)))
        self.factorial_display.config(state='readonly')
        
        self.button = tk.Button(root, text="Siguiente", command=self.calcular_factorial)
        self.button.grid(row=2, column=0, columnspan=2, pady=10)
    
    def calcular_factorial(self):
        self.n += 1
        self.n_display.config(state='normal')
        self.n_display.delete(0, tk.END)
        self.n_display.insert(0, str(self.n))
        self.n_display.config(state='readonly')
        
        fact_n = factorial(self.n)
        
        self.factorial_display.config(state='normal')
        self.factorial_display.delete(0, tk.END)
        self.factorial_display.insert(0, str(fact_n))
        self.factorial_display.config(state='readonly')

root = tk.Tk()
app = FactorialApp(root)
root.mainloop()


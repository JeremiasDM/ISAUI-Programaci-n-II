""""
Ejercicio 1 - Contador Creciente.

Escribir una aplicación GUI (llamada ContCreciente) como la que se
ve en la figura. Cada vez que se haga clic en el botón "+", el valor del
contador se incrementa en 1.

El programa lleva 3 componentes:
1 - Una Etiqueta "Contador"
2 - Un lineEdit no editable, que muestre el valor del contador
3 - Un Botón "+"
"""""

import tkinter as tk

class ContCreciente:
    def __init__(self, root):
        self.root = root
        self.root.title("Contador Creciente")
        self.root.configure(bg='#69002C')  
        
        self.contador = 0
        
        self.label = tk.Label(root, text="Contador", bg='#69002C', fg='white')
        self.label.grid(row=0, column=0, columnspan=2, pady=10)
        
        self.counter_display = tk.Entry(root, justify='center', state='readonly')
        self.counter_display.grid(row=1, column=0, columnspan=2, pady=10)
        self.counter_display.insert(0, str(self.contador))
        
        self.button = tk.Button(root, text="+", command=self.incrementar_contador)
        self.button.grid(row=2, column=0, columnspan=2, pady=10)
    
    def incrementar_contador(self):
        self.contador += 1

        self.counter_display.config(state='normal')
        self.counter_display.delete(0, tk.END)
        self.counter_display.insert(0, str(self.contador))
        self.counter_display.config(state='readonly')

root = tk.Tk()
app = ContCreciente(root)
root.mainloop()

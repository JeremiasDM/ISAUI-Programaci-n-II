""""
Ejercicio 2 - Contador Decreciente.

Escribir una aplicación GUI (llamada ContDecreciente) como la que se
ve en la figura. Cada ves que se haga clic en el botón "-", al valor de
contador se le resta 1.

El programa lleva 3 componentes:
1 - Una Etiqueta "Contador"
2 - Un lineEdit no editable, que muestre el valor de contador y que
inicie con el número 88
3 - Un Botón "-"
"""""

import tkinter as tk

class ContDecreciente:
    def __init__(self, root):
        self.root = root
        self.root.title("Contador Decreciente")
        self.root.configure(bg='#69002C')
        
        self.contador = 88
        
        self.label = tk.Label(root, text="Contador", bg='#69002C', fg='white')
        self.label.grid(row=0, column=0, columnspan=2, pady=10)
        
        self.counter_display = tk.Entry(root, justify='center')
        self.counter_display.grid(row=1, column=0, columnspan=2, pady=10)
        self.counter_display.insert(0, str(self.contador))
        self.counter_display.config(state='readonly')
        
        self.button = tk.Button(root, text="-", command=self.decrementar_contador)
        self.button.grid(row=2, column=0, columnspan=2, pady=10)
    
    def decrementar_contador(self):
        self.contador -= 1

        self.counter_display.config(state='normal')
        self.counter_display.delete(0, tk.END)
        self.counter_display.insert(0, str(self.contador))
        self.counter_display.config(state='readonly')

root = tk.Tk()
app = ContDecreciente(root)
root.mainloop()



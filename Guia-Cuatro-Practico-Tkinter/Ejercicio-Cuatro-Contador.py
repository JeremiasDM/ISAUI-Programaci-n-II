""""
Ejercicio 4 - Contador.

Escribir una aplicación GUI (llamada Contador) como la que se ve en
la figura. Con 3 botones (Count Up - Para incrementar, Count Down -
Para restar y Reset - Para comenzar de cero).

La aplicación lleva:
1 - Una etiqueta "Contador"
2 - Un lineEdit no editable, que muestre el contador y que inicie en 0
3 - 3 Botones
"""""

import tkinter as tk

class ContadorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contador")
        self.root.configure(bg='#69002C')
        
        self.contador = 0
        
        self.label = tk.Label(root, text="Contador", bg='#69002C', fg='white')
        self.label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        
        self.counter_display = tk.Entry(root, justify='center')
        self.counter_display.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        self.counter_display.insert(0, str(self.contador))
        self.counter_display.config(state='readonly')
        
        self.button_up = tk.Button(root, text="Count Up", command=self.incrementar_contador)
        self.button_up.grid(row=2, column=0, padx=10, pady=10)
        
        self.button_down = tk.Button(root, text="Count Down", command=self.decrementar_contador)
        self.button_down.grid(row=2, column=1, padx=10, pady=10)
        
        self.button_reset = tk.Button(root, text="Reset", command=self.resetear_contador)
        self.button_reset.grid(row=2, column=2, padx=10, pady=10)
    
    def incrementar_contador(self):
        self.contador += 1
        self.actualizar_display()

    def decrementar_contador(self):
        self.contador -= 1
        self.actualizar_display()

    def resetear_contador(self):
        self.contador = 0
        self.actualizar_display()
    
    def actualizar_display(self):
        self.counter_display.config(state='normal')
        self.counter_display.delete(0, tk.END)
        self.counter_display.insert(0, str(self.contador))
        self.counter_display.config(state='readonly')

root = tk.Tk()
app = ContadorApp(root)
root.mainloop()


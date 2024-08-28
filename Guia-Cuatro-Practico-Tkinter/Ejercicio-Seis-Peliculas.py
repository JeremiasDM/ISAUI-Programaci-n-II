"""""
Ejercicio 6 - Películas.

Escribir una aplicación GUI (llamada Películas). Su función será: al
pulsar el botón Añadir, agregará en el listWidget el contenido de
lineEdit (Películas).

La aplicación lleva:
1 - 2 Etiquetas (Escribe el título de una película y Películas)
2 - Un lineEdit donde se escribirá el nombre de la película
3 - Un listWidget que registra las películas añadidas
4 - Un botón "Añadir"
"""""

import tkinter as tk

class PeliculasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Películas")
        self.root.configure(bg='#69002C')
        
        self.label1 = tk.Label(root, text="Escribe el título de una película", bg='#69002C', fg='white')
        self.label1.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        
        self.pelicula_entry = tk.Entry(root)
        self.pelicula_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
        
        self.label2 = tk.Label(root, text="Películas", bg='#69002C', fg='white')
        self.label2.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        
        self.peliculas_listbox = tk.Listbox(root)
        self.peliculas_listbox.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
        
        self.add_button = tk.Button(root, text="Añadir", command=self.anadir_pelicula)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)
    
    def anadir_pelicula(self):
        pelicula = self.pelicula_entry.get()
        if pelicula:
            self.peliculas_listbox.insert(tk.END, pelicula)
            self.pelicula_entry.delete(0, tk.END)

root = tk.Tk()
app = PeliculasApp(root)
root.mainloop()


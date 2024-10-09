import tkinter as tk
from tkinter import ttk
from viewalta import abrir_alta
from viewlistado import LISTADO

class MENU(tk.Frame):
    def __init__(self, master):
        super().__init__(master, height=500, width=800, bg="#b39658")
        self.master = master
        self.pack_propagate(0)
        self.pack(expand=True)
        self.ventana_menu()

    def comando_alta(self):
        self.master.withdraw()
        ventana = tk.Toplevel(self.master)
        ventana.wm_title("Formulario de contacto para ISAUI")
        ventana.wm_resizable(0,0)
        entradas = abrir_alta(ventana)
        def on_closing():
            ventana.destroy()
            self.master.deiconify()  # Muestra la ventana principal nuevamente
    
        ventana.protocol("WM_DELETE_WINDOW", on_closing)
        entradas.mainloop()

    def comando_lista(self):
        self.master.withdraw()
        ventana = tk.Toplevel(self.master)
        ventana.wm_title("Listado de personas")
        ventana.wm_resizable(0,0)
        entradas = LISTADO(ventana, menu=self)
        def on_closing():
            ventana.destroy()
            self.master.deiconify()  # Muestra la ventana principal nuevamente
    
        ventana.protocol("WM_DELETE_WINDOW", on_closing)
        entradas.mainloop()
        

    def ventana_menu(self):
        stilo = ttk.Style()
        stilo.configure("TFrame", background="#b39658")
        stilo.configure("TLabel", background="#b39658", foreground="#ffffff")
        stilo.configure("TButton", background="#ffffff", foreground="#000000")

        frame_menu = tk.LabelFrame(self, text="Menú", bg="white", font=('Calibri', 22), borderwidth=5)
        frame_menu.pack(expand= True, ipadx= 100, ipady= 50)

        tk.Label(frame_menu, text="Bienvenido al menú", font=('Calibri', 20)).grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        contenedor = tk.Frame(frame_menu, bg="white")
        contenedor.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        btn_alta = tk.Button(contenedor, text="Agregar Persona", justify= tk.CENTER, font=('Calibri', 25), bg= "#bdbcbb", activebackground= "#659c71", command=self.comando_alta)
        btn_alta.grid(row= 0, column=0, padx= 15, ipadx= 50, ipady= 35)

        btn_lista = tk.Button(contenedor, text="Ver Personas", justify= tk.CENTER, font=('Calibri', 25), bg= "#bdbcbb", activebackground= "#659c71", command=self.comando_lista)
        btn_lista.grid(row= 0, column=1, padx= 15, ipadx= 50, ipady= 35)

        tk.Button(frame_menu, text="Salir", command=self.master.destroy).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        frame_menu.grid_columnconfigure(0, weight=1)
        frame_menu.grid_columnconfigure(1, weight=1)
        frame_menu.grid_rowconfigure(0, weight=1)
        frame_menu.grid_rowconfigure(1, weight=1)
        frame_menu.grid_rowconfigure(2, weight=1)

if __name__ == "__main__":  
    ventana = tk.Tk()
    ventana.wm_title("Menú")
    ventana.wm_resizable(0,0)
    ventana.geometry("+200+100")
    menu = MENU(ventana)
    menu.mainloop()
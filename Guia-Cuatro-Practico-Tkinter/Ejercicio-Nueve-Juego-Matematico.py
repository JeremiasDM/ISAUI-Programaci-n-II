"""""
Juego Matemático.

Escribir una aplicación GUI (llamada Juego Matemático) como la que
se ve en la figura.

La aplicación lleva:
1 - 7 etiquetas (Juegos:, 2, Buenos:, 1, Malos:, 1 y -) las etiquetas que
son números arrancan en vacías. La etiqueta - (entre medio de los dos
lineEdit) arranca con signo de pregunta (?) y cambia dependiendo el
valor del radioButton (Sumar = +, Restar = -, Multiplicar = * y Dividir =
/).
2 - 3 lineEdit (Sólo el lineEdit Resultado puede ser modificado)
3 - 2 Botones (Nuevo Numero y Resultado)

Como funciona:
 El jugador arranca con los radioButton y los lineEdit vacíos.
 Cuando el jugador presione Nuevo Juego saldrán 2 numero
aleatorios (en los lineEdit de arriba) junto con 1 radioButton.
 El jugador debe poner un resultado dependiendo de la
operación y presionar el botón Resultado.
 Si el jugador gana, Juego: suma 1 y Buenos: suma 1.
 El jugador presiona Nuevo Juego, salen dos números
aleatorios nuevos y una operación nueva (todo aleatorio).
 El jugador hace un mal cálculo y pierde (Juegos: suma 1 y
queda en 2, Malos: suma 1).
Un poco más de complejidad ¿Porqué no?
Puedes agregar 3 radioButton más para que el jugador pueda elegir
la dificultad.
Si elige Fácil (los números aleatorios serán de 0 a 10), si
elige Medio (los números aleatorios serán de 0 a 100) y si
elige Difícil (los números aleatorios serán de 0 a 1000).
Cada vez que elija una dificultad todo vuelve a 0.

Dificultad

Y puedes agregar un contador (LCD Number) que haga una cuenta
regresiva de 60 segundos (si el jugador no responde antes del tiempo
pierde ese juego). El tiempo en segundos puede ser también
dependiendo de la dificultad.
"""""

import tkinter as tk
from tkinter import messagebox, Radiobutton
import random

import tkinter as tk
from tkinter import messagebox, Radiobutton
import random

class JuegoMatematicoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego Matemático")
        self.root.configure(bg='#69002C')

        self.juegos = 0
        self.buenos = 0
        self.malos = 0
        self.dificultad = tk.StringVar(value="Medio")
        self.operacion = tk.StringVar(value="?")

        self.dificultad_label = tk.Label(root, text="Dificultad", bg='#69002C', fg='white')
        self.dificultad_label.grid(row=0, column=0, sticky="w")

        self.facil_rb = Radiobutton(root, text="Fácil (0-10)", variable=self.dificultad, value="Facil", command=self.reset, bg='#69002C', fg='white', selectcolor="#AA0044")
        self.facil_rb.grid(row=1, column=0, sticky="w")

        self.medio_rb = Radiobutton(root, text="Medio (0-100)", variable=self.dificultad, value="Medio", command=self.reset, bg='#69002C', fg='white', selectcolor="#AA0044")
        self.medio_rb.grid(row=2, column=0, sticky="w")

        self.dificil_rb = Radiobutton(root, text="Difícil (0-1000)", variable=self.dificultad, value="Dificil", command=self.reset, bg='#69002C', fg='white', selectcolor="#AA0044")
        self.dificil_rb.grid(row=3, column=0, sticky="w")

        self.juegos_label = tk.Label(root, text="Juegos: 0", bg='#69002C', fg='white')
        self.juegos_label.grid(row=0, column=1, sticky="e")

        self.buenos_label = tk.Label(root, text="Buenos: 0", bg='#69002C', fg='white')
        self.buenos_label.grid(row=1, column=1, sticky="e")

        self.malos_label = tk.Label(root, text="Malos: 0", bg='#69002C', fg='white')
        self.malos_label.grid(row=2, column=1, sticky="e")

        self.numero1_entry = tk.Entry(root, state='readonly', justify='center')
        self.numero1_entry.grid(row=4, column=0, columnspan=2, sticky="we", pady=(0, 20))

        self.operacion_label = tk.Label(root, textvariable=self.operacion, bg='#69002C', fg='white')
        self.operacion_label.grid(row=5, column=0, columnspan=2)

        self.numero2_entry = tk.Entry(root, state='readonly', justify='center')
        self.numero2_entry.grid(row=6, column=0, columnspan=2, sticky="we", pady=(20, 20))

        self.resultado_entry = tk.Entry(root, justify='center')
        self.resultado_entry.grid(row=7, column=0, columnspan=2, sticky="we", pady=(0, 20))

        self.nuevo_numero_button = tk.Button(root, text="Nuevo Número", command=self.generar_numeros)
        self.nuevo_numero_button.grid(row=8, column=0, sticky="we")

        self.resultado_button = tk.Button(root, text="Resultado", command=self.verificar_resultado)
        self.resultado_button.grid(row=8, column=1, sticky="we")

    def reset(self):
        """Resetea el juego al cambiar la dificultad."""
        self.juegos = 0
        self.buenos = 0
        self.malos = 0
        self.actualizar_etiquetas()

    def obtener_rango(self):
        """Obtiene el rango basado en la dificultad."""
        if self.dificultad.get() == "Facil":
            return 0, 10
        elif self.dificultad.get() == "Medio":
            return 0, 100
        elif self.dificultad.get() == "Dificil":
            return 0, 1000

    def generar_numeros(self):
        """Genera dos números aleatorios y una operación."""
        rango = self.obtener_rango()
        self.numero1 = random.randint(*rango)
        self.numero2 = random.randint(*rango)
        self.operacion.set(random.choice(["+", "-", "*", "/"]))

        self.numero1_entry.config(state='normal')
        self.numero1_entry.delete(0, tk.END)
        self.numero1_entry.insert(0, str(self.numero1))
        self.numero1_entry.config(state='readonly')

        self.numero2_entry.config(state='normal')
        self.numero2_entry.delete(0, tk.END)
        self.numero2_entry.insert(0, str(self.numero2))
        self.numero2_entry.config(state='readonly')

    def verificar_resultado(self):
        """Verifica si el resultado ingresado es correcto."""
        try:
            resultado_usuario = float(self.resultado_entry.get())
            if self.operacion.get() == "+":
                resultado_correcto = self.numero1 + self.numero2
            elif self.operacion.get() == "-":
                resultado_correcto = self.numero1 - self.numero2
            elif self.operacion.get() == "*":
                resultado_correcto = self.numero1 * self.numero2
            elif self.operacion.get() == "/":
                if self.numero2 != 0:
                    resultado_correcto = self.numero1 / self.numero2
                else:
                    messagebox.showerror("Error", "No se puede dividir por cero.")
                    return

            self.juegos += 1
            if abs(resultado_usuario - resultado_correcto) < 1e-5:
                self.buenos += 1
                messagebox.showinfo("Resultado", "¡Correcto!")
            else:
                self.malos += 1
                messagebox.showinfo("Resultado", f"Incorrecto. El resultado correcto era {resultado_correcto:.2f}")
            self.actualizar_etiquetas()

        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa un número válido.")

    def actualizar_etiquetas(self):
        """Actualiza las etiquetas de juegos, buenos y malos."""
        self.juegos_label.config(text=f"Juegos: {self.juegos}")
        self.buenos_label.config(text=f"Buenos: {self.buenos}")
        self.malos_label.config(text=f"Malos: {self.malos}")

root = tk.Tk()
app = JuegoMatematicoApp(root)
root.mainloop()




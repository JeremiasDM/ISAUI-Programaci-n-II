import tkinter as tk
from itertools import cycle

class VaporeonDanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Vaporeon Bailando")

        # Crear los "frames" del baile usando símbolos
        self.frames = cycle([
            """
            (\\(\\
            ( -.-)
            o_(")(")
            """,
            """
            (\\(\\
            (^_^)
            o_(")(")
            """,
            """
            (\\(\\
            (>_<)
            o_(")(")
            """,
            """
            (\\(\\
            (^o^)
            o_(")(")
            """
        ])

        # Crear un Label para mostrar la "animación"
        self.label = tk.Label(root, font=("Courier", 18), justify='left')
        self.label.pack()

        # Iniciar la animación
        self.animate()

    def animate(self):
        frame = next(self.frames)
        self.label.config(text=frame)
        self.root.after(500, self.animate)  # Cambiar de frame cada 500ms

if __name__ == "__main__":
    root = tk.Tk()
    app = VaporeonDanceApp(root)
    root.mainloop()

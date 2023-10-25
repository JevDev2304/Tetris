import tkinter as tk
from tkinter import PhotoImage
from tetris import run_game
from db import Db
from tkinter import ttk



class View:
    def __init__(self):
        self.main_window = tk.Tk()
        self.second_window = tk.Toplevel(self.main_window)
        self.second_window.withdraw()
        self.db = Db()

    def create_main_window(self):
        self.load_images()
        self.main_window.geometry("500x620")
        self.main_window.resizable(False, False)
        self.main_window.title("Tetris pygame")
        self.main_window.config(background="#000000")

        # Obtenemos el tamaño de la pantalla
        wtotal = self.main_window.winfo_screenwidth()
        htotal = self.main_window.winfo_screenheight()

        # Tamaño de la ventana
        wventana = 500
        hventana = 620

        # Calculamos la posición para centrar la ventana
        pwidth = wtotal // 2 - wventana // 2
        pheight = htotal // 2 - hventana // 2

        # Establecemos la geometría de la ventana
        self.main_window.geometry(f"{wventana}x{hventana}+{pwidth}+{pheight}")
        title = tk.Label(self.main_window, image=self.logo, background="#000000")
        jugar_button = tk.Button(self.main_window, bd=0, command=self.create_register_window,
                                 image=self.foto_iniciar_juego, background="#000000")
        ranking = tk.Button(self.main_window, bd=0, command=self.create_ranking_window,
                                 image=self.ranking, background="#000000")
        title.pack()
        jugar_button.pack()
        ranking.pack()

        self.main_window.mainloop()

    def create_register_window(self):
        self.main_window.withdraw()
        self.second_window = tk.Toplevel(self.main_window)
        self.second_window.geometry("500x620")
        self.second_window.resizable(False, False)
        self.second_window.title("Tetris pygame")
        self.second_window.config(background="#000000")

        # Obtenemos el tamaño de la pantalla
        wtotal = self.second_window.winfo_screenwidth()
        htotal = self.second_window.winfo_screenheight()

        # Tamaño de la ventana
        wventana = 500
        hventana = 620

        # Calculamos la posición para centrar la ventana
        pwidth = wtotal // 2 - wventana // 2
        pheight = htotal // 2 - hventana // 2

        # Establecemos la geometría de la ventana
        self.second_window.geometry(f"{wventana}x{hventana}+{pwidth}+{pheight}")
        title = tk.Label(self.second_window, image=self.nombre, background="#000000")
        self.entrada = tk.Entry(self.second_window, borderwidth=0, width=20, font=("courier", 12))
        jugar_button = tk.Button(self.second_window, bd=0, command=self.get_name, image=self.foto_iniciar_juego,
                                 background="#000000")

        title.pack()
        self.entrada.pack()
        jugar_button.pack()

        self.second_window.mainloop()

    def get_name(self):
        name = self.entrada.get()
        if not self.db.check_name_exists(name):
            self.db.add_player(name)
        self.second_window.withdraw()
        score = run_game(300, name)
        self.second_window.destroy()
        self.main_window.deiconify()
        id_jugador = self.db.get_id_user(name)
        self.db.add_score(id_jugador,score)

    def load_images(self):
        self.logo = PhotoImage(file="images/TETRIS.png")
        self.foto_iniciar_juego = PhotoImage(file="images/INICIAR JUEGO.png")
        self.nombre = PhotoImage(file="images/NOMBRE.png")
        self.ranking = PhotoImage(file = "images/RANKING.png")


    def create_ranking_window(self):
        self.main_window.withdraw()
        self.second_window = tk.Toplevel(self.main_window)
        self.second_window.config(background="black")
        self.second_window.title("Ranking Tetris")
        self.second_window.geometry("500x620")
        self.second_window.resizable(False, False)

    # Obtenemos el tamaño de la pantalla
        wtotal = self.second_window.winfo_screenwidth()
        htotal = self.second_window.winfo_screenheight()

    # Tamaño de la ventana
        wventana = 500
        hventana = 620

    # Calculamos la posición para centrar la ventana
        pwidth = wtotal // 2 - wventana // 2
        pheight = htotal // 2 - hventana // 2

        self.second_window.geometry(f"{wventana}x{hventana}+{pwidth}+{pheight}")

    # Crear un estilo personalizado para la tabla
        label = tk.Label(self.second_window, text="Top 10 ", background="black", foreground="white",
                         font=("Courier", 16))
        label.pack()
        style = ttk.Style()
        style.configure("Custom.Treeview", background="black", fieldbackground="black", foreground="white",
                    font=("Courier", 14))

    # Crear una tabla para mostrar los datos con el estilo personalizado
        tabla = ttk.Treeview(self.second_window, columns=("Nombre", "Puntaje"), show="headings", style="Custom.Treeview")
        tabla.heading("#1", text="Nombre")
        tabla.heading("#2", text="Puntaje")

    # Establecer el color de fondo de las filas de la tabla
        tabla.pack()

    # Cargar los datos iniciales
        self.db.cargar_datos(tabla)

    # Ejecutar la aplicación
        self.second_window.mainloop()



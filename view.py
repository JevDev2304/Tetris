import tkinter as tk
class View:
    def __init__(self):
        self.main_window = tk.Tk()


    def create_main_window(self):
        self.main_window.geometry("500x620")
        self.main_window.resizable(False, False)
        self.main_window.title(
            "Tetris pygame")
        self.main_window.config(background="#000000")
        self.main_window.maxsize(500, 620)
        self.main_window.mainloop()

view = View()
view.create_main_window()
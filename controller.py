from view import *
class Controller:
    def __init__(self):
        self.view = View()

    def start(self):
        self.view = View()
        self.view.create_main_window()



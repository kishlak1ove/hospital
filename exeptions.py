from tkinter import *
from tkinter import messagebox


class Error(Exception):
    pass


class InputError(Error):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

    def subscribe(self):
        return messagebox.showinfo(self.expression, self.message)


class InputPar(Error):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

    def subscribe(self):
        return messagebox.showinfo(self.expression, self.message)
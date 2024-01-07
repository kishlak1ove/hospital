import time
import tkinter as tk
from Forms import Forms

def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb



if __name__ == '__main__':
    root = tk.Tk()
    root.title("Стрелецкая ЦРБ")
    root.config(bg=rgb_hack((0, 159, 166)))
    root.geometry("280x140")
    app = Forms(root)
    app.createPanelWithButton()
    root.mainloop()

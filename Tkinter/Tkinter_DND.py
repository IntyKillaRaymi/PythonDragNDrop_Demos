import tkinter as tk

class Window:
    root = None
    choose_menu = None
    drag_canvas = None
    def __init__(self):
        self.root = tk.Tk()
        aux = tk.Label(self.root, text = "Choose")
        aux.pack()
        self.drag_canvas = tk.Frame(self.root, height = 200, bg="cyan")
        aux = tk.Label(self.drag_canvas, text = "Drag and Drop")
        self.drag_canvas.pack(fill = "both", expand = True)
        
        
    def SetTitle(self, name):
        self.root.title(str(name))

class Object:
    def __init__(self, tipo, pos):
        print("Tipo: " + tipo + " - Posición: "+ pos)

window  = Window()

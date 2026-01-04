import tkinter as tk
from tkinter import colorchooser

class SimpleDrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gelişmiş Çizim Programı")

        # Varsayılan renk, şekil ve kalınlık
        self.color = "black"
        self.shape = "line"
        self.pen_width = 2

        # Araç çubuğu
        toolbar = tk.Frame(root)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.color_btn = tk.Button(toolbar, text="Renk Seç", command=self.choose_color)
        self.color_btn.pack(side=tk.LEFT, padx=5)

        self.line_btn = tk.Button(toolbar, text="Çizgi", command=lambda: self.set_shape("line"))
        self.line_btn.pack(side=tk.LEFT, padx=5)

        self.rect_btn = tk.Button(toolbar, text="Dikdörtgen", command=lambda: self.set_shape("rectangle"))
        self.rect_btn.pack(side=tk.LEFT, padx=5)

        self.oval_btn = tk.Button(toolbar, text="Daire", command=lambda: self.set_shape("oval"))
        self.oval_btn.pack(side=tk.LEFT, padx=5)

        self.freehand_btn = tk.Button(toolbar, text="Kalem", command=lambda: self.set_shape("freehand"))
        self.freehand_btn.pack(side=tk.LEFT, padx=5)

        self.eraser_btn = tk.Button(toolbar, text="Silgi", command=lambda: self.set_shape("eraser"))
        self.eraser_btn.pack(side=tk.LEFT, padx=5)

        # Kalınlık seçici
        tk.Label(toolbar, text="Kalınlık:").pack(side=tk.LEFT, padx=5)
        self.width_var = tk.IntVar(value=self.pen_width)
        self.width_menu = tk.Spinbox(toolbar, from_=1, to=20, width=3, textvariable=self.width_var, command=self.change_width)
        self.width_menu.pack(side=tk.LEFT, padx=5)

        # Çizim alanı
        self.canvas = tk.Canvas(root, bg="white", width=600, height=400)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Mouse hareketleri
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

        self.start_x = None
        self.start_y = None
        self.current_shape = None

    def choose_color(self):
        color_code = colorchooser.askcolor(title="Renk Seç")
        if color_code[1]:
            self.color = color_code[1]

    def set_shape(self, shape):
        self.shape = shape

    def change_width(self):
        self.pen_width = self.width_var.get()

    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        if self.shape == "line":
            self.current_shape = self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill=self.color, width=self.pen_width)
        elif self.shape == "rectangle":
            self.current_shape = self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline=self.color, width=self.pen_width)
        elif self.shape == "oval":
            self.current_shape = self.canvas.create_oval(self.start_x, self.start_y, event.x, event.y, outline=self.color, width=self.pen_width)
        elif self.shape in ["freehand", "eraser"]:
            self.current_shape = None  # Freehand ve silgi için sürekli çizgi parçaları

    def on_move_press(self, event):
        if self.shape == "freehand":
            if self.start_x and self.start_y:
                self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill=self.color, width=self.pen_width, smooth=True)
                self.start_x, self.start_y = event.x, event.y
        elif self.shape == "eraser":
            if self.start_x and self.start_y:
                eraser_size = self.pen_width * 5  # Silgi boyutu
                self.canvas.create_rectangle(event.x - eraser_size/2, event.y - eraser_size/2,
                                             event.x + eraser_size/2, event.y + eraser_size/2,
                                             fill="white", outline="white")
                self.start_x, self.start_y = event.x, event.y
        elif self.current_shape:
            self.canvas.coords(self.current_shape, self.start_x, self.start_y, event.x, event.y)

    def on_button_release(self, event):
        self.current_shape = None
        self.start_x = None
        self.start_y = None

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleDrawingApp(root)
    root.mainloop()

from tkinter import *

DEEP_BLUE = "#004080"
ACCENT_ORANGE = "#ffa500"
STEEL_GREY = "#9a9a9a"
CHARCOAL = "#333333"
SKY_BLUE = "#87ceeb"
ACCENT_GREEN = "#00b33c"


window = Tk()
window.title("PC INFO")
window.config(bg=DEEP_BLUE, pady=10, padx=20)

canvas = Canvas(window, width=200, height=200, bg=SKY_BLUE)
canvas.pack()

circle_radius = 90
circle_center = (100, 100)

x1 = circle_center[0] - circle_radius  # 100 - 50
y1 = circle_center[1] - circle_radius  # 100 - 50    (x1,y1) = (50,50)
x2 = circle_center[0] + circle_radius  # 100 + 50
y2 = circle_center[1] + circle_radius  # 100 + 50    (x2,y2) = (150, 150)

canvas.create_oval(x1, y1, x2, y2, fill=ACCENT_ORANGE, outline=CHARCOAL, width=10)

window.mainloop()

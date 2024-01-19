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

# Circle Parameters
circle_radius = 50
circle_center = (100, 100)

# Calculate Bounding Box Coordinates for the Circle
x1 = circle_center[0] - circle_radius
y1 = circle_center[1] - circle_radius
x2 = circle_center[0] + circle_radius
y2 = circle_center[1] + circle_radius

# Draw the Circle
canvas.create_oval(x1, y1, x2, y2, fill=ACCENT_ORANGE, outline=CHARCOAL, width=10)

# Text Parameters
text_content = "Hello, Circle!"
text_x = circle_center[0]  # Center of the Circle
text_y = circle_center[1] - circle_radius - 20  # Above the Circle

# Draw the Text above the Circle
canvas.create_text(text_x, text_y, text=text_content, font=("Helvetica", 10), fill=ACCENT_GREEN)

# Colored Arc Parameters (representing 35%)
start_angle = 0  # Starting angle in degrees
extent_angle = 35 * 3.6  # Extent angle in degrees (35% of 360 degrees)

# Draw the Colored Arc
canvas.create_arc(x1, y1, x2, y2, start=start_angle, extent=extent_angle, fill=STEEL_GREY, outline="")

window.mainloop()

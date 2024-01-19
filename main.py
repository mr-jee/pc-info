import psutil
from tkinter import *

DEEP_BLUE = "#004080"
ACCENT_ORANGE = "#ffa500"
STEEL_GREY = "#9a9a9a"
CHARCOAL = "#333333"
SKY_BLUE = "#87ceeb"
ACCENT_GREEN = "#00b33c"


def update_disk_usage(canvas):
    disk_partitions = psutil.disk_partitions()
    for widget in canvas.find_all():
        canvas.delete(widget)

    for i, partition in enumerate(disk_partitions):
        device = partition.device
        disk_usage = psutil.disk_usage(device)
        draw_disks(i + 1, disk_usage, device)


def draw_disks(i, disk_usage, part_name):
    total_gb = round(disk_usage.total / (1024 ** 3), 3)
    used_gb = round(disk_usage.used / (1024 ** 3), 3)
    free_gb = round(disk_usage.free / (1024 ** 3), 3)

    circle_radius = 60
    x = 2 * i - 1
    circle_center = (x * circle_radius + (i * 15), 150)

    x1 = circle_center[0] - circle_radius  # 70 - 60
    y1 = circle_center[1] - circle_radius  # 150 - 60   (x1, y1) = (10, 90)
    x2 = circle_center[0] + circle_radius  # 70 + 60
    y2 = circle_center[1] + circle_radius  # 150 + 60   (x1, y1) = (130, 210)
    text_y = circle_center[1] - circle_radius  # Above the Circle

    partition_name_text = canvas.create_text(circle_center[0], text_y - 75, text=f" {part_name}")
    total_space_text = canvas.create_text(circle_center[0], text_y - 55, text=f"Total :{total_gb} GB")
    used_space_text = canvas.create_text(circle_center[0], text_y - 35, text=f"Used : {used_gb} GB", fill=DEEP_BLUE)
    free_space_text = canvas.create_text(circle_center[0], text_y - 15, text=f"Free : {free_gb} GB", fill=ACCENT_GREEN)

    canvas.create_oval(x1, y1, x2, y2, fill=ACCENT_GREEN, outline=CHARCOAL, width=2)

    used_space_percent = disk_usage.percent / 100
    canvas.create_arc(x1, y1, x2, y2, start=0, extent=used_space_percent * 360, fill=SKY_BLUE)


window = Tk()
window.title("PC INFO")
window.config(bg=DEEP_BLUE, pady=10, padx=20)

# CPU INFO===============================================================================
cpu_section_frame = Frame(window, bg=DEEP_BLUE, bd=2, relief=GROOVE, highlightthickness=2,
                          highlightbackground=ACCENT_ORANGE)
cpu_section_frame.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

cpu_info_label = Label(cpu_section_frame, text="CPU INFO")
cpu_info_label.grid(row=0, column=0)
# RAM INFO===============================================================================
ram_section_frame = Frame(window, bg=DEEP_BLUE, bd=2, relief=GROOVE, highlightthickness=2,
                          highlightbackground=ACCENT_ORANGE)
ram_section_frame.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
ram_info_label = Label(ram_section_frame, text="RAM INFO")
ram_info_label.grid(row=0, column=0)
# DISK INFO==============================================================================
disk_section_frame = Frame(window, bg=DEEP_BLUE, bd=2, relief=GROOVE, highlightthickness=2,
                           highlightbackground=ACCENT_ORANGE)
disk_section_frame.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

canvas = Canvas(disk_section_frame, width=900, height=250)
canvas.grid(row=0, column=0)
update_disk_usage(canvas)

window.mainloop()

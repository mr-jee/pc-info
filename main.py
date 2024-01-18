import psutil
import cpuinfo
import time
from tkinter import *





DEEP_BLUE = "#004080"
ACCENT_ORANGE = "#ffa500"
STEEL_GREY = "#9a9a9a"
CHARCOAL = "#333333"
SKY_BLUE = "#87ceeb"
ACCENT_GREEN = "#00b33c"



# cpu_info= cpuinfo.get_cpu_info()
# cpu_count = psutil.cpu_count()
#
# print('CPU Info:', cpu_info['brand_raw'])
# print('CPU Count:', cpu_count)
#
# memory_info = psutil.virtual_memory()
# print(memory_info)


# while True:
#     cpu_usage = psutil.cpu_percent()
#     memory_usage = psutil.virtual_memory().percent
#
#     print(f"CPU Usage: {cpu_usage}% | Memory Usage: {memory_usage}%")
#     time.sleep(1)

# disk_partitions = psutil.disk_partitions()

# for partition in disk_partitions:
#     # Extract the device (partition) path
#     device = partition.device
#
#     # Get disk usage for each partition
#     disk_usage = psutil.disk_usage(device)
#
#     print(f"Disk: {device}")
#     print(f"Total: {disk_usage.total / (1024**3):.2f} GB")
#     print(f"Used: {disk_usage.used / (1024**3):.2f} GB")
#     print(f"Free: {disk_usage.free / (1024**3):.2f} GB")
#     print()

def update_disk_usage():
    disk_partitions = psutil.disk_partitions()
    print(disk_partitions)
    for widget in canvas.find_all():
        canvas.delete(widget)

    for i, partition in enumerate(disk_partitions):
        device = partition.device
        print("device:", device)
        disk_usage = psutil.disk_usage(device)
        print("disk usage:", disk_usage.percent)

        total_gb = disk_usage.total / (1024**3)
        used_gb = disk_usage.used / (1024**3)
        free_gb = disk_usage.free / (1024**3)

        total_percentage = used_gb / total_gb
        free_percentage = free_gb / total_gb
        # x_position = 40 if i == 0 else i * 150

        print("total:",total_gb,"used:" ,used_gb,"free:", free_gb)
        print(f"total_percentage: {total_percentage} free_percentage: {free_percentage}\n")
        # draw_disk(canvas, x_position, total_percentage, free_percentage)

    # window.after(5000, update_disk_usage)  # Update every 5 seconds

# def draw_disk(canvas, x, total_percentage, free_percentage):
#     radius = 50
#     center = x + radius + 10, 110
#
#     canvas.create_text(center[0], center[1] - 70, text=f"Total: {total_percentage * 100:.2f}%")
#     canvas.create_text(center[0], center[1] - 50, text=f"Free: {free_percentage * 100:.2f}%")
#     canvas.create_text(center[0], center[1] - 30, text=f"Used: {(1 - free_percentage) * 100:.2f}%")
#
#     canvas.create_oval(x, 90, x + 2 * radius, 200, outline="black", width=2)
#     canvas.create_arc(x, 90, x + 2 * radius, 200, start=0, extent=total_percentage * 360, fill=SKY_BLUE)
#     canvas.create_arc(x, 90, x + 2 * radius, 200, start=total_percentage * 360, extent=free_percentage * 360, fill=ACCENT_GREEN)

window = Tk()
window.title("PC INFO")
# window.minsize(width=250, height=250)
window.config(bg=DEEP_BLUE, pady=10, padx=20)

# CPU INFO===============================================================================
cpu_section_frame = Frame(window, bg=DEEP_BLUE, bd=2, relief=GROOVE, highlightthickness=2, highlightbackground=ACCENT_ORANGE)
cpu_section_frame.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
# RAM INFO===============================================================================
ram_section_frame = Frame(window, bg=DEEP_BLUE, bd=2, relief=GROOVE, highlightthickness=2, highlightbackground=ACCENT_ORANGE)
ram_section_frame.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
# DISK INFO==============================================================================
disk_section_frame = Frame(window, bg=DEEP_BLUE, bd=2, relief=GROOVE, highlightthickness=2, highlightbackground=ACCENT_ORANGE)
disk_section_frame.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

canvas = Canvas(disk_section_frame, width=400, height=400)
canvas.grid(row=0, column=0)
update_disk_usage()



window.mainloop()
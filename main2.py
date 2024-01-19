import psutil
import time
from tkinter import *
import platform




DEEP_BLUE = "#004080"
ACCENT_ORANGE = "#ffa500"
STEEL_GREY = "#9a9a9a"
CHARCOAL = "#333333"
SKY_BLUE = "#87ceeb"
ACCENT_GREEN = "#00b33c"



# cpu_info= cpuinfo.get_cpu_info()
# cpu_count = psutil.cpu_count()
#
# print(psutil.cpu_freq())
# print(psutil.cpu_percent())
# print(psutil.cpu_stats())
# print(psutil.cpu_times())
# print(psutil.cpu_times_percent())
# print('CPU Count:', cpu_count)

print("PLATFORM")
cpu_info = platform.processor()
print(cpu_info)

memory_info = psutil.virtual_memory()
print("Memory:", memory_info)


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




window.mainloop()

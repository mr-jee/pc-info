import psutil
from tkinter import *
import cpuinfo
import wmi

DEEP_BLUE = "#004080"
ACCENT_ORANGE = "#ffa500"
STEEL_GREY = "#9a9a9a"
CHARCOAL = "#333333"
SKY_BLUE = "#87ceeb"
ACCENT_GREEN = "#00b33c"


def update_ram_usage():
    pass



def ddr_what(speed_mhz):
    if speed_mhz >= 2133:
        return "DDR4"
    elif 1066 <= speed_mhz < 2133:
        return "DDR3"
    else:
        return "Unknown"


def get_memory_details():
    memory_info = psutil.virtual_memory()
    wmi_object = wmi.WMI()
    for i, physical_memory in enumerate(wmi_object.Win32_PhysicalMemory()):
        # print(physical_memory)
        memory_module_label = Label(ram_section_frame, text=f"Memory Module {i}:", bg=DEEP_BLUE, fg="white")
        memory_module_label.grid(row=1, column=i, padx=10, sticky='w')

        capacity_label = Label(ram_section_frame, text=f"  Capacity: {int(physical_memory.Capacity) / (1024 ** 3)} GB",
                               bg=DEEP_BLUE, fg="white")
        capacity_label.grid(row=2, column=i, padx=10, sticky='w')

        manufacturer_label = Label(ram_section_frame, text=f"  Manufacturer: {physical_memory.Manufacturer}",
                                   bg=DEEP_BLUE, fg="white")
        manufacturer_label.grid(row=3, column=i, padx=10, sticky='w')

        part_number_label = Label(ram_section_frame, text=f"  Part Number: {physical_memory.PartNumber}",
                                  bg=DEEP_BLUE, fg="white")
        part_number_label.grid(row=4, column=i, padx=10, sticky='w')

        speed_label = Label(ram_section_frame, text=f"  Speed: {physical_memory.Speed} MHz",
                            bg=DEEP_BLUE, fg="white")
        speed_label.grid(row=5, column=i, padx=10, sticky='w')

        ddr_type = ddr_what(physical_memory.Speed)
        ddr_label = Label(ram_section_frame, text=f"  DDR Type: {ddr_type}",
                          bg=DEEP_BLUE, fg="white")
        ddr_label.grid(row=6, column=i, padx=10, sticky='w', pady=(0, 10))

    total_physical_memory = Label(ram_section_frame,
                                  text=f"Total Physical Memory: {memory_info.total / (1024 ** 3):.2f} GB",
                                  bg=DEEP_BLUE, fg="white")
    total_physical_memory.grid(row=7, column=0, sticky='w', padx=10)


def update_ram_and_cpu_usage():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    cpu_usage_value.config(text=f"{cpu_usage}%")
    ram_usage_label.config(text=f"RAM Usage: {memory_usage} %")
    window.after(1000, update_ram_and_cpu_usage)


def cpu_info():
    cpu_info = cpuinfo.get_cpu_info()
    return f"{cpu_info['brand_raw']}\nArchitecture: {cpu_info['arch']}"


def update_disk_usage(canvas):
    disk_partitions = psutil.disk_partitions()
    for widget in canvas.find_all():
        canvas.delete(widget)

    for i, partition in enumerate(disk_partitions):
        device = partition.device
        disk_usage = psutil.disk_usage(device)
        draw_disks(canvas, i + 1, disk_usage, device)


def draw_disks(canvas, i, disk_usage, part_name):
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

cpu_info_label = Label(cpu_section_frame, text="CPU INFO:", bg=DEEP_BLUE, fg="white")
cpu_info_label.grid(row=0, column=0)

cpu_info_value = Label(cpu_section_frame, text=cpu_info(), bg=DEEP_BLUE, fg="white")
cpu_info_value.grid(row=1, column=0, sticky='w')

cpu_usage_label = Label(cpu_section_frame, text="CPU Usage :", bg=DEEP_BLUE, fg="white")
cpu_usage_label.grid(row=1, column=1, padx=(15, 0), sticky='w')

cpu_usage_value = Label(cpu_section_frame, text=f"%", bg=DEEP_BLUE, fg="white")
cpu_usage_value.grid(row=1, column=2, sticky='w')

# RAM INFO===============================================================================
ram_section_frame = Frame(window, bg=DEEP_BLUE, bd=2, relief=GROOVE, highlightthickness=2,
                          highlightbackground=ACCENT_ORANGE)
ram_section_frame.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
ram_info_label = Label(ram_section_frame, text="RAM INFO:", bg=DEEP_BLUE, fg="white")
ram_info_label.grid(row=0, column=0)
ram_usage_label = Label(ram_section_frame, text="RAM Usage: ", bg=DEEP_BLUE, fg="white")
ram_usage_label.grid(row=8, column=0, sticky='w', padx=10)
# DISK INFO==============================================================================
disk_section_frame = Frame(window, bg=DEEP_BLUE, bd=2, relief=GROOVE, highlightthickness=2,
                           highlightbackground=ACCENT_ORANGE)
disk_section_frame.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

disk_canvas = Canvas(disk_section_frame, width=500, height=250)
disk_canvas.grid(row=0, column=0)
update_disk_usage(disk_canvas)
update_ram_and_cpu_usage()
get_memory_details()
update_ram_usage()
window.mainloop()

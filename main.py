import psutil
import cpuinfo
import time

cpu_info= cpuinfo.get_cpu_info()
cpu_count = psutil.cpu_count()


print('CPU Info:', cpu_info['brand_raw'])
print('CPU Count:', cpu_count)


memory_info = psutil.virtual_memory()
print(memory_info)


# while True:
#     cpu_usage = psutil.cpu_percent()
#     memory_usage = psutil.virtual_memory().percent
#
#     print(f"CPU Usage: {cpu_usage}% | Memory Usage: {memory_usage}%")
#     time.sleep(1)

disk_usage = psutil.disk_usage('/')
print(f"Total: {disk_usage.total / (1024**3):.2f} GB")
print(f"Used: {disk_usage.used / (1024**3):.2f} GB")
print(f"Free: {disk_usage.free / (1024**3):.2f} GB")
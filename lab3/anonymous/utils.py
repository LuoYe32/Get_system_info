import platform
import socket
import psutil

def get_system_info():
    system_info = {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Hostname": socket.gethostname(),
        "IP Address": socket.gethostbyname(socket.gethostname()),
        "CPU Cores": psutil.cpu_count(logical=False),
        "CPU Threads": psutil.cpu_count(logical=True),
        "RAM (GB)": round(psutil.virtual_memory().total / (1024 ** 3), 2),
        "Disk Space (GB)": round(psutil.disk_usage('/').total / (1024 ** 3), 2),
    }
    return system_info

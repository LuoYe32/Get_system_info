from django.shortcuts import render
from .utils import get_system_info
from .models import SystemInfo
from django.http import HttpResponseForbidden

def system_info(request):
    system_info_data = get_system_info()

    # Создаем и сохраняем объект модели
    system_info_object = SystemInfo(
        system=system_info_data["System"],
        node_name=system_info_data["Node Name"],
        release=system_info_data["Release"],
        version = system_info_data["Version"],
        machine = system_info_data["Machine"],
        processor = system_info_data["Processor"],
        host_name = system_info_data["Hostname"],
        ip_address = system_info_data["IP Address"],
        cpu_cores = system_info_data["CPU Cores"],
        cpu_threads = system_info_data["CPU Threads"],
        ram = system_info_data["RAM (GB)"],
        disk_space = system_info_data["Disk Space (GB)"]
    )
    system_info_object.save()

    return render(request, 'anonymous/home.html', {'system_info': system_info_data})

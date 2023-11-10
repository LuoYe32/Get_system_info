from django.shortcuts import render
from .utils import get_system_info

def system_info(request):
    system_info = get_system_info()
    return render(request, 'anonymous/system_info.html', {'system_info': system_info})


from django.db import models

class SystemInfo(models.Model):
    system = models.CharField(max_length=100)
    node_name = models.CharField(max_length=100)
    release = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    machine = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    host_name = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    cpu_cores = models.CharField(max_length=100)
    cpu_threads = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)
    disk_space = models.CharField(max_length=100)

    class Meta:
        verbose_name = "System_info"
        verbose_name_plural = "System_info"
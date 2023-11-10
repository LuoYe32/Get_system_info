from django.db import models

class File(models.Model):
    file_name = models.CharField(max_length=255)
    file_data = models.FileField(upload_to='files/')

    def __str__(self):
        return self.file_name

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"
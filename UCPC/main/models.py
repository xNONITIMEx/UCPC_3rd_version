from django.contrib.auth.models import User
from django.db import models

class Cards(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    image = models.ImageField(upload_to='img', verbose_name='Картинка', blank=True)
    desc = models.TextField(max_length=250, verbose_name='Описание')
    file = models.FileField(upload_to='file', verbose_name='Файл')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Карта сборки'
        verbose_name_plural = 'Карты сборок'


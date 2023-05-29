from django.contrib.auth.models import User
from django.db import models

class Cards(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    image = models.ImageField(upload_to='img', verbose_name='Картинка', blank=True)
    desc = models.TextField(max_length=250, verbose_name='Описание')
    file = models.FileField(upload_to='file', verbose_name='Файл')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    tags = models.ManyToManyField('Tag', verbose_name='Теги')

    def get_tags(self):
        tag_list = self.tags.all()
        res = [tag.title for tag in tag_list]
        return ', '.join(res)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Карта сборки'
        verbose_name_plural = 'Карты сборок'


class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Тэг')
    date_created = models.DateTimeField(auto_now_add='True')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


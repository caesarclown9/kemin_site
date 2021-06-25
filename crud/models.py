from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name = 'Заголовок')
    body = models.TextField(verbose_name='Текст')
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(verbose_name='Картинка')

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'


class Regulations(models.Model):
    num = models.CharField(max_length=200, verbose_name='№')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    file = models.FileField(verbose_name='Файл')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Приказы и Постановления'
        verbose_name_plural = 'Приказы и Постановления'



class Reports(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    file = models.FileField(verbose_name='Файл')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Отчеты'
        verbose_name_plural = 'Отчеты'

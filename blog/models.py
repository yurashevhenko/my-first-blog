from django.conf import settings   # импортируем код из файла settings
from django.db import models       # импортируем код из файла models
from django.utils import timezone  # импортируем код из файла timezone


class Post(models.Model): # определяет нашу модель, объект. Post — имя нашей модели. models.Model означает, что объект Post является моделью Django, так Django поймет, что он должен сохранить его в базу данных.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # ссылка на другую модель
    title = models.CharField(max_length=200)                                       # так мы определяем текстовое поле с ограничением на количество символов.
    text = models.TextField()                                                      #поле для неограниченно длинного текста
    created_date = models.DateTimeField(default=timezone.now)                      #дата и время
    published_date = models.DateTimeField(blank=True, null=True)                   #дата и время

    def publish(self): # функция\метод
        self.published_date = timezone.now()
        self.save()

    def __str__(self): # после вызова метода __str__() мы получим текст (строку) с заголовком записи.
        return self.title
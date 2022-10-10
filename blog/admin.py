from django.contrib import admin
from .models import Post # импортируем модель из models.py

admin.site.register(Post) #Чтобы модель стала доступна на странице администрирования, нужно зарегистрировать ее
# Register your models here.

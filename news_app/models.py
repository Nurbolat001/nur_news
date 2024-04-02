from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

from django.urls import reverse


class Post(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    image = models.CharField("Ссылка на изображение", max_length=500)
    description = models.TextField("Описание")
    post_date = models.DateTimeField("Дата публикации", default=datetime.now)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title


from django.db import models

class NewsAppUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username


class News:
    def __init__(self, title, content, pub_date):
        self.title = title
        self.content = content
        self.pub_date = pub_date

    def __str__(self):
        return f"{self.title} - {self.pub_date}"
# models.py
from django.db import models

class News(models.Model):
    photo = models.ImageField(upload_to='photos/')
    title = models.CharField(max_length=100)
    publication_date = models.DateField()
    description = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('delete_news', kwargs={'pk': self.pk})
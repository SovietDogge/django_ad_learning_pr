from django.db import models


class Category(models.Model):
    name = models.SlugField(max_length=150)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Location(models.Model):
    name = models.CharField(max_length=150)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Местонахождение'
        verbose_name_plural = 'Местонахождения'


class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, null=True)
    username = models.CharField(max_length=20, null=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    age = models.IntegerField()
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']


class Ad(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    description = models.TextField(null=True)
    is_published = models.BooleanField()
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ads/img/')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models

from ads.validators import ad_published_validate, check_birth_date, user_check_email, ad_name_validate

ADMIN = 'admin'
MODERATOR = 'moderator'
USER = 'user'
UNKNOWN = 'unknown'


class Category(models.Model):
    name = models.SlugField(max_length=150)
    slug = models.CharField(max_length=10, unique=True, validators=[MinValueValidator(5)], null=True)

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


class User(AbstractUser):
    ROLE = [(ADMIN, 'admin'), (MODERATOR, 'moderator'), (USER, 'user'), (UNKNOWN, 'unknown')]

    role = models.CharField(choices=ROLE, default=UNKNOWN)
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    username = models.CharField(max_length=100, unique=True, default=first_name)
    birth_date = models.DateField(validators=[check_birth_date], null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    email = models.CharField(validators=[user_check_email])

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']


class Ad(models.Model):
    name = models.CharField(max_length=150, validators=[ad_name_validate])
    price = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.TextField(null=True)
    is_published = models.BooleanField(validators=[ad_published_validate])
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='ads/img/')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Selection(models.Model):
    name = models.CharField(max_length=150)
    ad = models.ManyToManyField(Ad)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)

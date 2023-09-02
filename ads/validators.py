import datetime

from django.core.exceptions import ValidationError


def ad_published_validate(value):
    if value:
        ValidationError('Field cannot be True')


def check_birth_date(value: datetime.date):
    if datetime.date.today().year - value.year < 9:
        raise ValidationError('User must be older 9 year')


def user_check_email(value):
    email = value.split('@')[-1]
    if email == 'rumbler.ru':
        raise ValidationError('You cannot use rumbler.ru')


def ad_name_validate(value):
    if len(value) < 10:
        raise ValidationError('Name must have at least 10 symbols')

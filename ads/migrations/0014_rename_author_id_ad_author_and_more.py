# Generated by Django 4.2.4 on 2023-08-30 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0013_rename_location_id_user_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ad',
            old_name='author_id',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='ad',
            old_name='category_id',
            new_name='category',
        ),
    ]
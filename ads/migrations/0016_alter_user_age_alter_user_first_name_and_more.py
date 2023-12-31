# Generated by Django 4.2.4 on 2023-08-31 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0015_alter_user_managers_remove_user_role_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default=models.CharField(max_length=20, null=True), max_length=100, unique=True),
        ),
    ]

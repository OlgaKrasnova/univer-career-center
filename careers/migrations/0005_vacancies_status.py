# Generated by Django 3.1.5 on 2021-01-07 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0004_auto_20210107_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancies',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Статус'),
        ),
    ]

# Generated by Django 3.1.6 on 2021-02-24 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20210223_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='author',
        ),
        migrations.RemoveField(
            model_name='destination',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='destination',
            name='published_date',
        ),
    ]

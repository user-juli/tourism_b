# Generated by Django 3.1.6 on 2021-03-16 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_hotel_minimal_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='minimal_price',
            field=models.IntegerField(),
        ),
    ]

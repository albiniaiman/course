# Generated by Django 2.2.7 on 2019-12-22 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20191218_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cost',
            field=models.IntegerField(max_length=200),
        ),
    ]

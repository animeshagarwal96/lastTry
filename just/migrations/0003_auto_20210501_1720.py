# Generated by Django 3.1.7 on 2021-05-01 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('just', '0002_auto_20210501_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product_image',
            field=models.CharField(default='', max_length=100),
        ),
    ]

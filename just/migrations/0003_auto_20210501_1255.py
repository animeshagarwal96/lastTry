# Generated by Django 3.1.7 on 2021-05-01 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('just', '0002_auto_20210430_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size1',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='size2',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='size3',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='size4',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='size5',
            field=models.CharField(default='', max_length=100),
        ),
    ]
# Generated by Django 3.1.7 on 2021-04-28 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('just', '0003_auto_20210428_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='short_desc',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
    ]

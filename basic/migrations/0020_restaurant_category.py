# Generated by Django 3.0.4 on 2020-04-30 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0019_auto_20200429_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='category',
            field=models.CharField(max_length=30, null=True, verbose_name='Категория'),
        ),
    ]

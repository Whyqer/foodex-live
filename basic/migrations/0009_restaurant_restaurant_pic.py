# Generated by Django 3.0.4 on 2020-04-18 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0008_auto_20200418_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='restaurant_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

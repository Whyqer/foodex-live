# Generated by Django 3.0.4 on 2020-05-23 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0032_auto_20200523_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='category',
            field=models.CharField(choices=[('Горячие блюда', 'Горячие блюда'), ('Холодные блюда', 'Холодные блюда'), ('Закуски', 'Закуски'), ('Десерты', 'Десерты'), ('Напитки', 'Напитки')], max_length=30, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.FloatField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='weight',
            field=models.FloatField(verbose_name='Вес'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ordermenu',
            name='menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='basic.Menu'),
        ),
        migrations.AlterField(
            model_name='ordermenu',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='basic.Order'),
        ),
    ]

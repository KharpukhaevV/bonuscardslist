# Generated by Django 3.1.5 on 2021-01-20 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardslist', '0006_auto_20210120_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardslist',
            name='card_number',
            field=models.IntegerField(unique=True, verbose_name='Номер карты'),
        ),
    ]
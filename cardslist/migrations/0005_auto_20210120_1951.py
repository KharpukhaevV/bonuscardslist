# Generated by Django 3.1.5 on 2021-01-20 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardslist', '0004_auto_20210120_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardslist',
            name='card_number',
            field=models.CharField(max_length=12, verbose_name='Номер карты'),
        ),
    ]

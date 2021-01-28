# Generated by Django 3.1.5 on 2021-01-19 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardslist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardslist',
            name='card_issue_date',
            field=models.DateTimeField(verbose_name='Дата выпуска карты'),
        ),
        migrations.AlterField(
            model_name='cardslist',
            name='card_status',
            field=models.BinaryField(verbose_name='Статус карты'),
        ),
    ]

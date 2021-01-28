from django.db import models


class Cardslist(models.Model):
    card_series = models.IntegerField(verbose_name='Серия карты')
    card_number = models.IntegerField(verbose_name='Номер карты', unique=True)
    card_issue_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата выпуска карты')
    card_expiration_date = models.DateTimeField(verbose_name='Дата окончания активности карты')
    card_date_of_use = models.DateTimeField(verbose_name='Дата последнего использования карты')
    card_bonus_amount = models.FloatField(null=True, blank=True, verbose_name='Сумма бонуса карты')
    card_status = models.CharField(max_length=12, default='Не активна', verbose_name='Статус карты')

    class Meta:
        verbose_name_plural = 'Бонусные карты'
        verbose_name = 'Бонусная карта'
        ordering = ['-card_date_of_use']

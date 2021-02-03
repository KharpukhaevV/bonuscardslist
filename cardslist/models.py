from django.db import models


class CardsList(models.Model):
    card_series = models.IntegerField(verbose_name='Серия карты')
    card_number = models.IntegerField(verbose_name='Номер карты', unique=True)
    card_issue_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата выпуска карты')
    card_expiration_date = models.DateTimeField(verbose_name='Дата окончания активности карты')
    card_date_of_use = models.DateTimeField(verbose_name='Дата последнего использования карты', auto_now_add=True)
    card_bonus_amount = models.FloatField(null=True, blank=True, verbose_name='Сумма бонуса карты')
    card_status = models.CharField(max_length=12, default='Не активна', verbose_name='Статус карты')

    class Meta:
        verbose_name_plural = 'Бонусные карты'
        verbose_name = 'Бонусная карта'
        ordering = ['-card_date_of_use']

    def __str__(self):
        return 'Карта №' + str(self.card_number)


class CardDetail(models.Model):
    card = models.ForeignKey(CardsList, on_delete=models.CASCADE, verbose_name='Карта')
    date_last_use = models.DateTimeField(verbose_name='Дата последнего использования')
    purchase_amount = models.IntegerField(verbose_name='Сумма последней покупки')
    changing_amount_bonuses = models.IntegerField(verbose_name='Изменение суммы бонусов')

    class Meta:
        verbose_name_plural = 'Детали карт'
        verbose_name = 'Детали карты'
        ordering = ['-changing_amount_bonuses']

    def save(self, *args, **kwargs):
        self.card.card_date_of_use = self.date_last_use
        self.card.save()
        super(CardDetail, self).save(*args, **kwargs)

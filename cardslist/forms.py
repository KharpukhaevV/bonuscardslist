from django import forms


class CreateCardsForm(forms.Form):
    cards_series = forms.IntegerField(label='Серия карты', min_value=1000, max_value=9999)
    number_of_cards = forms.IntegerField(label='Количество создаваемых карт', min_value=1, max_value=100)
    cards_duration = forms.ChoiceField(label='Срок работы карт', choices=([('12', '12 месяцев'),
                                                                           ('6', '6 месяцев'),
                                                                           ('1', '1 месяц'), ]))
    bonus_amount = forms.IntegerField(label='Сумма бонуса', max_value=2500)

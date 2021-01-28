from django import forms
from django.forms import TextInput

from .models import Cardslist


class CreateCardsForm(forms.ModelForm):
    cards_series = forms.IntegerField(label='Серия карты', min_value=1000, max_value=9999)
    number_of_cards = forms.IntegerField(label='Количество создаваемых карт', min_value=1, max_value=100)
    cards_duration = forms.ChoiceField(label='Срок работы карт', choices=([('12', '12 месяцев'),
                                                                           ('6', '6 месяцев'),
                                                                           ('1', '1 месяц'), ]))
    bonus_amount = forms.IntegerField(label='Сумма бонуса', max_value=2500)

    class Meta:
        model = Cardslist
        fields = ('cards_series', 'number_of_cards', 'cards_duration', 'bonus_amount')


class CreateSearchForm(forms.Form):
    searchfield = forms.CharField(max_length=16)

    class Meta:
        fields = 'searchfield'
        widgets = {'searchfield': TextInput(attrs={
                'class': 'form-control form-control-dark w-50',
                'type': 'text',
                'placeholder': 'Поиск',
                'aria-label': 'Search'})}

import calendar
import random
import string

from datetime import datetime
from django.db import IntegrityError
from django.core.paginator import Paginator

from .models import CardsList


def get_random_card_number(series, date, amount):
    num = ''.join(random.choices(string.digits, k=8))
    n = int(str(series) + num)
    try:
        cards = CardsList(card_series=series,
                          card_number=n,
                          card_expiration_date=date,
                          card_bonus_amount=amount,
                          card_date_of_use=datetime.now())
        return cards
    except IntegrityError:
        get_random_card_number(series, date, amount)


def calculation_of_the_card_validity_period(months):
    sourcedate = datetime.now()
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year, month)[1])
    return datetime(year, month, day)


def create_random_cards(form):
    cards_series = form.cleaned_data.get('cards_series')
    number_of_cards = form.cleaned_data.get('number_of_cards')
    cards_duration = form.cleaned_data.get('cards_duration')
    bonus_amount = form.cleaned_data.get('bonus_amount')

    delta = int(cards_duration)
    date = calculation_of_the_card_validity_period(delta)

    for i in range(number_of_cards):
        cards = get_random_card_number(cards_series, date, bonus_amount)
        cards.save()


def pagination(request, model):
    paginator = Paginator(model, 19)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {'cards': page.object_list, 'page': page, 'p': paginator}
    return context

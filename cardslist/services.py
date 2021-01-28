import calendar
import random
import string

from datetime import datetime
from django.db import IntegrityError

from .models import Cardslist


def get_random_card_number(series, date, amount):
    num = ''.join(random.choices(string.digits, k=8))
    n = int(str(series) + num)
    try:
        cards = Cardslist(card_series=series,
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

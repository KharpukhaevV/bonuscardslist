from django.contrib import admin
from .models import Cardslist


class CardsListAdmin(admin.ModelAdmin):
    list_display = ('card_series', 'card_number', 'card_issue_date', 'card_expiration_date', 'card_date_of_use',
                    'card_bonus_amount', 'card_status')
    search_fields = ('card_series', 'card_number')


admin.site.register(Cardslist, CardsListAdmin)

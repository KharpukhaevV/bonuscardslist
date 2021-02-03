from django.contrib import admin
from .models import CardsList, CardDetail


class CardsListAdmin(admin.ModelAdmin):
    list_display = ('card_series', 'card_number', 'card_issue_date', 'card_expiration_date', 'card_date_of_use',
                    'card_bonus_amount', 'card_status')
    search_fields = ('card_series', 'card_number')


class CardsDetailsAdmin(admin.ModelAdmin):
    list_display = ('card', 'date_last_use', 'purchase_amount', 'changing_amount_bonuses')


admin.site.register(CardsList, CardsListAdmin)
admin.site.register(CardDetail, CardsDetailsAdmin)

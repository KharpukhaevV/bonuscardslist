from django.shortcuts import render
from django.views.generic import DetailView
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Cardslist
from .forms import CreateCardsForm, CreateSearchForm
from .services import calculation_of_the_card_validity_period, get_random_card_number


class CardDetailView(LoginRequiredMixin, DetailView):
    model = Cardslist
    template_name = 'cardslist/carddetails.html'
    context_object_name = 'details'


@login_required()
def index(request):
    if request.method == 'POST':
        search_form = CreateSearchForm(request.POST)
        if search_form.is_valid():
            field = int(search_form.cleaned_data.get('searchfield'))
            cards = Cardslist.objects.filter(card_number=field, card_series=field)
            paginator = Paginator(cards, 15)
            if 'page' in request.GET:
                page_num = request.GET['page']
            else:
                page_num = 1
            page = paginator.get_page(page_num)
            context = {'cards': page.object_list, 'page': page, 'form': search_form}
            return render(request, 'cardslist/index.html', context)
    else:
        search_form = CreateSearchForm()
        cards = Cardslist.objects.all()
        paginator = Paginator(cards, 15)
        if 'page' in request.GET:
            page_num = request.GET['page']
        else:
            page_num = 1
        page = paginator.get_page(page_num)
        context = {'cards': page.object_list, 'page': page, 'form': search_form}
        return render(request, 'cardslist/index.html', context)


@login_required()
def add_and_save(request):
    if request.method == 'POST':
        cards_form = CreateCardsForm(request.POST)
        if cards_form.is_valid():

            cards_series = cards_form.cleaned_data.get('cards_series')
            number_of_cards = cards_form.cleaned_data.get('number_of_cards')
            cards_duration = cards_form.cleaned_data.get('cards_duration')
            bonus_amount = cards_form.cleaned_data.get('bonus_amount')

            delta = int(cards_duration)
            date = calculation_of_the_card_validity_period(delta)

            for i in range(number_of_cards):
                cards = get_random_card_number(cards_series, date, bonus_amount)
                cards.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            context = {'form': cards_form}
            return render(request, 'cardslist/create.html', context)
    else:
        cards_form = CreateCardsForm()
        context = {'form': cards_form}
        return render(request, 'cardslist/create.html', context)


@login_required()
def delete(request, pk):
    card = Cardslist.objects.get(pk=pk)
    card.delete()

    return HttpResponseRedirect(reverse('index'))


@login_required()
def activate(request, pk):
    card = Cardslist.objects.get(pk=pk)
    if card.card_status == 'Не активна':
        card.card_status = 'Активна'
    elif card.card_status == 'Активна':
        card.card_status = 'Не активна'
    card.save()
    return HttpResponseRedirect(reverse('index'))

from django.shortcuts import render
from django.views.generic import DetailView
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from .models import Cardslist
from .forms import CreateCardsForm
from .services import create_random_cards, pagination


class CardDetailView(LoginRequiredMixin, DetailView):
    model = Cardslist
    template_name = 'cardslist/carddetails.html'
    context_object_name = 'details'


@login_required()
def index(request):
    search_query = request.GET.get('search', '')
    if search_query:
        cards = Cardslist.objects.filter(Q(card_series=search_query) | Q(card_number=search_query))
        context = {'cards': cards}
    else:
        cards = Cardslist.objects.all()
        context = pagination(request, cards)
    return render(request, 'cardslist/index.html', context)


@login_required()
def activation_cards(request):
    action = request.GET.get('action')
    if request.method == 'POST':
        not_active_cards = request.POST.getlist('activate')
        for pk in not_active_cards:
            card = Cardslist.objects.get(pk=pk)
            card.card_status = 'Активна'
            card.save()
    elif action == '':
        cards = Cardslist.objects.filter(card_status='Не активна')
        for card in cards:
            card.card_status = 'Активна'
            card.save()
        return HttpResponseRedirect(reverse('index'))
    cards = Cardslist.objects.filter(card_status='Не активна')
    context = pagination(request, cards)
    return render(request, 'cardslist/activation.html', context)
    

@login_required()
def add_and_save_cards(request):
    if request.method == 'POST':
        cards_form = CreateCardsForm(request.POST)
        if cards_form.is_valid():
            create_random_cards(cards_form)
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


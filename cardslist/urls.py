from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CardDetailView, index, add_and_save_cards, activation_cards, delete, activate


urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', CardDetailView.as_view(), name='card_detail'),
    path('activation/', activation_cards, name='activation'),
    path('add/', add_and_save_cards, name='add'),
    path('del/<int:pk>/', delete, name='delete'),
    path('activate/<int:pk>/', activate, name='activate'),
    path('accounts/logout/', LogoutView.as_view(next_page=index), name='logout'),
]

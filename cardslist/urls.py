from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import activate_all, index, CardDetailView, add_and_save, delete, activate, activation


urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', CardDetailView.as_view(), name='card_detail'),
    path('activation/', activation, name='activation'),
    path('add/', add_and_save, name='add'),
    path('del/<int:pk>/', delete, name='delete'),
    path('activate/<int:pk>/', activate, name='activate'),
    path('accounts/logout/', LogoutView.as_view(next_page=index), name='logout'),
    path('activate_all/', activate_all, name='activate_all')
]

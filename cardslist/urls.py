from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import index, CardDetailView, add_and_save, delete, activate, post_search


urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>', CardDetailView.as_view(), name='card_detail'),
    path('add/', add_and_save, name='add'),
    path('del/<int:pk>', delete, name='delete'),
    path('activate/<int:pk>', activate, name='activate'),
    path('accounts/logout/', LogoutView.as_view(next_page=index), name='logout'),
    path('test/', post_search, name='search')
]

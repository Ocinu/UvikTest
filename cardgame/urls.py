from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game', views.new, name='new_game'),
    path('next_turn', views.next_turn, name='next_turn')
]

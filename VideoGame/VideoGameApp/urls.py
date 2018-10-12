from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new_game, name='new_game'),
    path('edit/', views.edit_game, name='edit_game'),
]
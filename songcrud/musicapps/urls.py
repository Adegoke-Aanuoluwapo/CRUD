from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:name>', views.greet, name='greet'), 
    path('Ann', views.Ann, name='Ann'),
    path('Emma', views.Emma, name='Emma')
]
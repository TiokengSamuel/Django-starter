from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='home'),i
    path('add',views.add, name='add')
]
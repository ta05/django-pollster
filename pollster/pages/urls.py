from django.urls import path

from . import views

# Routes
urlpatterns = [
    path('', views.index, name='index'),
]
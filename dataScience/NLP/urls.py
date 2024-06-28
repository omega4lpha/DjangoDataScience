from django.urls import path
from . import views

urlpatterns = [
    path('procesamiento/', views.procesamiento_nlp, name='procesamiento_nlp'),
    # Añade más paths según tus necesidades
]

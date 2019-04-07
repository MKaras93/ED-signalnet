from django.urls import path
from api import views

urlpatterns = [
    path('signals/', views.Signals.as_view(), name='signals')
    ]
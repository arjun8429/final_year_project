# predictor/urls.py
from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
    path('predict/', views.predict_eligibility, name='predict_eligibility'),
]

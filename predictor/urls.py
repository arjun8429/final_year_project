from django.urls import path
from . import views
from .views import profile_view

urlpatterns = [
    path('', views.home, name='home'),
    path('predict/', views.predict_eligibility, name='predict_eligibility'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('profile/', profile_view, name='profile'),
    # path('logout/', views.logout_view, name='logout'),
    path('homepage/', views.homepage, name='homepage'),
    path('logout/', views.logout_view, name='Logout'),
]
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.home_view, name='home'),
    path('registration/', views.registration_view, name='registration'),
    path('logout/', views.user_logout, name='logout')
]

from . import views
from django.urls import path


urlpatterns = [
    
    path('',views.home_view, name='home'),
    path('login',views.login, name='login'),
     path('register',views.register, name='register'),
]

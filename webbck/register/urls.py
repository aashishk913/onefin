from django.urls import path
from register.api import RegisterApi
from register.authen import SimpleApI
from . import views 
from register import movies 
urlpatterns = [
    #path('', views.register, name='register'),
    path('api/register', RegisterApi.as_view()),
    path('authen/', SimpleApI.as_view() ),
    path('',  movies.func),
]
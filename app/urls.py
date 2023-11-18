from django.urls import path
from app.views import *

urlpatterns=[
    path('Login/',Login,name='Login'),
]
from django.urls import path
from .views import *

app_name = 'mein'


urlpatterns = [
    path('',HomepageView.as_view(),name='home'),
   
]



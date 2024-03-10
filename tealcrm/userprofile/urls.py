from django.urls import path
from django.contrib.auth import views

from userprofile.views import login_view

urlpatterns = [
    path('log-in/', login_view, name='login'),

]
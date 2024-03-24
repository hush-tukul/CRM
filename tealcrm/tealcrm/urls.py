
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from core.views import index, about, clients, estate
from userprofile.views import signup
from userprofile.views import login_view

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/leads/', include('lead.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('about/', about, name='about'),
    path('sign-up/', signup, name='signup'),
    path('log-in/', login_view, name='login'),
    path('log-out/',
         views.LogoutView.as_view(),
         name='logout'
         ),
    path("admin/", admin.site.urls),
    path('clients/', clients, name='clients'),
    path('estate/', clients, name='estate'),
]

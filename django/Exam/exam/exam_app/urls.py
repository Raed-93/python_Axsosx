from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('success', views.success),
    path('destroy', views.logout),
    path('dashbord', views.login),
    path('sightings/new',views.sightings),
    path('new',views.new_creat),
    path('view',views.view),
    path('page',views.page),
    
   
]
from django.urls import path
from . import views

urlpatterns = [
    path('',views.app),
    path('index',views.index),
    path('show',views.show)

]
from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('result',views.create_result),
    path('succes',views.succes),
]

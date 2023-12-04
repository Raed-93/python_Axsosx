from django.urls import path
from . import views
urlpatterns = [
  path('shwo/new',views.shwo_new),
  path('shwo',views.shwo_creat), 
  path('shwo/<int:id>',views.shwo), 
  path('shwos',views.shwos),
  path('show/<int:id>/eidt',views.eidt_show),
  path('updat<int:id>',views.update),
  
]
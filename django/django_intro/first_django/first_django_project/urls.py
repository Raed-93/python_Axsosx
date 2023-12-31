from django.urls import path
from  . import views 
urlpatterns = [
    path('',views.root),
    path('blog', views.root),
    path('blog/new',views.new),
    path('blog/create',views.create),
    path('blog/<int:number>',views.show),
    path('blog/<int:number>/edit',views.edit),
    path('blog/<int:number>/delete',views.destroy),
    path('redirected_route', views.redirected_method),
]

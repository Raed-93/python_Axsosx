from django.urls import path
from . import views
urlpatterns = [
    path('',views.app),
    path('index',views.index),
    path('authors',views.authors),
    path('books/<book_id>',views.php),
    path('add_author',views.add_author),
    path('authors/<author_id>',views.hello),
    
]
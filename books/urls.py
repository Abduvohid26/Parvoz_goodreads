from django.urls import path
from . import views

urlpatterns = [
    path('', views.books, name='books'),
    path('<int:id>/', views.book_detail, name='book_detail'),
    path('<int:id>/comments', views.book_comments, name='comment')
]
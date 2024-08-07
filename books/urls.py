from django.urls import path
from . import views

urlpatterns = [
    path('', views.books, name='books'),
    path('<int:id>/', views.book_detail, name='book_detail'),
    path('book_add/', views.BookAdd.as_view(), name='book_add'),
    path('<int:id>/comments', views.book_comments, name='comment'),
    path('<int:book_id>/<int:comment_id>/delete', views.comment_delete, name='comment_delete'), 
    path('<int:comment_id>/edit', views.comment_edit, name='comment_edit'), 
]
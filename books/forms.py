from django import forms
from .models import Comment, Book


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'star']


class BookForm(forms.ModelForm):
    class Meta:
        model =  Book
        fields = ['title', 'description', 'isbn', 'cover_pic']
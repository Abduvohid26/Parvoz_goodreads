from django.shortcuts import render, redirect
from .models import Book, Comment
from django.views import  View
from .forms import CommentForm
from django.contrib import messages
def books(request):
    book = Book.objects.all()
    context = {'books': book}
    return render(request=request, template_name='books.html', context=context)


def book_detail(request, id):
    book = Book.objects.get(id=id)
    form = CommentForm()
    context = {'book': book, 'form': form}
    return render(request, 'book_detail.html', context)

def book_comments(request, id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        user = request.user
        book = Book.objects.get(id=id)
        if form.is_valid():
            Comment.objects.create(
                user=user,
                book=book,
                text=form.cleaned_data['text'],
                star=form.cleaned_data['star'],
            )
            messages.success(request, 'Comment added successfully')
            return redirect('book_detail', id=id)
        return render(request, 'book_detail', context={'book': book, 'form': form})


from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Book, Author, Genre
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, get_user_model
import os
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from cart.forms import CartAddBookForm


def home(request):
    most_popular_books = Book.objects.exclude(quantity__exact=0)[:16]
    return render(request, 'index.html', context={'most_popular_books': most_popular_books}, )


def post_list(request):
    search_query = request.GET.get('q', '')
    if search_query:
        selected_books = Book.objects.filter(Q(title__icontains=search_query))
    else:
        selected_books = Book.objects.all()
    return render(request, 'book_list.html', context={'all_books': selected_books}, )


def books(request):
    all_books = Book.objects.all()
    return render(request, 'book_list.html', context={'all_books': all_books}, )


def authors(request):
    all_authors = Author.objects.all()
    return render(request, 'author_list.html', context={'all_authors': all_authors}, )


def genres(request):
    all_genres = Genre.objects.all()
    return render(request, 'genre_list.html', context={'all_genres': all_genres}, )


# class BookDetailView(generic.DetailView):
#    model = Book
def exp_book(request, pk):
    book = Book.objects.get(id=pk)
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)
    return render(request, 'shop/book_detail.html', locals(), )


class AuthorDetailView(generic.DetailView):
    model = Author


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print(request.POST)
    return JsonResponse(return_dict)


"""
def book_det(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'shop/book_detail.html', locals())
    

def BookDetail(request, iD, slug):
    book = get_object_or_404(Book, id=iD, slug=slug, available=True)
    cart_book_form = CartAddBookForm()
    return render_to_response('shop/book_detail.html',
                              {'book': book,
                               'cart_book_form': cart_book_form})
"""


def book_detail(request, pk):
    book = get_object_or_404(Book,
                             pk=pk,
                             )
    cart_book_form = CartAddBookForm()
    return render(request, 'shop/book_detail.html', {'book': book,
                                                     'cart_book_form': cart_book_form})


@login_required
def profile(request):
    render(request, 'profile.html', {'userfileslist': os.listdir(get_user_model().username)})
# Create your views here.

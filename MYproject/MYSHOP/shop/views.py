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
from .forms import buyForm

def home(request):
    most_popular_books = Book.objects.exclude(quantity__exact=0)[:16]
    return render(request, 'index.html', context={'most_popular_books': most_popular_books}, )


def post_list(request):
    search_query = request.GET.get('q', '')
    if search_query:
        selected_books = Book.objects.filter(Q(title__icontains=search_query) | Q(author__last_name=search_query)| Q(author__first_name=search_query))
    else:
        selected_books = Book.objects.all()
    return render(request, 'book_list.html', context={'all_books': selected_books}, )

def author_book(request,pk):
    book = Book.objects.get(id=pk)
    if book:
        selected_books = Book.objects.filter(Q(author__last_name=book.author.last_name))
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
    return render(request, 'shop/book_detail.html', locals(),)




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
            return redirect('/shop')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print(request.POST)
    return JsonResponse(return_dict)


def book_det(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'shop/book_detail.html', locals())
    

def BookDetail(request, iD, slug):
    book = get_object_or_404(Book, id=iD, slug=slug, available=True)
    cart_book_form = CartAddBookForm()
    return render_to_response('shop/book_detail.html',
                              {'book': book,
                               'cart_book_form': cart_book_form})



def book_detail(request, pk):
    book = get_object_or_404(Book,
                             pk=pk,
                             )
    cart_book_form = CartAddBookForm()
    return render(request, 'shop/book_detail.html', {'book': book,
                                                     'cart_book_form': cart_book_form})

def buy(request):
    if request.method == "POST":
        form = buyForm(request.POST)
        if form.is_valid():
            book_id = form.cleaned_data['book_id']
            book = Book.objects.get(id=book_id)
            quantity = form.cleaned_data['num']
            total_price = quantity*book.cost
            return render(request, 'shop/buy_book.html', context={'book': book, 'quantity': quantity, 'total_price': total_price}, )


@login_required
def profile(request):
    render(request, 'profile.html', {'userfileslist': os.listdir(get_user_model().username)})
# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Book
from .cart import Cart
from .forms import CartAddBookForm


@require_POST
def CartDetail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', context={'cart': cart})


def CartAdd(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    form = CartAddBookForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(book=book, quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:CartDetail')


def CartRemove(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    cart.remove(book)
    return redirect('cart:CartDetail')


def CartDetail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', context={'cart': cart})

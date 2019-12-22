from decimal import Decimal
from django.conf import settings
from shop.models import Book


class Cart(object):
    def init(self, request):
        # Инициализация корзины пользователя
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Сохраняем корзину пользователя в сессию
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    # Добавление товара в корзину пользователя или обновление количества товара

    def add(self, book, quantity=1, update_quantity=False):
        book_id = str(book.id)
        if book_id not in self.cart:
            self.cart[book_id] = {'quantity': 0,
                                  'cost': str(book.cost)}
        if update_quantity:
            self.cart[book_id]['quantity'] = quantity
        else:
            self.cart[book_id]['quantity'] += quantity
        self.save()

    # Сохранение данных в сессию
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        # Указываем, что сессия изменена
        self.session.modified = True

    def remove(self, book):
        book_id = str(book.id)
        if book_id in self.cart:
            del self.cart[book_id]
            self.save()


# Итерация по товарам
def iter(self):
    book_ids = self.cart.keys()
    books = Book.objects.filter(id__in=book_ids)
    for book in books:
        self.cart[str(book.id)]['book'] = book

    for item in self.cart.values():
        item['cost'] = Decimal(item['cost'])
        item['total_cost'] = item['cost'] * item['quantity']
        yield item


# Количество товаров
def len(self):
    return sum(item['quantity'] for item in self.cart.values())


def get_total_cost(self):
    return sum(Decimal(item['cost']) * item['quantity'] for item in self.cart.values())


def clear(self):
    del self.session[settings.CART_SESSION_ID]
    self.session.modified = True
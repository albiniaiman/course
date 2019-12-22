from django.contrib import admin
from .models import Author, Genre, Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'quantity')


admin.site.register(Book, BookAdmin)
# Define the admin class


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
# Register your models here.

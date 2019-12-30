from django import forms
from .models import Book

class buyForm(forms.Form):
    num = forms.IntegerField()
    book_id = forms.IntegerField()

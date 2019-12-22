from django.shortcuts import render

def home(request):
    return render(request, 'registration\index.html')

# Create your views here.

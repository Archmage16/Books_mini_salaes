from django.shortcuts import render
from .models import Book
from .forms import SearchForm
from datetime import datetime
from django.contrib import messages
from django.core import signing

def home(request):
    username = request.COOKIES.get('username', 'Неизвестный пользователь')
    return render(request, 'home.html', {'username': username})

def book_list(req):
    books = Book.objects.all()

    last_visit = req.COOKIES.get('last_visit', 'Первый раз?')
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    messages.info(req, f"Ваш предыдущий визит: {last_visit}")



    visits = int(req.COOKIES.get('visits', 0))+1
    signed_visits = signing.dumps({"visits": visits})

    context = {'books': books, 
               'visits': visits,
               'last_visit': last_visit,
               'signed_visits': signed_visits,}
    response = render(req, 'book_list.html',context=context)
    
    response.set_cookie('last_visit', now, max_age=60*60*24*30)
    response.set_cookie('visits', visits, max_age=3600*24*30)

    return response


def search_books(request):
    form = SearchForm(request.GET)
    results = []

    if request.GET and form.is_valid():
        query = form.cleaned_data['query']
        results = Book.objects.filter(title__icontains=query)

    return render(request, 'search.html', {'form': form, 'results': results})
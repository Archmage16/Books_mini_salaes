from django.shortcuts import render
from .models import Book
from .forms import SearchForm

def home(request):
    return render(request, 'home.html')

def search_books(request):
    form = SearchForm(request.GET)
    results = []

    if request.GET and form.is_valid():
        query = form.cleaned_data['query']
        results = Book.objects.filter(title__icontains=query)

    return render(request, 'search.html', {'form': form, 'results': results})

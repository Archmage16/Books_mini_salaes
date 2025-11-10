from django.shortcuts import render, redirect
from .forms import AuthorForm, PublisherForm, BookForm, PublicationForm, SalesForm
from .models import Author, Book, Publisher, Publication, Sales


def home(request):
    return render(request, "home.html")


def author_list(request):
    authors = Author.objects.all()
    return render(request, "author_list.html", {"authors": authors})


def author_create(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("author_list")
    return render(request, "form.html", {"form": form})


def publisher_list(request):
    publishers = Publisher.objects.all()
    return render(request, "publisher_list.html", {"publishers": publishers})


def publisher_create(request):
    form = PublisherForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("publisher_list")
    return render(request, "form.html", {"form": form})


def book_list(request):
    books = Book.objects.select_related("author")
    return render(request, "book_list.html", {"books": books})


def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("book_list")
    return render(request, "form.html", {"form": form})


def publication_list(request):
    publications = Publication.objects.select_related("book", "publisher")
    return render(request, "publication_list.html", {"publications": publications})


def publication_create(request):
    form = PublicationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("publication_list")
    return render(request, "form.html", {"form": form})


def sales_list(request):
    sales = Sales.objects.select_related("publication")
    return render(request, "sales_list.html", {"sales": sales})


def sales_create(request):
    form = SalesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("sales_list")
    return render(request, "form.html", {"form": form})

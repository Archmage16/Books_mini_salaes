from django.forms import ModelForm
from .models import Author, Book, Publisher, Publication, Sales


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ["full_name", "birth_year"]


class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        fields = ["name"]


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "genre", "year_written"]


class PublicationForm(ModelForm):
    class Meta:
        model = Publication
        fields = ["book", "publisher", "publish_date", "copies"]


class SalesForm(ModelForm):
    class Meta:
        model = Sales
        fields = ["publication", "year", "price", "qty_sold"]

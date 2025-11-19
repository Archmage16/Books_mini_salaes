from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label="Поиск", max_length=100)

class DynamicBookForm(forms.Form):
    title = forms.CharField(label='Название книги', max_length=100)
    author = forms.CharField(label='Автор', max_length=100)
    year = forms.IntegerField(label='Год издания')

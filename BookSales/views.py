from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Book, Author, Publisher
# Create your views here.
class IndexView(TemplateView):
    template_name = 'bookSales/mainBooks.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Books'] = Book.objects.all()
        
        return context
    
    
    
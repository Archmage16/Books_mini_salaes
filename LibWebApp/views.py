from django.shortcuts import render, redirect # redirect( 'home' )
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from .forms import *
from .models import *


def home( req ):
    return HttpResponse( 'Home page' )

def input_author( req : HttpRequest ) -> HttpResponse:
    if req.method == 'GET':
        return render( req, template_name='form_author.html',
                       context={ 'form' : FormAuthor(),
                                 'Title' : 'Введите информацию о новом авторе' })
    if req.method == 'POST':
        form = FormAuthor( req.POST, req.FILES )
        if form.is_valid():
            form.save()
            return render( req, template_name='form_author.html',
                    context={ 'form' : FormAuthor(),
                    'Title' : 'Инф. об авторе сохранена в БД успешно!\n' \
                              'Введите информацию о новом авторе' })
        return render( req, template_name='form_author.html',
                      context={
                        'form' : form,
                        'Title' : 'Ошибки при вводе!' \
                        '<br>Введите корректную информацию об авторе' })
    return HttpResponseBadRequest( 'Ошибочный тип запроса - не GET/POST' )        


def input_book( req : HttpRequest ) -> HttpResponse:
    if req.method == 'GET':
        return render( req, template_name='form_book.html',
                       context={ 'form' : FormBook(), 'Title' : 'Введите информацию о новой книге' })
        
    if req.method == 'POST':
        form = FormBook( req.POST, req.FILES )
        if form.is_valid():
            form.save()
            return render( req, template_name='form_book.html',
                    context={ 'form' : FormBook(), 'Title' : 'Инф. об книге сохранена в БД успешно!\n' \
                              'Введите информацию о новой книге' })
            
        return render( req, template_name='form_book.html',
                      context={
                        'form' : form,
                        'Title' : 'Ошибки при вводе! Введите корректную информацию о новой книге' })
        
        
    return HttpResponseBadRequest( 'Ошибочный тип запроса - не GET/POST' )
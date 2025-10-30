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

def input_book(req: HttpRequest) -> HttpResponse:
    if req.method == 'GET':
        return render(req, 'form_book.html', {
            'form': FormBook(),
            'Title': 'Введите информацию о новой книге'
        })

    elif req.method == 'POST':
        form = FormBook(req.POST, req.FILES)

        if form.is_valid():
            book = form.save(commit=False)  # сначала создаём объект, но не сохраняем в БД

            # если пользователь загрузил изображение в форме
            if 'cover_blob' in req.FILES:
                image = req.FILES['cover_blob']
                book.cover_blob = image.read()  # читаем файл как байты и сохраняем в поле BinaryField

            book.save()  # теперь сохраняем в БД

            return render(req, 'form_book.html', {
                'form': FormBook(),
                'Title': 'Информация о книге сохранена успешно! Введите новую книгу'
            })

        # если форма невалидна
        return render(req, 'form_book.html', {
            'form': form,
            'Title': 'Ошибки при вводе! Введите корректную информацию о книге'
        })

    return HttpResponseBadRequest('Ошибочный тип запроса — не GET/POST')


import base64
from django.shortcuts import get_object_or_404
def show_cover(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if not book.cover_blob:
        return HttpResponse("Нет изображения")

    # Конвертируем байты в base64 здесь, во вьюшке
    image_base64 = base64.b64encode(book.cover_blob).decode('utf-8')

    return render(request, 'show_image.html', {'image_base64': image_base64,
                                               'image_data': book.cover_blob})


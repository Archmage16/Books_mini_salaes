from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator


class Author( models.Model ):

    fio = models.CharField( max_length=100,
                            verbose_name='Автор',
                            blank=False, null=False,
                            db_index=True, 
                            validators=[ MinLengthValidator(3),
                                RegexValidator( r'^[A-Za-zА-Яа-я-\s]+$' ) ]
                          )
    birth_date = models.DateField( verbose_name='Дата рождения',
                                   blank=True, null=True )
    counrty = models.CharField( max_length=100, verbose_name='Страна рождения',
                                blank=True, null=True )
    # поле ссылки на файл изображения, хранящемся на дисковом устройстве/url
    photo = models.ImageField( upload_to='my_media/images', verbose_name='Фото автора',
                               blank=True, null=True )
    # небольшое изображение - битовое поле/байтовый массив - храниться в БД (BLOB)
    avatar = models.BinaryField( verbose_name='Аватарка автора', null=True )

    def __str__(self) -> str:
        return f'{self.fio}'
    
    class Meta:
        managed = True
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    pass # class Author( models.Model )


class Book( models.Model ):
    name = models.CharField( max_length=200, verbose_name='Название книги' )
    id_author = models.ForeignKey( 'Author',
                                   on_delete=models.SET_NULL, null=True )
    year  = models.DateField( verbose_name='Год издания' )
    cover = models.ImageField( upload_to='images', verbose_name='Обложка',
                               blank=True, null=True )
    cover_blob = models.BinaryField( verbose_name='Обложка в БД',
                                   blank=True, null=True )
    file = models.FileField( upload_to='pdf', verbose_name='Файл книги',
                             blank=True, null=True )
    info = models.TextField( verbose_name='Описание книги',
                             blank=True, null=True )
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    class Meta:
        managed = True
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    pass # class Book( models.Model )



from django import forms
from django.forms import widgets
from .models import *  
import datetime

class FormAuthor( forms.ModelForm ):
    # валидатор для поля birth_date
    # ???????
    def clean_birth_date(self ):
        val = self.cleaned_data.get('birth_date')
        if val > datetime.date.today():
            raise forms.ValidationError( 'Неверная дата!' )
        return val

    class Meta:
        model   = Author
        fields  = '__all__'
        widgets = { 'birth_date' : widgets.DateInput(), }

    pass # class FormAuthor( forms.ModelForm )

class FormBook( forms.ModelForm ):
    class Meta:
        model = Book
        fields = '__all__'
    pass

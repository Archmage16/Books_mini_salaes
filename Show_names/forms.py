# swWebApi/forms.py
from django import forms
from .models import Character

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'species', 'homeworld', 'birth_year', 'age']
        
    def clean_name(self):
        name = self.cleaned_data['name']
        if name[0].isdigit():
            raise forms.ValidationError("Имя не может начинаться с цифры.")
        return name

from django.shortcuts import render
from .forms import CharacterForm
import requests
from django.http import HttpResponse
# Create your views here.


def index(request):
    response = requests.get('https://www.swapi.tech/api/people')
    data = response.json()

    characters = data.get("results", [])
    return render(request, 'index.html', {'characters': characters})


def character_detail(request, char_id):
    response = requests.get(f"{'https://www.swapi.tech/api/people'}/{char_id}")
    data = response.json()
    character = data.get("result", {}).get("properties", {})

    return render(request, 'character_detail.html', {'character': character})


def add_character(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Character added successfully!")
        else:
            return render(request, 'character_f.html', {'form': form})
    else:
        form = CharacterForm()
    return render(request, 'character_f.html', {'form': form})

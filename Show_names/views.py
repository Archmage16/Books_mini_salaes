from django.shortcuts import render

import requests
# Create your views here.

BASE_URL = ""

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

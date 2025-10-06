from django.shortcuts import render

# Create your views here.
def main_page(request):
    return render(request, 'main_page.html')

def history_info(request):
    return render(request, 'history.html')
def info_1885(request):
    return render(request, 'history/eight.html')
def info_1914(request):
    return render(request, 'history/nine.html')


def cities_info(request):
    return render(request, 'cities.html')
def Paris_info(request):
    return render(request, 'cities/Paris.html')
def Marseille_info(request):
    return render(request, 'cities/Marseille.html')

def Paris_1924(request):
    return render(request, 'cities/Paris_1924.html')
def Marseille_1956(request):
    return render(request, 'cities/Marseille_1956.html')


def facts_info(request):
    return render(request, 'facts.html')


from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime

def get_time(request):
    now = datetime.now().strftime("%H:%M:%S")
    return JsonResponse({"time": now})

def get_date(request):
    today = datetime.now().strftime("%Y-%m-%d")
    return JsonResponse({"date": today})

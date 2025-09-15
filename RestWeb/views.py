from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse, request, HttpResponse
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmpSerializers
from .models import Employer
from django.http import Http404
# Create your views here.

# @api_view['GET']
def home(request):
    return HttpResponse('<h1>Welcome</h1>')

def EmployerView(req: request):
    if req.method == 'GET':
        data_empl = Employer.objects.all()
        seri = EmpSerializers(data_empl, many = True)
        return JsonResponse(seri.data, safe=False)
    elif req.method == 'POST':
        data_empl = req.data
        seri = EmpSerializers(data=data_empl)
        if seri.is_valid():
            seri.save()
            return HttpResponse('Everything is okey!')
        else:
            return Response(seri.errors, status=status.HTTP_400_BAD_REQUEST)

    pass

def OneEmployerView(req : request, id : int):
    match req.method:
        case 'GET': 
            # emp = Employer.objects.filter(pk = id).all()
            emp = Employer.objects.get(pk = id)
            if emp is not None:
                seri = EmpSerializers(emp, many = False)    
                # return Response(data = seri.data, status=status.HTTP_200_OK) 
                return JsonResponse(seri.data, safe=False) 
            else:
                return HttpResponse('Данных нету :)')
            
        case 'POST': 
            return Response("No", status=status.HTTP_400_BAD_REQUEST)
    pass
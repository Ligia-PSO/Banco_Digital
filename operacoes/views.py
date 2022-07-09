from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def index(request):
    if request.method=='POST':
        return HttpResponse("Hello world!")
    elif request.method=='GET':
        return JsonResponse({'teste':'resultado do teste'})

# Create your views here.

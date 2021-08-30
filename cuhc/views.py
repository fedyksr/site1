from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader

# Create your views here.
def cuhcpage(request):
    return render(request,'index1.html')
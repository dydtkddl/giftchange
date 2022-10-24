from django.shortcuts import render
from .models import *
from django.forms.models import model_to_dict
from django.http import JsonResponse
# Create your views here.
def first(request):

    a = Typelist.objects.all()
    return render(request, 'app/first.html', {'a':a})
def second(request):
    
    return render(request, 'app/second.html')
def filterbrand(request):
    type = request.GET.get('type')
    a = Brandlist.objects.filter(category__contains = type)
    data =[]
    for i in a:
        i = model_to_dict(i)
        data.append(i)
    return JsonResponse(data, safe = False)

  


from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello_world(request):
    if request.method == 'POST' :
        return render(request, 'accountapp/hello_world.html', context={'text': 'POST METHOD'})
    else :
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD'})
from django.contrib.contenttypes import views
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic.list import ListView


def mainpage(request):
    msg = request.GET['name']
    msg2 = request.GET['message']
    return render(request, 'travel_app/anotherpage.html', {'name': msg, 'message': msg2})

def welcome(request):
    return redirect('/hello?name=Recruto&message=Давай+дружить')
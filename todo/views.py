from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def todoView(request):
    render(request, 'todo.html')

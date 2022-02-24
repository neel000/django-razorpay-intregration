from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import get_object_or_404
from django.dispatch import receiver
from django.contrib import messages
# Create your views here.



def homeIndex(request):
    return render(request, 'home/homeIndex.html')

from django.shortcuts import render, redirect,session
import random

# Create your views here.
def index(request):
    return render(request,'index.html',context)
def earn(request, *args):
    return redirect('/')
def gamble(request):
    return redirect('/')

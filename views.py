from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def show_loop(request, count):
    numbers = range(1, count + 1)
    return render(request, 'loop.html', {'numbers': numbers})

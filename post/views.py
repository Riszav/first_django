from django.shortcuts import render
from django.http import HttpResponse
from post.models import Product
import datetime


def hello(request):
    if request.method == 'GET':
        return HttpResponse('Hello! It`s my project')

def current_date(request):
    now = datetime.datetime.now()
    print(now)
    if request.method == 'GET':
        return HttpResponse(now)

def goodby(request):
    if request.method == 'GET':
        return HttpResponse('Goodby user!')

def main_view(request):
    return render(request, 'index.html')

def product_view(request):
    if request.method == 'GET':
        posts = Product.objects.all()
        context = {
            'posts': posts
        }
        return render(request, 'products/products.html', context=context)


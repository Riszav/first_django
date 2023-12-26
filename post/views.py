from django.shortcuts import render
from django.http import HttpResponse
from post.models import Product, Category
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
        products = Product.objects.all()
        context = {
            'products': products
        }
        return render(request, 'products/products.html', context=context)

def product_detail_view(request, pk):
    if request.method == 'GET':
        try:
            product = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return render(request, '404.html')
        context = {
            'product': product
        }

        return render(request, 'products/detail_product.html', context=context)


def category_view(request):
    if request.method == 'GET':
        # 1 - получить все хэштеги из базы данных
        categories = Category.objects.all()

        # 2 - передать хэштеги в шаблон
        context = {
            'categories': categories,
        }

        # 3 - вернуть ответ с шаблоном и данными
        return render(
            request, # запрос от пользователя (объект HttpRequest) параметр обязательный
            'category/category.html',  # имя шаблона (строка) параметр обязательный
            context=context # словарь с данными (dict) параметр необязательный
        )
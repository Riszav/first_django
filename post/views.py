from django.shortcuts import render, redirect
from django.http import HttpResponse
from post.models import Product, Category, Review
import datetime
from post.forms import PostForm, PostForm2, CategoryForm, ReviewForm


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

def product_detail_view(requests, pk):
    if requests.method == 'GET':
        try:
            product = Product.objects.get(id=pk)
            review = Review.objects.all()
        except Product.DoesNotExist:
            return render(requests, '404.html')
        context = {
            'product': product,
            'form': ReviewForm
        }

        return render(requests, 'products/detail_product.html', context=context)
    if requests.method == 'POST':  # создать пост
        # 1 - получить данные из запроса
        form = ReviewForm(requests.POST, requests.FILES)

        # 2 - валидация данных
        if form.is_valid():  # True если форма валидна, False если форма не валидна
            # 3 - создать пост
            # cleaned_data - это словарь с данными, которые прошли валидацию

            # Если это Form, Post.objects.create(**form.cleaned_data)
            # Post.objects.create(**form.cleaned_data)

            # Если это ModelForm, form.save()
            form.save()

            return redirect('.')
        else:
            context = {
                'form': form,
            }

            return render(requests, 'products/detail_product.html', context=context)


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


def product_create_view(requests):
    if requests.method == 'GET':
        # отобразить форму
        context = {
            'form': PostForm2,
        }
        return render(requests, 'products/create.html', context=context)

    if requests.method == 'POST':  # создать пост
        # 1 - получить данные из запроса
        form = PostForm2(requests.POST, requests.FILES)

        # 2 - валидация данных
        if form.is_valid():  # True если форма валидна, False если форма не валидна
            # 3 - создать пост
            # cleaned_data - это словарь с данными, которые прошли валидацию

            # Если это Form, Post.objects.create(**form.cleaned_data)
            # Post.objects.create(**form.cleaned_data)

            # Если это ModelForm, form.save()
            form.save()

            return redirect('/products/')
        else:
            context = {
                'form': form,
            }

            return render(requests, 'products/create.html', context=context)


def category_create_view(requests):
    if requests.method == 'GET':
        # отобразить форму
        context = {
            'form': CategoryForm,
        }
        return render(requests, 'category/create.html', context=context)

    if requests.method == 'POST':  # создать пост
        # 1 - получить данные из запроса
        form = CategoryForm(requests.POST, requests.FILES)

        # 2 - валидация данных
        if form.is_valid():  # True если форма валидна, False если форма не валидна
            # 3 - создать пост
            # cleaned_data - это словарь с данными, которые прошли валидацию

            # Если это Form, Post.objects.create(**form.cleaned_data)
            # Post.objects.create(**form.cleaned_data)

            # Если это ModelForm, form.save()
            form.save()

            return redirect('/categories/')
        else:
            context = {
                'form': form,
            }

            return render(requests, 'category/create.html', context=context)
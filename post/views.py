from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from post.models import Product, Category, Review
import datetime
from post.forms import PostForm, PostForm2, CategoryForm, ReviewForm
from djangoProject.utils import create_100_products


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
        search = request.GET.get('search')
        order = request.GET.get('order')
        page = request.GET.get('page')
        limit = 9

        max_pages = products.__len__()/limit
        if max_pages > round(max_pages):
            max_pages = round(max_pages) + 1
        else:
            max_pages = round(max_pages)

        print(search)
        print(order)

        if search:
            products = products.filter(
                Q(title__icontains=search) | Q(text__icontains=search)
            )

        if order == 'date':
            products = products.order_by('created_at')

        if order == '-date':
            products = products.order_by('-created_at')

        if order == 'title':
            products = products.order_by('title')

        if order == '_':
            products = products

        if page:
            start = (int(page) - 1) * limit
            end = int(page) * limit
            context = {
                'products': products[start:end],
                'max_pages': range(1, int(max_pages) + 1)
            }

        else:
            context = {
                'products': products[0:limit],
                'max_pages': range(1, int(max_pages)+1)
            }
        print(max_pages)
        return render(request, 'products/products.html', context=context)

def product_detail_view(requests, pk):
    if requests.method == 'GET':
        try:
            product = Product.objects.get(id=pk)
            form = ReviewForm(requests.method)

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
        product = Product.objects.get(id=pk)

        # 2 - валидация данных
        if form.is_valid():  # True если форма валидна, False если форма не валидна
            # 3 - создать пост
            # cleaned_data - это словарь с данными, которые прошли валидацию

            # Если это Form, Post.objects.create(**form.cleaned_data)
            # Post.objects.create(**form.cleaned_data)
            form = form.save(commit=False)

            form.post = product
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

def product_update_view(requests, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return render(requests, "404.html")

    if requests.method == 'GET':
        # отобразить форму
        context = {
            'form': PostForm2(instance=product),
            'product': product,
        }

        return render(requests, 'products/update.html', context=context)

    if requests.method == 'POST':  # создать пост
        # 1 - получить данные из запроса
        form = PostForm2(requests.POST, requests.FILES, instance=product)

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
                'product': product
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
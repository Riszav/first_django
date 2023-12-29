"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from post.views import (hello, current_date, goodby, main_view, product_view, category_view, product_detail_view,
                        product_create_view, category_create_view)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('current_date/', current_date),
    path('goodby/', goodby),
    path('', main_view),
    path('products/', product_view),
    path('product/create/', product_create_view),
    path('products/<int:pk>/', product_detail_view),

    path('categories/', category_view),
    path('category/create/', category_create_view)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

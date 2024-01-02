from django.urls import path
from post.views import (main_view, product_view, category_view, product_detail_view,
                        product_create_view, category_create_view)


urlpatterns = [
    path('', main_view),
    path('products/', product_view),
    path('product/create/', product_create_view),
    path('products/<int:pk>/', product_detail_view),

    path('categories/', category_view),
    path('category/create/', category_create_view),
]

from django.contrib import admin

from post.models import Product, Category, Review
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'price', 'rate', 'created_at', 'updated_at']
    list_display_links = ['id', 'title']
    # readonly_fields = ['title', 'rate']
    search_fields = ['title', 'text']
    list_filter = ['rate', 'created_at']
    ordering = ['created_at']

    # def has_add_permission(self, request: HttpRequest) -> bool:
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     return False

    # def has_change_permission(self, request, obj=None):
    #     return False

admin.site.register(Category)

admin.site.register(Review)
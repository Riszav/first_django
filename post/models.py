from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    text = models.TextField(verbose_name='Описане')
    price = models.DecimalField(verbose_name='Стоимость', decimal_places=2, max_digits=9)
    rate = models.FloatField(default=0, verbose_name='Рейтинг')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='Дата изменения')
    image = models.ImageField(upload_to='media/products', null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.title} [{self.price}$]"
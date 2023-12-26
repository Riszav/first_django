from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания") # Поле для ввода даты и времени
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления") # Поле для ввода даты и времени

    class Meta:
        abstract = True

class Product(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Название')
    text = models.TextField(verbose_name='Описане')
    price = models.DecimalField(verbose_name='Стоимость', decimal_places=2, max_digits=9)
    rate = models.FloatField(default=0, verbose_name='Рейтинг')
    category = models.ForeignKey(
        "post.Category", # Поле для связи с другой моделью
        on_delete=models.DO_NOTHING, # Политика удаления записи в связанной модели (CASCADE - удалить все записи, которые связаны с этой записью)
        verbose_name="Категория", # Название поля в форме (админка, форма регистрации, форма авторизации)
        null=True,
        related_name="category" # Поле для обратной связи (по умолчанию appname_classname_set (post_postinfo_set))
    )
    image = models.ImageField(upload_to='products', null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.title} [{self.price}$]"

    class Meta:  # Мета класс - Это класс, который содержит дополнительную информацию о модели
        db_table = 'product'  # Название таблицы в базе данных (по умолчанию appname_classname (post_postinfo))
        verbose_name = 'Продукт'  # Название модели в единственном числе
        verbose_name_plural = 'Продукты'  # Название модели во множественном числе

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta: # Мета класс - Это класс, который содержит дополнительную информацию о модели
        db_table = 'category' # Название таблицы в базе данных (по умолчанию appname_classname (post_postinfo))
        verbose_name = 'Категория' # Название модели в единственном числе
        verbose_name_plural = 'Категории' # Название модели во множественном числе

class Review(BaseModel):
    post = models.ForeignKey(
        "post.Product", # Поле для связи с другой моделью
        on_delete=models.CASCADE, # Политика удаления записи в связанной модели (CASCADE - удалить все записи, которые связаны с этой записью)
        verbose_name="Пост", # Название поля в форме (админка, форма регистрации, форма авторизации)
        related_name="reviews" # Поле для обратной связи (по умолчанию appname_classname_set (post_comments_set))
    )
    text = models.TextField(null=True, blank=True, verbose_name="Текст") # Поле для ввода текста без ограничения

    def __str__(self) -> str:
        return f"{self.text}"

    class Meta: # Мета класс - Это класс, который содержит дополнительную информацию о модели
        db_table = 'reviews' # Название таблицы в базе данных (по умолчанию appname_classname (post_comments))
        verbose_name = 'Отзыв' # Название модели в единственном числе
        verbose_name_plural = 'Отзывы' # Название модели во множественном числе
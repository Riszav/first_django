from django import forms

from post.models import Product, Category, Review




class PostForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        min_length=3,
        label='Название поста',
    )
    text = forms.CharField(
        widget=forms.Textarea,
        label='Текст поста',
        required=False,
    )
    image = forms.ImageField(
        required=False,
        label='Картинка',
    )
    rate = forms.IntegerField(
        label='Рейтинг',
        required=False,
    )

    def clean_title(self):
        title = self.cleaned_data['title']

        if 'python' not in title.lower():
            raise forms.ValidationError('В заголовке должно быть слово "python"')

        return title

    # def clean(self):
    #     cleaned_data = super().clean()

    #     title = cleaned_data.get('title')
    #     text = cleaned_data.get('text')

    #     if title and text and title == text:
    #         raise forms.ValidationError('Заголовок и текст не должны совпадать')

    #     return cleaned_data


class PostForm2(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'category', 'text', 'image', 'rate', 'price')
        labels = {
            'title': 'Название поста',
            'category': 'Категория продукта',
            'text': 'Текст поста',
            'image': 'Картинка',
            'rate': 'Рейтинг',
            'price': 'Цена',
        }
        help_texts = {
            'title': 'Введите название поста',
            'category': 'Введите категорию',
            'text': 'Введите текст поста',
            'image': 'Загрузите картинку',
            'rate': 'Введите рейтинг',
            'price': 'Введите стоимость',
        }



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        labels = {
            'name': 'Название категории',
        }
        help_texts = {
            'name': 'Введите название категории',
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('post', 'text')
        labels = {
            'post': 'Пост',
            'text': 'Отзыв',
        }
        help_texts = {
            'post': 'Выберите пост ',
            'text': 'Введите отзыв',
        }
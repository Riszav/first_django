from post.models import Product


def create_100_products():
    '''
        Функция для создания 100 постов.
    '''
    for i in range(100):
        Product.objects.create(
            title=f'Test product№{i}',
            text=f'Text of product #{i}',
            price=500 + (i * 10)
        )
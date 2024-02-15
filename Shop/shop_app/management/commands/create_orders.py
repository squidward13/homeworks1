from django.core.management.base import BaseCommand
from shop_app.models import Client, Product, Order
import random


class Command(BaseCommand):
    """
    Заполение таблицы заказы
    (10 шт заказов)
    """

    help = "Create orders"

    def handle(self, *args, **kwargs):

        clients = Client.objects.all()
        products = Product.objects.all()

        for i in range(10):
            products_list = random.sample(
                list(products), 5
            )  # Выбор рандомных продуктов
            for product in products_list:
                total_price = 0  # Подсчет стоимости заказа
                total_price += product.price * products_list.count(product)
            orders = Order.objects.create(
                client=random.choice(clients), total_price=total_price
            )
            orders.products.set(products_list)  # Создание множества продуктов из списка
            orders.save()  # Cохрание объекста заказа
            self.stdout.write(f"{orders}")

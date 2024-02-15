from django.core.management.base import BaseCommand
from shop_app.models import Product
import random
import decimal


class Command(BaseCommand):
    """
    Заполение таблицы продукты
    (10 шт продуктов)
    """

    help = "Create products"

    def handle(self, *args, **kwargs):
        for i in range(10):
            products = Product(
                name=f"product{i}",
                description=f"description{i}",
                price=(random.randint(1000, 10000)),
                quantity=random.randint(1, 1000),
            )
            products.save()
            self.stdout.write(f"{products}")

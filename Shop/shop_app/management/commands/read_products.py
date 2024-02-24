from django.core.management.base import BaseCommand
from shop_app.models import Product


class Command(BaseCommand):
    """
    Выбор всех  товаров
    """

    help = "Read products"

    def handle(self, *args, **kwargs):

        products = Product.objects.all()
        self.stdout.write(f"{products}")

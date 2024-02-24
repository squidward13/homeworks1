from django.core.management.base import BaseCommand
from shop_app.models import Product


class Command(BaseCommand):
    """
    Обновление модели товара ( обновление названия товара )
    """

    help = "Update product"

    def add_arguments(self, parser):
        """
        Аргумент поиска
        """
        parser.add_argument("pk", type=int, help="Product ID")
        parser.add_argument("name", type=str, help="Product name")

    def handle(self, *args, **kwargs):

        pk = kwargs.get("pk")
        new_name = kwargs.get("name")
        product = Product.objects.filter(pk=pk).first()
        if product:
            product.name = new_name
            product.save()
            self.stdout.write(f"Название {product.name} обновлено ")
        else:
            self.stdout.write("Not found")

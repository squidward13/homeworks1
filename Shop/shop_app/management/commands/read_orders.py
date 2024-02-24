from django.core.management.base import BaseCommand
from shop_app.models import Order


class Command(BaseCommand):
    """
    Выбор всех  заказов
    """

    help = "Read products"

    def handle(self, *args, **kwargs):

        orders = Order.objects.all()
        self.stdout.write(f"{orders}")

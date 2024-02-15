from django.core.management.base import BaseCommand
from shop_app.models import Order


class Command(BaseCommand):
    """
    Обновление модели заказа ( изеняем общую стоимость)
    """

    help = "Update order"

    def add_arguments(self, parser):
        """
        Аргумент поиска
        """
        parser.add_argument("pk", type=int, help="Order ID")
        parser.add_argument("total_price", type=int, help="Order total_price")

    def handle(self, *args, **kwargs):

        pk = kwargs.get("pk")
        new_price = kwargs.get("total_price")
        order = Order.objects.filter(pk=pk).first()
        if order:
            order.total_price = new_price
            order.save()
            self.stdout.write(f"Стоимость заказа {order.total_price} изменена")
        else:
            self.stdout.write("Not found")

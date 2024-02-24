from django.core.management.base import BaseCommand
from shop_app.models import Client


class Command(BaseCommand):
    """
    Заполение таблицы клиенты
    (10 шт клиентов)
    """

    help = "Create clients"

    def handle(self, *args, **kwargs):
        for i in range(10):
            clients = Client(
                name=f"user{i}",
                email=f"my{i}mail@.com",
                phone_number=f"{str(i) *10}",
                address=f"My{i} adress",
            )
            clients.save()
            self.stdout.write(f"{clients}")

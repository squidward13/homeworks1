from django.core.management.base import BaseCommand
from shop_app.models import Client


class Command(BaseCommand):
    """
    Выбор всех клиентов
    """

    help = "Read clients"

    def handle(self, *args, **kwargs):

        clients = Client.objects.all()
        self.stdout.write(f"{clients}")

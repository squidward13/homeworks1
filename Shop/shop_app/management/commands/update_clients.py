from django.core.management.base import BaseCommand
from shop_app.models import Client


class Command(BaseCommand):
    """
    Обновление модели клиента ( обновление имени )
    """

    help = "Update client"

    def add_arguments(self, parser):
        """
        Аргумент поиска
        """
        parser.add_argument("pk", type=int, help="Client ID")
        parser.add_argument("name", type=str, help="Client name")

    def handle(self, *args, **kwargs):

        pk = kwargs.get("pk")
        new_name = kwargs.get("name")
        client = Client.objects.filter(pk=pk).first()
        if client:
            client.name = new_name
            client.save()
            self.stdout.write(f" Имя {client.name} обновлено ")
        else:
            self.stdout.write("Not found")

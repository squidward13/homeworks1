from django.core.management.base import BaseCommand
from shop_app.models import Client


class Command(BaseCommand):
    """
    Удаление одного клиента по ID
    """

    help = "Delete single user"

    def add_arguments(self, parser):
        """
        Аргумент поиска
        """
        parser.add_argument("pk", type=int, help="User ID")

    def handle(self, *args, **kwargs):

        pk = kwargs["pk"]
        client = Client.objects.filter(pk=pk).first()
        if client:
            client.delete()
            self.stdout.write(f"{client} удален")
        else:
            self.stdout.write("Not found")

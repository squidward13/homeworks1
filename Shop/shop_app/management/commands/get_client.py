from django.core.management.base import BaseCommand
from shop_app.models import Client


class Command(BaseCommand):
    """
    Выбор одного клиента по ID
    """

    help = "Get single user"

    def add_arguments(self, parser):
        """
        Аргумент поиска
        """
        parser.add_argument("pk", type=int, help="User ID")

    def handle(self, *args, **kwargs):

        pk = kwargs["pk"]
        client = Client.objects.filter(pk=pk).first()
        if client:
            self.stdout.write(f"{client}")
        else:
            self.stdout.write("Not found")

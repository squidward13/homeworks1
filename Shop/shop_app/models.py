from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

from django.db import models


class Client(models.Model):
    """
    Модель покупатель
    """
    
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(
        blank=False,
        null=False,
    )
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    registration_date = models.DateField(auto_now_add=True)

    class Meta:
        """
        Отображение названия таблицы в админке
        """

        verbose_name_plural = "Clients"

    def __str__(self):
        """
        Отображение полей в админке
        """
        return f"{self.name} {self.email} {self.phone_number}  {self.address}  {self.registration_date}"


class Product(models.Model):
    """
    Модель товар (продукт)
    """

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(null=True, blank=True, upload_to='image/%Y')
    quantity = models.IntegerField()
    added_date = models.DateField(auto_now_add=True)

    class Meta:
        """
        Отображение названия таблицы в админке
        """

        verbose_name_plural = "Products"

    def __str__(self):
        """
        Отображение полей в админке
        """
        return f"{self.name} {self.description} {self.price}  {self.quantity} {self.image} {self.added_date}"


class Order(models.Model):
    """
    Модель заказ
    """

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField(auto_now_add=True)

    class Meta:
        """
        Отображение названия таблицы в админке
        """

        verbose_name_plural = "Orders"

    def __str__(self):
        """
        Отображение полей в админке
        """
        return f"{self.client} {self.products} {self.total_price}  {self.order_date}"

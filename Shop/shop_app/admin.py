from django.contrib import admin

from django.contrib import admin
from .models import Client,Order, Product

# Register your models here.

#admin.site.register(Client)
#admin.site.register(Product)
#admin.site.register(Order)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """
    Отображение модели клиент
    """ 
    list_display = (
        'name', 
        'email',
        "phone_number",
        "address",
        "registration_date"
        )
    
    ordering =["name"]
    list_filter =["name"]
    search_fields = ["phone_number"]
    search_help_text = 'Поиск по полю номер телефона'


    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Отображение модели заказ
    """ 
    list_display = (
        'client',
        "total_price",
        "order_date"
        )
    ordering =["total_price","order_date"]
    list_filter =["order_date"]
    search_fields = ["order_date"]
    search_help_text = 'Дата заказа'
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Отображение модели продукт
    """ 
    list_display = (
        'name', 
        'description',
        "price",
        "image",
        "quantity",
        "added_date"
        )
    
    ordering = ["name","price","added_date"]
    list_filter =["price","added_date"]
    search_fields = ["name"]
    search_help_text = 'Название'
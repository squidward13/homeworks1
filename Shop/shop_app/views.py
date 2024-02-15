from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView, FormView,View,CreateView
from .models import Client, Order, Product
from .forms import AddProductForm
from django.contrib import messages
from datetime import date, timedelta
# Create your views here.

class IndexPageView(TemplateView):
    """
    Представление стартовой страницы
    """
    template_name = 'index.html'


    

class AllOrdersView(ListView):
   """
   Представление страницы с отображением 
   всех заказов клиента  за неделю
   за месяц и за год
   Используется пользователь Vasya 
   т.к только для него были созданы 
   вручную заказы (через коммандс отображаются не слишком читабельно
   тк  используется цикл заполения тестовыми данными)
   """
   def get(self,request, pk):
       today = date.today()
       week_delta = today - timedelta(days=7)
       month_delta = today - timedelta(days=30)
       year_delta  = today - timedelta(days=365)
       user = Client.objects.get(id = pk)
       orders_week = Order.objects.filter(client=user, order_date__gte=week_delta).all()
       orders_month = Order.objects.filter(client=user, order_date__gte= month_delta).all()
       orders_year = Order.objects.filter(client=user, order_date__gte=year_delta).all()
       
       return render(request, 'all_orders.html', {'orders_week': orders_week, 'orders_month': orders_month, 'orders_year': orders_year})
   

class AllProductsInOrdersView(ListView):
    """
    Список продуктов в заказах за неделю 
    месяц и год
    """
    def get(self,request,pk):
       user = Client.objects.get(id = pk)
       today = date.today()
       week_delta = today - timedelta(days=7)
       month_delta = today - timedelta(days=30)
       year_delta  = today - timedelta(days=365)
       orders_week = Order.objects.filter(client=user, order_date__gte=week_delta).all()
       orders_month = Order.objects.filter(client=user, order_date__gte=month_delta).all()
       orders_year = Order.objects.filter(client=user, order_date__gte= year_delta).all()
       
       return render(request, 'order_products.html', {'orders_week': orders_week, 'orders_month': orders_month, 'orders_year': orders_year})
    
    



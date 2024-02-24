from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView, FormView,View,CreateView
from .models import Client, Order, Product
from .forms import AddProductForm
from django.contrib import messages

# Create your views here.

class IndexPageView(TemplateView):
    """
    Представление стартовой страницы
    """
    template_name = 'index.html'


class AddNewProductView(TemplateView):
    """
    Представление  страницы
    c формой добавления продукта
    """
    template_name = 'new_product.html'
    

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
       user = Client.objects.get(id = pk)
       orders_week = Order.objects.filter(client=user, order_date__gte='2024-02-01').all()
       orders_month = Order.objects.filter(client=user, order_date__gte='2024-01-08').all()
       orders_year = Order.objects.filter(client=user, order_date__gte='2023-02-08').all()
       
       return render(request, 'all_orders.html', {'orders_week': orders_week, 'orders_month': orders_month, 'orders_year': orders_year})
   

class AllProductsInOrdersView(ListView):
    """
    Список продуктов в заказах за неделю 
    месяц и год 
    """
    def get(self,request, pk):
       user = Client.objects.get(id = pk)
       orders_week = Order.objects.filter(client=user, order_date__gte='2024-02-01').all()
       orders_month = Order.objects.filter(client=user, order_date__gte='2024-01-08').all()
       orders_year = Order.objects.filter(client=user, order_date__gte='2023-02-08').all()
       
       return render(request, 'order_products.html', {'orders_week': orders_week, 'orders_month': orders_month, 'orders_year': orders_year})
    
    
class AddNewProductFormView(FormView):
    """
    Представление формы добавления продукта
    """

    def post(self,request,*args,**kwargs):
        """
        Получение данных из формы
        """
        form = AddProductForm(request.POST,request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            messages.success(request,"Продукт сохранен")
            return redirect("add_product")
        messages.error(request,"Ошибка заполения формы")
        return redirect("add_product")



class AllProductsView(ListView):
    """
    Страница отображения всех 
    всех продуктов (с картинками)
    чтоб было видно что все сохранилось нормально
    """
    def get(self,request, *args, **kwargs):

        products = Product.objects.all().order_by("-id",)

        return render(request, 'all_products.html',{"products":products})
        


from django.urls import path
from . import views

urlpatterns =[
 
path('', views.IndexPageView.as_view(), name="index"),
<<<<<<< HEAD
path("all_orders/", views.AllOrdersView.as_view(), name="all_orders"),
path("all_orders_products/", views.AllProductsInOrdersView.as_view(), name="all_orders_products"),
path("add_product/", views.AddNewProductView.as_view(), name='add_product'),
path("add_product_form/", views.AddNewProductFormView.as_view(), name="add_product_form"),
path("all_products", views.AllProductsView.as_view(),name="all_products")
=======
path("all_orders/<int:pk>/", views.AllOrdersView.as_view(), name="all_orders"),
path("all_orders_products/<int:pk>/", views.AllProductsInOrdersView.as_view(), name="all_orders_products")
>>>>>>> Hometask_3
]
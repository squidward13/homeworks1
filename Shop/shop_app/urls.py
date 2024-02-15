from django.urls import path
from . import views

urlpatterns =[
 
path('', views.IndexPageView.as_view(), name="index"),
path("all_orders/<int:pk>/", views.AllOrdersView.as_view(), name="all_orders"),
path("all_orders_products/<int:pk>/", views.AllProductsInOrdersView.as_view(), name="all_orders_products")
]
"""
URL configuration for sklad_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from warehouse.views import (
    index, products_page, categories_page, employees_page, positions_page, deliveries_page,
    ProductList, CategoryList, EmployeeList, PositionList, DeliveryList,
    ProductDetail, CategoryDetail, EmployeeDetail, PositionDetail, DeliveryDetail
)

urlpatterns = [
    path('', index, name='index'),
    path('products/', products_page, name='products_page'),
    path('categories/', categories_page, name='categories_page'),
    path('employees/', employees_page, name='employees_page'),
    path('positions/', positions_page, name='positions_page'),
    path('deliveries/', deliveries_page, name='deliveries_page'),
    path('admin/', admin.site.urls),
    path('api/v1/', include('warehouse.urls')),
    path('api-auth/', include('rest_framework.urls')), # URL для авторизации
    path('api/v1/products/', ProductList.as_view(), name='product-list'),
    path('api/v1/products/<int:P_ID>/', ProductDetail.as_view(), name='product-detail'),
    path('api/v1/categories/', CategoryList.as_view(), name='category-list'),
    path('api/v1/categories/<int:C_ID>/', CategoryDetail.as_view(), name='category-detail'),
    path('api/v1/employees/', EmployeeList.as_view(), name='employee-list'),
    path('api/v1/employees/<int:E_ID>/', EmployeeDetail.as_view(), name='employee-detail'),
    path('api/v1/positions/', PositionList.as_view(), name='position-list'),
    path('api/v1/positions/<int:P_ID>/', PositionDetail.as_view(), name='position-detail'),
    path('api/v1/deliveries/', DeliveryList.as_view(), name='delivery-list'),
    path('api/v1/deliveries/<int:S_ID>/', DeliveryDetail.as_view(), name='delivery-detail'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('employees/delete/<int:pk>/', views.EmployeeDeleteView.as_view(), name='delete_employee'),
    path('categories/delete/<int:pk>/', views.CategoryDeleteView.as_view(), name='delete_category'),
    path('products/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='delete_product'),
    path('deliveries/delete/<int:pk>/', views.DeliveryDeleteView.as_view(), name='delete_delivery'),
    path('positions/', views.PositionList.as_view()),
    path('positions/<int:pk>/', views.PositionDetail.as_view()),
    path('employees/', views.EmployeeList.as_view()),
    path('employees/<int:pk>/', views.EmployeeDetail.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>/', views.ProductDetail.as_view()),
    path('deliveries/', views.DeliveryList.as_view()),
    path('deliveries/<int:pk>/', views.DeliveryDetail.as_view()),
]
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .models import Employee, Position, Category, Product, Delivery
from .serializers import EmployeeSerializer, PositionSerializer, CategorySerializer, ProductSerializer, DeliverySerializer


def index(request):
    return render(request, 'warehouse/index.html')

def products_page(request):
    return render(request, 'warehouse/products.html')

def categories_page(request):
    return render(request, 'warehouse/categories.html')

def employees_page(request):
    return render(request, 'warehouse/employees.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'warehouse/products.html', {'products': products})

def categories(request):
    categories = Category.objects.all()
    return render(request, 'warehouse/categories.html', {'categories': categories})

def employees(request):
    employees = Employee.objects.all()
    return render(request, 'warehouse/employees.html', {'employees': employees})

def positions_page(request):
    return render(request, 'warehouse/positions.html')

class PositionList(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class PositionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    lookup_field = 'P_ID'

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'E_ID'

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'C_ID'

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'P_ID'

class DeliveryList(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

class DeliveryDeleteView(generics.DestroyAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    lookup_field = 'pk'

class DeliveryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

class EmployeeDeleteView(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'

class CategoryDeleteView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'

class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
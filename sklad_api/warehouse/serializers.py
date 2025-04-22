from rest_framework import serializers
from .models import Employee, Position, Category, Product, Delivery


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    E_POST_detail = PositionSerializer(source='E_POST', read_only=True)
    
    class Meta:
        model = Employee
        fields = ['E_ID', 'E_NAME', 'E_SURNAME', 'E_LASTNAME', 'E_PHONE', 'E_ADDRESS', 'E_POST', 'E_POST_detail']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['C_ID', 'C_NAME', 'C_DESCRIPTION']


class ProductSerializer(serializers.ModelSerializer):
    P_CATEGORY_detail = CategorySerializer(source='P_CATEGORY', read_only=True)
    
    class Meta:
        model = Product
        fields = ['P_ID', 'P_NAME', 'P_QUANTITY', 'P_PRICE', 'P_CATEGORY', 'P_CATEGORY_detail']


class DeliverySerializer(serializers.ModelSerializer):
    S_EMPLOYER_detail = EmployeeSerializer(source='S_EMPLOYER', read_only=True)
    
    class Meta:
        model = Delivery
        fields = ['S_ID', 'S_NUMBER', 'S_DATE', 'S_AMOUNT', 'S_EMPLOYER', 'S_EMPLOYER_detail']
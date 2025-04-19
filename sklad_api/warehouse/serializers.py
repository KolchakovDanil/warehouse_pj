from rest_framework import serializers
from .models import Employee, Position, Category, Product, Delivery


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    E_POST = PositionSerializer(read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    P_CATEGORY = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class DeliverySerializer(serializers.ModelSerializer):
    S_EMPLOYER = EmployeeSerializer(read_only=True)

    class Meta:
        model = Delivery
        fields = '__all__'
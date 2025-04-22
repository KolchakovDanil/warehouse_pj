from django.db import models


class Position(models.Model):
    P_ID = models.AutoField(primary_key=True)
    P_NAME = models.CharField(max_length=25)

    def __str__(self):
        return self.P_NAME


class Employee(models.Model):
    E_ID = models.AutoField(primary_key=True)
    E_SURNAME = models.CharField(max_length=25)
    E_NAME = models.CharField(max_length=25)
    E_LASTNAME = models.CharField(max_length=25)
    E_PHONE = models.CharField(max_length=25)
    E_ADDRESS = models.CharField(max_length=50)
    E_POST = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.E_SURNAME} {self.E_NAME}"


class Category(models.Model):
    C_ID = models.AutoField(primary_key=True)
    C_NAME = models.CharField(max_length=25)
    C_DESCRIPTION = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.C_NAME


class Product(models.Model):
    P_ID = models.AutoField(primary_key=True)
    P_NAME = models.CharField(max_length=25)
    P_QUANTITY = models.IntegerField(default=0)
    P_PRICE = models.DecimalField(max_digits=10, decimal_places=2)
    P_CATEGORY = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.P_NAME


class Delivery(models.Model):
    S_ID = models.AutoField(primary_key=True)
    S_NUMBER = models.IntegerField()
    S_DATE = models.DateField()
    S_AMOUNT = models.IntegerField()
    S_EMPLOYER = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.S_NUMBER)
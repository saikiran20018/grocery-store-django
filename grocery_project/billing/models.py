from django.db import models
from inventory.models import Product

class Sale(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    total_amount = models.FloatField()
    payment_method = models.CharField(max_length=20, default="Cash")

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField()
    price = models.FloatField()

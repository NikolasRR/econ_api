from django.db import models
from categories.models import Category

class Transaction(models.Model):
  description = models.CharField(max_length=255)
  value = models.DecimalField(max_digits=10, decimal_places=2)
  type = models.CharField(max_length=6)
  date = models.DateTimeField()
  category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
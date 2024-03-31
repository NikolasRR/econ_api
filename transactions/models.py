from django.db import models

class TransactionCategory(models.Model):
  description = models.CharField(max_length=255)

class Transaction(models.Model):
  value = models.DecimalField(max_digits=10, decimal_places=2)
  type = models.CharField(max_length=6)
  date = models.DateTimeField()
  category_id = models.ForeignKey(TransactionCategory)
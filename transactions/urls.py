from django.urls import path
from .views import transactions

urlpatterns = [
    path("", transactions.TransactionsView.as_view({"get": "list", "post": "create"})),
    path("<int:transaction>", transactions.TransactionsView.as_view({"get": "retrive"})),
]

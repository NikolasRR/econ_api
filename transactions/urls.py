from django.urls import path
from rest_framework import routers
from .views.transactions import TransactionsView

router = routers.SimpleRouter()
router.register("transaction", TransactionsView, "transaction")
urlpatterns = router.urls

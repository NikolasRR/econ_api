from django.urls import path
from rest_framework import routers
from .views import CategoriesView

router = routers.SimpleRouter()
router.register("category", CategoriesView, "category")
urlpatterns = router.urls
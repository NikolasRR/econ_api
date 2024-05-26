from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from .repository import CategoryRepository
from .serializers import CategorySerializer

class CategoriesView(ViewSet):
  repo = CategoryRepository()
  
  def list(self, request: Request):
    return Response(
      map(
        lambda category: CategorySerializer(category).data,
        self.repo.getAll()
      )
    )
  
  def retrieve(self, request: Request, pk: int):
    return Response(
      f"rota de detalhes da categoria {pk}"
    )
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.request import Request

class CategoriesView(ViewSet):
  def list(self, request: Request):
    return Response(
      "rota de listagem de categorias"
    )
  
  def retrieve(self, request: Request, pk: int):
    return Response(
      f"rota de detalhes da categoria {pk}"
    )
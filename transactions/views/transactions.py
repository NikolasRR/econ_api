from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from ..models import Transaction


# Create your views here.
class TransactionsView(ViewSet):
    def __init__(self) -> None:
        pass

    def list(self, request: Request):
        
        return Response(
            "Hello, World!",
        )
    
    def create(self,  request: Request):
        body = request.data
        transaction = Transaction(
            description=body["description"],
            value=body["value"],
            type=body["type"],
            date=body["date"],
            category_id=body["category_id"]
        ).save()
        return Response(
            transaction,
            status=201
        )
    
    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

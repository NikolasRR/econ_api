from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from categories.models import Category
from ..models import Transaction
from ..repository import TransactionRepository
from ..serializers import TransactionSerializer


# Create your views here.
class TransactionsView(ViewSet):
    repo = TransactionRepository()

    def list(self, request: Request):
        
        return Response(
            map(
                lambda transaction: TransactionSerializer(transaction).data,
                self.repo.list()
            )
        )
    
    def create(self,  request: Request):
        body = request.data
        category = Category(
            id=1,
            description="categoria de teste"
        )
        transaction = Transaction(
            description=body["description"],
            value=body["value"],
            type=body["type"],
            date=body["date"],
            category_id=category
        )

        self.repo.create(transaction)

        return Response(
            TransactionSerializer(transaction).data,
            status=201
        )
    
    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

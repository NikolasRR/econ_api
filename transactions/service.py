from models import Transaction
from repository import TransactionRepository

class TransactionService:
    def __init__(self):
        self.transactionRepository = TransactionRepository()

    def create(self, transaction: Transaction):
        self.transactionRepository.create(transaction)
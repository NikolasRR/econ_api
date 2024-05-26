from models import Transaction, TransactionCategory

class TransactionRepository:
    def create(self, transaction: Transaction):
        transaction.save()
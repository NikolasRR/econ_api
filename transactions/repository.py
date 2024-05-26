from .models import Transaction

class TransactionRepository:
    transactions = []
    
    def create(self, transaction: Transaction):
        self.transactions.append(transaction)

    def list(self):
        return self.transactions
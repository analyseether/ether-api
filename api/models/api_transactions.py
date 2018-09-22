from ether_sql.models import Transactions
import sys
from sqlalchemy.sql.expression import func
from .api_blocks import ApiBlocks
sys.path.append('../')
from sessions import Session

ss=Session()
session=ss.connect_to_psql()
Transaction=ss.get_table_object('transactions')

class ApiTransactions(Transactions):

    @staticmethod
    def get_all_transactions():
        results = []
        blocks = session.query(Transaction).limit(10).all()
        columns = Transaction.columns.keys()
        for row in blocks:
            results.append(dict(zip(columns, row)))
        return results

    @staticmethod
    def get_transaction_by_hash(transaction_hash):
        results = []
        transactions = session.query(Transaction).filter_by(transaction_hash=transaction_hash).all()
        columns = Transaction.columns.keys()
        for row in transactions:
            results.append(dict(zip(columns, row)))
        return results

    @staticmethod
    def get_transaction_by_block_hash_and_index(transaction_index, block_hash):
        results = []
        blocks = ApiBlocks.get_block_by_hash(block_hash)
        if blocks==[]:
            return []
        transactions =session.query(Transaction).filter_by(transaction_index=transaction_index, block_number=blocks[0]['block_number']).all()
        columns = Transaction.columns.keys()
        for row in transactions:
            results.append(dict(zip(columns, row)))
        return results

    @staticmethod
    def get_transaction_by_block_number_and_index(transaction_index, blockno):
        results = []
        transactions =session.query(Transaction).filter_by(transaction_index=transaction_index, block_number=blockno).all()
        columns = Transaction.columns.keys()
        for row in transactions:
            results.append(dict(zip(columns, row)))
        return results

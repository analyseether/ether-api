from ether_sql.models import Receipts
import sys
from sqlalchemy.sql.expression import func
sys.path.append('../')
from sessions import Session

ss=Session()
session=ss.connect_to_psql()
Receipt=ss.get_table_object('receipts')

class ApiReceipts(Receipts):

    @staticmethod
    def get_receipt(transaction_hash):
        results = []
        receipts = session.query(Receipt).filter_by(transaction_hash=transaction_hash).all()
        columns = Receipt.columns.keys()
        for row in receipts:
            results.append(dict(zip(columns, row)))
        return results

from ether_sql.models import Receipts
import sys
from sqlalchemy.sql.expression import func
sys.path.append("../")
from sessions import Session

ss=Session()
session=ss.connect_to_psql()
Receipt=ss.get_table_object('receipts')

class ApiReceipts(Receipts):
    """
    Extends the Receipts class from ether_sql.models.
    The functions defined here access the psql Receipts table and retrieve the results based on requesting parameters.
    Receipts Class maps a block table in the psql database to a block in ethereum node.

    :param str transaction_hash: The Keccak 256-bit hash of this transaction

    """
    @staticmethod
    def get_receipt(transaction_hash):
        """
        Returns the data of the receipt of the given transaction hash

        :param string transaction_hash: Transaction Hash that we want to retrieve data of
        """
        results = []
        receipts = session.query(Receipt).filter_by(transaction_hash=transaction_hash).all()
        columns = Receipt.columns.keys()
        for row in receipts:
            results.append(dict(zip(columns, row)))
        return results

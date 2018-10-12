from ether_sql.models import Transactions
import sys
from sqlalchemy.sql.expression import func
from .api_blocks import ApiBlocks
sys.path.append("../")
from sessions import Session

ss=Session()
session=ss.connect_to_psql()
Transaction=ss.get_table_object('transactions')

class ApiTransactions(Transactions):
    """
    Extends the Transactions class from ether_sql.models.
    The functions defined here access the psql Transactions table and retrieve the results based on requesting parameters.
    Transactions Class maps a block table in the psql database to a block in ethereum node.

    :param str transaction_hash: The Keccak 256-bit hash of this transaction
    :param int block_number: Number of the block containing this transaction
    :param datetime transaction_index: Position of this transaction in the transaction list of this block

    """

    @staticmethod
    def get_all_transactions():
        """
        Returns all the transactions data in the database. Limit set to 10 for test phase.
        """
        results = []
        blocks = session.query(Transaction).limit(10).all()
        columns = Transaction.columns.keys()
        for row in blocks:
            results.append(dict(zip(columns, row)))
        return results

    @staticmethod
    def get_transaction_by_hash(transaction_hash):
        """
        Returns the data of the transaction of the given transaction hash

        :param string transaction_hash: Transaction Hash that we want to retrieve data of
        """
        results = []
        transactions = session.query(Transaction).filter_by(transaction_hash=transaction_hash).all()
        columns = Transaction.columns.keys()
        for row in transactions:
            results.append(dict(zip(columns, row)))
        return results

    @staticmethod
    def get_transaction_by_block_hash_and_index(transaction_index, block_hash):
        """
        Returns the data of the transaction of the given transaction index and block hash

        :param int transaction_index: Transaction Index that we want to retrieve data of
        :param string block_hash: Block Hash that we want to retrieve data of
        """
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
        """
        Returns the data of the transaction of the given transaction index and block number

        :param int transaction_index: Transaction Index that we want to retrieve data of
        :param int blockno: Block Number that we want to retrieve data of
        """
        results = []
        transactions =session.query(Transaction).filter_by(transaction_index=transaction_index, block_number=blockno).all()
        columns = Transaction.columns.keys()
        for row in transactions:
            results.append(dict(zip(columns, row)))
        return results

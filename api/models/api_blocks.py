from ether_sql.models import Blocks
import sys
from sqlalchemy.sql.expression import func
sys.path.append("../")
from sessions import Session
ss=Session()
session=ss.connect_to_psql()
Block=ss.get_table_object('blocks')
class ApiBlocks(Blocks):
    """
    Extends the Blocks class from ether_sql.models.
    The functions defined here access the psql Blocks table and retrieve the results based on requesting parameters.
    Blocks Class maps a block table in the psql database to a block in ethereum node.

    :param int block_number: Quantity equal to number of blocks behind the current block
    :param str block_hash: The Keccak 256-bit hash of this block
    :param int uncle_count: Number of uncles in this block
    :param int transaction_count: Number of transactions in this block

    """
    @staticmethod
    def get_all_blocks():
        """
        Returns all the blocks data in the database. Limit set to 10 for test phase.
        """
        results = []
        blocks = session.query(Block).limit(10).all()
        columns = Block.columns.keys()
        for row in blocks:
            results.append(dict(zip(columns, row)))
        return results

    @staticmethod
    def get_current_block_number():
        """
        Return the block number of the latest block in the database.
        """
        results = []
        blocks = session.query(func.max(Block.columns.block_number).label('block_number'))
        column_names = [c["name"] for c in blocks.column_descriptions]
        results=[dict(zip(column_names, row)) for row in blocks.all()]
        return results

    @staticmethod
    def get_block_by_number(blockno):
        """
        Returns the data of the block of the given block number

        :param int blockno: Block Number that we want to retrieve data of
        """
        results = []
        blocks = session.query(Block).filter_by(block_number=blockno).all()
        columns = Block.columns.keys()
        for row in blocks:
            results.append(dict(zip(columns, row)))
        return results

    @staticmethod
    def get_block_by_hash(block_hash):
        """
        Returns the data of the block of the given block hash

        :param string block_hash: Block Hash that we want to retrieve data of
        """
        results = []
        blocks = session.query(Block).filter_by(block_hash=block_hash).all()
        columns = Block.columns.keys()
        for row in blocks:
            results.append(dict(zip(columns, row)))
        return results

    @staticmethod
    def get_block_transaction_count_by_hash(block_hash):
        """
        Returns the transaction count of the block of the given block hash

        :param string block_hash: Block Hash that we want to retrieve data of
        """
        try:
            blocks = session.query(Block).filter_by(block_hash=block_hash).first()
            return [{'transaction_count':blocks.transaction_count}]
        except:
            return [{'transaction_count':0}]

    @staticmethod
    def get_block_transaction_count_by_number(blockno):
        """
        Returns the transaction count of the block of the given block number

        :param int blockno: Block Number that we want to retrieve data of
        """
        try:
            blocks = session.query(Block).filter_by(block_number=blockno).first()
            return [{'transaction_count':blocks.transaction_count}]
        except:
            return [{'transaction_count':0}]

    @staticmethod
    def get_uncle_count_by_block_hash(block_hash):
        """
        Returns the uncle count of the block of the given block hash

        :param string block_hash: Block Hash that we want to retrieve data of
        """
        try:
            blocks = session.query(Block).filter_by(block_hash=block_hash).first()
            return [{'uncle_count':blocks.uncle_count}]
        except:
            return [{'uncle_count':0}]

    @staticmethod
    def get_uncle_count_by_block_number(blockno):
        """
        Returns the uncle count of the block of the given block number

        :param int blockno: Block Number that we want to retrieve data of
        """
        try:
            blocks = session.query(Block).filter_by(block_number=blockno).first()
            return [{'uncle_count':blocks.uncle_count}]
        except:
            return [{'uncle_count':0}]

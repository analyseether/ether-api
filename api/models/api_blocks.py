from ether_sql.models import Blocks
import sys
from sqlalchemy.sql.expression import func
sys.path.append('../')
from sessions import Session

ss=Session()
session=ss.connect_to_psql()
Block=ss.get_table_object('blocks')
class ApiBlocks(Blocks):

    @staticmethod
    def get_all_blocks():
        results = []
        blocks = session.query(Block).limit(10).all()
        columns = Block.columns.keys()
        for row in blocks:
            results.append(dict(zip(columns, row)))
        return results

    @staticmethod
    def get_current_block_number():
        results = []
        blocks = session.query(func.max(Block.columns.block_number).label('block_number'))
        column_names = [c["name"] for c in blocks.column_descriptions]
        results=[dict(zip(column_names, row)) for row in blocks.all()]
        return results

    @staticmethod
    def get_block_by_number(blockno):
        results = []
        blocks = session.query(Block).filter_by(block_number=blockno).all()
        columns = Block.columns.keys()
        for row in blocks:
            results.append(dict(zip(columns, row)))
        return results

    @staticmethod
    def get_block_by_hash(block_hash):
        results = []
        blocks = session.query(Block).filter_by(block_hash=block_hash).all()
        columns = Block.columns.keys()
        for row in blocks:
            results.append(dict(zip(columns, row)))
        return results

    @staticmethod
    def get_block_transaction_count_by_hash(block_hash):
        try:
            blocks = session.query(Block).filter_by(block_hash=block_hash).first()
            return [{'transaction_count':blocks.transaction_count}]
        except:
            return [{'transaction_count':0}]

    @staticmethod
    def get_block_transaction_count_by_number(blockno):
        try:
            blocks = session.query(Block).filter_by(block_number=blockno).first()
            return [{'transaction_count':blocks.transaction_count}]
        except:
            return [{'transaction_count':0}]

    @staticmethod
    def get_uncle_count_by_block_hash(block_hash):
        try:
            blocks = session.query(Block).filter_by(block_hash=block_hash).first()
            return [{'uncle_count':blocks.uncle_count}]
        except:
            return [{'uncle_count':0}]

    @staticmethod
    def get_uncle_count_by_block_number(blockno):
        try:
            blocks = session.query(Block).filter_by(block_number=blockno).first()
            return [{'uncle_count':blocks.uncle_count}]
        except:
            return [{'uncle_count':0}]

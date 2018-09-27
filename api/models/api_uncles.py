from ether_sql.models import Uncles
import sys
from sqlalchemy.sql.expression import func
sys.path.append('../')
from sessions import Session

ss=Session()
session=ss.connect_to_psql()
Uncle=ss.get_table_object('uncles')

class ApiUncles(Uncles):

    @staticmethod
    def get_uncle_by_uncle_hash(uncle_hash):
        results = []
        uncles = session.query(Uncle).filter_by(uncle_hash=uncle_hash).all()
        columns = Uncle.columns.keys()
        for row in uncles:
            results.append(dict(zip(columns, row)))
        return results

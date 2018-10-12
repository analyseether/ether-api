from ether_sql.models import Uncles
import sys
from sqlalchemy.sql.expression import func
sys.path.append("../")
from sessions import Session

ss=Session()
session=ss.connect_to_psql()
Uncle=ss.get_table_object('uncles')

class ApiUncles(Uncles):
    """
    Extends the Uncles class from ether_sql.models.
    The functions defined here access the psql Uncles table and retrieve the results based on requesting parameters.
    Uncles Class maps a block table in the psql database to a block in ethereum node.

    :param str uncle_hash: The Keccak 256-bit hash of this uncle

    """
    def get_uncle_by_uncle_hash(uncle_hash):
        """
        Returns the data of the uncle of the given uncle hash

        :param string uncle_hash: Uncle Hash that we want to retrieve data of
        """
        results=[]
        uncles = session.query(Uncle).filter_by(uncle_hash=uncle_hash).all()
        columns = Uncle.columns.keys()
        for row in uncles:
            results.append(dict(zip(columns, row)))
        return results

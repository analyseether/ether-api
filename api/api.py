from flask import Flask, jsonify
import simplejson as json
import psycopg2
from datetime import date, datetime
from sqlalchemy.sql.expression import func
from sqlalchemy.exc import NoInspectionAvailable

if __package__ is None or __package__ == '':
  from sessions import Session
else:
  from .sessions import Session

app = Flask(__name__)

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))



#ESTABLISHING CONNECTION WITH THE POSTGRES DATABASE
ss=Session()
session=ss.connect_to_psql()


Blocks=ss.get_table_object('blocks')
Transactions=ss.get_table_object('transactions')
Receipts=ss.get_table_object('receipts')
Uncles=ss.get_table_object('uncles')


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))


#TO GET ALL BLOCKS (LIMIT SET TO 10)
@app.route('/v1.0/all_blocks/', methods=['GET'])
def get_all_block():
    results = []
    blocks = session.query(Blocks).limit(10).all()
    columns = Blocks.columns.keys()
    for row in blocks:
        results.append(dict(zip(columns, row)))

    return json.dumps(results, indent=2, default=json_serial)


# #TO GET LATEST BLOCK'S BLOCKNUMBER
@app.route('/v1.0/current_blockNumber/', methods=['GET'])
def eth_blockNumber():
    results = []
    blocks = session.query(func.max(Blocks.columns.block_number).label('block_number'))
    column_names = [c["name"] for c in blocks.column_descriptions]
    results=[dict(zip(column_names, row)) for row in blocks.all()]
    return json.dumps(results, indent=2, default=json_serial)


#TO GET A BLOCK BY ITS BLOCK NUMBER
@app.route('/v1.0/getBlockByNumber/<int:blockno>/', methods=['GET'])
def eth_getBlockByNumber(blockno):
    results = []
    blocks = session.query(Blocks).filter_by(block_number=blockno).all()
    columns = Blocks.columns.keys()
    for row in blocks:
        results.append(dict(zip(columns, row)))

    return json.dumps(results, indent=2, default=json_serial)

#TO GET A BLOCK BY ITS BLOCK HASH
@app.route('/v1.0/getBlockByHash/<string:block_hash>/', methods=['GET'])
def eth_getBlockByHash(block_hash):
    results = []
    blocks = session.query(Blocks).filter_by(block_hash=block_hash).all()
    columns = Blocks.columns.keys()
    for row in blocks:
        results.append(dict(zip(columns, row)))

    return json.dumps(results, indent=2, default=json_serial)

#TO GET A BLOCK TRANSACTION COUNT BY ITS BLOCK HASH
@app.route('/v1.0/getTransactionCountByHash/<string:block_hash>/', methods=['GET'])
def eth_getBlockTransactionCountByHash(block_hash):
    try:
        blocks = session.query(Blocks).filter_by(block_hash=block_hash).first()
        return json.dumps([{'transaction_count':blocks.transaction_count}], indent=2, default=json_serial)
    except:
        return json.dumps([{'transaction_count':0}], indent=2, default=json_serial)

#TO GET A BLOCK TRANSACTION COUNT BY ITS BLOCK NUMBER
@app.route('/v1.0/getTransactionCountByNumber/<int:blockno>/', methods=['GET'])
def eth_getBlockTransactionCountByNumber(blockno):
    try:
        blocks = session.query(Blocks).filter_by(block_number=blockno).first()
        return json.dumps([{'transaction_count':blocks.transaction_count}], indent=2, default=json_serial)
    except:
        return json.dumps([{'transaction_count':0}], indent=2, default=json_serial)


#TO GET A BLOCK UNCLE COUNT BY ITS BLOCK HASH
@app.route('/v1.0/getUncleCountByBlockHash/<string:block_hash>/', methods=['GET'])
def eth_getUncleCountByBlockHash(block_hash):
    try:
        blocks = session.query(Blocks).filter_by(block_hash=block_hash).first()
        return json.dumps([{'uncle_count':blocks.uncle_count}], indent=2, default=json_serial)
    except:
        return json.dumps([{'uncle_count':0}], indent=2, default=json_serial)

#TO GET A BLOCK UNCLE COUNT BY ITS BLOCK NUMBER
@app.route('/v1.0/getUncleCountByBlockNumber/<int:blockno>/', methods=['GET'])
def eth_getUncleCountByBlockNumber(blockno):
    try:
        blocks = session.query(Blocks).filter_by(block_number=blockno).first()
        return json.dumps([{'uncle_count':blocks.uncle_count}], indent=2, default=json_serial)
    except:
        return json.dumps([{'uncle_count':0}], indent=2, default=json_serial)

#TO GET A TRANSACTION BY ITS HASH
@app.route('/v1.0/getTransactionByHash/<string:hash1>/', methods=['GET'])
def eth_getTransactionByHash(hash1):
    results = []
    transactions = session.query(Transactions).filter_by(transaction_hash=hash1).all()
    columns = Transactions.columns.keys()
    for row in transactions:
        results.append(dict(zip(columns, row)))
    return json.dumps(results, indent=2, default=json_serial)

#TO GET A TRANSACTION BY BLOCK HASH AND INDEX
@app.route('/v1.0/getTransactionByBlockHashAndIndex/<string:hash1>/<int:index>/', methods=['GET'])
def eth_getTransactionByBlockHashAndIndex(hash1, index):
    results = []
    blocks = session.query(Blocks).filter_by(block_hash=hash1).first()
    if blocks==None:
        return json.dumps([], indent=2, default=json_serial)
    transactions = session.query(Transactions).filter_by(transaction_index=index, block_number=blocks.block_number).all()
    columns = Transactions.columns.keys()
    for row in transactions:
        results.append(dict(zip(columns, row)))
    return json.dumps(results, indent=2, default=json_serial)


#TO GET A TRANSACTION BY BLOCK NUMBER AND INDEX
@app.route('/v1.0/getTransactionByBlockNumberAndIndex/<int:blockno>/<int:index>/', methods=['GET'])
def eth_getTransactionByBlockNumberAndIndex(blockno, index):
    results = []
    transactions = session.query(Transactions).filter_by(transaction_index=index, block_number=blockno).all()
    columns = Transactions.columns.keys()
    for row in transactions:
        results.append(dict(zip(columns, row)))
    return json.dumps(results, indent=2, default=json_serial)

#TO GET A TRANSACTION RECEIPTS BY ITS HASH
@app.route('/v1.0/getReceipt/<string:hash1>/', methods=['GET'])
def eth_getTransactionReceipt(hash1):
    results = []
    receipts = session.query(Receipts).filter_by(transaction_hash=hash1).all()
    columns = Transactions.columns.keys()
    for row in receipts:
        results.append(dict(zip(columns, row)))
    return json.dumps(results, indent=2, default=json_serial)

#TO GET AN UNCLE BY ITS HASH
@app.route('/v1.0/getUncleByHash/<string:hash1>/', methods=['GET'])
def eth_getUncleByUncleHash(hash1):
    results = []
    uncles = session.query(Uncles).filter_by(uncle_hash=hash1).all()
    columns = Transactions.columns.keys()
    for row in uncles:
        results.append(dict(zip(columns, row)))
    return json.dumps(results, indent=2, default=json_serial)

if __name__ == '__main__':
    app.run(debug=True)

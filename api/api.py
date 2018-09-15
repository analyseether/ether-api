from flask import Flask, jsonify
import simplejson as json
import psycopg2
from datetime import date, datetime
from session import Session

app = Flask(__name__)

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))



#ESTABLISHING CONNECTION WITH THE POSTGRES DATABASE
cur= Session.connect_to_psql()


#TO GET ALL BLOCKS (LIMIT SET TO 10)
@app.route('/v1.0/all_blocks/', methods=['GET'])
def get_all_block():
    cur.execute("""SELECT * FROM blocks LIMIT 10""")
    # columns = ('block_number', 'block_hash', 'parent_hash', 'difficulty', 'gas_used', 'miner', 'timestamp', 'sha3uncles', 'extra_data',
    #     'gas_limit', 'uncle_count', 'transaction_count')
    # for row in cur.fetchall():
    #     results.append(dict(zip(columns, row)))
    # print(json.dumps(results, indent=2, default=json_serial))

    results = []

    columns = cur.description

    for value in cur.fetchall():
    	tmp = {}
    	for (index,column) in enumerate(value):
        	tmp[columns[index][0]] = column
    	results.append(tmp)

    resJSON = json.dumps(results, indent=2, default=json_serial)
    return resJSON


#TO GET LATEST BLOCK'S BLOCKNUMBER
@app.route('/v1.0/latest_block_number/', methods=['GET'])
def get_latest_block():
    cur.execute("""SELECT block_number FROM blocks WHERE block_number = (SELECT max(block_number) from blocks)""")
    results = []

    columns = cur.description

    for value in cur.fetchall():
    	tmp = {}
    	for (index,column) in enumerate(value):
        	tmp[columns[index][0]] = column
    	results.append(tmp)

    resJSON = json.dumps(results, indent=2, default=json_serial)
    return resJSON


#TO GET A BLOCK BY ITS BLOCK NUMBER
@app.route('/v1.0/block_by_number/<int:blockno>/', methods=['GET'])
def get_block_by_blockno(blockno):

    cur.execute("""SELECT * FROM blocks WHERE block_number="""+str(blockno))
    
    results = []

    columns = cur.description

    for value in cur.fetchall():
    	tmp = {}
    	for (index,column) in enumerate(value):
        	tmp[columns[index][0]] = column
    	results.append(tmp)

    resJSON = json.dumps(results, indent=2, default=json_serial)
    return resJSON

#TO GET A BLOCK BY ITS BLOCK HASH
@app.route('/v1.0/block_by_hash/<string:block_hash>/', methods=['GET'])
def get_block_by_blockhash(block_hash):

    cur.execute("""SELECT * FROM blocks WHERE block_hash="""+ "'" + block_hash + "'")
    
    results = []

    columns = cur.description

    for value in cur.fetchall():
    	tmp = {}
    	for (index,column) in enumerate(value):
        	tmp[columns[index][0]] = column
    	results.append(tmp)

    resJSON = json.dumps(results, indent=2, default=json_serial)
    return resJSON

#TO GET A BLOCK TRANSACTION COUNT BY ITS BLOCK HASH
@app.route('/v1.0/block_transcount_by_hash/<string:block_hash>/', methods=['GET'])
def get_block_transcount_by_blockhash(block_hash):

    cur.execute("""SELECT transaction_count FROM blocks WHERE block_hash="""+ "'" + block_hash + "'")
    results = []

    columns = cur.description

    for value in cur.fetchall():
    	tmp = {}
    	for (index,column) in enumerate(value):
        	tmp[columns[index][0]] = column
    	results.append(tmp)

    resJSON = json.dumps(results, indent=2, default=json_serial)
    return resJSON

#TO GET A BLOCK TRANSACTION COUNT BY ITS BLOCK NUMBER
@app.route('/v1.0/block_transcount_by_number/<int:blockno>/', methods=['GET'])
def get_block_transcount_by_blockno(blockno):

    cur.execute("""SELECT transaction_count FROM blocks WHERE block_number="""+ str(blockno))
    results = []

    columns = cur.description

    for value in cur.fetchall():
    	tmp = {}
    	for (index,column) in enumerate(value):
        	tmp[columns[index][0]] = column
    	results.append(tmp)

    resJSON = json.dumps(results, indent=2, default=json_serial)
    return resJSON


#TO GET A BLOCK UNCLE COUNT BY ITS BLOCK HASH
@app.route('/v1.0/block_unclecount_by_hash/<string:block_hash>/', methods=['GET'])
def get_block_unclecount_by_blockhash(block_hash):

    cur.execute("""SELECT uncle_count FROM blocks WHERE block_hash="""+ "'" + block_hash + "'")
    results = []

    columns = cur.description

    for value in cur.fetchall():
    	tmp = {}
    	for (index,column) in enumerate(value):
        	tmp[columns[index][0]] = column
    	results.append(tmp)

    resJSON = json.dumps(results, indent=2, default=json_serial)
    return resJSON

#TO GET A BLOCK UNCLE COUNT BY ITS BLOCK NUMBER
@app.route('/v1.0/block_unclecount_by_number/<int:blockno>/', methods=['GET'])
def get_block_unclecount_by_blockno(blockno):

    cur.execute("""SELECT uncle_count FROM blocks WHERE block_number="""+ str(blockno))
    results = []

    columns = cur.description

    for value in cur.fetchall():
    	tmp = {}
    	for (index,column) in enumerate(value):
        	tmp[columns[index][0]] = column
    	results.append(tmp)

    resJSON = json.dumps(results, indent=2, default=json_serial)
    return resJSON

#TO GET A TRANSACTION BY ITS HASH
@app.route('/v1.0/transaction/<string:hash1>/', methods=['GET'])
def get_transaction_by_hash(hash1):

    cur.execute("""SELECT * FROM transactions WHERE transaction_hash="""+ "'" + hash1 + "'")
    columns = ('transaction_hash', 'block_number', 'nonce', 'sender', 'receiver', 'start_gas', 'value', 'data', 'gas_price',
        'timestamp', 'transaction_index')
    results = []

    for row in cur.fetchall():
        results.append(dict(zip(columns, row)))
    # print(json.dumps(results, indent=2, default=json_serial))

    resJSON = json.dumps(results, indent=2, default=json_serial)
    return resJSON



if __name__ == '__main__':
    app.run(debug=True)

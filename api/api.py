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
    print("Here")
    cur.execute("""SELECT * FROM blocks LIMIT 10""")
    columns = ('block_number', 'block_hash', 'parent_hash', 'difficulty', 'gas_used', 'miner', 'timestamp', 'sha3uncles', 'extra_data',
        'gas_limit', 'uncle_count', 'transaction_count')
    results = []

    for row in cur.fetchall():
        results.append(dict(zip(columns, row)))
    # print(json.dumps(results, indent=2, default=json_serial))

    resJSON = json.dumps(results, indent=2, default=json_serial)
    return resJSON


#TO GET A BLOCK BY ITS BLOCK NUMBER
@app.route('/v1.0/block/<int:blockno>/', methods=['GET'])
def get_block_by_blockno(blockno):

    cur.execute("""SELECT * FROM blocks WHERE block_number="""+str(blockno))
    columns = ('block_number', 'block_hash', 'parent_hash', 'difficulty', 'gas_used', 'miner', 'timestamp', 'sha3uncles', 'extra_data',
        'gas_limit', 'uncle_count', 'transaction_count')
    results = []

    for row in cur.fetchall():
        results.append(dict(zip(columns, row)))
    # print(json.dumps(results, indent=2, default=json_serial))

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

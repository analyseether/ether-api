from flask import Flask, jsonify
import simplejson as json
from datetime import date, datetime
from models import *

if __package__ is None or __package__ == '':
  from utils import json_serial
else:
  from .utils import json_serial

app = Flask(__name__)



#TO GET ALL BLOCKS (LIMIT SET TO 10)
@app.route('/v1.0/all_blocks/', methods=['GET'])
def get_all_blocks():
    """
        Returns all the blocks data in the database. Limit set to 10 for test phase.
    """
    results = ApiBlocks.get_all_blocks()
    return json.dumps(results, indent=2, default=json_serial)


#TO GET LATEST BLOCK'S BLOCKNUMBER
@app.route('/v1.0/current_blockNumber/', methods=['GET'])
def eth_blockNumber():
    """
        Returns the block number of the latest block in the database.
    """
    results=ApiBlocks.get_current_block_number()
    return json.dumps(results, indent=2, default=json_serial)


#TO GET A BLOCK BY ITS BLOCK NUMBER
@app.route('/v1.0/getBlockByNumber/<int:blockno>/', methods=['GET'])
def eth_getBlockByNumber(blockno):
    """
        Returns the data of the block of the given block number

        :param int blockno: Block Number that we want to retrieve data of
    """
    results=ApiBlocks.get_block_by_number(blockno)
    return json.dumps(results, indent=2, default=json_serial)

#TO GET A BLOCK BY ITS BLOCK HASH
@app.route('/v1.0/getBlockByHash/<string:block_hash>/', methods=['GET'])
def eth_getBlockByHash(block_hash):
    """
        Returns the data of the block of the given block hash

        :param string block_hash: Block Hash that we want to retrieve data of
    """
    results=ApiBlocks.get_block_by_hash(block_hash)
    return json.dumps(results, indent=2, default=json_serial)

#TO GET A BLOCK TRANSACTION COUNT BY ITS BLOCK HASH
@app.route('/v1.0/getTransactionCountByHash/<string:block_hash>/', methods=['GET'])
def eth_getBlockTransactionCountByHash(block_hash):
    """
        Returns the transaction count of the block of the given block hash

        :param string block_hash: Block Hash that we want to retrieve data of
    """
    results=ApiBlocks.get_block_transaction_count_by_hash(block_hash)
    return json.dumps(results, indent=2, default=json_serial)

#TO GET A BLOCK TRANSACTION COUNT BY ITS BLOCK NUMBER
@app.route('/v1.0/getTransactionCountByNumber/<int:blockno>/', methods=['GET'])
def eth_getBlockTransactionCountByNumber(blockno):
    """
        Returns the transaction count of the block of the given block number

        :param int blockno: Block Number that we want to retrieve data of
    """
    results=ApiBlocks.get_block_transaction_count_by_number(blockno)
    return json.dumps(results, indent=2, default=json_serial)

#TO GET A BLOCK UNCLE COUNT BY ITS BLOCK HASH
@app.route('/v1.0/getUncleCountByBlockHash/<string:block_hash>/', methods=['GET'])
def eth_getUncleCountByBlockHash(block_hash):
    """
        Returns the uncle count of the block of the given block hash

        :param string block_hash: Block Hash that we want to retrieve data of
    """
    results=ApiBlocks.get_uncle_count_by_block_hash(block_hash)
    return json.dumps(results, indent=2, default=json_serial)

#TO GET A BLOCK UNCLE COUNT BY ITS BLOCK NUMBER
@app.route('/v1.0/getUncleCountByBlockNumber/<int:blockno>/', methods=['GET'])
def eth_getUncleCountByBlockNumber(blockno):
    """
        Returns the uncle count of the block of the given block number

        :param int blockno: Block Number that we want to retrieve data of
    """
    results=ApiBlocks.get_uncle_count_by_block_number(blockno)
    return json.dumps(results, indent=2, default=json_serial)





#TO GET A TRANSACTION BY ITS HASH
@app.route('/v1.0/getTransactionByHash/<string:transaction_hash>/', methods=['GET'])
def eth_getTransactionByHash(transaction_hash):
    """
        Returns the data of the transaction of the given transaction hash

        :param string transaction_hash: Transaction Hash that we want to retrieve data of
    """
    results=ApiTransactions.get_transaction_by_hash(transaction_hash)
    return json.dumps(results, indent=2, default=json_serial)

#TO GET A TRANSACTION BY BLOCK HASH AND INDEX
@app.route('/v1.0/getTransactionByBlockHashAndIndex/<string:block_hash>/<int:index>/', methods=['GET'])
def eth_getTransactionByBlockHashAndIndex(block_hash, index):
    """
        Returns the data of the transaction of the given transaction index and block hash

        :param int transaction_index: Transaction Index that we want to retrieve data of
        :param string block_hash: Block Hash that we want to retrieve data of
    """
    results=ApiTransactions.get_transaction_by_block_hash_and_index(index, block_hash)
    return json.dumps(results, indent=2, default=json_serial)

#TO GET A TRANSACTION BY BLOCK NUMBER AND INDEX
@app.route('/v1.0/getTransactionByBlockNumberAndIndex/<int:blockno>/<int:index>/', methods=['GET'])
def eth_getTransactionByBlockNumberAndIndex(blockno, index):
    """
        Returns the data of the transaction of the given transaction index and block number

        :param int transaction_index: Transaction Index that we want to retrieve data of
        :param int blockno: Block Number that we want to retrieve data of
    """
    results=ApiTransactions.get_transaction_by_block_number_and_index(index, blockno)
    return json.dumps(results, indent=2, default=json_serial)





#TO GET A TRANSACTION RECEIPTS BY ITS HASH
@app.route('/v1.0/getReceipt/<string:transaction_hash>/', methods=['GET'])
def eth_getTransactionReceipt(transaction_hash):
    """
        Returns the data of the receipt of the given transaction hash

        :param string transaction_hash: Transaction Hash that we want to retrieve data of
    """
    results = ApiReceipts.get_receipt(transaction_hash)
    return json.dumps(results, indent=2, default=json_serial)





#TO GET AN UNCLE BY ITS HASH
@app.route('/v1.0/getUncleByHash/<string:uncle_hash>/', methods=['GET'])
def eth_getUncleByUncleHash(uncle_hash):
    """
        Returns the data of the uncle of the given uncle hash

        :param string uncle_hash: Uncle Hash that we want to retrieve data of
    """
    results = ApiUncles.get_uncle_by_uncle_hash(uncle_hash)
    return json.dumps(results, indent=2, default=json_serial)

if __name__ == '__main__':
    app.run(debug=True)

import os
import pytest
import sys
import simplejson as json

sys.path.append('../api')
import api

@pytest.fixture
def test_links():
    test_get_all_blocks()
    test_eth_blockNumber()
    test_eth_getBlockByNumber(5000000)
    test_eth_getBlockByHash('0x7d5a4369273c723454ac137f48a4f142b097aa2779464e6505f1b1c5e37b5382')
    test_eth_getBlockTransactionCountByHash('0x7d5a4369273c723454ac137f48a4f142b097aa2779464e6505f1b1c5e37b5382')
    test_eth_getBlockTransactionCountByNumber(5000000)
    test_eth_getUncleCountByBlockHash('0x7d5a4369273c723454ac137f48a4f142b097aa2779464e6505f1b1c5e37b5382')
    test_eth_getUncleCountByBlockNumber(5000000)

    test_eth_getTransactionByHash('0xf29819bc5b114851494262c25728e697bd1b679646be9a5e4d12431868057b39')
    test_eth_getTransactionByBlockHashAndIndex('0x7d5a4369273c723454ac137f48a4f142b097aa2779464e6505f1b1c5e37b5382', 2)
    test_eth_getTransactionByBlockNumberAndIndex(5000000, 3)

    test_eth_getTransactionReceipt('0x569c5b35f203ca6db6e2cec44bceba756fad513384e2bd79c06a8c0181273379')
    #test_eth_getUncleByUncleHash('0xb31db2ee05835be4fd025ae16eecaa55b670c1b67a009969a7912bea39f9951b')

@pytest.fixture
def test_get_all_blocks():
    rv=json.loads(api.get_all_blocks())
    assert isinstance(rv[0]['block_number'],int)

@pytest.fixture
def test_eth_blockNumber():
    rv=json.loads(api.eth_blockNumber())
    assert isinstance(rv[0]['block_number'],int)

@pytest.fixture
def test_eth_getBlockByNumber(blockno):
    rv=json.loads(api.eth_getBlockByNumber(blockno))
    assert rv[0]['block_number']==blockno

@pytest.fixture
def test_eth_getBlockByHash(block_hash):
    rv=json.loads(api.eth_getBlockByHash(block_hash))
    assert rv[0]['block_hash']==block_hash

@pytest.fixture
def test_eth_getBlockTransactionCountByHash(block_hash):
    block=json.loads(api.eth_getBlockByHash(block_hash))
    rv=json.loads(api.eth_getBlockTransactionCountByHash(block_hash))
    assert rv[0]['transaction_count']==block[0]['transaction_count']

@pytest.fixture
def test_eth_getBlockTransactionCountByNumber(blockno):
    block=json.loads(api.eth_getBlockByNumber(blockno))
    rv=json.loads(api.eth_getBlockTransactionCountByNumber(blockno))
    assert rv[0]['transaction_count']==block[0]['transaction_count']

@pytest.fixture
def test_eth_getUncleCountByBlockHash(block_hash):
    block=json.loads(api.eth_getBlockByHash(block_hash))
    rv=json.loads(api.eth_getUncleCountByBlockHash(block_hash))
    assert rv[0]['uncle_count']==block[0]['uncle_count']

@pytest.fixture
def test_eth_getUncleCountByBlockNumber(blockno):
    block=json.loads(api.eth_getBlockByNumber(blockno))
    rv=json.loads(api.eth_getUncleCountByBlockNumber(blockno))
    assert rv[0]['uncle_count']==block[0]['uncle_count']




@pytest.fixture
def test_eth_getTransactionByHash(transaction_hash):
    rv=json.loads(api.eth_getTransactionByHash(transaction_hash))
    assert rv[0]['transaction_hash']==transaction_hash

@pytest.fixture
def test_eth_getTransactionByBlockHashAndIndex(block_hash, transaction_index):
    block=json.loads(api.eth_getBlockByHash(block_hash))
    rv=json.loads(api.eth_getTransactionByBlockHashAndIndex(block_hash, transaction_index))
    assert rv[0]['transaction_index']==transaction_index
    assert rv[0]['block_number']==block[0]['block_number']

@pytest.fixture
def test_eth_getTransactionByBlockNumberAndIndex(blockno, transaction_index):
    rv=json.loads(api.eth_getTransactionByBlockNumberAndIndex(blockno, transaction_index))
    assert rv[0]['transaction_index']==transaction_index
    assert rv[0]['block_number']==blockno



@pytest.fixture
def test_eth_getTransactionReceipt(transaction_hash):
    rv=json.loads(api.eth_getTransactionReceipt(transaction_hash))
    assert rv[0]['transaction_hash']==transaction_hash


@pytest.fixture
def test_eth_getUncleByUncleHash(uncle_hash):
    rv=json.loads(api.eth_getUncleByUncleHash(uncle_hash))
    assert rv[0]['uncle_hash']==uncle_hash


test_links()

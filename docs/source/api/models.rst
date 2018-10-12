API Classes & Methods
=====================

This section aims at giving a detailed description of the psql tables in the database and their corresponding helper functions.

ApiBlocks
---------
A blockchain is literally a chain of blocks. A block contains a list of transactions, few features to prove the work done by a miner and a list of uncles.

.. autoclass:: api.models.api_blocks.ApiBlocks

ApiTransactions
---------------
A transaction is the basic method for Ethereum accounts to interact with each other. The transaction is a single cryptographically signed instruction sent to the Ethereum network and has the capacity to change the world state.

.. autoclass:: api.models.api_transactions.ApiTransactions

ApiUncles
---------
Due to ethereum block-chains fast block propagation time (~15 seconds), the probability of a block with sufficient proof-of-work becoming stale becomes quite high. This reduces the security and miner decentralization of block-chain. To rectify this issue ethereum proposes a modified-GHOST protocol by including and rewarding uncles (ommers) or stale blocks not included in the blockchain.

.. autoclass:: api.models.api_uncles.ApiUncles

ApiReceipts
-----------
Receipts information concerning the execution of a transaction in the block-chain. They can be useful to form a zero-knowledge proof, index and search, and debug transactions. The status column was included after the Byzantinium hardfork.

.. autoclass:: api.models.api_receipts.ApiReceipts

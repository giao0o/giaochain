from giao_blockchain.block import Block
from giao_blockchain.blockchain import Blockchain

chain = Blockchain()

# 添加新交易区块
block1 = Block(index=1, transactions=[{'from': 'alice', 'to': 'bob', 'amount': 100}], previous_hash="")
chain.add_block(block1)

block2 = Block(index=2, transactions=[{'from': 'bob', 'to': 'giao', 'amount': 50}], previous_hash="")
chain.add_block(block2)

# 显示整个链
for block in chain.chain:
    print(block)

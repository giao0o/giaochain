from giao_blockchain.block import Block
from giao_blockchain.blockchain import Blockchain
from giao_blockchain.utils import current_timestamp, sha256, pretty_print_block

chain = Blockchain()

# 添加新交易区块
block1 = Block(index=1, transactions=[{'from': 'alice', 'to': 'bob', 'amount': 100}], previous_hash="")
chain.add_block(block1)

block2 = Block(index=2, transactions=[{'from': 'bob', 'to': 'giao', 'amount': 50}], previous_hash="")
chain.add_block(block2)

# 显示整个链
for block in chain.chain:
    print(block)
    pretty_print_block(block)

print("当前时间戳:", current_timestamp())
print("哈希值:", sha256({"hello": "giao"}))


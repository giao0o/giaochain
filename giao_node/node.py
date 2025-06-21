from giao_blockchain.blockchain import Blockchain
from giao_blockchain.block import Block


class GiaoNode:
    def __init__(self):
        self.blockchain = Blockchain()
        self.transaction_pool = []

    def receive_transaction(self, tx):
        # 简单验证
        if "from" in tx and "to" in tx and "amount" in tx:
            self.transaction_pool.append(tx)
            return True
        return False

    def mine_block(self):
        if not self.transaction_pool:
            return None
        new_block = Block(
            index=len(self.blockchain.chain),
            transactions=self.transaction_pool,
            previous_hash=self.blockchain.get_latest_block().hash
        )
        self.blockchain.add_block(new_block)
        self.transaction_pool = []
        return new_block

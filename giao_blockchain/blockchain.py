from giao_blockchain.block import Block


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4  # basic PoW

    def create_genesis_block(self):
        return Block(index=0, transactions=[{'from': 'system', 'to': 'first_user', 'amount': 10000}],
                     previous_hash='0')

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        self.proof_of_work(new_block)
        self.chain.append(new_block)

    def proof_of_work(self, block):
        while not block.hash.startswith('0' * self.difficulty):
            block.nonce += 1
            block.hash = block.calculate_hash()

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]
            if curr.hash != curr.calculate_hash() or curr.previous_hash != prev.hash:
                return False
        return True

from flask import Flask, jsonify, request
from giao_node.node import GiaoNode

app = Flask(__name__)
node = GiaoNode()

@app.route('/chain', methods=['GET'])
def get_chain():
    return jsonify([block.__dict__ for block in node.blockchain.chain]), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    tx = request.get_json()
    success = node.receive_transaction(tx)
    return jsonify({'status': 'ok' if success else 'invalid transaction'})

@app.route('/mine', methods=['POST'])
def mine():
    block = node.mine_block()
    if block:
        return jsonify(block.__dict__), 201
    return jsonify({'message': 'No transactions to mine'}), 400

if __name__ == '__main__':
    app.run(port=5000)

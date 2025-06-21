import hashlib
import json
import time


def current_timestamp():
    """返回当前 UNIX 时间戳（float）"""
    return time.time()


def sha256(data):
    """对任意对象数据进行 SHA256 哈希"""
    if isinstance(data, dict):
        data = json.dumps(data, sort_keys=True)
    elif not isinstance(data, str):
        data = str(data)
    return hashlib.sha256(data.encode()).hexdigest()


def pretty_print_block(block):
    """美化输出一个区块的内容（调试用）"""
    print(f"Block #{block.index}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Hash: {block.hash}")
    print(f"Nonce: {block.nonce}")
    print("Transactions:")
    for tx in block.transactions:
        print(f"  - From {tx['from']} to {tx['to']}: {tx['amount']}")
    print("-" * 40)

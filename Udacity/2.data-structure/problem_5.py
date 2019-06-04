# linked list with hash
import hashlib
from datetime import datetime

class Block:
    
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = (str(self.previous_hash) + str(self.data) + str(self.timestamp)).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class BlockChain:

    def __init__(self):
        self.head = None
        self.pre_hash = 0

    def add_block(self, data):
        utc_now = lambda : datetime.utcnow()
        new_block = Block(utc_now, data, self.pre_hash) 
        self.pre_hash = new_block.hash
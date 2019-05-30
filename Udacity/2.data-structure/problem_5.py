# linked list with hash
import hashlib
from datetime import datetime

class Block:
    
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = (str(self.previous_hash) + str(self.data) + str(self.timestamp)).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class BlockChain:

    def __init__(self):
        """
        double headed linked list
        """
        self.head = None
        self.tail = None
        self.pre_hash = 0

    def add_block(self, data):
        if not data: raise Exception("argument cannot be empty.")
        utc_now = datetime.utcnow()
        new_block = Block(utc_now, data, self.pre_hash) 
        self.pre_hash = new_block.hash
        
        if not self.head: 
            self.head = new_block
            self.tail = new_block
            return 
        
        self.tail.next = new_block
        self.tail = self.tail.next
    

    def print_block_chain(self):
        if not self.head: print("block chain is empty.")

        cur = self.head
        while cur:
            print("-----------")
            print("timestamp: ", str(cur.timestamp))
            print("data: ", cur.data)
            print("hash: ", cur.hash)
            print("previous hash: ", cur.previous_hash)
            print("-----------")
            print(r" || ")
            print(r" \/ ")

            cur = cur.next
    
print("=== test case 1 ===")
block_chain = BlockChain()
block_chain.add_block("Hello!!!")
block_chain.add_block("I am very happy!")
block_chain.add_block(":)")
block_chain.print_block_chain()
# should return 3 blocks with associated data

print("=== test case 2 ===")
block_chain = BlockChain()
block_chain.add_block("only one block")
block_chain.print_block_chain()
# should return one block with associated data

print("=== test case 3 ===")
block_chain = BlockChain()
block_chain.print_block_chain()
# should return "block chain is empty."

print("=== test case 4 ===")
block_chain = BlockChain()
block_chain.add_block("")
# should raise an error "argument cannot be empty."
Desicion:

Using a class to encapsulate the data as a block. When creating a BlockChain, we dynamically add blocks to the BlockChain.

Using double headed linked list (head, tail) for fast insertion when adding new block


Time: 
add_block: O(1)
print_block: O(n)


Space: O(n)    to store n blocks in the chain
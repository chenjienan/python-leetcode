import sys
import collections
import heapq

class HuffmanNode:
    def __init__(self, ch, freq):
        self.freq = freq
        self.ch = ch
        self.left = None
        self.right = None

    # define a method __cmp__() within class definition, which 
    # will compare itself to another instance of the same class
    def __lt__(self, other):
        return self.freq < other.freq

# hashtable + tree
def huffman_encoding(data):
    """
    1. Take a string and determine the relevant frequencies of the characters.
    2. Build and sort a list of tuples from lowest to highest frequencies.
    3. Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters. (This is the heart of the Huffman algorithm.)
    4. Trim the Huffman Tree (remove the frequencies from the previously built tree).
    """
    # map frequencies to characters
    fequency = collections.Counter(data)
    
    # construct a min heap to store (freq, huffman_node)
    # rather than using a list, heap is able to auto-sort when re-insert the node
    heap = []
    for ch, freq in fequency.items():

        # create huffman node object
        new_node = HuffmanNode(ch, freq)
        heapq.heappush(heap, new_node)

    huffman_root = None
    # print(heap)
    while len(heap) > 1:
        first_min = heapq.heappop(heap)
        second_min = heapq.heappop(heap)

        # merge two node and generate a new one
        merge_node = HuffmanNode('#', first_min.freq + second_min.freq)
        merge_node.left = first_min
        merge_node.right = second_min

        # The remaining node is the root node
        huffman_root = merge_node
        heapq.heappush(heap, merge_node)
    
    codes = get_compressed_form(huffman_root)
    encoded_data = ""
    for ch in data:
        encoded_data += codes[ch]
    print('====', codes)
    return encoded_data, huffman_root


def get_compressed_form(huffman_root):
    """    
    left => 0
    right => 1
    the charater is the leaf    
    """    
    codes = {}
    # tuple: (node, path to this node)
    stack = [(huffman_root, "")]
    
    while stack:
        cur_node, path = stack.pop()
        
        # leaf
        if not cur_node.left and not cur_node.right:            
            codes[cur_node.ch] = path
        if cur_node.left:
            stack.append((cur_node.left, path + '0'))
        if cur_node.right:
            stack.append((cur_node.right, path + '1'))
                
    return codes

def huffman_decoding(encoded_data, tree):
    '''
    iterate through the encoded data until we find the leaf
    '''
    cur_node = tree
    decoded_data = ""
    for i in range(len(encoded_data)):
        if encoded_data[i] == '0':
            cur_node = cur_node.left
        else:
            cur_node = cur_node.right
        
        if not cur_node.left and not cur_node.right:
            decoded_data += cur_node.ch
            # reset cur_node to root once a char is found
            cur_node = tree
        
    return decoded_data

if __name__ == "__main__":

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
        
    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)
    
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        cur_node = self.root
        for w in word:
            cur_node = cur_node.insert(w)

        cur_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        cur_node = self.root
        for w in prefix:
            if w not in cur_node.children: return None

            cur_node = cur_node.children[w]

        return cur_node            




# insert word: AND
# Trie root = TrieNode
# no children
#      TrieNode (root)
#           |
#           A
#           |
#           N
#           |
#           D

from collections import defaultdict
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = defaultdict(TrieNode)
        self.is_word = False
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
        return self.children[char]
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        words = []

        while self.children:


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');
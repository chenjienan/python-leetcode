#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
from collections import defaultdict

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur_node = self.root
        for ch in word:
            # the following step can be save 
            # when used defaultdict 

            # ########################################
            # if ch not in cur_node.children:        #
            #     cur_node.children[ch] = TrieNode() #
            # ########################################
            # set next node like a chain
            cur_node = cur_node.children[ch]
        cur_node.is_word = True    
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur_node = self.root

        if not cur_node:
            return False
        
        for ch in word:
            if ch not in cur_node.children:
                return False
            cur_node = cur_node.children[ch]
        
        return cur_node.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur_node = self.root

        if not cur_node:
            return False
        
        for ch in prefix:
            if ch not in cur_node.children:
                return False
            cur_node = cur_node.children[ch]
        
        return True
        

class TrieNode:

    def __init__(self):
        # self.children = {}

        # use defaultdict instead
        self.children = defaultdict(TrieNode)
        self.is_word = False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


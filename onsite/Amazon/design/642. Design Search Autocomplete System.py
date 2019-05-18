class Trie:
    def __init__(self):
        self.root = {}
    
    def insert(self, word):
        cur = self.root
        for l in word:
            if l not in cur:
                cur[l] = {}
            cur = cur[l]
        cur['#'] = word
    
    def search(self, prefix, cur = None): #Python cannot set default value to be self.varible cuz it's not a value yet
        if not cur: cur = self.root
        for l in prefix:
            if l not in cur:
                return []
            cur = cur[l]
        #dfs from l to get the word
        ret = []
        
        for k in cur:
            if k == '#':
                ret.append(cur[k])
            else:
                ret += self.search('', cur[k])
        return ret

class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.lookUp = {}
        for i, s in enumerate(sentences):
            self.lookUp[s] = times[i]
        self.trie = Trie()
        for s in sentences:
            self.trie.insert(s)
        self.keyword = ""

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == '#': #should be saved as a historical sentence in system
            self.lookUp[self.keyword] = self.lookUp.get(self.keyword, 0) + 1
            self.trie.insert(self.keyword)
            self.keyword = ""
            return []
        
        self.keyword += c
        lst = self.trie.search(self.keyword)
        lst.sort(key = lambda x: (-self.lookUp[x], x)) 
        return lst[:3]

# template
class Trie:
    
    def __init__(self):
        self.root = TrieNode()  #global var

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        
        node.is_word = True
        
    def find(self, word):
        node = self.root
        
        if not node:
            return None
        for c in word:
            if c not in node.children:
                return None
            node = node.children[c]
        return node
        
    def search(self, word):
        node = self.find(word)
        return node != None and node.is_word

    def startsWith(self, prefix):
        node = self.find(prefix)
        return node != None
        

class TrieNode:
    
    def __init__(self):
        self.children ={}
        self.is_word = False
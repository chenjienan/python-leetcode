import collections

class LRU_Cache(object):
    
    def __init__(self, capacity):
        # Initialize class variables
        if capacity <= 0: 
            raise Exception("capacity cannot be 0 or nagtive.")
        self.dict = collections.OrderedDict()
        self.cap = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key not in self.dict: return -1
        
        val = self.dict[key]
        self.dict.move_to_end(key)
        return val

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key in self.dict:
            self.dict[key].move_to_end
        
        else:
            if len(self.dict) < self.cap:
                self.dict[key] = value
            else:
                self.dict.popitem(last=False)
                self.dict[key] = value

# test case 1
print("===Test case 1===")
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(3))       # return -1

# test case 2
print("===Test case 2===")
our_cache = LRU_Cache(10)
print(our_cache.get(5))        # return -1
our_cache.set('a', 123) 
print(our_cache.get('a'))      # return 123

# test case 3
print("===Test case 3===")
our_cache = LRU_Cache(2)
our_cache.set('a', None)
print(our_cache.get('a'))       # return None

# test case 4
print("===Test case 4===")
our_cache = LRU_Cache(2)
our_cache.set('a', 123456789)
our_cache.set('b', 'abcdefg')
our_cache.set('c', 'xyz')
print(our_cache.get('a'))          # return -1
print(our_cache.get('b'))          # return 'abcdefg'
print(our_cache.get('c'))          # return 'xyz'

# test case 5
print("===Test case 5===")
our_cache = LRU_Cache(2)
our_cache.set('a', 123456789)
our_cache.set('b', 'abcdefg')
print(our_cache.get('a'))          # return 123456789
our_cache.set('c', 'xyz')
print(our_cache.get('a'))          # return 123456789
print(our_cache.get('b'))          # return -1
print(our_cache.get('c'))          # return 'xyz'

# test case 6
print("===Test case 6===")
our_cache = LRU_Cache(-1)   # return Exception: capacity cannot be 0 or nagtive
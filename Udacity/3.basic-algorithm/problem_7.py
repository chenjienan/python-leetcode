# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, ...):
        # Initialize the trie with an root node and a handler, this is the root path or home page node

    def insert(self, ...):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path

    def find(self, ...):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, ...):
        # Initialize the node with children as before, plus a handler

    def insert(self, ...):
        # Insert the node as before
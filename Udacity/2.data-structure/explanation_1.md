
### Decision:

using Python OrderedDict to simplify the code.

Orderdict support regular hashmap feature for O(1) get and set.

Orderdict has method move_to_end(key) and we can easily move the key to the rear end if the key is recently used.

Orderdict can remove the key from the left side(popitem(last=False)) so that we can easily remove the key that is least recent used if capacity is reached.

time complexity:
get(key): O(1) on average
set(key): O(1) on average

Space complexity
O(n): n is the capacity of the LRU cache

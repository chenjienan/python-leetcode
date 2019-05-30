def get_min_max(ints):
   """
   Return a tuple(min, max) out of list of unsorted integers.

   Args:
      ints(list): list of integers containing one or more integers
   """
   if not ints: return 0, 0
   
   min_val = float('inf')
   max_val = -float('inf')

   for d in ints:
      min_val = min(min_val, d)
      max_val = max(max_val, d)
   
   return min_val, max_val

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
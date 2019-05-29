Decision:

Using collections.Counter to quickly calculate the frequency of each character. O(n)

In order to keep the list of tuples in order when pop and re-insert, I use min heap to build the huffman tree. O(logk)

the length of heap is O(k)

Constucting the huffman tree requires O(logk)
I create a new tree node for storing the frequency and character, and the relationship between it's child node (left child, right child)

it takes O(logk) to decode a symbol


Assuming the encoded text has length of n, and k distinct alphabet

time: O(nlogk) 

space: O(k)  needs to store each char
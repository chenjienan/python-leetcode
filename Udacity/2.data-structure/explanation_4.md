Decision:

Not quite sure what the requirements are.
I use recursion to determine if a user is in input group or in sub_groups of the input group

Assuming we have n user in each group, and we have m groups.

time: O(n + n*m) => O(n*m)

space: O(n*m)   we need to visit m groups recursively
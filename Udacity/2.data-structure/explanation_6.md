Desicion:

Using a linked list to collect all the data

union method:
Used the provided linked list, I construct the list with two given linked list. Then remove all the duplicates

intersection method:
sort and de-dup each linked list then traverse two list for the intersection.

Assuming the length of llist_1 is n, and the length of llist_2 is m.

Time:

- remove_duplicates: O(n+m)
- total: O(2(n+m)) => O(n+m)

Space: O(n+m)

intersection method:

Time:

- sorted_list + merge_sorted_lists: O(nlogn + mlogm)
- remove_duplicates: O(n+m)
- total: O(nlogn + mlogm + n + m + n + m) => O(nlogn + mlogm + n + m)

Space: O (n + m)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    """
    merge two list and remove duplicates
    """
    dummy = Node(-1)
    dummy.next = llist_1.head
    
    ptr = llist_1.head    
    while ptr.next:        
        ptr = ptr.next
        
    ptr.next = llist_2.head
    de_dup_ls_head = remove_duplicates(dummy.next)
    res_ls = LinkedList()
    while de_dup_ls_head:
        res_ls.append(de_dup_ls_head.value)
        de_dup_ls_head = de_dup_ls_head.next
        
    return res_ls


def intersection(llist_1, llist_2):
    sorted_ls_1 = sort_list(llist_1.head)
    sorted_ls_2 = sort_list(llist_2.head)

    dedup_ls_head_1 = remove_duplicates(sorted_ls_1)
    dedup_ls_head_2 = remove_duplicates(sorted_ls_2)

    new_head = LinkedList()
    while dedup_ls_head_1 and dedup_ls_head_2:
        if dedup_ls_head_1.value == dedup_ls_head_2.value:
            new_head.append(dedup_ls_head_1)
            dedup_ls_head_1 = dedup_ls_head_1.next
            dedup_ls_head_2 = dedup_ls_head_2.next
        
        while dedup_ls_head_1 and dedup_ls_head_1.value < dedup_ls_head_2.value:
            dedup_ls_head_1 = dedup_ls_head_1.next

        while dedup_ls_head_2 and dedup_ls_head_1.value > dedup_ls_head_2.value:
            dedup_ls_head_2 = dedup_ls_head_2.next

    return new_head

def remove_duplicates(head):
    hash_set = set()
    if head is None: return head
    hash_set.add(head.value)

    new_head = head;
    cur = head.next;
    while cur is not None:
        if cur.value not in hash_set:
            hash_set.add(cur.value)
            new_head.next = cur
            new_head = new_head.next
        cur = cur.next;

    new_head.next = None;
    return head;

def sort_list(head):
    if not head or not head.next: return head
    
    slow, fast = head, head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    
    mid = slow.next
    slow.next = None

    ls_1 = sort_list(mid)
    ls_2 = sort_list(head)

    return merge_sorted_lists(ls_1, ls_2)

def merge_sorted_lists(ls_1, ls_2):
    if not ls_1: return ls_2
    if not ls_2: return ls_1

    dummy = Node(-1)
    ptr = dummy
    while ls_1 and ls_2:
        if ls_1.value < ls_2.value:
            ptr.next = ls_1
            ls_1 = ls_1.next
        else:
            ptr.next = ls_2
            ls_2 = ls_2.next
        
        ptr = ptr.next
    
    ptr.next = ls_1 or ls_2
    return dummy.next


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

# print (union(linked_list_1,linked_list_2))
# print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)
    
print (intersection(linked_list_3,linked_list_4))
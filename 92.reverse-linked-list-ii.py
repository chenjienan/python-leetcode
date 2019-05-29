#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        # need dummy node for head reference
        # because the linkedlist changed after reversed.
        dummy = ListNode(-1)
        dummy.next = head        # append the list
        
        # 除了移动节点之外，关键是链接头和尾
        pre_ls_node = nth_node = dummy
        for _ in range(1, m):
            pre_ls_node = pre_ls_node.next

        for _ in range(1, n+1):
            nth_node = nth_node.next
                
        # pre_ls是reversed list的前节点
        # nxt_ls是reversed list的后节点
        mth_node = pre_ls_node.next
        nxt_ls_node = nth_node.next      # mark down 后节点
        nth_node.next = None        # set mth-node next to None for reversing

        self.reverseList(mth_node)
        pre_ls_node.next = nth_node
        mth_node.next = nxt_ls_node

        return dummy.next
        
    def reverseList(self, head):
        pre = None
        cur = head

        while cur:
            nxt = cur.next  # for moving to the next pointer
            cur.next = pre
            pre = cur
            cur = nxt
        
        return pre

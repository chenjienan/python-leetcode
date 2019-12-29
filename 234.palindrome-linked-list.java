/*
 * @lc app=leetcode id=234 lang=java
 *
 * [234] Palindrome Linked List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        
        if (head == null) {
            return true;
        }
        
        // only one node
        if (head != null && head.next == null) {
            return true;
        }
        
        ListNode slow = head;
        ListNode fast = head.next;
        
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        
        ListNode secHead = slow.next;
        slow.next = null;
        
        secHead = reverseList(secHead);
        
        while (head != null && secHead != null) {
            if (head.val != secHead.val) {
                return false;
            }
            head = head.next;
            secHead = secHead.next;
        }
        
        return true;
    }
    
    public ListNode reverseList(ListNode head) {
		ListNode pre = null;
		ListNode cur = head;

		while (cur != null) {
			ListNode nxt = cur.next;
			cur.next = pre;
			pre = cur;
			cur = nxt;
		}

		return pre;
	}
}
// @lc code=end


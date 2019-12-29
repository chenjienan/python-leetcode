/*
 * @lc app=leetcode id=230 lang=java
 *
 * [230] Kth Smallest Element in a BST
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public int kthSmallest(TreeNode root, int k) {
        List<Integer> ls = new ArrayList<Integer>();
        
        inOrder(root, ls);
        return ls.get(k-1);
    }
    
    private void inOrder(TreeNode node, List<Integer> ls){
        if (node == null){
            return; 
        }
        
        inOrder(node.left, ls);
        ls.add(node.val);
        inOrder(node.right, ls);
    }
}
// @lc code=end


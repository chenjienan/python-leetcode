/*
 * @lc app=leetcode id=226 lang=java
 *
 * [226] Invert Binary Tree
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
    public TreeNode invertTree(TreeNode node) {
        if (node == null) {
            return null;
        }
        
        TreeNode tmp = invertTree(node.left);
        node.left = invertTree(node.right);
        node.right = tmp;
        
        return node;
    }
}
// @lc code=end


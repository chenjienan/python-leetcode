#
# @lc app=leetcode id=655 lang=python3
#
# [655] Print Binary Tree
#
# https://leetcode.com/problems/print-binary-tree/description/
#
# algorithms
# Medium (51.46%)
# Total Accepted:    19.2K
# Total Submissions: 37.3K
# Testcase Example:  '[1,2]'
#
# Print a binary tree in an m*n 2D string array following these rules: 
# 
# 
# The row number m should be equal to the height of the given binary tree.
# The column number n should always be an odd number.
# The root node's value (in string format) should be put in the exactly middle
# of the first row it can be put. The column and the row where the root node
# belongs will separate the rest space into two parts (left-bottom part and
# right-bottom part). You should print the left subtree in the left-bottom part
# and print the right subtree in the right-bottom part. The left-bottom part
# and the right-bottom part should have the same size. Even if one subtree is
# none while the other is not, you don't need to print anything for the none
# subtree but still need to leave the space as large as that for the other
# subtree. However, if two subtrees are none, then you don't need to leave
# space for both of them. 
# Each unused space should contain an empty string "".
# Print the subtrees following the same rules.
# 
# 
# Example 1:
# 
# Input:
# ⁠    1
# ⁠   /
# ⁠  2
# Output:
# [["", "1", ""],
# ⁠["2", "", ""]]
# 
# 
# 
# 
# Example 2:
# 
# Input:
# ⁠    1
# ⁠   / \
# ⁠  2   3
# ⁠   \
# ⁠    4
# Output:
# [["", "", "", "1", "", "", ""],
# ⁠["", "2", "", "", "", "3", ""],
# ⁠["", "", "4", "", "", "", ""]]
# 
# 
# 
# Example 3:
# 
# Input:
# ⁠     1
# ⁠    / \
# ⁠   2   5
# ⁠  / 
# ⁠ 3 
# ⁠/ 
# 4 
# Output:
# 
# [["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
# ⁠["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
# ⁠["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
# ⁠["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
# 
# 
# 
# Note:
# The height of binary tree is in the range of [1, 10].
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# tree/tree height, recursion
class Solution:
    def printTree(self, root):
        
        height = self.getHeight(root)                       # get the height recursively
        width = 2 ** height - 1                             # binary tree attribute: 2 node with root
        
        # construct a 2D list
        self.res = [[""] * width for _ in range(height)]    # initialize the result list        
        self.fill(root, 0, 0, width - 1)                    # recursively 
        return self.res

    def fill(self, node, h, l, r):
        if not node: return
        mid = (l + r) // 2
        self.res[h][mid] = str(node.val)
        self.fill(node.left, h + 1, l, mid - 1)
        self.fill(node.right, h + 1, mid + 1, r)
        
    def getHeight(self, root):
        if not root: return 0        
        return max(
            self.getHeight(root.left), 
            self.getHeight(root.right)) + 1


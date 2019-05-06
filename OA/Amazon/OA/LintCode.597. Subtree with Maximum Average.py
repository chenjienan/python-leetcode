# Given a binary tree, find the subtree with maximum average. Return the root of the subtree.

# LintCode will print the subtree which root is your return node.
# It's guaranteed that there is only one subtree with maximum average.

# Have you met this question in a real interview?  
# Example
# Example 1

# Input：
#      1
#    /   \
#  -5     11
#  / \   /  \
# 1   2 4    -2 
# Output：11(it's a TreeNode)
# Example 2

# Input：
#      1
#    /   \
#  -5     11
# Output：11(it's a TreeNode)

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the root of the maximum average of subtree
    
    def findSubtree2(self, root):
        # Write your code here
        self.max_ave_pair = (-float('inf'), None)    # store max-average and the node

        self._helper(root)
        return self.max_ave_pair[1]

        # return the total value and the size
        # of the subtree
    def _helper(self, node):       
        if not node: return 0, 0
        
        # divide and conquer 
        left_total, left_num = self._helper(node.left)
        right_total, right_num = self._helper(node.right)
        
        total = left_total + right_total + node.val
        size = left_num + right_num + 1

        # search for the max_ave of the subtree
        # then replace the old one
        ave = total / size
        if ave > self.max_ave_pair[0]:
            self.max_ave_pair = (ave, node)
            
        return total, size




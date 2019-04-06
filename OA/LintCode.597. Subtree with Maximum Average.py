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
    average_val = 0
    node = None
    
    def findSubtree2(self, root):
        # Write your code here
        self.visit(root)
        return self.node
        
    
    def visit(self, node):
        
        if node is None:
            return 0, 0
        
        left_sum, left_size = self.visit(node.left)
        right_sum, right_size = self.visit(node.right)
        
        # avg = sum / size
        cur_max = left_sum + right_sum + node.val
        node_num = left_size + right_size + 1
        
        cur_average = cur_max * 1.0 / node_num
        
        if self.node is None or cur_average > self.average_val:
            self.average_val = cur_average
            self.node = node
        
        return cur_max, node_num
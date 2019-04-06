# LintCode 1561
# Given a list of numbers, construct a BST from it(you need to insert nodes one-by-one with the given 
# order to get the BST) and find the distance between two given nodes.

# If two nodes do not appear in the BST, return -1
# We guarantee that there are no duplicate nodes in BST
# The node distance means the number of edges between two nodes
# Have you met this question in a real interview?  
# Example
# Example 1

# Input:
# numbers = [2,1,3]
# node1 = 1
# node2 = 3
# Output:
# 2
# Explaination:
# The tree is look like this.
#   2
#  / \
# 1  3 
# Example 2

# Input:
# numbers = [2,1]
# node1 = 1
# node2 = 3
# Output: -1

# class TreeNode:
    
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    """
    @param numbers: the given list
    @param node1: the given node1
    @param node2: the given node2
    @return: the distance between two nodes
    """
    def bstDistance(self, numbers, node1, node2):
        # Write your code here
        res = 0
        if not numbers: return 0
        root = self.insertBST(None, numbers[0])
        for num in numbers[1:]:
            self.insertBST(root, num)
        
        if node1 > node2:
            node1, node2 = node2, node1
        
        if node1 in numbers and node2 in numbers:
            return self.distanceBetweenNodes(root, node1, node2)
        else:
            return -1
            
    def distanceFromRoot(self, root, x):
        if not root or root.val == x:
            return 0
        elif root.val > x:
            return 1 + self.distanceFromRoot(root.left, x)
        else:
            return 1 + self.distanceFromRoot(root.right, x)
    
    def distanceBetweenNodes(self, root, node1, node2):
        if not root: return 0
        
        # both nodes lie in left
        if root.val > node1 and root.val > node2:
            return self.distanceBetweenNodes(root.left, node1, node2)
        
        # both nodes lie in right
        elif root.val < node1 and root.val < node2:
            return self.distanceBetweenNodes(root.right, node1, node2)
            
        # lie in opposite directions (Root is LCA of two nodes)
        return self.distanceFromRoot(root, node1) + self.distanceFromRoot(root, node2)
        
    def insertBST(self, root, val):
        if not root:
            root = TreeNode(val)
        elif val < root.val:
            root.left = self.insertBST(root.left, val)
        else:
            root.right = self.insertBST(root.right, val)
        return root
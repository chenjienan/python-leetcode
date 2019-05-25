#
# @lc app=leetcode id=450 lang=python
#
# [450] Delete Node in a BST
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: return None
        
        # delete from the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # delete from the left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # delete the current node
        else:
            # the node is a leaf
            if not root.left and not root.right: root = None
            # the node is not a leaf and has a right child
            elif root.right:
                # 晚辈
                # replace by successor and remove cur-successor (右子树最小)
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            # the node is not a leaf, has no right child, and has a left child    
            else:
                # 前辈
                # replace by predecessor and remove cur-predecessor (左子树最大)
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
                        
        return root

        # if not root: return None

        # if root.val == key:
        #     if not root.left and not root.right: return None    # leaf
        #     if not root.left: return root.right                 # 没左节点,右节点接上
        #     if not root.right: return root.left                 # 没右节点,左节点接上
            
        #     left = root.left
        #     right = root.right

        #     # predecessor: one step right, then always left
        #     p = right
        #     while p.left: 
        #         p = p.left
        #     p.left = left
        #     return right

        # if key > root.val: 
        #     root.right = self.deleteNode(root.right, key)
        # else: 
        #     root.left = self.deleteNode(root.left, key)
        # return root

    def successor(self, root):
        """
        One step right and then always left
        """
        root = root.right
        while root.left:
            root = root.left
        return root.val
    
    def predecessor(self, root):
        """
        One step left and then always right
        """
        root = root.left
        while root.right:
            root = root.right
        return root.val    
        


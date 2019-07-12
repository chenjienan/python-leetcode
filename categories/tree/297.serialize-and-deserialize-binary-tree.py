#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ""
        res = []
        queue = collections.deque([root])

        while queue:
            cur_node = queue.popleft()
            # add self
            res.append(str(cur_node.val) if cur_node else '#')
            
            # add child nodes
            if cur_node:
                queue.append(cur_node.left)
                queue.append(cur_node.right)
            
        return ' '.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        
        # keep a record of the serialized data in list format
        node_ls = data.split()
        root = TreeNode(int(node_ls[0]))
        queue = collections.deque([root])
        # counter to find left and right children
        i = 1
        while queue:
            cur_node = queue.popleft()  
            # find left child
            if node_ls[i] != '#':
                cur_node.left = TreeNode(int(node_ls[i]))
                queue.append(cur_node.left)
            # increment to the next char
            i += 1

            # find right child
            if node_ls[i] != '#':
                cur_node.right = TreeNode(int(node_ls[i]))
                queue.append(cur_node.right)
            i += 1

        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


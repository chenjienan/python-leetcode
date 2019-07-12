#
# @lc app=leetcode id=662 lang=python
#
# [662] Maximum Width of Binary Tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # (node, index)
        # index从0开始
        #      0
        #    1   2
        #  3  4   6
        queue = collections.deque([(root, 0)])

        res = 0
        while queue:
            # left指针用来记录当前层的最左端
            left = queue[0][1]
            right = left
            for _ in range(len(queue)):
                # right指针一直往右走, 直到没有节点
                node, right = queue.popleft()
                # 赋值给下一层 (此处需要技巧)
                if node.left: queue.append((node.left, right * 2 + 1))
                if node.right: queue.append((node.right, right * 2 + 2))
            res = max(res, right - left + 1)

        return res
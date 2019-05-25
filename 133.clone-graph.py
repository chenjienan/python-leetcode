#
# @lc app=leetcode id=133 lang=python
#
# [133] Clone Graph
#

# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

import collections
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        # mapping from the nodes in the original graph to the cloned graph.
        visited = {}
        dummy = Node(-1, [])

        # (node, parent_node)
        queue = collections.deque([(node, dummy)])
        while queue:
            cur_node, parent = queue.popleft()

            if cur_node not in visited:
                # create a new node and add it to parent.nei
                new_node = Node(cur_node.val, [])
                parent.neighbors.append(new_node)
                
                # get next node
                for neighbor in cur_node.neighbors:
                    queue.append((neighbor, new_node))
                visited[cur_node] = new_node
            else:
                parent.neighbors.append(visited[cur_node])
            
        return dummy.neighbors[0]


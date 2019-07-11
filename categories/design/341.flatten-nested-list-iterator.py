#
# @lc app=leetcode id=341 lang=python
#
# [341] Flatten Nested List Iterator
#
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):
   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.next_item = None
        self.stack = []
        for item in reversed(nestedList):
            self.stack.append(item)

    #  # return the next element in the iteration
    def next(self):
        """
        :rtype: int
        """
        # 0和None在if statement中都等于False，
        # 当用if self.next_elem:时可能会把0值误判为None
        if self.next_item is None:
            self.hasNext()

        cur_item, self.next_item = self.next_item, None
        return cur_item

    # return true if the iteration has more element or false
    def hasNext(self):
        """
        :rtype: bool
        """
        if self.next_item: return True
        
        while self.stack:
            top = self.stack.pop()
            if top.isInteger():
                self.next_item = top.getInteger()
                return True
            for item in reversed(top.getList()):
                self.stack.append(item)
        return False
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())


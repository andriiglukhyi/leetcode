# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.items = []
        for item in nestedList:
            self.unpack(nestedList)
        self.pos = 0
        print(self.items)
    def unpack(self, array):
        if not array:
            return
        for item in array:
            print(item)
            if type(item) is list:
                unpack(item)
            else:
                self.items.append(item)
                
    def next(self):
        """
        :rtype: int
        """
        self.pos += 1
        return self.items[self.pos-1]
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.pos > len(self.items)-1:
            return True
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
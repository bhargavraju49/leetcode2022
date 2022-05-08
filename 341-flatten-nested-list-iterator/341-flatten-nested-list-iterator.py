# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.arr = []
        self.counter = 0
        
        def flattern(x):
            # print(x)
            for i in x:
                if i.isInteger():
                    self.arr.append(i.getInteger())
                else:
                    l = i.getList()
                    flattern(l)
        flattern(nestedList)
        
    
    def next(self) -> int:
        
        ele = self.arr[self.counter]
        self.counter += 1
        return ele
        
    
    def hasNext(self) -> bool:
        if self.counter < len(self.arr):
            return True
        return False
        
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
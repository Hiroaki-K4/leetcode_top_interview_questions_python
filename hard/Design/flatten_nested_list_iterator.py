# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
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
    def __init__(self, nestedList):
        self.stack = nestedList[::-1]  # Initial stack (reversed)

    def next(self):
        if not self.hasNext():
            return None

        return self.stack.pop().getInteger()  # Directly pop and get integer

    def hasNext(self):
        while self.stack:
            top = self.stack[-1]  # Peek at the top
            if top.isInteger():
                return True
            else:
                self.stack.pop()  # Remove the list
                lst = top.getList()
                # Crucial fix: Extend the stack with the list elements in REVERSE order
                self.stack.extend(
                    lst[::-1]
                )  # Correctly reverse the list elements onto the stack
        return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

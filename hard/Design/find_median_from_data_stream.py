import heapq


class MedianFinder:
    def __init__(self):
        # Max heap for the left half (inverted to work with Python's min heap)
        self.left = []
        # Min heap for the right half
        self.right = []

    def addNum(self, num: int) -> None:
        # Insert into max heap (left)
        heapq.heappush(self.left, -num)

        # Ensure max of left is not greater than min of right
        if self.left and self.right and (-self.left[0] > self.right[0]):
            heapq.heappush(self.right, -heapq.heappop(self.left))

        # Balance the heap sizes (left can have at most one more element than right)
        if len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        elif len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (-self.left[0] + self.right[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

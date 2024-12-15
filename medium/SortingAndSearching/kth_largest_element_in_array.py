import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)
            # Ensure heap size does not exceed k
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]


if __name__ == "__main__":
    solution = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print("Input: nums = {0}, k = {1}".format(nums, k))
    print("Output: {0}".format(solution.findKthLargest(nums, k)))
    print()

    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print("Input: nums = {0}, k = {1}".format(nums, k))
    print("Output: {0}".format(solution.findKthLargest(nums, k)))

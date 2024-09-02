from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Use a sliding window for speed and memory efficiency
        current_sum = sum(nums[:k])
        max_sum = current_sum
        for i in range(k, len(nums)):
            current_sum = current_sum - nums[i - k] + nums[i]
            max_sum = max(current_sum, max_sum)

        return max_sum / k


if __name__ == '__main__':
    solution = Solution()
    nums = [1,12,-5,-6,50,3]
    k = 4
    print("Input: nums={0}, k={1}".format(nums, k))
    print("Output: {0}".format(solution.findMaxAverage(nums, k)))
    print()
    nums = [5]
    k = 1
    print("Input: nums={0}, k={1}".format(nums, k))
    print("Output: {0}".format(solution.findMaxAverage(nums, k)))

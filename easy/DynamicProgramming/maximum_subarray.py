from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane’s Algorithm
        max_sum = current_sum = nums[0]  # Start with the first element

        for num in nums[1:]:
            current_sum = max(
                num, current_sum + num
            )  # Continue the subarray or start a new one
            max_sum = max(max_sum, current_sum)  # Update the maximum sum found

        return max_sum


if __name__ == "__main__":
    solution = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.maxSubArray(nums)))
    print()

    nums = [1]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.maxSubArray(nums)))
    print()

    nums = [5, 4, -1, 7, 8]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.maxSubArray(nums)))

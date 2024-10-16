from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # Initialize dp array
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # Fill dp array using the recurrence relation
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        # The last element of dp contains the result
        return dp[-1]


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 1]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.rob(nums)))
    print()

    nums = [2, 7, 9, 3, 1]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.rob(nums)))

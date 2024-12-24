from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n  # dp[i] is the length of LIS ending at index i

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


if __name__ == "__main__":
    solution = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.lengthOfLIS(nums)))
    print()

    nums = [0, 1, 0, 3, 2, 3]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.lengthOfLIS(nums)))
    print()

    nums = [7, 7, 7, 7, 7, 7, 7]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.lengthOfLIS(nums)))

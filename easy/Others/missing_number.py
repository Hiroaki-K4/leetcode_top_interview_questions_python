from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        candidates = list(range(len(nums) + 1))
        for num in nums:
            candidates.remove(num)

        return candidates[0]


if __name__ == "__main__":
    solution = Solution()
    nums = [3, 0, 1]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.missingNumber(nums)))
    print()

    solution = Solution()
    nums = [0, 1]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.missingNumber(nums)))
    print()

    solution = Solution()
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.missingNumber(nums)))

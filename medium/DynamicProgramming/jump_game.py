from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
            if farthest >= len(nums) - 1:
                return True
        return False


if __name__ == "__main__":
    solution = Solution()
    nums = [2, 3, 1, 1, 4]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.canJump(nums)))
    print()

    nums = [3, 2, 1, 0, 4]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.canJump(nums)))

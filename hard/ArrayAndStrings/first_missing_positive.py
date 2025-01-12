from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Step 1: Place each number in its correct position
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with the number at its correct position
                temp = nums[i]
                nums[i] = nums[temp - 1]
                nums[temp - 1] = temp

        # Step 2: Identify the first missing positive
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # Step 3: If all numbers are in place, return n + 1
        return n + 1


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 0]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.firstMissingPositive(nums)))
    print()

    nums = [3, 4, -1, 1]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.firstMissingPositive(nums)))
    print()

    nums = [7, 8, 9, 11, 12]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.firstMissingPositive(nums)))

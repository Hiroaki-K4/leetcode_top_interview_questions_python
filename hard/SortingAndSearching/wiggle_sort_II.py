from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums.sort()

        temp = [0] * n
        mid = n // 2

        left = mid - 1 if n % 2 == 0 else mid
        right = n - 1

        for i in range(n):
            if i % 2 == 0:
                temp[i] = nums[left]
                left -= 1
            else:
                temp[i] = nums[right]
                right -= 1

        nums[:] = temp[:]


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 5, 1, 1, 6, 4]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.wiggleSort(nums)))
    print()

    nums = [1, 3, 2, 2, 3, 1]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.wiggleSort(nums)))

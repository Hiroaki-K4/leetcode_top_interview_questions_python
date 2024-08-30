from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < k:
            nums.insert(0, nums[-1])
            nums.pop(-1)
            i += 1


if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    k = 3
    print("Input: nums={0}, k={1}".format(nums, k))
    solution = Solution()
    solution.rotate(nums, k)
    print("Output: {0}".format(nums))
    print()
    nums = [-1,-100,3,99]
    k = 2
    print("Input: nums={0}, k={1}".format(nums, k))
    solution.rotate(nums, k)
    print("Output: {0}".format(nums))

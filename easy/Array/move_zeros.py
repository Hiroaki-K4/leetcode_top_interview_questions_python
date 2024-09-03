from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < len(nums) - 1:
            # Stop loop if the remaining elements are all zero
            if sum(nums[i:]) == 0:
                break
            # If element is zero, move it to the last of list
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
            else:
                i += 1


if __name__ == "__main__":
    solution = Solution()
    nums = [0, 1, 0, 3, 12]
    print("Input: nums ={0}".format(nums))
    solution.moveZeroes(nums)
    print("Output: {0}".format(nums))
    print()
    nums = [0]
    print("Input: nums ={0}".format(nums))
    solution.moveZeroes(nums)
    print("Output: {0}".format(nums))

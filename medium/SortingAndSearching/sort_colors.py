from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums) - 1

        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] == 1:
                white += 1
            elif nums[white] == 2:
                nums[blue], nums[white] = nums[white], nums[blue]
                blue -= 1


if __name__ == "__main__":
    solution = Solution()
    nums = [2, 0, 2, 1, 1, 0]
    print("Input: nums = {0}".format(nums))
    solution.sortColors(nums)
    print("Output: {0}".format(nums))
    print()

    nums = [2, 0, 1]
    print("Input: nums = {0}".format(nums))
    solution.sortColors(nums)
    print("Output: {0}".format(nums))

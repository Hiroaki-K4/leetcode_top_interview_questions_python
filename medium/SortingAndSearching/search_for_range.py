from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_left_index(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def find_right_index(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left_index = find_left_index(nums, target)
        right_index = find_right_index(nums, target)

        # Verify if the target exists in the range
        if (
            left_index <= right_index
            and left_index < len(nums)
            and nums[left_index] == target
        ):
            return [left_index, right_index]
        else:
            return [-1, -1]


if __name__ == "__main__":
    solution = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print("Input: nums = {0}, target = {1}".format(nums, target))
    print("Output: {0}".format(solution.searchRange(nums, target)))
    print()

    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    print("Input: nums = {0}, target = {1}".format(nums, target))
    print("Output: {0}".format(solution.searchRange(nums, target)))
    print()

    nums = []
    target = 0
    print("Input: nums = {0}, target = {1}".format(nums, target))
    print("Output: {0}".format(solution.searchRange(nums, target)))

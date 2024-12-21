from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # Check if the middle element is the target
            if nums[mid] == target:
                return mid
            # Determine which part is sorted
            if nums[left] <= nums[mid]:
                # Left part is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Right part is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


if __name__ == "__main__":
    solution = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print("Input: nums = {0}, target = {1}".format(nums, target))
    print("Output: {0}".format(solution.search(nums, target)))
    print()

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    print("Input: nums = {0}, target = {1}".format(nums, target))
    print("Output: {0}".format(solution.search(nums, target)))
    print()

    nums = [1]
    target = 0
    print("Input: nums = {0}, target = {1}".format(nums, target))
    print("Output: {0}".format(solution.search(nums, target)))

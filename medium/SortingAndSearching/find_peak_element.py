from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[mid + 1]:
                # The peak is in the left half (including mid)
                high = mid
            else:
                # The peak is in the right half
                low = mid + 1

        return low


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 1]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.findPeakElement(nums)))
    print()

    nums = [1, 2, 1, 3, 5, 6, 4]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.findPeakElement(nums)))

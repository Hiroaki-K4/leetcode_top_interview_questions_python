from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float("inf")  # Initialize with infinity

        for num in nums:
            if num <= first:
                first = num  # Update the smallest value
            elif num <= second:
                second = num  # Update the second smallest value
            else:
                # If we find a number greater than both first and second
                return True

        return False


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    print("Input: strs = {0}".format(nums))
    print("Output: {0}".format(solution.increasingTriplet(nums)))
    print()

    nums = [5, 4, 3, 2, 1]
    print("Input: strs = {0}".format(nums))
    print("Output: {0}".format(solution.increasingTriplet(nums)))
    print()

    nums = [2, 1, 5, 0, 4, 6]
    print("Input: strs = {0}".format(nums))
    print("Output: {0}".format(solution.increasingTriplet(nums)))

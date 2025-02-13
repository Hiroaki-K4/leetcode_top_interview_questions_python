from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert integers to strings
        nums = list(map(str, nums))

        # Custom sorting comparator
        def compare(x, y):
            if x + y > y + x:
                return -1  # x before y
            elif x + y < y + x:
                return 1  # y before x
            else:
                return 0  # No change in order

        # Sort using custom comparator
        nums.sort(key=cmp_to_key(compare))

        # Join sorted numbers to form the largest number
        result = "".join(nums)

        # Handle case where the largest number is 0
        return "0" if result[0] == "0" else result


if __name__ == "__main__":
    solution = Solution()
    nums = [10, 2]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.largestNumber(nums)))
    print()

    nums = [3, 30, 34, 5, 9]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.largestNumber(nums)))

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array to use the two-pointer approach
        nums.sort()
        result = []

        for i in range(len(nums)):
            # Skip duplicate elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Two-pointer approach
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Move both pointers and skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move pointers inward
                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result


if __name__ == "__main__":
    solution = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.threeSum(nums)))
    print()

    nums = [0, 1, 1]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.threeSum(nums)))
    print()

    nums = [0, 0, 0]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.threeSum(nums)))

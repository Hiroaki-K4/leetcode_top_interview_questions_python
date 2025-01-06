from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n  # Result array

        # Compute left products
        left = 1
        for i in range(n):
            answer[i] = left
            left *= nums[i]

        # Compute right products and multiply
        right = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.productExceptSelf(nums)))
    print()

    nums = [-1, 1, 0, -3, 3]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.productExceptSelf(nums)))

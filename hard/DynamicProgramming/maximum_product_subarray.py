from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_product = min_product = result = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_product, min_product = min_product, max_product
            max_product = max(nums[i], nums[i] * max_product)
            min_product = min(nums[i], nums[i] * min_product)

            result = max(result, max_product)

        return result


if __name__ == "__main__":
    solution = Solution()
    nums = [2, 3, -2, 4]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.maxProduct(nums)))
    print()

    nums = [-2, 0, -1]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.maxProduct(nums)))

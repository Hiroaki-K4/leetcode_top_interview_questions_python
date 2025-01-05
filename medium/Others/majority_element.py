from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = None, 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate


if __name__ == "__main__":
    solution = Solution()
    nums = [3, 2, 3]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.majorityElement(nums)))
    print()

    nums = [2, 2, 1, 1, 1, 2, 2]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.majorityElement(nums)))

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start_idx, curr_nums):
            result.append(curr_nums[:])
            for i in range(start_idx, len(nums)):
                curr_nums.append(nums[i])
                backtrack(i + 1, curr_nums)
                curr_nums.pop()

        result = []
        backtrack(0, [])

        return result


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.subsets(nums)))
    print()

    nums = [0]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.subsets(nums)))

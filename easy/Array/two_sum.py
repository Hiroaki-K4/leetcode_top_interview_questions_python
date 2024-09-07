from typing import List
import copy


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sort_list = copy.copy(nums)
        sort_list.sort()
        for i in range(len(sort_list) - 1):
            for j in range(i + 1, len(sort_list)):
                num_sum = sort_list[i] + sort_list[j]
                if num_sum == target:
                    if sort_list[i] == sort_list[j]:
                        return [
                            nums.index(sort_list[i]),
                            nums.index(sort_list[j], nums.index(sort_list[i]) + 1),
                        ]
                    else:
                        return [nums.index(sort_list[i]), nums.index(sort_list[j])]
                # The search range is narrowed to speed up the search
                if num_sum > target:
                    break


if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print("Input: nums={0}, target={1}".format(nums, target))
    print("Output: {0}".format(solution.twoSum(nums, target)))
    print()
    nums = [3, 2, 4]
    target = 6
    print("Input: nums={0}, target={1}".format(nums, target))
    print("Output: {0}".format(solution.twoSum(nums, target)))
    print()
    nums = [3, 3]
    target = 6
    print("Input: nums={0}, target={1}".format(nums, target))
    print("Output: {0}".format(solution.twoSum(nums, target)))

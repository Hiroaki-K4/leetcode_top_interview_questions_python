import copy
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # step1: extract number and add 1 to comb_list
        # step2: pop target index from curr_list
        # step3: rerun recursion by using loop for other indices

        result = []

        def get_combinations(idx: int, curr_list: List[int], comb_list: List[int]):
            num = curr_list[idx]
            comb_list.append(num)
            curr_list.pop(idx)
            if len(curr_list) == 0:
                result.append(comb_list)
                return
            for idx in range(len(curr_list)):
                get_combinations(idx, copy.copy(curr_list), copy.copy(comb_list))

        for idx in range(len(nums)):
            get_combinations(idx, copy.copy(nums), [])

        return result


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.permute(nums)))
    print()

    nums = [0, 1]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.permute(nums)))
    print()

    nums = [1]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.permute(nums)))

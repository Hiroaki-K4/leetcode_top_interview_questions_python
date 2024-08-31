from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        once = []
        for num in nums:
            if num in once:
                once.remove(num)
            else:
                once.append(num)

        return once[0]


if __name__ == '__main__':
    nums = [2,2,1]
    print("Input: nums={0}".format(nums))
    solution = Solution()
    print("Output: {0}".format(solution.singleNumber(nums)))
    print()
    nums = [4,1,2,1,2]
    print("Input: nums={0}".format(nums))
    print("Output: {0}".format(solution.singleNumber(nums)))
    print()
    nums = [1]
    print("Input: nums={0}".format(nums))
    print("Output: {0}".format(solution.singleNumber(nums)))

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Searching for an element in a dictionary is faster than in a list. 
        exist = {}
        for num in nums:
            if num in exist:
                return True
            else:
                exist[num] = 0

        return False


if __name__ == '__main__':
    nums = [1,2,3,1]
    print("Input: nums={0}".format(nums))
    solution = Solution()
    print("Output: {0}".format(solution.containsDuplicate(nums)))
    print()
    nums = [1,2,3,4]
    print("Input: nums={0}".format(nums))
    print("Output: {0}".format(solution.containsDuplicate(nums)))
    print()
    nums = [1,1,1,3,3,4,3,2,4,2]
    print("Input: nums={0}".format(nums))
    print("Output: {0}".format(solution.containsDuplicate(nums)))

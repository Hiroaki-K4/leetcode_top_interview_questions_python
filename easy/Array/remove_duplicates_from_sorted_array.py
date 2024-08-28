from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        exists = []
        delete_idx = []
        k = 0
        for i in range(len(nums)):
            if nums[i] in exists:
                # Duplicate case
                delete_idx.append(i)
            else:
                # No duplicate case
                k += 1
                exists.append(nums[i])

        # Delete duplicates
        for idx in reversed(delete_idx):
            nums.pop(idx)

        return k


if __name__ == '__main__':
    nums = [1, 1, 2]
    print("Input: nums={0}".format(nums))
    solution = Solution()
    k = solution.removeDuplicates(nums)
    print("Output: k={0}, nums={1}".format(k, nums))

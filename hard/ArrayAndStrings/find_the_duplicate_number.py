from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Detect the cycle
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]  # Move slow by 1 step
            fast = nums[nums[fast]]  # Move fast by 2 steps
            if slow == fast:  # Cycle detected
                break

        # Phase 2: Find the start of the cycle
        slow = nums[0]  # Reset slow to start
        while slow != fast:  # Move both pointers 1 step at a time
            slow = nums[slow]
            fast = nums[fast]

        return slow  # The duplicate number


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 3, 4, 2, 2]
    print("Input: height = {0}".format(nums))
    print("Output: {0}".format(solution.findDuplicate(nums)))
    print()

    nums = [3, 1, 3, 4, 2]
    print("Input: height = {0}".format(nums))
    print("Output: {0}".format(solution.findDuplicate(nums)))
    print()

    nums = [3, 3, 3, 3, 3]
    print("Input: height = {0}".format(nums))
    print("Output: {0}".format(solution.findDuplicate(nums)))

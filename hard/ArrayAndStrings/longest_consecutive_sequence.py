from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Convert the list to a set for O(1) lookups
        num_set = set(nums)
        longest_streak = 0

        # Iterate through each number in the set
        for num in num_set:
            # Check if this number is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # Count the length of the current consecutive sequence
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                # Update the longest streak
                longest_streak = max(longest_streak, current_streak)

        return longest_streak


if __name__ == "__main__":
    solution = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.longestConsecutive(nums)))
    print()

    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print("Input: nums = {0}".format(nums))
    print("Output: {0}".format(solution.longestConsecutive(nums)))

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Create plus one number from list
        num_sum = 0
        for i in range(len(digits)):
            num_sum += 10 ** (len(digits) - 1 - i) * digits[i]
        num_sum += 1

        # Convert number to list
        plus_one = []
        while num_sum > 0:
            rest = num_sum % 10
            plus_one.insert(0, rest)
            num_sum = num_sum // 10

        return plus_one


if __name__ == "__main__":
    solution = Solution()
    digits = [1, 2, 3]
    print("Input: digits={0}".format(digits))
    print("Output: {0}".format(solution.plusOne(digits)))
    print()
    digits = [4, 3, 2, 1]
    print("Input: digits={0}".format(digits))
    print("Output: {0}".format(solution.plusOne(digits)))
    print()
    digits = [9]
    print("Input: digits={0}".format(digits))
    print("Output: {0}".format(solution.plusOne(digits)))

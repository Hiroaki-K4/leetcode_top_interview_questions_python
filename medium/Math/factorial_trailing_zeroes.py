class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n > 0:
            n //= 5
            count += n

        return count


if __name__ == "__main__":
    solution = Solution()
    n = 3
    print("Input: n = {0}".format(n))
    print("Output: {0}".format(solution.trailingZeroes(n)))
    print()

    n = 5
    print("Input: n = {0}".format(n))
    print("Output: {0}".format(solution.trailingZeroes(n)))
    print()

    n = 0
    print("Input: n = {0}".format(n))
    print("Output: {0}".format(solution.trailingZeroes(n)))

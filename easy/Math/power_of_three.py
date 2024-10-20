class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        while n % 3 == 0:
            n //= 3

        if n == 1:
            return True

        return False


if __name__ == "__main__":
    solution = Solution()
    n = 27
    print("Input: n = {0}".format(n))
    print("Output: {0}".format(solution.isPowerOfThree(n)))
    print()

    n = 0
    print("Input: n = {0}".format(n))
    print("Output: {0}".format(solution.isPowerOfThree(n)))
    print()

    n = -1
    print("Input: n = {0}".format(n))
    print("Output: {0}".format(solution.isPowerOfThree(n)))

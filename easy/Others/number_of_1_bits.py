class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1  # Add 1 if the least significant bit is set
            n >>= 1  # Right shift n by 1 to check the next bit

        return count


if __name__ == "__main__":
    solution = Solution()
    n = 11
    print("Input: n = {0}".format(n))
    print("Output: {0}".format(solution.hammingWeight(n)))
    print()

    solution = Solution()
    n = 128
    print("Input: n = {0}".format(n))
    print("Output: {0}".format(solution.hammingWeight(n)))
    print()

    solution = Solution()
    n = 2147483645
    print("Input: n = {0}".format(n))
    print("Output: {0}".format(solution.hammingWeight(n)))

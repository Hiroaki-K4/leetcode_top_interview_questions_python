class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        # Generate all perfect squares <= n
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        for i in range(1, n + 1):
            for square in squares:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)

        return dp[n]


if __name__ == "__main__":
    solution = Solution()
    n = 12
    print("Input: n = {0}".format(n))
    print("Output: {0}".format(solution.numSquares(n)))
    print()

    n = 13
    print("Input: n = {0}".format(n))
    print("Output: {0}".format(solution.numSquares(n)))

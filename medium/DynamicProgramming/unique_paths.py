class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize the DP table
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]


if __name__ == "__main__":
    solution = Solution()
    m = 3
    n = 7
    print("Input: m = {0}, n = {1}".format(m, n))
    print("Output: {0}".format(solution.uniquePaths(m, n)))
    print()

    m = 3
    n = 2
    print("Input: m = {0}, n = {1}".format(m, n))
    print("Output: {0}".format(solution.uniquePaths(m, n)))

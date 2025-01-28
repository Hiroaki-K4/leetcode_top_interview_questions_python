class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)  # m = length of string, n = length of pattern

        # Create a DP table, initialized to False
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Base case: empty string matches empty pattern
        dp[0][0] = True

        # Fill in the case where pattern has only '*'
        for j in range(1, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 1]

        # Fill the table for all substrings of s and p
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    # '*' matches zero characters (dp[i][j-1]) or more characters (dp[i-1][j])
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == "?" or p[j - 1] == s[i - 1]:
                    # '?' matches one character, or exact match
                    dp[i][j] = dp[i - 1][j - 1]

        # Return whether the full string matches the full pattern
        return dp[m][n]


if __name__ == "__main__":
    solution = Solution()
    s = "aa"
    p = "a"
    print("Input: s = {0}, p = {1}".format(s, p))
    print("Output: {0}".format(solution.isMatch(s, p)))
    print()

    s = "aa"
    p = "*"
    print("Input: s = {0}, p = {1}".format(s, p))
    print("Output: {0}".format(solution.isMatch(s, p)))
    print()

    s = "cb"
    p = "?a"
    print("Input: s = {0}, p = {1}".format(s, p))
    print("Output: {0}".format(solution.isMatch(s, p)))

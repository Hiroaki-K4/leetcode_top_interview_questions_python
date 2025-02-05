from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)  # Convert list to set for O(1) lookups
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # Base case: empty string

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break

        return dp[n]  # The final answer


if __name__ == "__main__":
    solution = Solution()
    s = "leetcode"
    wordDict = ["leet", "code"]
    print("Input: s = {0}, wordDict = {1}".format(s, wordDict))
    print("Output: {0}".format(solution.wordBreak(s, wordDict)))
    print()

    s = "applepenapple"
    wordDict = ["apple", "pen"]
    print("Input: s = {0}, wordDict = {1}".format(s, wordDict))
    print("Output: {0}".format(solution.wordBreak(s, wordDict)))
    print()

    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print("Input: s = {0}, wordDict = {1}".format(s, wordDict))
    print("Output: {0}".format(solution.wordBreak(s, wordDict)))

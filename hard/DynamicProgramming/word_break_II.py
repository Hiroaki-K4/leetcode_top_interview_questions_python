from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)  # Convert wordDict to a set for O(1) lookups
        memo = {}  # Dictionary to memoize results

        def backtrack(start):
            if start in memo:
                return memo[start]
            if start == len(s):
                return [
                    ""
                ]  # Return a list with an empty string to help in constructing sentences

            sentences = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    rest_sentences = backtrack(end)
                    for sentence in rest_sentences:
                        sentences.append(word + (" " + sentence if sentence else ""))

            memo[start] = sentences
            return sentences

        return backtrack(0)


if __name__ == "__main__":
    solution = Solution()
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    print("Input: s = {0}, wordDict = {1}".format(s, wordDict))
    print("Output: {0}".format(solution.wordBreak(s, wordDict)))
    print()

    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    print("Input: s = {0}, wordDict = {1}".format(s, wordDict))
    print("Output: {0}".format(solution.wordBreak(s, wordDict)))
    print()

    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print("Input: s = {0}, wordDict = {1}".format(s, wordDict))
    print("Output: {0}".format(solution.wordBreak(s, wordDict)))

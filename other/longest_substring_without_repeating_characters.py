class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            ans_len = 0
        else:
            ans_len = 1

        for i in range(len(s)-1):
            # Use a dictionary for speed
            exist = {}
            exist[s[i]] = 0
            for j in range(i+1, len(s)):
                if s[j] in exist:
                    break
                else:
                    exist[s[j]] = 0
            ans_len = max(len(exist.keys()), ans_len)

        return ans_len


if __name__ == '__main__':
    solution = Solution()
    s = "abcabcbb"
    print("Input: s={0}".format(s))
    print("Output: {0}".format(solution.lengthOfLongestSubstring(s)))
    print()
    s = "bbbbb"
    print("Input: s={0}".format(s))
    print("Output: {0}".format(solution.lengthOfLongestSubstring(s)))
    print()
    s = "pwwkew"
    print("Input: s={0}".format(s))
    print("Output: {0}".format(solution.lengthOfLongestSubstring(s)))

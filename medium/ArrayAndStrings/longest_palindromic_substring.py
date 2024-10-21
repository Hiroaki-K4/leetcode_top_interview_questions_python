class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                target_str = s[i : j + 1]
                if target_str == target_str[::-1] and len(target_str) > len(palindrome):
                    palindrome = target_str

        return palindrome


if __name__ == "__main__":
    solution = Solution()
    s = "babad"
    print("Input: s = {0}".format(s))
    print("Output: {0}".format(solution.longestPalindrome(s)))
    print()

    s = "cbbd"
    print("Input: s = {0}".format(s))
    print("Output: {0}".format(solution.longestPalindrome(s)))

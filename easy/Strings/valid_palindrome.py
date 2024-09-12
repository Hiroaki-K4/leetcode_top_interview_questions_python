class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        updated_s = ""
        # Remove non-alphanumeric characters
        for i in range(len(s)):
            if s[i].isdigit() or s[i].isalpha():
                updated_s += s[i]

        # Check if it is a palindrome
        for i in range(len(updated_s) // 2):
            if updated_s[i] != updated_s[~i]:
                return False

        return True


if __name__ == "__main__":
    solution = Solution()
    s = "A man, a plan, a canal: Panama"
    print('Input: s="{0}"'.format(s))
    print("Output: {0}".format(solution.isPalindrome(s)))
    print()
    s = "race a car"
    print('Input: s="{0}"'.format(s))
    print("Output: {0}".format(solution.isPalindrome(s)))
    print()
    s = " "
    print('Input: s="{0}"'.format(s))
    print("Output: {0}".format(solution.isPalindrome(s)))

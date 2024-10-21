class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            # If the character at right is already in the set, shrink the window from the left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # Add the current character to the set and update max_length
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length


if __name__ == "__main__":
    solution = Solution()
    s = "abcabcbb"
    print("Input: s = {0}".format(s))
    print("Output: {0}".format(solution.lengthOfLongestSubstring(s)))
    print()

    s = "bbbbb"
    print("Input: s = {0}".format(s))
    print("Output: {0}".format(solution.lengthOfLongestSubstring(s)))
    print()

    s = "pwwkew"
    print("Input: s = {0}".format(s))
    print("Output: {0}".format(solution.lengthOfLongestSubstring(s)))

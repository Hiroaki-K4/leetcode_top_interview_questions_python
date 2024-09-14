class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        for i in range(len(haystack) - len(needle) + 1):
            if needle == haystack[i : i + len(needle)]:
                return i

        return -1


if __name__ == "__main__":
    solution = Solution()
    haystack = "sadbutsad"
    needle = "sad"
    print('Input: haystack="{0}", needle="{1}"'.format(haystack, needle))
    print("Output: {0}".format(solution.strStr(haystack, needle)))
    print()
    haystack = "leetcode"
    needle = "leeto"
    print('Input: haystack="{0}", needle="{1}"'.format(haystack, needle))
    print("Output: {0}".format(solution.strStr(haystack, needle)))

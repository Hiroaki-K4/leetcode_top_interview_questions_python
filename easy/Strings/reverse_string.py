from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]


if __name__ == "__main__":
    solution = Solution()
    s = ["h", "e", "l", "l", "o"]
    print("Input: {0}".format(s))
    solution.reverseString(s)
    print("Output: {0}".format(s))
    print()
    s = ["H", "a", "n", "n", "a", "h"]
    print("Input: {0}".format(s))
    solution.reverseString(s)
    print("Output: {0}".format(s))

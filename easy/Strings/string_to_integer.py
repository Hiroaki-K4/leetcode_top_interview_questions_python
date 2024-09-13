class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        ans_int = 0
        first = True
        minus = False
        for i in range(len(s)):
            if not first and not s[i].isdigit():
                break
            if s[i].isdigit():
                ans_int = ans_int * 10 + int(s[i])
            elif s[i] == "-":
                minus = True
            elif s[i] == "+":
                pass
            else:
                break
            first = False

        if minus:
            ans_int *= -1
        if ans_int < -(2 ** 31):
            ans_int = -(2 ** 31)
        if ans_int > 2 ** 31 - 1:
            ans_int = 2 ** 31 - 1

        return ans_int


if __name__ == "__main__":
    solution = Solution()
    s = "42"
    print('Input: s="{0}"'.format(s))
    print("Output: {0}".format(solution.myAtoi(s)))
    print()
    s = "-042"
    print('Input: s="{0}"'.format(s))
    print("Output: {0}".format(solution.myAtoi(s)))
    print()
    s = "1337c0d3"
    print('Input: s="{0}"'.format(s))
    print("Output: {0}".format(solution.myAtoi(s)))
    print()
    s = "0-1"
    print('Input: s="{0}"'.format(s))
    print("Output: {0}".format(solution.myAtoi(s)))
    print()
    s = "words and 987"
    print('Input: s="{0}"'.format(s))
    print("Output: {0}".format(solution.myAtoi(s)))

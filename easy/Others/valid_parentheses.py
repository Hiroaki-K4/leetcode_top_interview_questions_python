class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for str in s:
            if str == "(" or str == "[" or str == "{":
                if str == "(":
                    stack.append(")")
                elif str == "[":
                    stack.append("]")
                elif str == "{":
                    stack.append("}")
            else:
                if len(stack) == 0:
                    return False
                if str != stack.pop(-1):
                    return False

        if len(stack) > 0:
            return False

        return True


if __name__ == "__main__":
    solution = Solution()
    s = "()"
    print("Input: n = {0}".format(s))
    print("Output: {0}".format(solution.isValid(s)))
    print()

    s = "()[]{}"
    print("Input: n = {0}".format(s))
    print("Output: {0}".format(solution.isValid(s)))
    print()

    s = "(]"
    print("Input: n = {0}".format(s))
    print("Output: {0}".format(solution.isValid(s)))
    print()

    s = "([])"
    print("Input: n = {0}".format(s))
    print("Output: {0}".format(solution.isValid(s)))

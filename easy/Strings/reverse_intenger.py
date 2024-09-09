class Solution:
    def reverse(self, x: int) -> int:
        # Convert int to List(string)
        x_str = str(x)
        str_list = []
        for i in range(len(x_str)):
            str_list.append(x_str[i])

        # Remove minus because it is in the way when reverse processing
        is_minus = False
        if str_list[0] == "-":
            is_minus = True
            str_list.pop(0)

        # Reverse string(int)
        str_len = len(str_list)
        for i in range(str_len // 2):
            str_list[i], str_list[str_len - i - 1] = (
                str_list[str_len - i - 1],
                str_list[i],
            )

        # If number is minus, add minus to the top of string
        if is_minus:
            rev_str = "-"
        else:
            rev_str = ""

        # Make int from string list
        for i in range(str_len):
            rev_str += str_list[i]
        rev_int = int(rev_str)

        # Check if it is outside the threshold
        if rev_int > 2 ** 31 - 1 or rev_int < -(2 ** 31):
            return 0

        return rev_int


if __name__ == "__main__":
    solution = Solution()
    x = 123
    print("Input: {0}".format(x))
    print("Output: {0}".format(solution.reverse(x)))
    print()
    x = -123
    print("Input: {0}".format(x))
    print("Output: {0}".format(solution.reverse(x)))
    print()
    x = 120
    print("Input: {0}".format(x))
    print("Output: {0}".format(solution.reverse(x)))

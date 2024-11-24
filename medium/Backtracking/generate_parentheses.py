from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left_count = n
        right_count = n
        result = []

        def create_parenthesis(curr_words: str, left_count: int, right_count: int):
            if left_count == 0 and right_count == 0:
                result.append(curr_words)
                return
            if left_count >= 1:
                create_parenthesis(curr_words + "(", left_count - 1, right_count)
            if right_count >= 1 and right_count > left_count:
                create_parenthesis(curr_words + ")", left_count, right_count - 1)

        create_parenthesis("(", left_count - 1, right_count)

        return result


if __name__ == "__main__":
    solution = Solution()
    n = 3
    print("Input: n = {0}".format(n))
    print("Output: {0}".format(solution.generateParenthesis(n)))
    print()

    n = 1
    print("Input: n = {0}".format(n))
    print("Output: {0}".format(solution.generateParenthesis(n)))

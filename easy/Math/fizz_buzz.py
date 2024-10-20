from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans_list = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                ans_list.append("FizzBuzz")
            elif i % 3 == 0:
                ans_list.append("Fizz")
            elif i % 5 == 0:
                ans_list.append("Buzz")
            else:
                ans_list.append(str(i))

        return ans_list


if __name__ == "__main__":
    solution = Solution()
    n = 3
    print("Input: n = {0}".format(n))
    print("Output: {0}".format(solution.fizzBuzz(n)))
    print()

    n = 5
    print("Input: n = {0}".format(n))
    print("Output: {0}".format(solution.fizzBuzz(n)))
    print()

    n = 15
    print("Input: n = {0}".format(n))
    print("Output: {0}".format(solution.fizzBuzz(n)))

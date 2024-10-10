class Solution:
    def climbStairs(self, n: int) -> int:
        # For any step i, the number of ways to reach step i is
        # the sum of the ways to reach step i - 1 (by taking a 1-step)
        # and step i - 2 (by taking a 2-step).
        # This is because you can only arrive at step i from either of these two previous steps.

        if n == 1:
            return 1
        elif n == 2:
            return 2

        # Initialize base cases
        a, b = 1, 2

        # Use the recurrence relation to calculate ways for each step
        for i in range(2, n):
            a, b = b, a + b

        return b


if __name__ == "__main__":
    solution = Solution()
    n = 2
    print("Input: n = {0}".format(n))
    print("Output: {0}".format(solution.climbStairs(n)))
    print()

    n = 3
    print("Input: n = {0}".format(n))
    print("Output: {0}".format(solution.climbStairs(n)))

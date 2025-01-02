class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            elif square > x:
                right = mid - 1

        return right


if __name__ == "__main__":
    solution = Solution()
    x = 4
    print("Input: x = {0}".format(x))
    print("Output: {0}".format(solution.mySqrt(x)))
    print()

    x = 8
    print("Input: x = {0}".format(x))
    print("Output: {0}".format(solution.mySqrt(x)))

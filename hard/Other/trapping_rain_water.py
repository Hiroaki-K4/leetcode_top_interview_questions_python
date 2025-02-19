from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water_trapped = 0

        while left < right:
            if left_max < right_max:
                left += 1
                if height[left] < left_max:
                    water_trapped += left_max - height[left]
                else:
                    left_max = height[left]
            else:
                right -= 1
                if height[right] < right_max:
                    water_trapped += right_max - height[right]
                else:
                    right_max = height[right]

        return water_trapped


if __name__ == "__main__":
    solution = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print("Input: height = {0}".format(height))
    print("Output: {0}".format(solution.trap(height)))
    print()

    height = [4, 2, 0, 3, 2, 5]
    print("Input: height = {0}".format(height))
    print("Output: {0}".format(solution.trap(height)))

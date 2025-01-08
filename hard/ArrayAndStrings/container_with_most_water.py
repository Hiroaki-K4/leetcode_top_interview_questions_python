from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            # Calculate the area
            current_area = min(height[left], height[right]) * (right - left)
            # Update the maximum area
            max_water = max(max_water, current_area)

            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water


if __name__ == "__main__":
    solution = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print("Input: height = {0}".format(height))
    print("Output: {0}".format(solution.maxArea(height)))
    print()

    height = [1, 1]
    print("Input: height = {0}".format(height))
    print("Output: {0}".format(solution.maxArea(height)))

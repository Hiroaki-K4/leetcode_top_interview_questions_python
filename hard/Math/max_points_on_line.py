from collections import defaultdict
from math import gcd
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return len(points)

        max_points = 1  # At least one point is always in a line

        for i in range(len(points)):
            slope_count = defaultdict(int)
            same_points = 0
            cur_max = 0

            for j in range(len(points)):
                if i == j:
                    continue

                x1, y1 = points[i]
                x2, y2 = points[j]

                # Handle duplicate points
                if x1 == x2 and y1 == y2:
                    same_points += 1
                    continue

                # Compute slope as (dy / dx) in reduced form
                dx, dy = x2 - x1, y2 - y1
                g = gcd(dx, dy)
                slope = (dy // g, dx // g)  # Store slope as a tuple

                slope_count[slope] += 1
                cur_max = max(cur_max, slope_count[slope])

            max_points = max(
                max_points, cur_max + same_points + 1
            )  # Include the anchor point

        return max_points


if __name__ == "__main__":
    solution = Solution()
    points = [[1, 1], [2, 2], [3, 3]]
    print("Input: nums = {0}".format(points))
    print("Output: {0}".format(solution.maxPoints(points)))
    print()

    points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    print("Input: nums = {0}".format(points))
    print("Output: {0}".format(solution.maxPoints(points)))

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if len(merged) == 0 or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


if __name__ == "__main__":
    solution = Solution()
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print("Input: intervals = {0}".format(intervals))
    print("Output: {0}".format(solution.merge(intervals)))
    print()

    intervals = [[1, 4], [4, 5]]
    print("Input: intervals = {0}".format(intervals))
    print("Output: {0}".format(solution.merge(intervals)))

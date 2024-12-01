from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        sorted_nums = sorted(freq_map.keys(), key=lambda x: freq_map[x], reverse=True)

        return sorted_nums[:k]


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print("Input: nums = {0}, k = {1}".format(nums, k))
    print("Output: {0}".format(solution.topKFrequent(nums, k)))
    print()

    nums = [1]
    k = 1
    print("Input: nums = {0}, k = {1}".format(nums, k))
    print("Output: {0}".format(solution.topKFrequent(nums, k)))

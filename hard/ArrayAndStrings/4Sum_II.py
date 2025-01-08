from collections import Counter
from typing import List


class Solution:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        # Step 1: Calculate sums of pairs from nums1 and nums2
        sum_count = Counter()
        for num1 in nums1:
            for num2 in nums2:
                sum_count[num1 + num2] += 1

        # Step 2: Find complementary pairs from nums3 and nums4
        result = 0
        for num3 in nums3:
            for num4 in nums4:
                target = -(num3 + num4)
                if target in sum_count:
                    result += sum_count[target]

        return result


if __name__ == "__main__":
    solution = Solution()
    nums1, nums2, nums3, nums4 = [1, 2], [-2, -1], [-1, 2], [0, 2]
    print(
        "Input: nums1 = {0}, nums2 = {1}, nums3 = {2}, nums4 = {3}".format(
            nums1, nums2, nums3, nums4
        )
    )
    print("Output: {0}".format(solution.fourSumCount(nums1, nums2, nums3, nums4)))
    print()

    nums1, nums2, nums3, nums4 = [0], [0], [0], [0]
    print(
        "Input: nums1 = {0}, nums2 = {1}, nums3 = {2}, nums4 = {3}".format(
            nums1, nums2, nums3, nums4
        )
    )
    print("Output: {0}".format(solution.fourSumCount(nums1, nums2, nums3, nums4)))

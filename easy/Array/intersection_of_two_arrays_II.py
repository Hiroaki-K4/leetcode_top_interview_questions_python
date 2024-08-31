from collections import Counter
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Count the occurrences of each number in both arrays
        count1 = Counter(nums1)
        count2 = Counter(nums2)

        # Find the intersection
        intersection = []
        for num in count1:
            if num in count2:
                # Append the minimum count of the number found in both arrays
                intersection.extend([num] * min(count1[num], count2[num]))

        return intersection


if __name__ == '__main__':
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print("Input: num1={0}, num2={1}".format(nums1, nums2))
    solution = Solution()
    print("Output: {0}".format(solution.intersect(nums1, nums2)))
    print()
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print("Input: num1={0}, num2={1}".format(nums1, nums2))
    print("Output: {0}".format(solution.intersect(nums1, nums2)))

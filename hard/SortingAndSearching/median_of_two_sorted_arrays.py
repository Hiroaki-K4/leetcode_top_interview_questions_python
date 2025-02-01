from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1  # Ensure nums1 is the smaller array

        m, n = len(nums1), len(nums2)
        left_half_size = (m + n + 1) // 2  # Number of elements in left half

        left, right = 0, m  # Binary search on the smaller array
        while left <= right:
            partition1 = (left + right) // 2  # Partition index for nums1
            partition2 = left_half_size - partition1  # Partition index for nums2

            maxLeft1 = float("-inf") if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float("inf") if partition1 == m else nums1[partition1]

            maxLeft2 = float("-inf") if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float("inf") if partition2 == n else nums2[partition2]

            # Ensure correct partitioning
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # If odd total length, return max of left half
                if (m + n) % 2 == 1:
                    return max(maxLeft1, maxLeft2)
                # If even total length, return average of two middle elements
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
            elif maxLeft1 > minRight2:
                right = partition1 - 1  # Move left in nums1
            else:
                left = partition1 + 1  # Move right in nums1


if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 3]
    nums2 = [2]
    print("Input: nums1 = {0}, nums2 = {1}".format(nums1, nums2))
    print("Output: {0}".format(solution.findMedianSortedArrays(nums1, nums2)))
    print()

    nums1 = [1, 2]
    nums2 = [3, 4]
    print("Input: nums1 = {0}, nums2 = {1}".format(nums1, nums2))
    print("Output: {0}".format(solution.findMedianSortedArrays(nums1, nums2)))

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        last_elm = m
        for i in range(n):
            while j < m + n:
                # Remaining 0 case
                if j >= last_elm and nums1[j] == 0:
                    nums1[j] = nums2[i]
                    j += 1
                    break

                # Upcating case
                if nums2[i] < nums1[j]:
                    # Slide elements
                    nums1[j + 1 :] = nums1[j : m + n - 1]
                    nums1[j] = nums2[i]
                    j += 1
                    last_elm += 1
                    break

                j += 1


if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(
        "Input: nums1 = {0}, m = {1}, nums2 = {2}, n = {3}".format(nums1, m, nums2, n)
    )
    solution.merge(nums1, m, nums2, n)
    print("Output: {0}".format(nums1))
    print()

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    print(
        "Input: nums1 = {0}, m = {1}, nums2 = {2}, n = {3}".format(nums1, m, nums2, n)
    )
    solution.merge(nums1, m, nums2, n)
    print("Output: {0}".format(nums1))
    print()

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    print(
        "Input: nums1 = {0}, m = {1}, nums2 = {2}, n = {3}".format(nums1, m, nums2, n)
    )
    solution.merge(nums1, m, nums2, n)
    print("Output: {0}".format(nums1))

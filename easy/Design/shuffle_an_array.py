import random
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.original_arr = nums
        self.curr_arr = nums

    def reset(self) -> List[int]:
        self.curr_arr = self.original_arr
        return self.curr_arr

    def shuffle(self) -> List[int]:
        self.curr_arr = random.sample(self.curr_arr, len(self.curr_arr))
        return self.curr_arr


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

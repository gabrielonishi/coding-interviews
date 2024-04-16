from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new_array = list()

        for i in range(n):
            new_array.append(nums[i])
            new_array.append(nums[n + i])

        return new_array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 0
        last_num = None
        last_i = 0

        for i, num in enumerate(nums): # 1, 0
            if num != last_num: #True
                nums[last_i] = num #[1, ...]
                counter += 1
                last_i += 1
                last_num = num

        return counter

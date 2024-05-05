class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        total = sum(nums)
        expected_total = sum([i for i in range(len(nums) + 1)])

        return expected_total - total

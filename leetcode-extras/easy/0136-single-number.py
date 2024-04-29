class Solution:
    def singleNumber(self, nums: List[int]) -> int:
                
        res = reduce(lambda x, y: x ^ y, nums)
        
        return res

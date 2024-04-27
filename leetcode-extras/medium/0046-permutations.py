class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        last = nums.pop()
        without = self.permute(nums)
        print(without)
        res = []

        for seq in without:
            for i in range(len(seq)):
                res.append(seq[0:i] + [last] + seq[i:])
            seq.append(last)
            res.append(seq)

        return res

class Solution(object):
    def subarrayBitwiseORs(self, arr):
        result = tmp = set()
        for n in arr:
            tmp = {num | n for num in tmp} | {n}
            result |= tmp
        return len(result)

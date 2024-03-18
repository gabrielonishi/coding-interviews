class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        current_index = 0

        for element in t:
            if s[current_index] == element:
                current_index += 1

        if current_index == len(s):
            return True
        
        return False
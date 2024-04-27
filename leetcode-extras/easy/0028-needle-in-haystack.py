class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        sadbutsad -> 9
        sad -> 3
        abcd
        '''
        len_n = len(needle)
        len_h = len(haystack)

        i = 0
        while i < len_h - len_n + 1:
            if haystack[i: i + len_n] == needle:
                return i
            i += 1
        
        return -1
            
            

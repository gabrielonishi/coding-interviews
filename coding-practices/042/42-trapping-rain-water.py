from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
         0  1  2  3  4  5  6  7  8  9 10 11
        '''
        
        if len(height) < 3:
            return 0
        
        l = 0
        r = len(height) - 1
        
        l_max = height[0]
        r_max = height[-1]
        
        volume = 0
        
        while l != r:
            if l_max < r_max:
                l += 1
                if height[l] > l_max:
                    l_max = height[l]
                volume += l_max - height[l]
            else:
                r -= 1
                if height[r] > r_max:
                    r_max = height[r]
                volume += r_max - height[r]
        
        print(volume)
        return volume   
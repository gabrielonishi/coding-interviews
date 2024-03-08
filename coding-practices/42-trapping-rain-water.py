from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0
        borders = dict()

        for h in height:
            if h > 0 and h not in borders:
                borders[h] = 0
            for border in borders:
                if h < border:
                    borders[border] += border - h
                else:
                    this_vol = borders[border]
                    for b in borders:
                        if b > border:
                            borders[b] -= this_vol
                    borders[border] = 0
                    volume += this_vol
        
        print(volume)
        return(volume)
                    
if __name__ == '__main__':
    test = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    test.trap(height=height)
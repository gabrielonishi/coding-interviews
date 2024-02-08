class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        positions = dict()
        
        for i, points in enumerate(score):
            positions[points] = i
        
        for sorted_i, points in enumerate(sorted(score, reverse = True)):
            positions[points] = sorted_i
        
        pos = list()

        for points in positions:
            if positions[points] == 0:
                pos.append('Gold Medal')
            elif positions[points] == 1:
                pos.append('Silver Medal')
            elif positions[points] == 2:
                pos.append('Bronze Medal')
            else:
                pos.append(str(positions[points] + 1))
        
        return pos
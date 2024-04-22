from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations = sorted(citations, reverse=True)

        h = 0

        for i in range(len(citations)):
            if citations[i] > i:
                h += 1
            else:
                break

        return h

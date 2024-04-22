from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_map = dict()
        max_citations = 0
        for n_citations in citations:
            h_map.setdefault(n_citations, 0)
            h_map[n_citations] += 1
            max_citations = max(max_citations, n_citations)

        carry = 0

        print(h_map)
        for n_citations in range(max_citations, -1, -1):
            if n_citations in h_map:
                carry += h_map[n_citations]
            if carry >= n_citations:
                return n_citations

        return 0

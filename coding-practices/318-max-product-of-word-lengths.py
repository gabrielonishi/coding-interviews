from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words_set = [set(word) for word in words]
        res = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if not words_set[i] & words_set[j]:
                    res = max(res, len(words[i] * len(words[j])))

        return res

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = set()

        def search(s) -> bool:
            if s in memo:
                return False

            current_word = ""
            for i, char in enumerate(s):
                current_word += char
                if current_word in wordDict:
                    rest = s[i+1:]
                    if len(rest) == 0 or search(rest):
                        return True

            memo.add(s)

            return False

        return search(s)

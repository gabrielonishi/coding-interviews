class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = start_index = 0
        special_sequences = []

        for index, char in enumerate(s):
            count += 1 if char == '1' else -1
            if count == 0:
                inner_special = self.makeLargestSpecial(
                    s[start_index + 1:index])
                special_sequences.append('1' + inner_special + '0')
                start_index = index + 1

        return ''.join(sorted(special_sequences, reverse=True))

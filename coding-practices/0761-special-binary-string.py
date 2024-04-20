class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        """
        Dado s, qual o valor máximo possível?
        Começando com todos os 1s da string

        Ideia:
         - Criar função pra checar se substring é especial
         - Varrer s procurando substrings seguidas
         - Dar prioridade para strings que comecem com um 1

        11011000
        11100100
        """

        def is_special(s: str) -> bool:
            if len(s) % 2 == 1 or len(s) == 0:
                return False

            zero_count = 0
            one_count = 0
            for char in s:
                if char == "0":
                    zero_count += 1
                else:
                    one_count += 1

                if zero_count > one_count:
                    return False

            if zero_count == one_count:
                return True

        special_binaries = dict()
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                # print(s[i:j + 1])
                if is_special(s[i:j + 1]):
                    special_binaries[(i, j)] = s[i:j + 1]

        adj_special_binaries = dict()
        for start1, finish1 in special_binaries:
            for start2, finish2 in special_binaries:
                if finish1 + 1 == start2:
                    adj_special_binaries[(start1, start2, finish2)] = (
                        special_binaries[(start1, finish1)], special_binaries[(start2, finish2)])

        res = s
        for start1, start2, finish2 in adj_special_binaries:
            this_res = s[:start1] + adj_special_binaries[(start1, start2, finish2)][1] + adj_special_binaries[(
                start1, start2, finish2)][0] + s[finish2 + 1:]
            if this_res > res:
                res = this_res

        return res

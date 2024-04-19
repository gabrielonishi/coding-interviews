class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        """
        Ideia: percorrer árvore
            0
          0   1
        0  1 1  0
        """
        def turn(num: int, direction: str) -> int:
            if num == 0:
                if direction == "right":
                    return 1
                else:
                    return 0
            if direction == "right":
                return 0
            return 1

        num = 0

        while (n > 1):
            if k > 2 ** (n - 2):
                num = turn(num, 'right')
                k -= 2 ** (n - 2)
            else:
                num = turn(num, 'left')
            n -= 1

        return num

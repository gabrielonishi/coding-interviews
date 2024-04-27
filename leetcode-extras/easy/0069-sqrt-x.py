class Solution:
    def mySqrt(self, x: int) -> int:

        for n in range(x + 1):
            if n * n > x:
                return n - 1

        return x

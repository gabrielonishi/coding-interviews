class Solution:
    def minOperations(self, s: str) -> int:
        counter_zero, counter_one = 0, 0

        def alternate(char: str) -> str:
            if char == "1":
                return "0"
            return "1"

        correct_zero = "0"
        correct_one = "1"

        for char in s:
            if char != correct_zero:
                counter_zero += 1
            if char != correct_one:
                counter_one += 1
            correct_zero = alternate(correct_zero)
            correct_one = alternate(correct_one)

        return min(counter_zero, counter_one)

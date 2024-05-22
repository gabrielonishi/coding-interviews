class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()

        opposites = {
            "]": "[",
            "}": "{",
            ")": "("
        }

        for char in s:
            stack.append(char)
            while len(stack) >= 2:
                if opposites.get(stack[-1], "0") == stack[-2]:
                    stack.pop()
                    stack.pop()
                else:
                    break

        if stack:
            return False

        return True

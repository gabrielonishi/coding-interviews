class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = s[0]

        for i in range(len(s)):
            l, r = i - 1, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(longest_palindrome):
                    longest_palindrome = s[l:r+1]
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(longest_palindrome):
                    longest_palindrome = s[l:r+1]
                l -= 1
                r += 1

        return longest_palindrome

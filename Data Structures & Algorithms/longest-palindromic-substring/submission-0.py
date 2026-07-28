class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ""
        max_len = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                if len(s[l:r + 1]) > max_len:
                    res = s[l:r + 1]
                    max_len = r - l + 1
                l -= 1
                r += 1

        for i in range(len(s)):
            l, r = i, i + 1
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                if len(s[l:r + 1]) > max_len:
                    res = s[l:r + 1]
                    max_len = r - l + 1
                l -= 1
                r += 1

        return res

        
class Solution:
    def numDecodings(self, s: str) -> int:

        memo = {}

        def decode(s):
            if s[0] == '0':
                return 0

            if len(s) == 1:
                return 1

            if len(s) == 2:
                c = 0
                if 10 <= int(s) <= 26:
                    c += 1
                if s[1] != '0':
                    c += 1
                return c

            if s in memo:
                return memo[s]
                
            memo[s] = decode(s[1:])

            if 10 <= int(s[:2]) <= 26:
                memo[s] += decode(s[2:])
            
            return memo[s]

        return decode(s)
        
                
        
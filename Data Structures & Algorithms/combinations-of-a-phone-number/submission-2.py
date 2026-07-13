class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        hash_map = {'2': ('a', 'b', 'c'),
                    '3': ('d', 'e', 'f'),
                    '4': ('g', 'h', 'i'),
                    '5': ('j', 'k', 'l'),
                    '6': ('m', 'n', 'o'),
                    '7': ('p', 'q', 'r', 's'),
                    '8': ('t', 'u', 'v'),
                    '9': ('w', 'x', 'y', 'z'),
        }


        s = []
        output = []

        def dfs(i):

            if i == len(digits):
                output.append(''.join(s))
                return

            for char in hash_map[digits[i]]:
                s.append(char)
                dfs(i + 1)
                s.pop()
        
        dfs(0)
        return output
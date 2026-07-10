class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        output = []
        s = []

        def dfs(open, close):
            if len(s) == 2*n:
                output.append("".join(s))
                return

            if open < n:
                s.append("(")
                dfs(open + 1, close)
                s.pop()

            if close < n and close < open:
                s.append(")")
                dfs(open, close + 1)
                s.pop()
    
        dfs(0, 0)
        return output
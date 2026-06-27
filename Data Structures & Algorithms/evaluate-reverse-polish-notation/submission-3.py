class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c in "+-*/":
                n = stack.pop()
                m = stack.pop()

                if c == "+":
                    res = m + n

                elif c == "-":
                    res = m - n

                elif c == "*":
                    res = m * n

                elif c == "/":
                    res = int(m / n)
                
                stack.append(res)
                    

            else:
                stack.append(int(c))

        return stack[-1]
        
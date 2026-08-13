class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m = len(num1)
        n = len(num2)

        res = [0] * (m + n)

        l1 = [ord(d) - ord('0') for d in reversed(num1)]
        l2 = [ord(d) - ord('0') for d in reversed(num2)]
    
        for j in range(len(l2)):
            d2 = l2[j]
            for i in range(len(l1)):
                d1 = l1[i]

                mul = d1 * d2

                res[i + j] += mul % 10
                carry = res[i + j] // 10

                res[i + j] %= 10
                res[i + j + 1] += mul // 10 + carry

        res.reverse()
        
        i = 0
        while i < len(res) - 1 and res[i] == 0:
            i += 1

        return ''.join(str(d) for d in res[i:])
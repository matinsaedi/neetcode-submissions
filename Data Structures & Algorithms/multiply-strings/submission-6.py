class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m = len(num1)
        n = len(num2)

        res = [0] * (m + n)

        l1 = []
        for d1 in num1[::-1]:
            l1.append(ord(d1) - ord('0'))

        l2 = []
        for d2 in num2[::-1]:
            l2.append(ord(d2) - ord('0'))


        for j in range(len(l2)):
            d2 = l2[j]
            for i in range(len(l1)):
                d1 = l1[i]
                mul = d1 * d2

                res[i + j] += (mul % 10)
                carry = res[i + j] // 10

                res[i + j] %= 10
                res[i + j + 1] += (mul // 10) + carry

        res = res[::-1]
        index = 0
        for digit in res:
            if digit != 0:
                break
            index += 1

        return ''.join([str(i) for i in res[index:]]) if index < m + n else '0'
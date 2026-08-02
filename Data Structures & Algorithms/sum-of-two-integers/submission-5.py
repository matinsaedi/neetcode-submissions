class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = 0

        for i in range(32):
            a_bit = 1 if (a & (1 << i)) else 0
            b_bit = 1 if (b & (1 << i)) else 0

            res_bit = a_bit ^ b_bit ^ carry
            carry = (a_bit + b_bit + carry) >= 2
            
            res |= (res_bit << i)

        if res >= (1 << 31):
            res -= 1 << 32
        
        return res

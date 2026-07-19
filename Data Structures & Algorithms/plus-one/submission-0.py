class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry = 1
        res = []

        # if digits[-1] != 9:
        #     res.append(digits[-1] + 1)
        
        # else:
        #     res.append(0)
        #     carry = 1

        
        for d in digits[::-1]:
            res.append((d + carry) % 10)
            carry = (d + carry) // 10

        if carry != 0:
            res.append(carry)

        return res[::-1]


        
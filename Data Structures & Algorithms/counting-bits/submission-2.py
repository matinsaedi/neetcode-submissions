class Solution:
    def countBits(self, n: int) -> List[int]:
        def helper_count(n):
            c = 0

            for i in range(10):
                if n & (1 << i):
                    c += 1

            return c

        output = []
        for i in range(n + 1):
            output.append(helper_count(i))

        return output


            

    
        
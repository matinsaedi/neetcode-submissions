class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        permutations = []
        p = []
        seen = set()

        def dfs():
            if len(p) >= len(nums):
                permutations.append(p.copy())
                return

            for num in nums:
                if num not in seen:
                    p.append(num)
                    seen.add(num)

                    dfs()
                    seen.remove(num)
                    p.pop()
        
        dfs()
        return permutations
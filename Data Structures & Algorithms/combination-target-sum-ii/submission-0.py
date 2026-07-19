class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        c = []
        candidates.sort()
        
        def dfs(i, total):

            if total == target:
                combinations.append(c.copy())
                return

            if i >= len(candidates) or total > target:
                return

            c.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            c.pop()

            while i < len(candidates) - 1 and candidates[i + 1] == candidates[i]:
                i += 1

            dfs(i + 1, total)

        dfs(0, 0)
        return combinations

        [1, 2, 2, 4, 5, 6, 9]
        [1, 2, 2, 4]
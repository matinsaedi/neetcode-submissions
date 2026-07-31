class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False

        dp = {0}
        target = sum(nums) / 2

        for i in range(len(nums) - 1, -1, -1):
            candidates = []
            for k in dp:
                candidates.append(nums[i] + k)
            dp.update(candidates)
            if target in dp:
                return True

        return False
        
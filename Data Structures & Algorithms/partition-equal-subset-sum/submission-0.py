class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False

        s = {0}
        for i in range(len(nums) - 1, -1, -1):
            candidates = []
            for k in s:
                candidates.append(nums[i] + k)
            s.update(candidates)

        return sum(nums) / 2 in s
        
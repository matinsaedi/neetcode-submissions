class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False

        dp = {0}
        target = sum(nums) / 2

        for i in range(len(nums) - 1, -1, -1):
            candidates = set()
            for k in dp:
                if nums[i] + k == target:
                    return True

                candidates.add(nums[i] + k)

            dp.update(candidates)

        return False
        
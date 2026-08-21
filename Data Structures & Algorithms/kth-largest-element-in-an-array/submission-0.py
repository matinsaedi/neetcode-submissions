class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        candidates = nums[:k]

        heapq.heapify(candidates)

        if k < len(nums):
            for num in nums[k:]:
                if num > candidates[0]:
                    heapq.heappop(candidates)
                    heapq.heappush(candidates, num)

        return candidates[0]
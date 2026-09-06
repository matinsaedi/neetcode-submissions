class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        cur = intervals[0]
        res = 0
        for i in intervals[1:]:
            if i[0] >= cur[1]:
                cur = i
            elif i[1] > cur[1]:
                res += 1
            else:
                cur = i
                res += 1

        return res
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x:x[0])

        cur = intervals[0]
        res = 0
        for i in intervals[1:]:
            if i[0] >= cur[1]:
                cur = i
                continue
            elif i[1] > cur[1]:
                res += 1
            else:
                cur = i
                res += 1

        return res
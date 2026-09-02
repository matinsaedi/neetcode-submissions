class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals = sorted(intervals, key=lambda x:x[0])

        res = []
        cur = intervals[0]
        for i in intervals[1:]:
            if i[0] <= cur[1]:
                cur[1] = max(i[1], cur[1])
            
            else:
                res.append(cur)
                cur = i

        res.append(cur)
        return res
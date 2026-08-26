"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        if not intervals:
            return True

        intervals_list = [(i.start, i.end) for i in intervals]
        intervals_list.sort()

        for i in range(1, len(intervals_list)):
            if intervals_list[i - 1][1] > intervals_list[i][0]:
                return False
        
        return True
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

        prev_end = intervals_list[0][1]
        for i in intervals_list[1:]:
            if i[0] < prev_end:
                return False

            prev_end = i[1]
        
        return True

            

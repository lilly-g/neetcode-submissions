"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) < 2 :
            return True
        
        # sort by start time 
        intervals.sort(key=lambda x: x.start)

        # for each succeeding time, check if it starts after end time
        for i in range(1, len(intervals)) :
            print(intervals[i].start)
            if intervals[i].start < intervals[i-1].end :
                return False

        return True
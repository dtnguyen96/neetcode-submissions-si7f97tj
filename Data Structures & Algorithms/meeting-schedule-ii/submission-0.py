"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 1:
            return 1 
        if len(intervals) == 0:
            return 0

        intervals.sort(key = lambda i : i.start)
        min_heap = []

        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start: 
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)
        return len(min_heap)
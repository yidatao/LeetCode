# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        if len(intervals) == 0: return [newInterval]
        if newInterval.start <= intervals[0].start:
            res = [newInterval]
            i = 0
            used = True
        else:
            res = [intervals[0]]
            i = 1
            used = False

        while i < len(intervals):
            curIV = res[-1]
            iv = intervals[i]
            if not used and newInterval.start >= curIV.start and newInterval.start <= iv.start:
                #overlap
                if newInterval.start <= curIV.end:
                    newIV = Interval(curIV.start, max(curIV.end, newInterval.end))
                    res.pop()
                    res.append(newIV)
                else:
                    res.append(newInterval)
                used = True
            else:
                if iv.start <= curIV.end:
                    newIV = Interval(curIV.start, max(curIV.end, iv.end))
                    res.pop()
                    res.append(newIV)
                else:
                    res.append(iv)
                i += 1

        #don't forget the final case
        if not used:
            curIV = res[-1]
            if newInterval.start <= curIV.end:
                newIV = Interval(curIV.start, max(curIV.end, newInterval.end))
                res.pop()
                res.append(newIV)
            else:
                res.append(newInterval)

        return res



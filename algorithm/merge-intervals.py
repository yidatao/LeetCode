# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        if len(intervals) == 0: return []
        #sort intervals by starting time
        intervals = sorted(intervals, key=lambda x:x.start)

        res = [intervals[0]]
        for i in range(1, len(intervals)):
            iv = intervals[i]
            cur_iv = res[-1]
            #check if intervals overlap
            if cur_iv.end >= iv.start:
                #merge
                new_iv = Interval(cur_iv.start,max(cur_iv.end, iv.end))
                res.pop()
                res.append(new_iv)
            else:
                res.append(iv)
        return res

print(Solution().merge([[1,3],[2,6],[8,10],[9,11]]))
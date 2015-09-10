# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if len(points) <= 2:
            return len(points)
        res = -1
        for i in range(len(points)-1):
            p = points[i]
            #when slope is inf, the value is # of points that are on the same *vertical* line with p
            #key is slope, value is the # of points that have this slope with p (i.e., on the same line)
            slope = {float("inf"): 0}
            #number of same points as p, initialize it as 1 as itself
            samepoint = 1
            for j in range(i+1, len(points)):
                q = points[j]
                if p.x == q.x and p.y == q.y:
                    samepoint += 1
                elif p.x == q.x:
                    slope[float("inf")] += 1
                else:
                    k = 1.0 * (p.y - q.y) / (p.x - q.x)
                    if k in slope:
                        slope[k] += 1
                    else:
                        slope[k] = 1
            #don't forget to add the same points
            res = max(res, max(slope.values()) + samepoint)
        return res


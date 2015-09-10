class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt0(self, x):
        if x <= 1: return x
        #(x/2+1)^2 > x
        start,end = 1,x/2+1
        while start <= end:
            mid = (start + end) / 2
            tmp = mid ** 2
            if tmp > x:
                #in case mid == end
                end = min(end-1, mid)
            elif tmp < x:
                #in case start == end
                start = max(start+1, mid)
            else:
                return mid
        return end

    #Newton
    def sqrt(self,x):
        if x <= 1: return x
        a = x / 2
        new_x = (a + x / float(a)) / float(2)
        while int(a) != int(new_x):
            a = new_x
            new_x = (a + x / float(a)) / float(2)
        return int(a)

print(Solution().sqrt(222))
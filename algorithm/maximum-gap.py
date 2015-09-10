class Solution:
    # @param num, a list of integer
    # @return an integer
    # refer to http://bookshadow.com/weblog/2014/12/14/leetcode-maximum-gap/
    def maximumGap(self, num):
        N = len(num)
        if N < 2: return 0
        A, B = min(num), max(num)
        #in case range is 0
        bucketRange = max(1, int((B - A - 1) / (N - 1)) + 1)
        bucketLen = (B - A) / bucketRange + 1
        buckets = [None] * bucketLen

        for x in num:
            index = (x - A) / bucketRange
            if buckets[index] is None:
                buckets[index] = {'min': x, 'max':x}
            else:
                buckets[index]['min'] = min(buckets[index]['min'],x)
                buckets[index]['max'] = max(buckets[index]['max'],x)

        res = 0
        for i in range(bucketLen-1):
            if buckets[i] is None:
                continue
            j = i + 1
            while buckets[j] is None:
                j += 1
            #successive elements are ith's max and jth's min
            res = max(res, buckets[j]['min'] - buckets[i]['max'])
            #skip None elements
            i = j
        return res
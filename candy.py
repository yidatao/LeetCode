class Solution:
    # @param ratings, a list of integer
    # @return an integer
    # Time limit exceeded
    def candy0(self, ratings):
        if len(ratings) == 1:
            return 1
        candy = [1 for x in range(len(ratings))]
        while True:
            change = False
            for i in range(len(candy)-1):
                if ratings[i] > ratings[i+1] and candy[i] <= candy[i+1]:
                    candy[i] = candy[i+1] + 1
                    change = True
                if ratings[i] < ratings[i+1] and candy[i] >= candy[i+1]:
                    candy[i+1] = candy[i] + 1
                    change = True
            if not change:
                break
        return sum(candy)

    def candy(self, ratings):
        candy = [1 for x in range(len(ratings))]
        #more candy if rating is higher than left neighbor
        for i in range(1, len(candy)):
            if ratings[i] > ratings[i-1] and candy[i] <= candy[i-1]:
                candy[i] = candy[i-1] + 1
        #more candy if rating is higher than right neighbor
        for i in range(len(candy)-2,-1,-1):
            if ratings[i] > ratings[i+1] and candy[i] <= candy[i+1]:
                candy[i] = candy[i+1] + 1
        return sum(candy)

print(Solution().candy([4,3,4,2,1]))

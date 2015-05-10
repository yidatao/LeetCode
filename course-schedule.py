class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        dependent = {}
        block = {}
        for i in range(numCourses):
            dependent[i] = []
            block[i] = []
        starting= [i for i in range(numCourses)]
        for p in prerequisites:
            dependent[p[0]] += [p[1]]
            #courses that depend on others cannot be starting points
            if p[0] in starting:
                starting.remove(p[0])
            block[p[1]] += [p[0]]
        
        clist = []
        while starting:
            c = starting.pop(0)
            clist += [c]
            for b in block[c]:
                #after taking c, courses that depend on it can be "unblocked"
                dependent[b].remove(c)
                #totally "unblocked" courses
                if len(dependent[b]) == 0:
                    starting += [b]
        return True if len(clist) == numCourses else False
class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        paths = []
        path = path.replace('//','/')
        s = path.split('/')
        for p in s:
            if p == '' or p == '.':
                continue
            if p == '..':
                if len(paths) > 0:
                    paths.pop()
            else:
                paths.append(p)

        res = ''
        for p in paths:
            res += '/' + p
        return res if len(res) > 0 else '/'

print(Solution().simplifyPath('/home//foo/'))
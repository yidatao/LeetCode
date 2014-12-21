class Solution:
    # @param s, a string
    # @return a boolean
    # a number is of form aEb, where a is a real number, b is an integer
    def isNumber(self, s):
        self.num = [str(x) for x in range(10)]
        #preprocess
        #lower() in case it uses E instead of e
        s = s.strip().lower()
        if " " in s or len(s) == 0: 
            return False

        #first divide by e
        parts = s.split("e")
        #contains multiple e
        if len(parts) > 2:
            return False
        elif len(parts) == 2:
            p1,p2 = parts[0],parts[1]
            #p1 should be real, while p2 should be integer (but can have signs)
            if p2.startswith("+") or p2.startswith("-"):
                p2 = p2[1:]
            return self.isReal(p1) and self.isInt(p2)
        elif len(parts) == 1:
            return self.isReal(parts[0])

    def isReal(self, s):
        if len(s) == 0: return False
        if s.startswith("+") or s.startswith("-"):
            s = s[1:]
        decimal = s.split(".")
        #more than 1 dot
        if len(decimal) > 2:
            return False
        elif len(decimal) == 2:
            p1,p2 = decimal[0],decimal[1]
            return p1 == "" and self.isInt(p2) or p2 == "" and self.isInt(p1) or self.isInt(p1) and self.isInt(p2)
        elif len(decimal) == 1:
            return self.isInt(decimal[0])

    #is s an integer with no signs.
    #Note 00123 is also valid
    def isInt(self, s):
        if len(s) == 0: return False
        for c in s:
            if c not in self.num:
                return False
        return True
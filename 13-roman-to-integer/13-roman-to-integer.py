class Solution:
    def romanToInt(self, s: str) -> int:
        k = {'I':1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        res = 0
        prev = 0
        for i in s[::-1]:
            if k[i]>=prev:
                res+=k[i]
            else:
                res-=k[i]
            prev = k[i]
        return res
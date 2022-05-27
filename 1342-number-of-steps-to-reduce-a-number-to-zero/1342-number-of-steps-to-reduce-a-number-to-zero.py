class Solution:
    def numberOfSteps(self, num: int) -> int: 
        res = -1
        for i in bin(num)[2:]:
            if i=='0':
                res+=1
            else:
                res+=2
        return res
class Solution:
    def numberOfSteps(self, num: int) -> int:
        x = bin(num)[2:]
        res = -1
        for i in x:
            if i=='0':
                res+=1
            else:
                res+=2
        return res
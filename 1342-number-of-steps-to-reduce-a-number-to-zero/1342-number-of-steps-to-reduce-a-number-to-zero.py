class Solution:
    def numberOfSteps(self, num: int) -> int:
        x = bin(num)[2:]
        return x.count('0')+2*x.count('1')-1
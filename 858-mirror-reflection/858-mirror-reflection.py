class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        if p ==  q :return 1
        while p%2==0 and q%2 ==0:
            p=p//2
            q=q//2
        if p%2!=0:
            if q%2!=0:
                return 1
            return 0
        else:return 2
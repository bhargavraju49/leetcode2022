# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n):
        if isBadVersion(1)==True:
            return 1
        else:
            l=0
            r=n-1
            while(l+1!=r):
                p=(l+r)//2
                if isBadVersion(p+1)==False :
                    l=p
                else:
                    r=p
            return(r+1)
class Solution:
    def candy(self, r: List[int]) -> int:
        dp = [1 for i in range(len(r))]
        topcheck = False
        top = 0
        res = 0
        for i in range(1,len(r)):
            if i-2>=0 and r[i]<r[i-1] and r[i-1]>r[i-2]:
                topcheck = True
                top = dp[i-1]
                dp[i] = 1
            elif i-2>=0 and r[i]>r[i-1] and r[i-1]<r[i-2]:
                if topcheck:
                    if dp[i-1]>=top:
                        res+=dp[i-1]+1-top
                        top = 0
                        topcheck=False
                    top = 0
                    topcheck=False
                dp[i] = 2
            elif r[i]==r[i-1]:
                if topcheck:
                    if dp[i-1]>=top:
                        res+=dp[i-1]+1-top
                        top = 0
                        topcheck=False
                top = 0
                topcheck = False
            elif r[i]<r[i-1] or r[i]>r[i-1]:
                dp[i]=dp[i-1]+1
        if topcheck:
            if dp[len(r)-1]>=top:
                res+=dp[len(r)-1]+1-top
                top = 0
                topcheck=False
                return sum(dp)+res 
        return sum(dp)+res
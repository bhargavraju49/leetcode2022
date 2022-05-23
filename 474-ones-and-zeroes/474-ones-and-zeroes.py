class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        strs = [collections.Counter(s) for s in strs]
        dp = {}
        
        def helper(i, m, n):
            if i == len(strs):
                return 0
            
            x = (i, m, n)
            if x in dp:
                return dp[x]
            
            count0, count1 = strs[i]['0'], strs[i]['1']
            dp[x] = helper(i + 1, m, n)
            if m - count0 >= 0 and n - count1 >= 0:
                dp[x] = max(dp[x], helper(i + 1, m - count0, n - count1) + 1)
                
            return dp[x]
        
        return helper(0, m, n)
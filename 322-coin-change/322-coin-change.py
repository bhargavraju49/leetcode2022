class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[0 for i in range(amount+1)] for i in range(len(coins)+1)]
        for i in range(1,amount+1):
            dp[0][i] = sys.maxsize

        for i in range(1,len(coins)+1):
            for j in range(1,amount+1):
                if j-coins[i-1]>=0:
                    include = 1 + dp[i][j-coins[i-1]]
                else:
                    include = sys.maxsize
                exclude = dp[i-1][j]

                dp[i][j] = min(include,exclude)
        if dp[len(coins)][amount] == sys.maxsize:
            return -1
        return dp[len(coins)][amount]
        pass

        
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        dp = [0 for i in range(len(word1))]
        
        maxl = 0
        for i in range(len(word2)):
            k = [i1 for i1 in dp]
            for j in range(len(word1)):
                if word2[i]==word1[j]:
                    if j==0:
                        k[j]=1
                        maxl = max(maxl,k[j])
                    else:
                        k[j]=dp[j-1]+1
                        maxl = max(maxl,k[j])
                else:
                    if j!=0:
                        k[j] = max(k[j-1],dp[j])
            print(k)

            dp = [i1 for i1 in k]
        return len(word1)+len(word2)-2*maxl
        
                    
        
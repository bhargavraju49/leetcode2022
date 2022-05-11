class Solution:
    def countVowelStrings(self, n: int) -> int:
        N = [1]*5
        sigN = sum(N)
        for i in range(n-1):
            k = [sigN]
            for j in range(1,5):
                k.append(k[j-1] - N[j-1])
                sigN+=k[j]
            N=k
            sigN = sum(N)
            pass
        return (sigN)
            
        
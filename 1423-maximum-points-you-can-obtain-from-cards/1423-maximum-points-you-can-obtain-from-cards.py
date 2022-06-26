class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        dpArray = [0 for i in range(k + 1)]
        
        dpArray[0] = sum(cardPoints[:k])
        
        for i in range(1, k + 1):
            dpArray[i] = dpArray[i - 1] - cardPoints[k - i] + cardPoints[-i]
        return max(dpArray)
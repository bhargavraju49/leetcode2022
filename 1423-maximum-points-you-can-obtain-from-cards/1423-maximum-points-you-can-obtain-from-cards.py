class Solution:
#     def maxScore(self, cardPoints: List[int], k: int) -> int:
#         dpArray = [0 for i in range(k + 1)]
        
#         dpArray[0] = sum(cardPoints[:k])
        
#         for i in range(1, k + 1):
#             dpArray[i] = dpArray[i - 1] - cardPoints[k - i] + cardPoints[-i]
#         return max(dpArray)
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        
        remaining_length = n - k
        subarray_sum = sum(cardPoints[:remaining_length])
        
        min_sum = subarray_sum
        for i in range(remaining_length, n):
            # Update the sliding window sum to the subarray ending at index i
            subarray_sum += cardPoints[i]
            subarray_sum -= cardPoints[i - remaining_length]
            # Update min_sum to track the overall minimum sum so far
            min_sum = min(min_sum, subarray_sum)
        return total - min_sum
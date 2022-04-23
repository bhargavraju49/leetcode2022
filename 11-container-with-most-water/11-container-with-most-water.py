class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1
        
        maxl = 0
        
        while start<end:
            ans = (end - start) * min(height[start], height[end])
            
            maxl = max(ans,maxl)
            
            if height[start] > height[end]:
                end-=1
            else:
                start+=1
                
        return maxl
        
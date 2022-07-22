class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], H: int, C: int, target: int) -> int:
        
        dp={}
        inf=math.inf
        
        def finder(i,last_color,neigh):
            
            if i==H:
                if neigh==target:
                    return 0
                return inf
            
            if neigh>target:
                return inf 
            
            if (i,last_color,neigh) in dp:
                return dp[(i,last_color,neigh)]
            
            if houses[i]==0:
                
                ans=inf
                
                for current_color in range(1,C+1):
                    
                    if last_color==current_color:
                        ans= min(ans,finder(i+1,last_color,neigh)+cost[i][current_color-1])
                    else:
                        ans= min(ans,finder(i+1,current_color,neigh+1)+cost[i][current_color-1])
                        
                dp[(i,last_color,neigh)]=ans
                return ans
            
            else:
                
                ans=None
    
                if last_color==houses[i]:
                    ans= finder(i+1,last_color,neigh)
                else:
                    ans= finder(i+1,houses[i],neigh+1)
                    
                dp[(i,last_color,neigh)]=ans
                return ans
            
        ans=finder(0,0,0)
            
        if ans>=inf:
            return -1
        return ans
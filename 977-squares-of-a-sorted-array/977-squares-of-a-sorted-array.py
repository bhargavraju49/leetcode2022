class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        k=[0]*len(nums)
        b=0
        e=len(nums)-1
        for i in range(e,-1,-1):
            p=nums[b]*nums[b]
            q=nums[e]*nums[e]
            if(p>q):
                k[i]=p
                b=b+1
            else:
                k[i]=q
                e=e-1
            
        return k
            
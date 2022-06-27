#User function Template for python3
class Solution:
	def minJumps(self, a, n):
        maxj = a[0]
        jump = a[0]
        res = 0
        for i in range(1,len(a)):
            if jump-i < 0:
                return -1
            if jump>= len(a)-1:
                    res+=1
                    break
            maxj = max(maxj,a[i]+i)
            if jump-i == 0:
                res+=1
                jump = maxj
                maxj = 0
                
        return res
	        
	        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends
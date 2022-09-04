# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(lambda : defaultdict(list))
        r = [0,0]
        
        def helper(root,x,y):
            if root is None:
                return 
            res[x][y].append(root.val)
            r[0] = min(r[0],x)
            r[1] = max(r[1],x)
            
            # res.append((root.val,x,y))
            
            helper(root.left,x-1,y+1)
            helper(root.right,x+1,y+1)
            return 
        
        helper(root,0,0)
        # print(res,*r)
        mainres = []
        for i in range(r[0],r[1]+1):
            k = res[i]
            j = list(k.keys())
            j.sort()
            rr = []
            for l in j:
                k2 = k[l]
                k2.sort()
                rr+=k2
            mainres.append(rr)
        return mainres
        
        
        
        
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        res = [0]
        for i in range(1,len(heights)):
            p = heights[i]-heights[i-1]
            if p>0:
                res.append(p)
            else:
                res.append(0)
        lo = 1
        hi = len(res)-1
        ans = 0
        while(lo<=hi):
            mid = (lo+hi)//2
            def check(mid,bricks,ladder):
                p = res[:mid+1]
                p.sort()
                for i in range(len(p)):
                    if p[i]<=bricks:
                        bricks-=p[i]
                    else:
                        if ladder>0:
                            ladder-=1
                        else:
                            return False
                return True
            if check(mid,bricks,ladders):
                lo = mid + 1
                ans = mid
            else:
                hi = mid - 1
        return ans
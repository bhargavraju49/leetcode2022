class Solution:
    def maxArea(self, h: int, w: int, H: List[int], V: List[int]) -> int:
        V.append(0)
        V.append(w)
        H.append(0)
        H.append(h)
        
        H.sort()
        V.sort()
        
        mh = 0
        mv = 0
        
        for i in range(len(V)-1):
            mv = max(mv,V[i+1]-V[i])
        for i in range(len(H)-1):
            mh = max(mh,H[i+1]-H[i])
        if mh*mv > ((10**9)+7):
            return (mh*mv)%((10**9)+7)
        return(mh*mv)
        
        
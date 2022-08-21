class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        target = list(target)
        res = []
        progress = True
        todo = len(target)
        visited = [False] * todo
        
        def canReplace(tIndex):
            for i in range(len(stamp)):
                if(target[tIndex] != "?" and target[tIndex] != stamp[i]):
                    return False
                tIndex += 1
            return True
        
        def doReplace(tIndex):
            visited[tIndex] = True
            replace = 0
            for _ in range(len(stamp)):
                if target[tIndex] != "?": replace += 1 
                target[tIndex] = "?"
                tIndex += 1
            return replace                
        
        while(todo and progress):
            progress = False
            for i in range(len(target) - len(stamp) + 1):
                if (not visited[i] and canReplace(i)):
                    todo -= doReplace(i)
                    progress = True
                    res.append(i)
        
        if(not progress): return []
        return reversed(res)
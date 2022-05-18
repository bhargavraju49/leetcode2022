class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        
        for i,j in connections:
            graph[i].append(j)
            graph[j].append(i)
        time = [None]*n
        res = []
        def getcc(node = 0, parent = -1, t = 1):
            if time[node]:
                return
            time[node] = t
            for Nvertex in graph[node]:
                if Nvertex == parent:
                    continue
                getcc(Nvertex, node, t+1)
                if time[Nvertex] == t+1:
                    res.append((node,Nvertex))
                else:
                    time[node] = min(time[Nvertex],time[node]) 
        getcc()
        return res
                    
                
                
            
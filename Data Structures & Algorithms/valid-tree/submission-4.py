class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)>(n-1):
            return False #no. of edges should be equal to n - 1
        
        adj = [[] for _ in range(n)] #create adjacency list where index is mapped to other nodes
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u) #appended u and v to each other as the edges are undirected
        
        visit = set()
        #cycle detection
        def dfs(node,par): #par is parent node
            if node in visit:
                return False
            visit.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei,node):
                    return False
            return True
        
        return dfs(0,-1) and len(visit) == n
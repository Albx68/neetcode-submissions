class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        count = 0
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            neighbours = adj[node]
            for n in neighbours:
                dfs(n)
            return True
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count
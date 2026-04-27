class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preReqMap = {i:[] for i in range(numCourses)}
        res = []
        cycle = set()
        visited = set()
        for crs,pre in prerequisites:
            preReqMap[crs].append(pre)
        
        def dfs(crs):
            nonlocal res
            if crs in cycle:
                return False
            if crs in visited:
                return True

            cycle.add(crs)
            for pre in preReqMap[crs]:
                if not dfs(pre):
                    return False
            # preReqMap[crs] = []
            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
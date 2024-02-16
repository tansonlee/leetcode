class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        
        for a, b in prerequisites:
            graph[a].append(b)

        #####
        # Topological sort
        #####
        current_nodes = []
        indegrees = {}
        for i in range(numCourses):
            indegrees[i] = 0
        
        for a, b in prerequisites:
            indegrees[b] += 1
        
        for i in range(numCourses):
            if indegrees[i] == 0:
                current_nodes.append(i)
        
        visited_count = 0
        while len(current_nodes) > 0:
            node = current_nodes.pop()
            visited_count += 1
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    current_nodes.append(neighbor)
        return visited_count == numCourses


        #####
        # Cycle detection with dfs
        #####
        def dfs(node, visited, path):
            visited.add(node)
            path.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor, visited, path) == False:
                        return False
                elif neighbor in path:
                    return False
            path.remove(node)
            return True 
        
        visited = set()
        for i in range(numCourses):
            if i not in visited:
                if dfs(i, visited, set()) == False:
                    return False
        return True


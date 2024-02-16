class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        indegrees = {}
        for i in range(numCourses):
            graph[i] = []
            indegrees[i] = 0
        for a, b in prerequisites:
            graph[b].append(a)
            indegrees[a] += 1
        
        current_nodes = []
        ordered = []
        for i in range(numCourses):
            if indegrees[i] == 0:
                current_nodes.append(i)
        while len(current_nodes) > 0:
            node = current_nodes.pop()
            ordered.append(node)

            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    current_nodes.append(neighbor)
        if len(ordered) == numCourses:
            return ordered 
        return []

        

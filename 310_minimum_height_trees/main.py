class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {}
        for i in range(n):
            graph[i] = []
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def farthest_point(node, prev):
            result = (1, node, [node])
            
            for neighbor in graph[node]:
                if neighbor != prev:
                    d, other, head = farthest_point(neighbor, node)
                    if d + 1 > result[0]:
                        result = (d + 1, other, head + [node])
            return result
        
        end1 = farthest_point(0, None)
        end2 = farthest_point(end1[1], None)
        path = end2[2]

        if len(path) % 2 == 0:
            return [path[len(path) // 2 - 1], path[len(path) // 2]]
        else:
            return [path[len(path) // 2]]



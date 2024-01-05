from collections import deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        # Create the graph.
        def has_common_stop(route1, route2):
            route1.sort()
            route2.sort()
            i = 0
            j = 0
            while i < len(route1) and j < len(route2):

                if route1[i] == route2[j]:
                    return True
                if route1[i] < route2[j]:
                    i += 1
                else:
                    j += 1
            return False
        
        def get_routes_with_stop(stop):
            result = []
            for i in range(len(routes)):
                if stop in routes[i]:
                    result.append(i)
            return result

        adj = {}
        for i in range(len(routes)):
            adj[i] = []
        for i in range(len(routes)):
            for j in range(len(routes)):
                if i != j and has_common_stop(routes[i], routes[j]):
                    adj[i].append(j)
        
        # Perform a BFS
        q = deque([(n, 1) for n in get_routes_with_stop(source)])
        print(adj)
        print(q)
        visited = set()
        while len(q):
            node, dist = q.popleft()
            visited.add(node)
            if target in routes[node]:
                return dist
            
            for neighbor in adj[node]:
                if neighbor not in visited:
                    q.append((neighbor, dist + 1))

        return -1



        # adj = {}
        # for route in routes:
        #     for i in range(len(route)):
        #         if route[i] not in adj:
        #             adj[route[i]] = []
        #         for j in range(len(route)):
        #             if i != j:
        #                 adj[route[i]].append(route[j])
        
        # # Perform a BFS from source to target
        # visited = set()
        # q = deque([(source, 0)])
        # while len(visited) < len(adj):
        #     if len(q) == 0:
        #         return -1
        #     node, dist = q.popleft()
        #     visited.add(node)
        #     if node == target:
        #         return dist
        #     for neighbor in adj[node]:
        #         if neighbor in visited:
        #             continue
        #         q.append((neighbor, dist + 1))





        
        

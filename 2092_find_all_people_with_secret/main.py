class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        """
        1. Group all the meetings that happen at the same time and order the groups by their time
        2. Go through all the groups of meetings and use a dfs to spread the secret
        """

        def dfs(graph, person):
            all_know.add(person)
            if person not in graph:
                return
            
            for neighbor in graph[person]:
                if neighbor not in all_know:
                    dfs(graph, neighbor)

        all_know = set([0, firstPerson])
        ordered_meetings = sorted([(t, x, y) for x, y, t in meetings])
        grouped_meetings = []
        i = 0
        while i < len(ordered_meetings):
            time = ordered_meetings[i][0]
            curr = []
            while i < len(ordered_meetings) and ordered_meetings[i][0] == time:
                curr.append((ordered_meetings[i][1], ordered_meetings[i][2]))
                i += 1
            grouped_meetings.append(curr)

        for meetings in grouped_meetings:
            people = set()
            graph = {}
            for x, y in meetings:
                people.add(x)
                people.add(y)
                if x not in graph:
                    graph[x] = []
                if y not in graph:
                    graph[y] = []
                graph[x].append(y)
                graph[y].append(x)
            for p in people:
                if p in all_know:
                    dfs(graph, p)
        
        return list(all_know)


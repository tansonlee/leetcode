class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_index = defaultdict(list)

        for i in range(len(accounts)):
            for email in accounts[i][1:]:
                email_to_index[email].append(i)
        
        graph = defaultdict(set)
        for email in email_to_index:
            # All of these nodes are neighbors with each other
            neighbors = email_to_index[email]

            for i in range(len(neighbors)):
                for j in range(i + 1, len(neighbors)):
                    graph[neighbors[i]].add(neighbors[j])
                    graph[neighbors[j]].add(neighbors[i])
        
        def get_emails_from(node, visited):
            if node in visited:
                return set()
            
            visited.add(node)
            result = set()
            result.update(accounts[node][1:])

            neighbors = graph[node]
            for neighbor in neighbors:
                result.update(get_emails_from(neighbor, visited))
            
            return result
        
        # Each connected component is an account
        result = []
        visited = set()
        for i in range(len(accounts)):
            if i in visited:
                continue
            name = accounts[i][0]
            emails = get_emails_from(i, visited)
            result.append([name] + sorted(list(emails)))

        return result



        

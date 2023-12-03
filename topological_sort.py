from collections import deque

def topological_sort_bfs(graph):
	n = len(graph)
	in_degree = [0 for _ in range(n)]
	visited = [False for _ in range(n)]

	for node in range(n):
		for neighbor in graph[node]:
			in_degree[neighbor] += 1
	
	q = deque([])
	for node in range(n):
		if in_degree[node] == 0:
			q.append(node)

	result = []
	while len(q) > 0:
		node = q.popleft()
		visited[node] = True
		result.append(node)
		for neighbor in graph[node]:
			if visited[neighbor]:
				continue
			in_degree[neighbor] -= 1
			if in_degree[neighbor] == 0:
				q.append(neighbor)
	
	return result

def topological_sort_dfs(graph):
	result = []
	visited = [False for _ in range(len(graph))]

	def helper(node):
		nonlocal visited, result
		visited[node] = True
		for neighbor in graph[node]:
			if not visited[neighbor]:
				helper(neighbor)
		result.append(node)

	for node in range(len(graph)):
		if not visited[node]:
			helper(node)

	return result


g1 = [[1,2], [3,4], [3,5], [4], [5], []]
g2 = [[], [0], [0], [1,2], [1,3], [4,2]]
res = topological_sort_dfs(g2)
print(res)

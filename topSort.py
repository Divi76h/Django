input = [("A", "B"), ("B", "C"), ("B", "D"), ("C", "A"), ("D", "E")]

# Build graph
nodes = set()
for u, v in input:
    nodes.add(u)
    nodes.add(v)

print(nodes)
adj = {node: [] for node in nodes}
for u, v in input:
    adj[v].append(u)  # reverse edges: to build adj list

visited = {node: False for node in nodes}
ordering = []

def dfs(node, cycle):
    cycle.append(node)
    visited[node] = True
    for neighbor in adj[node]:
        if neighbor in cycle:
            print("Cycle exists!")
            quit()
        if not visited[neighbor]:
            dfs(neighbor, cycle)

    cycle.remove(node)
    ordering.append(node)

# Call DFS on all unvisited nodes
for node in nodes:
    if not visited[node]:
        dfs(node, [])

# Topological order (reverse)
ordering.reverse()
print(ordering)
print(adj)

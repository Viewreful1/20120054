import sys

N, M, V = map(int, sys.stdin.readline().split())

graph = dict()

for i in range(M):
    node1, node2 = map(int, sys.stdin.readline().split())
    if node1 not in graph.keys():
        graph[node1] = set([node2])
    else:
        graph[node1].add(node2)
    if node2 not in graph.keys():
        graph[node2] = set([node1])
    else:
        graph[node2].add(node1)

for k in graph:
    graph[k] = list(graph[k])
    graph[k].sort()

# Depth First Search starting from node V
visited = dict()
for k in graph.keys():
    visited[k] = False

st = []
for node in graph[V]:
    st.append(V)
    while st:
        curr_node = st.pop()
        if not visited[curr_node]:
            visited[curr_node] = True
            print(curr_node),
            for i in xrange(len(graph[curr_node])-1, -1, -1):
                st.append(graph[curr_node][i])
print('')

# Breadth First Search starting from node V
visited = dict()
for k in graph.keys():
    visited[k] = False

q0 = [V]
visited[V] = True
print(V),
while q0:
    curr_node = q0.pop()
    for x in graph[curr_node]:
        if not visited[x]:
            visited[x] = True
            print(x),
            q0.insert(0, x)
print('')

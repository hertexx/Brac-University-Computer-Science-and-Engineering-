inp = open("input3.txt", "r")
out = open("output3.txt", "w")
N, M = map(int, inp.readline().split())
graphSet = {i: [] for i in range(N + 1)}
for i in range(M):
    n = tuple(map(int,inp.readline().split()))
    arr = graphSet[n[0]]
    arr.append(n[1])
    arr = graphSet[n[1]]
    arr.append(n[0])
visited = [0] * (N+1)
path = []
def DFS(G, u):
    visited[u] = 1
    path.append(u)

    for v in G[u]:
        if visited[v] != 1:
            DFS(G, v)
    return path
DFS(graphSet, 1)
out.write(" ".join(list(map(str, path))))
inp.close()
out.close()
# The code addresses the problem by implementing Depth-First Search (DFS) on an
# undirected graph representing cities and roads in Doraland. It initializes a dictionary
# (graphSet) to store the adjacency lists of cities and populates the graph based on the given roads.
# The DFS traversal function (DFS) is invoked to explore the graph starting from city 1, and the
# resulting DFS path is stored in the variable path. Finally, the DFS path is written to
# the output file, representing Dora's exploration path following DFS traversal.
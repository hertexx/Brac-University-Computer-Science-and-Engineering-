inp = open("input2.txt", "r")
out = open("output2.txt", "w")
N, M = map(int, inp.readline().split())
graphDicSet = {i: [] for i in range(N + 1)}
for i in range(M):
    n = tuple(map(int, inp.readline().split()))
    arr = graphDicSet[n[0]]
    arr.append(n[1])
    arr = graphDicSet[n[1]]
    arr.append(n[0])
def BFS(G, s):
    visited = []
    queue = []
    path = []
    visited.append(s)
    queue.append(s)
    while queue:
        u = queue.pop(0)
        path.append(u)
        for v in G[u]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
    return path
path = BFS(graphDicSet, 1)
out.write(" ".join(list(map(str, path))))
inp.close()
out.close()
#The code solves the problem by performing a Breadth-First Search (BFS)
# traversal on an undirected graph representing cities and roads in Doraland.
# It initializes a dictionary (graphDicSet) to store the adjacency lists of cities.
# Then, it reads the input, populates the graph, and applies BFS starting from city 1.
# The BFS path is stored in the variable path and is written to the output file, representing
# Dora's exploration path in level-order traversal. The output provides a valid BFS order for
# Dora to visit the cities in Doraland.
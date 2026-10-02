inp = open("input4.txt", "r")
out = open("output4.txt", "w")
N, M = map(int, inp.readline().split())
graphSet = {i: [] for i in range(N + 1)}
for i in range(M):
    n = tuple(map(int, inp.readline().split()))
    arr = graphSet[n[0]]
    arr.append(n[1])
def DFS(gset, u, visited, stack):
    visited[u] = True
    stack[u] = True
    for v in gset[u]:
        if not visited[v]:
            if DFS(gset, v, visited, stack):
                return True
        elif stack[v]:
            return True
    stack[u] = False
    return False
def checkCycle(gSet, N):
    for u in range(N):
        if DFS(gSet, u, visited, stack):
            return True
    return False
visited = [False] * (N+1)
stack = [False] * (N+1)
if checkCycle(graphSet, N):
    out.write("YES")
else:
    out.write("NO")
inp.close()
out.close()
#The code addresses the problem of detecting cycles in a directed graph.
# It initializes an adjacency list to represent the graph. The DFS function is
# implemented to perform a depth-first traversal and check for cycles during exploration.
# The containsCycle function iterates through vertices using DFS, determining if any cycles exist.
# The code outputs "YES" if a cycle is found and "NO" otherwise, providing a solution to the problem.
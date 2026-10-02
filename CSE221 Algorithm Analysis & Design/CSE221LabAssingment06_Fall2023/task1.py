import heapq as hq
import math

def djikstra(G, s):
    dist = [math.inf]*len(G)
    dist[s] = 0
    Q = []
    hq.heappush(Q, (dist[s], s))
    prev = [None]*len(G)
    visited = [False]*len(G)
    cost = 0

    while Q:
        num, u = hq.heappop(Q)
        if visited[u] == True:
            continue
        visited[u] = True
        for v,cost in G[u]:
            alt = dist[u] + cost
            if alt<dist[v]:
                dist[v] = alt
                prev[v] = u
                hq.heappush(Q, (dist[v], v))

    dist.pop(0)
    while math.inf in dist:
        idx = dist.index(math.inf)
        dist[idx] = -1
    return dist

f1 = open("input1.txt", "r")
f2 = open("output1.txt", "w")

inp = list(map(int,f1.read().strip().split()))
print(inp)
f1.close()
nodes = inp[0]
edges = inp[1]
source = (inp[-1])

dic = {i:[] for i in range(nodes+1)}
for i in range(2, len(inp)-2, 3):
    node1 = inp[i]
    node2 = inp[i+1]
    cost = inp[i+2]
    arr = dic[node1]
    arr.append((node2, cost))

costs = djikstra(dic, source)
f2.write(" ".join(list(map(str, costs))))
#The provided Python code reads a graph representation from "input1.txt," applies Dijkstra's algorithm to find the shortest path distances from a specified source node, and writes the results to "output1.txt." The graph is represented as an adjacency list, and the algorithm employs a priority queue to efficiently explore the graph's nodes. The code uses a dictionary to organize the graph, and the resulting shortest path distances are stored in the output file. Considerations for code organization and file handling are suggested for improved readability and robustness.
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

f1 = open("input2.txt", "r")
f2 = open("output2.txt", "w")

inp = f1.read().split("\n")
print(inp)
inp=inp[:-1]
print(inp)
f1.close()
line1 = inp[0].split(" ")
lineN = inp[-1].split(" ")
nodes = int(line1[0])
edges = int(line1[1])
source1 = int(lineN[0])
source2 = int(lineN[1])

dic = {i:[] for i in range(nodes+1)}
for i in range(1, len(inp)-1, 1):
    info = inp[i].split(" ")
    node1 = int(info[0])
    node2 = int(info[1])
    cost = int(info[2])
    arr = dic[node1]
    arr.append((node2, cost))

costs1 = djikstra(dic, source1)
costs2 = djikstra(dic, source2)

time = math.inf
node = math.inf
for i in range(len(costs1)):
    if costs1[i] in [0,-1] or costs2[i] in [0, -1]:
        continue
    time2 = max(costs1[i], costs2[i])
    if time2 < time:
        time = time2
        node = i+1

if time == math.inf:
    f2.write("IMPOSSIBLE")
else:
    f2.write("Time "+str(time)+'\nNode '+str(node))
# The code reads a graph with two source nodes from "input2.txt" and applies Dijkstra's algorithm to find the shortest path distances from both sources. It then identifies the earliest time and corresponding node reachable simultaneously from both sources. The results are written to "output2.txt," including the earliest time and node, or "IMPOSSIBLE" if no common reachable node is found. The graph is represented as an adjacency list, and the algorithm utilizes a priority queue for efficient node exploration. Considerations for code organization and file handling are recommended for better readability and robustness.